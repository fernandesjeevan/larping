"""N01 — Framing: cut a TCP byte stream into messages.

`sock` is anything with a .recv(n) method that behaves like a real socket:
returns up to n bytes, possibly fewer, and b"" when the peer has closed.
"""


def recv_until(sock, delimiter: bytes, max_bytes: int = 8192) -> tuple[bytes, bytes]:
    """Read until `delimiter` appears. Return (message_without_delimiter, leftover_after_it).

    Raise ConnectionError if the peer closes before the delimiter arrives.
    Raise ValueError if more than `max_bytes` are buffered without finding the delimiter.
    """
    raise NotImplementedError


def recv_exact(sock, n: int, already: bytes = b"") -> bytes:
    """Return exactly n bytes, using `already` first, then reading the rest from sock.

    Raise ConnectionError if the peer closes before n bytes arrive.
    (If `already` is longer than n, return only the first n bytes.)
    """
    raise NotImplementedError


def read_http_message(sock) -> tuple[bytes, bytes]:
    """Read one HTTP/1.1 message. Return (head, body).

    head = everything before b"\\r\\n\\r\\n" (request/status line + headers).
    body = exactly Content-Length bytes (header name is case-insensitive); empty if absent.
    """
    raise NotImplementedError
