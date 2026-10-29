# S02 — TCP: turning unreliable packets into a reliable stream
> ⏱ 15 min · Day 1 · Passive · Prev: S01 · Next: S02b (bytes vs text)

## The problem TCP solves
From S01: packets get lost, reordered, duplicated. Your code doesn't want to deal with that.
It wants: "what I write on one end comes out **exactly the same, in the same order**, on the
other end, or I get an error." That is what **TCP** (Transmission Control Protocol) provides.

## 1. Connection first: the 3-way handshake
Before any data moves, both sides agree to talk:
```
 client                         server (listening on :8000)
   | ---- SYN (let's talk) -----> |
   | <--- SYN-ACK (ok, you too) - |
   | ---- ACK (great) ----------> |
   |   connection ESTABLISHED     |
```
That costs **one round trip** before your first byte. From India to a US server that's about
200 ms. This is why connection reuse (keep-alive, connection pools) matters, and it comes up
again with DB pools in L02.

## 2. Reliability: numbering + acknowledgements + resend
- TCP numbers every **byte** it sends (sequence numbers).
- The receiver replies "I have everything up to byte 5,000" (**ACK**).
- No ACK within a timeout → the sender **retransmits**.
- The receiver uses sequence numbers to **reorder** and to **drop duplicates**.

Result: loss, reordering and duplication are handled for you, at the cost of extra latency
when packets are lost.

## 3. The most important sentence in this whole module
> **TCP is a stream of bytes, not a stream of messages.**

If the client does two writes, `send(b"HELLO")` and `send(b"WORLD")`, the server might `recv`:
```
b"HELLOWORLD"            # both in one go
b"HEL"  then b"LOWORLD"  # split in weird places
b"H" b"E" b"L" ...       # one byte at a time (legal!)
```
TCP keeps the **order** of the bytes but not where your writes started and ended. So **every
protocol on top of TCP has to mark where its own messages end** (this is called *framing*;
see S04). HTTP does it with a blank line and `Content-Length`. Most beginner socket bugs are
"I assumed one recv = one message."

## 4. Closing
Either side says "I'm done sending" (**FIN**). The other side, when reading, sees **end of
stream**; in Python, `recv()` returns `b""`. A **RST** is the rude version, "connection reset
by peer", which you'll see in logs when a server crashes or a load balancer kills a connection.

## 5. UDP: the other option (one paragraph)
UDP sends individual packets with **no** handshake, ordering, or resend. It's fast and fine for
video calls, DNS and games, where a late packet is useless anyway. Backends almost always use TCP.
(HTTP/3 runs on QUIC over UDP and reimplements reliability itself; that's trivia-level for you.)

## Interview-ready line
"TCP gives me a reliable, ordered byte stream over an unreliable packet network using sequence
numbers, ACKs and retransmission. But it's a stream, not messages, so the application protocol
has to do its own framing, like HTTP's headers terminator and Content-Length."

## Check yourself
1. Client sends 2 KB in one `send()`. The server calls `recv(4096)` once. Is it guaranteed to
   get all 2 KB? Why or why not?
2. Why does opening a new DB connection per request hurt latency, even on a fast network?
3. In Python, what does `recv()` returning `b""` mean?
