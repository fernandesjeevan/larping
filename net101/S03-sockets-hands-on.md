# S03 — Sockets: your program's handle on a TCP connection
> ⏱ 15–20 min · Day 1 · Hands-on (2 terminals, Python stdlib only) · Prev: S02b · Next: S04

## What a socket is
A **socket** is the object your OS hands your program so it can use TCP. You write bytes into
it and read bytes out of it. Every database driver, HTTP client and web server is built on
sockets.

## The server's 4 calls and the client's 1
```
 SERVER                                   CLIENT
 s = socket()          make a socket
 s.bind((ip, port))    claim an address
 s.listen()            "I accept calls"
 conn, addr = s.accept()  <── handshake ──  c = socket.create_connection((ip, port))
   # accept() BLOCKS until a client connects, then returns a NEW socket `conn`
   # just for that client. The listening socket `s` keeps waiting for others.
 conn.recv(n)  /  conn.sendall(b)   <── bytes ──>   c.sendall(b) / c.recv(n)
 conn.close()                                        c.close()
```
Why a **new** socket per client? `s` is the receptionist answering the main line; `conn` is the
private line to one caller. One receptionist, many private lines.

## The 3 rules of `recv(n)`
1. It returns **up to** `n` bytes: possibly fewer, possibly 1. (Stream, S02!)
2. It **blocks** (waits) until at least 1 byte arrives.
3. It returns `b""` when the other side closed: end of stream.

And for sending: use `sendall(data)`, not `send(data)`. `send` may write only part of the
data and return how much it wrote; `sendall` loops until everything is written.

## Try it: an echo server (copy into two files, run in two terminals)

`echo_server.py`
```python
import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 + TCP
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 9000))
srv.listen()
print("waiting on 127.0.0.1:9000 ...")

while True:
    conn, addr = srv.accept()          # blocks here until a client connects
    print("connected:", addr)          # addr = the client's (ip, port), a random high port
    while True:
        data = conn.recv(1024)         # blocks until bytes arrive
        if not data:                   # b"" -> client closed
            print("client left")
            break
        print("got", data)
        conn.sendall(data.upper())     # echo back, shouting
    conn.close()
```

`echo_client.py`
```python
import socket
import time

c = socket.create_connection(("127.0.0.1", 9000), timeout=5)
c.sendall(b"hello ")
time.sleep(0.5)
c.sendall(b"world")
print("reply:", c.recv(1024))
time.sleep(0.5)
print("reply:", c.recv(1024))
c.close()
```

Run `python echo_server.py` in terminal 1 and `python echo_client.py` in terminal 2.

**Experiments (spend 5 min, they teach more than the reading):**
1. Remove `time.sleep(0.5)` between the two `sendall`s. Does the server now print one `got` or
   two? Run it several times. That's S02's "stream, not messages" in action.
2. Start the client **twice at the same time** (two terminals). The second one waits until the
   first finishes. Why? (Hint: where is the server stuck while client 1 is connected?) Hold on
   to this; it's the core of LAB00 and of L01 async.
3. Stop the server, run the client: `ConnectionRefusedError`. Nothing is listening on that port.

No Python handy? Same idea with curl: run the server, then `curl http://127.0.0.1:9000/`. The
server prints the raw HTTP request curl sent. That's a preview of S05.

## Check yourself
1. What's the difference between the listening socket and the socket `accept()` returns?
2. Why `sendall` instead of `send`?
3. Experiment 2: why did client 2 have to wait? What are two ways you could fix it?
