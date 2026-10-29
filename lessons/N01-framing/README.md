# N01 — Framing exercise
> Theory: `net101/S04-framing.md` · Used in: A01 (LAB00) · ⏱ 15–25 min

Implement the three functions in `solution.py`. Tests use a `FakeSocket` that hands out bytes
in nasty chunks (sometimes one byte at a time), the way a real network can.

Run: `python -m pytest lessons/N01-framing -q`

Order: `recv_until` → `recv_exact` → `read_http_message` (which uses the other two).
Stuck? `/hint`.
