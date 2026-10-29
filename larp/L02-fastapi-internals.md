# L02 — FastAPI internals: ASGI, dependency injection, Pydantic v2, sync vs async
> LARP topic L02 (planned Thu 29 Oct) · Part A ⏱ 20 min · Part B ⏱ 20 min · Quiz ⏱ 15 min (`/quiz L02`)
> Builds on: A01 (you wrote the server half yourself), L01 (event loop).
> Running the snippets is optional: `uv run --with fastapi --with uvicorn python file.py`. Reading them is enough.

---
## PART A — What happens between the socket and your function

### 1. The stack
```
 client ──TCP──> Uvicorn            the ASGI *server*: accepts sockets, parses HTTP bytes
                   (you built a baby version of this in A01)
                   │ calls app(scope, receive, send)
                   ▼
               Starlette            the ASGI *toolkit*: routing, middleware, Request/Response
                   ▼
               FastAPI              on top: dependency injection, Pydantic validation, OpenAPI docs
                   ▼
               your endpoint function
```
**ASGI** (Asynchronous Server Gateway Interface) is the contract between server and app. Its
older sync sibling, **WSGI**, is what Flask/Django use(d): one request in, one response out,
with no websockets or streaming. ASGI is async and supports websockets, SSE and streaming.

### Snippet: a raw ASGI app (no framework), to demystify it
```python
async def app(scope, receive, send):
    # scope: dict describing the request: type, method, path, headers...
    assert scope["type"] == "http"
    body = f"you asked for {scope['path']}".encode()
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"text/plain")]})
    await send({"type": "http.response.body", "body": body})

# run: uvicorn this_file:app   then  curl http://127.0.0.1:8000/hello
```
That's all FastAPI is at the bottom: a very fancy `app(scope, receive, send)`.
Uvicorn's job is exactly A01's: sockets, framing, parsing HTTP, but asynchronously, with the
event loop from L01.

### 2. A request's lifecycle (say this in interviews)
1. Uvicorn accepts the TCP connection, parses the HTTP request → builds `scope`.
2. **Middleware** runs (CORS, request-id, timing): wraps everything, in → out.
3. **Router** matches method + path → finds your endpoint.
4. **Dependencies** are resolved (auth user, DB session, settings).
5. **Request validation**: path/query/body parsed into Pydantic models; failure → **422**
   automatically.
6. Your endpoint runs.
7. **Response validation/serialisation** through `response_model`.
8. Back out through middleware; `yield`-dependency cleanup runs; bytes go to the socket.

### 3. `async def` vs `def` endpoints (an L01 tie-in, asked constantly)
```python
@app.get("/a")
async def a():            # runs ON the event loop. Must never block (L01 §6)
    return await http.get(...)

@app.get("/b")
def b():                  # FastAPI runs it in a THREADPOOL (default 40 threads, via anyio)
    return requests.get(...)   # blocking is OK here
```
Rule: async libraries → `async def`. Sync libraries → plain `def`. The worst combination is
**`async def` + blocking call**: it freezes the whole worker.

### 4. Workers
`uvicorn app:app --workers 4` (or gunicorn with uvicorn workers) = 4 **processes**, each with
its own event loop. That's parallelism across cores (L01 §3) and also why in-memory state (a
dict cache, a counter) is **not shared** between workers. You'll exploit that in D01/D04.

**Check:** (1) What does Uvicorn do that Starlette doesn't? (2) Where does a 422 come from?
(3) `async def` endpoint calls `requests.get` with a 3-second response time, and 10 users hit
it at once. What happens to an 11th user calling `/health`?

---
## PART B — Dependency injection, Pydantic, lifespan

### 5. Dependency injection with `Depends`
Instead of each endpoint *creating* what it needs, it *declares* what it needs, and FastAPI
provides it per request.
```python
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

def get_settings():
    return Settings()                        # could be cached with @lru_cache

async def get_current_user(authorization: str = Header(...)):
    user = await verify_token(authorization)
    if not user:
        raise HTTPException(401, "bad token")
    return user

async def get_session():                     # a *yield* dependency
    async with SessionLocal() as session:    # setup
        yield session                        # endpoint runs here
    # teardown runs after the response: session closed, connection back to the pool

@app.get("/documents")
async def list_documents(user=Depends(get_current_user), db=Depends(get_session)):
    return await DocumentRepo(db).list_for(user.workspace_id)
```
Key facts:
- Dependencies form a **graph**: a dependency can `Depends` on others.
- Within one request, each dependency is **cached**: used 3 times, created once.
- **`yield` dependencies** = setup/teardown per request (DB sessions, locks).
- **Testing:** `app.dependency_overrides[get_session] = fake_session` swaps it without
  monkeypatching. This is *why* DI exists (course lesson A03 makes you feel this pain first).

### 6. Pydantic v2 in 60 seconds
```python
from pydantic import BaseModel, Field, EmailStr

class SignupIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=12)

class UserOut(BaseModel):
    id: int
    email: EmailStr          # note: NO password_hash field

@app.post("/users", response_model=UserOut, status_code=201)
async def signup(body: SignupIn): ...
    # returns a DB object with password_hash -> response_model FILTERS it out
```
- **Input validation:** bad body → 422 with a precise error list, before your code runs.
- **`response_model`:** output validation + **filtering** (never leak `password_hash`) + OpenAPI docs.
- v2's core is written in **Rust** (pydantic-core), roughly 5–50× faster than v1.
  `model_validate()` / `model_dump()` replace v1's `parse_obj()` / `dict()`.

### 7. Lifespan: things created ONCE, not per request
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    app.state.engine = create_async_engine(DB_URL, pool_size=10)   # pool: created once
    app.state.reranker = load_model()                               # heavy ML model: load once
    yield
    await app.state.engine.dispose()                                # clean shutdown

app = FastAPI(lifespan=lifespan)
```
Per request → `Depends` (session borrowed from the pool). Per process → `lifespan` (pool, model,
HTTP client). Mixing these up is behind the classic L02 scenario: **"QueuePool limit reached"**,
where sessions are held too long (e.g. across a 20-second LLM call) or leaked, the pool runs
dry, and requests 500 under load.

### 8. Say it like a senior
"I keep endpoints thin: dependencies give me the principal and a session, a service layer does
the work, and response models guarantee we never leak internal fields."

**Now:** run `/quiz L02`.
