# S02b — Bytes vs text: what actually goes over the wire
> ⏱ 10 min · Day 1 · Passive + a few lines in a Python shell · Prev: S02 · Next: S03
> ➕ Added after the first plan: every later session uses `b"..."`, `.encode()` and `.decode()`.

## Words you need first
| Word | Plain meaning |
|---|---|
| **bit** | a single 0 or 1 |
| **byte** | 8 bits, so a number from 0 to 255. The unit everything on a network is measured in. |
| **character** | one letter/symbol as a human sees it: `a`, `é`, `₹`, `😀` |
| **encoding** | the agreed rulebook for turning characters into bytes and back |
| **ASCII** | an old rulebook: 128 characters (English letters, digits, punctuation), 1 byte each |
| **UTF-8** | today's standard rulebook: every character in every language. ASCII characters still take 1 byte; others take 2–4. |
| **`\xc3`** | how Python *shows* a byte that isn't a printable ASCII character: `\x` + two hex digits. `\xc3` = 195. |
| **`Content-Length`** | (preview of S05) a line in an HTTP message saying "the body is N **bytes** long" |
| **400** | (preview of S05) the HTTP reply code for "bad request: what you sent me is broken" |

## The idea
Networks, files and sockets only move **bytes**: numbers 0–255. Python's `str` holds **text**
(characters). To send text you must **encode** it into bytes; to read bytes as text you must
**decode** them. Both sides have to agree on *how*, which is the **encoding**. On the web that's
almost always **UTF-8**.

```
 "héllo"  ──.encode("utf-8")──>  b'h\xc3\xa9llo'  ──network──>  b'h\xc3\xa9llo'  ──.decode("utf-8")──>  "héllo"
   str (5 characters)              bytes (6 bytes)                                          str
```

## Try it (open `python` in a terminal)
```python
>>> s = "héllo"
>>> b = s.encode("utf-8")
>>> b
b'h\xc3\xa9llo'          # é became TWO bytes: \xc3 \xa9
>>> len(s), len(b)
(5, 6)                   # 5 characters, 6 bytes  <- why HTTP Content-Length counts BYTES
>>> b.decode("utf-8")
'héllo'
>>> b"GET / HTTP/1.1"    # b"..." is a bytes literal: only plain ASCII characters allowed inside
b'GET / HTTP/1.1'
>>> "abc" + b"abc"       # TypeError: can't mix str and bytes; the classic socket-code error
>>> b"\xff".decode("utf-8")   # UnicodeDecodeError: not valid UTF-8 (a client can send you anything!)
```

## Rules of thumb for backend code
1. **At the edges, bytes. In the middle, str.** Decode right after reading from a socket or
   file, and encode right before writing.
2. **Measure lengths after encoding.** `len(text)` ≠ number of bytes on the wire.
3. **Never trust incoming bytes to be valid UTF-8.** Wrap `.decode()` in `try/except
   UnicodeDecodeError` and answer with a 400. (A01's tests send `b"\xff\xfe"` on purpose.)
4. ASCII (English letters, digits, `\r\n`) is 1 byte per character in UTF-8, which is why
   HTTP headers are easy to handle as bytes.

## Check yourself
1. `"₹100".encode("utf-8")` has how many bytes? (Guess, then check in Python. ₹ is not ASCII.)
   b'\xe2\x82\xb9100'
2. Your server reads `data = conn.recv(1024)` and does `data.split("\r\n")`. What error do you
   get, and what are two ways to fix it?
   i don't know you must help
3. Why must `Content-Length` be computed from the encoded body, not the string?
because the encoded length is different
