# L01 — Python async/await and the event loop
> LARP topic L01 (planned Wed 4 Nov) · Part A ⏱ 15 min · Part B ⏱ 20 min · Quiz ⏱ 15 min (`/quiz L01`)
> Builds on: S03 experiment 2 (client 2 had to wait). Feeds: A01 break rounds, L02.

---
## PART A — Concurrency, parallelism, and why servers wait a lot

### 1. Where time goes in a backend request
A typical DocuLens `/ask` request:
```
 parse JSON           0.1 ms   CPU
 DB query             5   ms   waiting (I/O)
 embedding API call  80   ms   waiting (I/O)
 LLM call          1500   ms   waiting (I/O)
 build response       0.2 ms   CPU
```
More than 99% of the time the process is **waiting** for another machine. That's what
**I/O-bound** means. **CPU-bound** is the opposite: the CPU is busy the whole time (OCR,
resizing images, running a model on CPU).

### 2. Concurrency vs parallelism
- **Concurrency:** many tasks *in progress* at once, taking turns. A chef with 5 pans: stirs one
  while the others simmer. **One** worker.
- **Parallelism:** many tasks *executing at the same instant*. 5 chefs. **Many** workers (CPU
  cores).

For I/O-bound work, concurrency is enough: while request A waits for the LLM, serve request B.

### 3. Your three tools in Python
| Tool | What it is | Good for | Cost |
|---|---|---|---|
| **threads** (`threading`, thread pools) | OS switches between threads | blocking I/O with sync libraries | ~8 MB stack reservation each; OS switching; shared-state races |
| **processes** (`multiprocessing`, Celery workers, `uvicorn --workers 4`) | separate Python interpreters | CPU-bound work, true parallelism | memory per process, no shared memory |
| **asyncio** (`async`/`await`) | one thread, tasks voluntarily take turns | lots of concurrent I/O (thousands of connections) | everything must be async-aware; one blocking call stalls all |

### 4. The GIL in three lines
CPython's **Global Interpreter Lock** lets only **one thread run Python bytecode at a time**. So
threads don't speed up CPU-bound Python. But a thread **releases the GIL while waiting on I/O**
(socket, file, `time.sleep`), so threads *do* help I/O-bound work. CPU-bound → processes.
(Python 3.13 has an experimental no-GIL build; say "experimental" if asked.)

### Snippet: feel the difference (run it)
```python
import time
from concurrent.futures import ThreadPoolExecutor

def fake_io(i):          # pretend: a 1-second HTTP call
    time.sleep(1)
    return i

t = time.perf_counter()
[fake_io(i) for i in range(5)]
print(f"sequential: {time.perf_counter() - t:.1f}s")      # ~5.0s

t = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    list(pool.map(fake_io, range(5)))
print(f"5 threads:  {time.perf_counter() - t:.1f}s")      # ~1.0s

def fake_cpu(i):
    return sum(range(10_000_000))

t = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    list(pool.map(fake_cpu, range(5)))
print(f"CPU in threads: {time.perf_counter() - t:.1f}s  <- no faster than sequential: the GIL")
```

**Check (answer before Part B):** (1) Your server is slow because it OCRs PDFs. Threads or
processes? (2) It's slow because it waits on 3 APIs per request. Which tools could help?

---
## PART B — The event loop, `await`, and how to not break it

### 5. What the event loop is
One thread running a loop like:
```
while there are tasks:
    run the next READY task until it hits an `await` on something not ready yet
    park it; ask the OS "which sockets/timers are ready now?"
    mark those tasks READY again
```
A **coroutine** (`async def`) is a function that can pause. **`await` is the pause point**:
"I'm waiting for this; loop, go run someone else." This is **cooperative** multitasking: a
task only gives up control at an `await`. Threads are **preemptive**: the OS can interrupt
them anywhere.

### Snippet: async version of the same experiment
```python
import asyncio, time

async def fake_io(i):
    await asyncio.sleep(1)       # pause point: loop runs others meanwhile
    return i

async def main():
    t = time.perf_counter()
    results = await asyncio.gather(*(fake_io(i) for i in range(1000)))
    print(f"1000 'calls' in {time.perf_counter() - t:.1f}s on ONE thread")   # ~1.0s

asyncio.run(main())
```
1,000 concurrent waits on one thread. With threads you'd need 1,000 threads.

### 6. The cardinal sin: blocking the loop
```python
async def bad(i):
    time.sleep(1)                # NOT awaitable: freezes the whole loop for 1s
    return i
```
Swap that into the snippet: 1,000 calls now take **1,000 seconds**. In FastAPI this looks like
"every endpoint got slow when one user uploaded a PDF" (an L01 scenario question). Common
culprits: `requests.get`, `time.sleep`, sync DB drivers, PDF parsing, model inference, and
big JSON parsing inside `async def`.

**Fixes:**
- use an async library (`httpx.AsyncClient`, `asyncpg`, `redis.asyncio`)
- offload: `await asyncio.to_thread(parse_pdf, path)` (runs in a thread, loop stays free)
- CPU-heavy → a process / Celery worker
- in FastAPI: declare the endpoint with plain `def` → FastAPI runs it in a threadpool (L02)

### 7. Running many things: `gather` vs `TaskGroup`
```python
# gather: run concurrently, collect results in order
a, b = await asyncio.gather(fetch_user(), fetch_orders())

# TaskGroup (3.11+): structured concurrency. If one fails, the others are CANCELLED,
# and errors are raised together as an ExceptionGroup. Safer default.
async with asyncio.TaskGroup() as tg:
    t1 = tg.create_task(fetch_user())
    t2 = tg.create_task(fetch_orders())
user, orders = t1.result(), t2.result()
```
With `gather`, if one call fails the others keep running unattended (unless you handle it).
TaskGroup guarantees nothing is left running when the block exits.

### 8. Limiting concurrency + timeouts (you'll need these with LLM APIs)
```python
sem = asyncio.Semaphore(5)                    # max 5 LLM calls in flight

async def call_llm(prompt):
    async with sem:                           # 6th caller waits here
        async with asyncio.timeout(30):       # 3.11+: cancel if > 30s
            return await client.complete(prompt)
```
Semaphore = per-process limit. Across many processes/pods you need a shared limiter
(Redis), which is lesson D04.

### 9. Say it like a senior (from your LARP bank)
"Most of our latency was I/O: DB, embeddings, LLM calls. So async gave us concurrency
cheaply. The one CPU-heavy step, reranking, I moved to a thread so it couldn't block the
loop."

**Now:** run `/quiz L01` (9 questions from your bank, graded 0–2, with model answers).
