# Learning journal (append-only archive)

Per-session detail: taught, learnt (evidence), struggled with, insights. **Don't read this at
session start**; the live summary is the "Carry forward" block in `progress.md`. Open this only
when the learner asks ("what did I struggle with in caching?") or to look up a specific past
session. Append new entries at the bottom without reading the file.

<!-- entry format:
### YYYY-MM-DD (~N min) · S01, S02
- Taught: ...
- Learnt (evidence): ...
- Struggled with: ... (and what made it click, or "not yet")
- Insights for next time: ...
- Scores: ...
- Added to tracker: ...
-->

### 2026-10-31 [personal] · planning (no lesson)
- Taught: nothing; re-planned around the real evening (gym with a physio-friend trainer, family until ~22:30).
- Decided: planner v5. Weeknights 22:30–00:00 project, 00:00–01:00 LARP; DSA 18:15–19:15 at the office
  (normal days); Fundamentals FN01–FN15 in 5–10 min office breaks; SHIP week after stages 1–5; ends Sun 4 Jul 2027.
- Insights for next time: the learner wants local files (not online docs) and practical plans that don't
  spread thin; 0 hours logged so far, so the first win is the doculens `/health` commit.
- Added to tracker: ➕ 2b Fundamentals FN01–FN15; v5 change-log row.

## 2026-11-01 [personal] · planning follow-up
- Roadmap docx made v5-synced (`Marathon_Roadmap_v5.docx`, v4 archived); Word-checked, TOC refreshed, 89 pages.
- Council verdicts #1-#3 + final decisions saved to `council-verdicts.md`; online council doc deleted.

- 2026-11-02 [work] S01 mid-session: Q2 struggle, unclear why a 127.0.0.1 listener cannot be reached from another machine. Re-explained as "one machine has several network cards (doors)"; experiment: python http.server bound to 127.0.0.1 vs 0.0.0.0, curl own Wi-Fi IP.
- 2026-11-02 [work] S02: could describe the handshake but could not turn it into a latency number (didn't count round trips: handshake 1 RTT + request/response 1 RTT = 400 ms). Re-check with a 2-connection variant later.
- 2026-11-02 [work] S02 check: Q1 misconception "reliable => one recv gets the whole send" (key S02 idea, must fix before S03/S04). Q3 answered "byte stream" for recv()==b"" (did not know = peer closed/EOF). Q2 1/2.

## 2026-11-02 [work] · S01 + S02 (office breaks)
- S01 IP/ports/packets 5/6: ran nslookup/netstat; spotted own Postgres on 0.0.0.0:5432. Bind address only clicked with the "OS listening table, match (IP, port) like a dict key" framing.
- S02 TCP 4/6 (+ round-trip q 1/2): HELLO/WORLD recv demo made "stream, not messages" land; predicted the merge case on its own.
- Tutor fixes from learner feedback: questions end the message (no answer after it); define every term first (S02 got a glossary); turned off Claude Code prompt suggestions (they pre-filled answers).
- Removed the user-level /council skill. Created missing CLAUDE.local.md (work laptop). S01 Try-it now uses `curl.exe`.
- 2026-11-02 [work] S02b warm-up: RTT re-check (2 sequential new connections) answered 400 ms; still not counting per-connection cost.
- 2026-11-02 [work] S02b 4/6: predicted len 5/6 and ₹100=6 bytes; needed scaffolding for split(b"
") / .decode() fixes; bad-UTF-8 answer missed the 400 reply and the uncaught-crash consequence.

## 2026-11-06 [work] · S03 started (stopped early), communication track added
- Added an opt-in "delivery track" to /quiz (spoken transcript + seconds, wpm, defensive phrases, stakeholder round). OFF until learner says "delivery on".
- Learner is ~4 days behind PLAN.md; chose not to reschedule anything: just continue in order.
- S03: glossary + socket shape shown; S01 bind re-check question (127.0.0.1 vs colleague on Wi-Fi) asked but not answered yet. Ask it first next time.
- Stopped early (job-market news); no sessions finished.
