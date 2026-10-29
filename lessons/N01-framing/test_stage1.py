"""N01 framing tests. FakeSocket hands out bytes in awkward chunks, like a real network."""
import pytest

from solution import read_http_message, recv_exact, recv_until


class FakeSocket:
    def __init__(self, *chunks: bytes):
        self.chunks = list(chunks)
        self.recv_calls = 0

    def recv(self, n: int) -> bytes:
        self.recv_calls += 1
        if not self.chunks:
            return b""  # peer closed
        chunk = self.chunks.pop(0)
        if len(chunk) > n:  # honour the "up to n bytes" contract
            self.chunks.insert(0, chunk[n:])
            chunk = chunk[:n]
        return chunk


def one_byte_at_a_time(data: bytes) -> FakeSocket:
    return FakeSocket(*[bytes([b]) for b in data])


# ---------- recv_until ----------

def test_until_single_chunk():
    assert recv_until(FakeSocket(b"PING\r\n"), b"\r\n") == (b"PING", b"")


def test_until_split_across_chunks():
    assert recv_until(FakeSocket(b"PI", b"NG\r", b"\n"), b"\r\n") == (b"PING", b"")


def test_until_delimiter_split_in_half():
    sock = FakeSocket(b"GET / HTTP/1.1\r\n\r", b"\n")
    assert recv_until(sock, b"\r\n\r\n") == (b"GET / HTTP/1.1", b"")


def test_until_keeps_leftover():
    sock = FakeSocket(b"first\r\nsecond\r\n")
    msg, leftover = recv_until(sock, b"\r\n")
    assert msg == b"first"
    assert leftover == b"second\r\n", "bytes after the delimiter belong to the next message"


def test_until_one_byte_at_a_time():
    assert recv_until(one_byte_at_a_time(b"hello\r\n"), b"\r\n") == (b"hello", b"")


def test_until_peer_closes_early():
    with pytest.raises(ConnectionError):
        recv_until(FakeSocket(b"no delimiter here"), b"\r\n")


def test_until_too_big():
    sock = FakeSocket(*[b"A" * 1000 for _ in range(100)])
    with pytest.raises(ValueError):
        recv_until(sock, b"\r\n", max_bytes=4096)
    assert sock.recv_calls < 20, f"kept reading {sock.recv_calls} times after passing the limit"


# ---------- recv_exact ----------

def test_exact_from_chunks():
    assert recv_exact(FakeSocket(b"ab", b"cd", b"ef"), 5) == b"abcde"


def test_exact_uses_already():
    sock = FakeSocket(b"llo")
    assert recv_exact(sock, 5, already=b"he") == b"hello"


def test_exact_already_enough():
    sock = FakeSocket()
    assert recv_exact(sock, 3, already=b"abcdef") == b"abc"
    assert sock.recv_calls == 0, "didn't need the network at all"


def test_exact_zero():
    assert recv_exact(FakeSocket(), 0) == b""


def test_exact_peer_closes_early():
    with pytest.raises(ConnectionError):
        recv_exact(FakeSocket(b"abc"), 10)


# ---------- read_http_message ----------

def test_http_no_body():
    sock = FakeSocket(b"GET /health HTTP/1.1\r\nHost: x\r\n\r\n")
    head, body = read_http_message(sock)
    assert head == b"GET /health HTTP/1.1\r\nHost: x"
    assert body == b""


def test_http_body_in_same_chunk_as_headers():
    sock = FakeSocket(b"POST /echo HTTP/1.1\r\nContent-Length: 5\r\n\r\nhello")
    _, body = read_http_message(sock)
    assert body == b"hello"


def test_http_body_dribbles_in():
    raw = b"POST /echo HTTP/1.1\r\ncontent-length: 11\r\n\r\nhello world"
    _, body = read_http_message(one_byte_at_a_time(raw))
    assert body == b"hello world"


def test_http_body_is_bytes_not_chars():
    payload = "héllo".encode()  # 6 bytes
    raw = b"POST / HTTP/1.1\r\nContent-Length: 6\r\n\r\n" + payload
    _, body = read_http_message(FakeSocket(raw[:40], raw[40:]))
    assert body == payload
