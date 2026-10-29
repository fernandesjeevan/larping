# A01 — Serving HTTP with nothing but a socket
> Maps to: LARP L01 (async/await, event loop) · Saturday LAB00 · Project: what uvicorn does under DocuLens's FastAPI
> Time: ~60–90 min in 2–3 sittings · Stage: 0–1
> **Before this:** `net101/S01`–`S05` and the N01 framing exercise. The theory below recaps
> them; if it feels new, go back. You may copy your own N01 functions into this `solution.py`.

## Why you care
Every FastAPI endpoint you write sits on a server loop like the one you're about to build. When
an interviewer asks "why async?", "what's a worker?", or "why did p99 latency spike when one
client was slow?", the answer is in this lesson. Once you've written the loop yourself, you can
explain the trade-offs from experience instead of reciting them.

## Theory

### 1. HTTP is just text over a TCP connection
TCP gives you a reliable, ordered **stream of bytes** between two machines. HTTP/1.1 is a text
format written onto that stream. There are no "messages" at the TCP level; HTTP adds its own
framing on top (a blank line ends the headers; `Content-Length` says how long the body is).

A full request, byte for byte (`\r\n` = CRLF line endings):
```
GET /health HTTP/1.1\r\n          <- request line: METHOD SP PATH SP VERSION
Host: localhost:8080\r\n          <- headers: Name: value
User-Agent: curl/8.4\r\n
\r\n                              <- empty line = end of headers
```
A full response:
```
HTTP/1.1 200 OK\r\n               <- status line: VERSION SP CODE SP REASON
Content-Type: application/json\r\n
Content-Length: 15\r\n            <- body length in BYTES, not characters
Connection: close\r\n
\r\n
{"status":"ok"}                   <- body, exactly 15 bytes
```

### Snippet: be the browser
Run this in a Python shell. It's a raw HTTP client: no `requests`, no `urllib`.
```python
import socket

s = socket.create_connection(("example.com", 80), timeout=5)
s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n")
chunks = []
while True:
    data = s.recv(4096)   # returns b"" when the server closes the connection
    if not data:
        break
    chunks.append(data)
s.close()
raw = b"".join(chunks)
head, _, body = raw.partition(b"\r\n\r\n")
print(head.decode())
print(len(body), "body bytes")
```
Note the loop around `recv`. Why do you think a single `recv(4096)` isn't enough? Keep that
question in mind.

### 2. The server side of a socket
A server socket does four things: **bind** to an address, **listen**, **accept** a connection
(blocks until a client arrives and returns a *new* socket for that client), then talk on that new
socket with `recv`/`sendall`.

### Snippet: the smallest server that exists
```python
import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # restart without "address in use"
srv.bind(("127.0.0.1", 8080))
srv.listen()
print("listening on 8080")
conn, addr = srv.accept()        # BLOCKS until someone connects
print("client", addr, "sent:", conn.recv(1024))
conn.sendall(b"hi\n")
conn.close()
srv.close()
```
Run it, then in another terminal run `curl http://127.0.0.1:8080/`. curl will complain because
`hi` isn't valid HTTP. Your job is to fix that.

### 3. Status codes you need today
| Code | Meaning | When |
|---|---|---|
| 200 OK | it worked | known path, GET |
| 400 Bad Request | can't parse what you sent | garbage request line |
| 404 Not Found | path doesn't exist | unknown path |
| 405 Method Not Allowed | path exists, method doesn't | POST to `/` (add an `Allow: GET` header) |

### 4. bytes vs str
Sockets speak `bytes`. `"héllo"` is 5 characters but `"héllo".encode()` is **6 bytes**.
`Content-Length` counts bytes. Encode first, then measure.

## Check yourself
1. TCP guarantees order and delivery. Why does HTTP still need `Content-Length` (or a blank line)
   to know where a message ends?
2. `accept()` returns a new socket. Why not just talk on the listening socket?

Answer both in chat before starting the challenge.

## Challenge — stage 1 (brute force)
Implement in `solution.py`:

- `handle_request(raw: bytes) -> bytes`: a **pure function** that takes the raw request bytes
  and returns raw response bytes. Routes:
  - `GET /` → 200, `Content-Type: text/plain; charset=utf-8`, body `hello, backend`
  - `GET /health` → 200, `Content-Type: application/json`, body `{"status": "ok"}`
  - `GET /echo?msg=<text>` → 200, text/plain, body = the decoded `msg` value
    (`urllib.parse` is allowed)
  - known path with another method → 405 with `Allow: GET`
  - unknown path → 404
  - unparseable request line → 400
  - every response has the status line, `Content-Type`, a correct `Content-Length`, and
    `Connection: close`
- `run_server(host, port, ready=None)`: listen on `host:port`, call `ready.set()` once listening
  (if given), and serve connections **forever**: accept → read the request → `handle_request`
  → send → close.

Rules: build the simplest thing that works. No threads, no asyncio, no frameworks; just
`socket` from the stdlib. Don't optimise yet.

Run: `python -m pytest lessons/A01-http-from-sockets -q`
Try it for real: `python lessons/A01-http-from-sockets/solution.py` then `curl -i http://127.0.0.1:8080/health`

When it's green, type `/check`.

<!-- STAGE 3 (pattern reveal) is appended below by the tutor after /check rounds -->
