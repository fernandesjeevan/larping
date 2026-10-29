"""Stage 1: does the brute-force server work at all?"""
import json
import socket
import threading

import pytest

from solution import handle_request, run_server


def parse_response(raw: bytes):
    head, sep, body = raw.partition(b"\r\n\r\n")
    assert sep, f"response has no blank line ending the headers: {raw[:200]!r}"
    lines = head.decode("iso-8859-1").split("\r\n")
    version, code, *reason = lines[0].split(" ")
    assert version == "HTTP/1.1", f"bad status line: {lines[0]!r}"
    headers = {}
    for line in lines[1:]:
        name, _, value = line.partition(":")
        headers[name.strip().lower()] = value.strip()
    return int(code), headers, body


def req(method: str, target: str) -> bytes:
    return f"{method} {target} HTTP/1.1\r\nHost: test\r\n\r\n".encode()


# ---------- handle_request (pure function) ----------

def test_root_returns_hello():
    code, headers, body = parse_response(handle_request(req("GET", "/")))
    assert code == 200
    assert body == b"hello, backend"
    assert headers["content-type"].startswith("text/plain")


def test_health_returns_json():
    code, headers, body = parse_response(handle_request(req("GET", "/health")))
    assert code == 200
    assert headers["content-type"].startswith("application/json")
    assert json.loads(body) == {"status": "ok"}


def test_echo_decodes_query():
    code, _, body = parse_response(handle_request(req("GET", "/echo?msg=hi%20there")))
    assert code == 200
    assert body == b"hi there"


def test_content_length_counts_bytes_not_chars():
    code, headers, body = parse_response(handle_request(req("GET", "/echo?msg=h%C3%A9llo")))
    assert code == 200
    assert body == "héllo".encode()
    assert int(headers["content-length"]) == len(body) == 6, "Content-Length must count bytes"


def test_unknown_path_404():
    code, headers, body = parse_response(handle_request(req("GET", "/nope")))
    assert code == 404
    assert int(headers["content-length"]) == len(body)


def test_wrong_method_405_with_allow():
    code, headers, _ = parse_response(handle_request(req("POST", "/health")))
    assert code == 405
    assert headers.get("allow") == "GET"


@pytest.mark.parametrize("garbage", [b"", b"hello\r\n\r\n", b"GET\r\n\r\n", b"\xff\xfe\r\n\r\n"])
def test_garbage_400(garbage):
    code, _, _ = parse_response(handle_request(garbage))
    assert code == 400


def test_connection_close_header():
    _, headers, _ = parse_response(handle_request(req("GET", "/")))
    assert headers.get("connection", "").lower() == "close"


# ---------- run_server (real sockets) ----------

@pytest.fixture(scope="module")
def server():
    probe = socket.socket()
    probe.bind(("127.0.0.1", 0))
    port = probe.getsockname()[1]
    probe.close()
    ready = threading.Event()
    t = threading.Thread(target=run_server, args=("127.0.0.1", port, ready), daemon=True)
    t.start()
    assert ready.wait(5), "run_server never called ready.set()"
    return port


def fetch(port: int, target: str) -> bytes:
    with socket.create_connection(("127.0.0.1", port), timeout=5) as s:
        s.sendall(req("GET", target))
        chunks = []
        while data := s.recv(4096):
            chunks.append(data)
    return b"".join(chunks)


def test_server_serves_health(server):
    code, _, body = parse_response(fetch(server, "/health"))
    assert code == 200
    assert json.loads(body) == {"status": "ok"}


def test_server_handles_sequential_clients(server):
    for _ in range(5):
        code, _, body = parse_response(fetch(server, "/"))
        assert code == 200 and body == b"hello, backend"
