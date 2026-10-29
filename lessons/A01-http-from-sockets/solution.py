"""A01 — Serving HTTP with nothing but a socket.

Your code goes here. Stdlib only.
"""
import socket
import threading


def handle_request(raw: bytes) -> bytes:
    """Parse one raw HTTP/1.1 request and return the raw HTTP response bytes."""
    raise NotImplementedError


def run_server(host: str = "127.0.0.1", port: int = 8080, ready: threading.Event | None = None) -> None:
    """Listen on host:port and serve connections forever. Call ready.set() once listening."""
    raise NotImplementedError


if __name__ == "__main__":
    run_server()
