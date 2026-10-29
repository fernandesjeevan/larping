# S05 — HTTP is just text written into a TCP connection
> ⏱ 15 min · Day 2 · Passive + curl · Prev: S04 · Next: A01 (LAB00)

## Where we are
S02: TCP gives a byte stream. S04: protocols frame messages on top of it. **HTTP/1.1 is that
kind of protocol, and it's plain text.** You can type it by hand.

## 1. A request
```
POST /documents?workspace=7 HTTP/1.1\r\n     <- request line: METHOD  TARGET  VERSION
Host: api.doculens.dev\r\n                   <- headers: "Name: value", one per line
Content-Type: application/json\r\n
Content-Length: 18\r\n                       <- body length in BYTES (S04: length prefix)
\r\n                                         <- blank line = end of headers (S04: delimiter)
{"name": "policy"}                           <- body: exactly 18 bytes
```
- **Method:** what you want to do. `GET` read, `POST` create/action, `PUT` replace,
  `PATCH` partial update, `DELETE` remove.
- **Target:** path + optional query string (`?workspace=7`). Special characters are
  percent-encoded: a space becomes `%20`.
- **Headers:** metadata. `Host` is mandatory in HTTP/1.1, because one IP can host many sites.

## 2. A response
```
HTTP/1.1 201 Created\r\n                     <- status line: VERSION  CODE  REASON
Content-Type: application/json\r\n
Content-Length: 26\r\n
\r\n
{"id": 42, "name": "policy"}
```
Status code families: **2xx** worked · **3xx** go elsewhere · **4xx** *you* (client) messed up ·
**5xx** *we* (server) messed up. The ones you'll use constantly:
`200 OK`, `201 Created`, `202 Accepted` (queued for later), `204 No Content`,
`400 Bad Request`, `401 Unauthorized` (who are you?), `403 Forbidden` (I know you; no),
`404 Not Found`, `405 Method Not Allowed`, `409 Conflict`, `422 Unprocessable` (FastAPI's
validation error), `429 Too Many Requests`, `500 Internal Server Error`, `502 Bad Gateway`,
`503 Service Unavailable`, `504 Gateway Timeout`.

## 3. Keep-alive (why connections are reused)
The TCP handshake costs a round trip (S02). HTTP/1.1 therefore **keeps the connection open** by
default and sends the next request on it; that's why framing matters so much. `Connection:
close` means "one request and done", which is simpler and is what your LAB00 server will do.

## 4. HTTPS in one paragraph
HTTPS = the same HTTP text, but inside **TLS**: an encryption layer between TCP and HTTP. TLS
adds its own handshake (certificates prove the server's identity, then keys are agreed), so the
bytes on the wire are unreadable. Your code still reads plain HTTP after decryption. In production
TLS usually ends at the load balancer / ingress ("TLS termination"), and the hop to your FastAPI
app is plain HTTP inside the private network.

## Try it
```powershell
curl -v http://example.com/          # > lines = what curl SENT, < lines = what came back
curl -v https://example.com/         # spot the TLS handshake lines before the HTTP
curl -i -X POST http://httpbin.org/post -H "Content-Type: application/json" -d "{\"a\":1}"
```

## Check yourself
1. Which two framing strategies does HTTP/1.1 use, and for which parts of the message?
2. 401 vs 403?
3. Why would a server prefer keep-alive connections?
4. Where does TLS usually terminate in a cloud deployment, and what does the app then receive?
