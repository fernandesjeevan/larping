# Session brief (the ONLY file read at session start; keep it under ~40 lines)

**Now:** S03 Sockets hands-on · `net101/S03-sockets-hands-on.md` (started 2026-11-06: glossary + shape done;
  bind re-check Q pending, then the echo server code-along)
**Open exercises:** none started (N01 framing, A01 LAB00 later)
**Checkpoint (May 2027):** review the route using real interview feedback. Real interviews start Feb 2027.
  The route stays fixed until then; new doubts or roadmap ideas get parked for the checkpoint.

## Up next (max 4)
1. S03 Sockets hands-on · `net101/S03-...`
2. S04 Framing · `net101/S04-framing.md`
3. S05 HTTP is text on TCP · `net101/S05-...`
4. L01 Part A (Tue 3) · `larp/L01-async-await.md`

## Carry forward (struggles, insights, owed follow-ups; rolling, max ~8 bullets)
- **2026-11-14 PLANNER RESET (the only one):** 0 of Nov 4-14 planned items done. Re-flowed: D01 = TODAY Sat 14 Nov,
  Fridays = holiday, no BUF days/weekly mocks, must-finish = planned (no buffer); ends Wed 14 Jul 2027, AI-102 still 20 Feb.
  Learner said a repeat is NOT acceptable: refuse a 2nd reset. Pattern = prepping instead of starting; rule = 10-min minimum, never zero.
- **2026-11-14 PATH DECIDED: SWE (backend + AI), no second thoughts.** Govt-job idea parked until ~Nov 2028 at the earliest;
  if it resurfaces before then, it's the "prepare instead of start" loop: answer "parked" and point back to today's card.
- Learner is a self-described networking beginner: start from zero, analogy first, then runnable code.
- Sittings are 10–60 min on work breaks; always stop at a clean point.
- Planner is v5 (v4 in archive/): LARP 00:00–01:00, project 22:30–00:00, DSA 18:15 office, Fundamentals
  FN01–FN15 in office breaks from Wed 4 Nov (`/quiz FN01`, score with `update_planner.py fund`).
- S01: bind address (127.0.0.1 vs 0.0.0.0) needed 2 re-explanations; the "OS listening table, match (IP, port)
  like a dict key" framing clicked, doors analogy didn't. Re-check in S03 when they bind a socket.
- Learner wants questions to END the message: never reveal or pre-explain the answer (S02 feedback).
- S02b: str vs bytes TypeError fixes needed scaffolding; answers "exception handling" vaguely: push for which
  exception + what reply (400). RTT re-check 2 conns: 400 then 800 after nudge.
- S02: round-trip counting weak (new conn = handshake RTT + request RTT); re-check with a variant. "recv returns what's in the
  tray now; b'' = peer closed" landed after the HELLO/WORLD demo. Scan session files for undefined terms first.
- /quiz has an opt-in delivery track ("delivery on"): typed or spoken answers; learner self-reviews recordings.
- On work laptop PowerShell `curl` = Invoke-WebRequest; always write `curl.exe`.

## Last 3 scores
| Date | What | Score |
|---|---|---|
| 2026-11-02 | S02b Bytes vs text | 4/6 |
| 2026-11-02 | S02 TCP | 4/6 (+ RTT q 1/2) |
