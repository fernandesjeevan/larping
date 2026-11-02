# Session brief (the ONLY file read at session start; keep it under ~40 lines)

**Now:** S02b Bytes vs text · `net101/S02b-bytes-vs-text.md` (S01 5/6, S02 4/6 done 2026-11-02)
**Open exercises:** none started (N01 framing, A01 LAB00 later)

## Up next (max 4)
1. S02b ➕ Bytes vs text · `net101/S02b-...`
2. S03 Sockets hands-on · `net101/S03-...`
3. S04 Framing · `net101/S04-framing.md`
4. S05 HTTP is text on TCP · `net101/S05-...`

## Carry forward (struggles, insights, owed follow-ups; rolling, max ~8 bullets)
- Learner is a self-described networking beginner: start from zero, analogy first, then runnable code.
- Sittings are 10–60 min on work breaks; always stop at a clean point.
- Planner is v5 (v4 in archive/): LARP 00:00–01:00, project 22:30–00:00, DSA 18:15 office, Fundamentals
  FN01–FN15 in office breaks from Wed 4 Nov (`/quiz FN01`, score with `update_planner.py fund`).
- S01: bind address (127.0.0.1 vs 0.0.0.0) needed 2 re-explanations; the "OS listening table, match (IP, port)
  like a dict key" framing clicked, doors analogy didn't. Re-check in S03 when they bind a socket.
- Learner wants questions to END the message: never reveal or pre-explain the answer (S02 feedback).
- S02: round-trip counting weak (new conn = handshake RTT + request RTT); re-check with a variant. "recv returns what's in the
  tray now; b'' = peer closed" landed after the HELLO/WORLD demo. Scan session files for undefined terms first.
- On work laptop PowerShell `curl` = Invoke-WebRequest; always write `curl.exe`.

## Last 3 scores
| Date | What | Score |
|---|---|---|
| 2026-11-02 | S02 TCP | 4/6 (+ RTT q 1/2) |
| 2026-11-02 | S01 IP, ports, packets | 5/6 |
