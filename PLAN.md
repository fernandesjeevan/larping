# Week 1 plan: Sun 1 Nov → Sun 8 Nov

**Scope of this repo:** backend patterns (labs) + LARP interview prep only. Project cards
(D01–D05) happen in your evenings and are tracked there, not here.

**Restarted on Sat 31 Oct:** nothing from the old Thu 29 – Sun 1 catch-up was done, so the whole
Excel marathon moved **+1 week** (D01 + L01 now Wed 4 Nov, LAB00 Sat 7 Nov, ends Sun 30 May).
Sun 1 – Tue 3 are a prep mini-week: networking basics from zero so L01 and LAB00 make sense.
From Wed 4 the sessions line up with the planner days again (L01 Wed, L02 Thu, mock Fri, LAB00 Sat).

Every session is **10–20 min** so it fits a break. Do them in order; tick as you go.
Long free stretch? Chain several. Only 10 minutes? Do one.

| ✓ | # | Day | Session | ⏱ | Type | File |
|---|---|---|---|---|---|---|
| ☐ | 1 | Sun 1 | How computers find each other (IP, ports, packets) | 10–15 | read + 3 commands | `net101/S01-how-computers-find-each-other.md` |
| ☐ | 2 | Sun 1 | TCP: reliable byte stream, handshake | 15 | read | `net101/S02-tcp-reliable-byte-stream.md` |
| ☐ | 2b ➕ | Sun 1 | Bytes vs text (encode/decode, UTF-8) | 10 | read + Python shell | `net101/S02b-bytes-vs-text.md` |
| ☐ | 3 | Sun 1 | Sockets hands-on: echo server | 15–20 | code along | `net101/S03-sockets-hands-on.md` |
| ☐ | 4 | Mon 2 | Framing: where does a message end? | 20–25 | exercise + tests | `net101/S04-framing.md` → `lessons/N01-framing/` |
| ☐ | 5 | Mon 2 | HTTP is text on TCP | 15 | read + curl | `net101/S05-http-is-text-on-tcp.md` |
| ☐ | 6 | Tue 3 | L01 Part A: concurrency vs parallelism, GIL | 15 | read + run | `larp/L01-async-await.md` |
| ☐ | 7 | Tue 3 | L01 Part B: event loop, await, blocking the loop | 20 | read + run | `larp/L01-async-await.md` |
| ☐ | 8 | Wed 4 | **L01 quiz** (9 Qs, graded) | 15 | `/quiz L01` | |
| ☐ | 9 | Wed 4 | L02 Part A: ASGI, Uvicorn, request lifecycle | 20 | read | `larp/L02-fastapi-internals.md` |
| ☐ | 10 | Thu 5 | L02 Part B: Depends, Pydantic, lifespan | 20 | read | `larp/L02-fastapi-internals.md` |
| ☐ | 11 | Thu 5 | **L02 quiz** (9 Qs, graded) | 15 | `/quiz L02` | |
| ☐ | 12 | Fri 6 | **Weekly mock**: L01 + L02 + networking basics | 30–45 | `/quiz mock` | |
| ☐ | 13 | Sat 7 | **LAB00** part 1: `handle_request` | 20–30 | exercise | `lessons/A01-http-from-sockets/` |
| ☐ | 14 | Sat 7 | **LAB00** part 2: `run_server`, then `/check` break rounds (slow client → threads → asyncio) | 30–60 | exercise | same |
| ☐ | 15 | Sun 8 | Wrap-up: flashcards, Excel update, push | 10 | `/lesson wrap` | |

Optional on Sun 8: "Tell me about yourself" v1 (90 s) as a `/quiz` behavioural drill.

**Rough load:** Sun ≈ 55 min · Mon ≈ 40 min · Tue ≈ 35 min · Wed ≈ 35 min · Thu ≈ 35 min ·
Fri ≈ 45 min · Sat ≈ 50–90 min · Sun ≈ 10 min.

This plan isn't fixed. If a session shows a gap, the tutor inserts a ➕ session here (logged in
`TRACKER.md`), and later sessions slide back if needed.

## How to run a session
- Passive (reading): open the file, read, try the snippet, answer the "Check yourself"
  questions, either out loud or by pasting your answers to me for grading.
- Exercise: `/lesson` tells you what to do; `/check` when tests are green; `/hint` when stuck.
- Quiz: `/quiz L01` etc. I ask one question at a time and grade it.
- End of each sitting: say **"wrap up"**. I update `progress.md`, `TRACKER.md`, `JOURNAL.md`,
  flashcards and the Excel planner, then commit and push, so your personal laptop is in sync.

## After Sun 8
Week 2 (Mon 9 Nov) follows the same pattern from the planner: L03–L06 LARP topics + LAB01 (caching),
pulled forward and done on breaks instead of waiting for Saturday.
