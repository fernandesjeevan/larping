# S04 — Framing: where does a message end?
> ⏱ 15–25 min · Day 1 · Hands-on exercise with tests · Prev: S03 · Next: S05

## The problem
TCP hands you a stream of bytes (S02). Your application thinks in **messages**: one HTTP
request, one Redis command, one Postgres query. Something has to cut the stream into messages.
That's **framing**, and there are only three ways to do it:

| Strategy | How the reader knows the message ended | Used by |
|---|---|---|
| **Delimiter** | a special byte sequence marks the end | HTTP headers end with `\r\n\r\n`; Redis lines end with `\r\n` |
| **Length prefix** | the message starts by saying how long it is | HTTP body (`Content-Length: 15`), Postgres wire protocol, Kafka |
| **Close the connection** | end of stream (`recv` → `b""`) = end of message | old HTTP/1.0, `Connection: close` responses |

HTTP/1.1 uses **two** of them: a delimiter for the headers, then a length prefix for the body.

## Snippet: the bug everyone writes first
```python
data = conn.recv(1024)          # "one recv = one request"... wrong (S02)
request = data.decode()
```
It works in local testing because a small request on localhost usually arrives in one piece.
It breaks in production when requests are big, the network is slow, or a client sends in chunks.

## Snippet: the correct shape (a read loop with a buffer)
```python
buf = b""
while DELIMITER not in buf:
    chunk = conn.recv(4096)
    if not chunk:               # peer closed before finishing the message
        raise ConnectionError("closed mid-message")
    buf += chunk
message, _, leftover = buf.partition(DELIMITER)
```
Notice the **leftover**: the bytes after the delimiter may already belong to the *next*
message (or the body). Never throw it away.

## Exercise (your first code: brute force allowed)
Open `lessons/N01-framing/`. You implement three small functions that read from a *fake
socket* (a test object that hands out bytes in awkward chunks, the way a real network does):

- `recv_until(sock, delimiter, max_bytes)` → `(message, leftover)`: read until the delimiter;
  raise `ValueError` if more than `max_bytes` arrive without one (otherwise an attacker can make
  you buffer forever).
- `recv_exact(sock, n, already=b"")` → exactly `n` bytes, starting with what you already have.
- `read_http_message(sock)` → `(head_bytes, body_bytes)`: headers via `recv_until(b"\r\n\r\n")`,
  then the body via `Content-Length` and `recv_exact`. (No Content-Length = empty body.)

Run: `python -m pytest lessons/N01-framing -q` → then `/check` (or just tell me it's green).

## Check yourself
1. Name the 3 framing strategies and one protocol for each.
2. Why does `recv_until` need a `max_bytes` limit?
3. After reading HTTP headers you have some leftover bytes. What are they?
