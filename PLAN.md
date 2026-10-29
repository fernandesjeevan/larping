# Week 1 catch-up plan: Thu 29 Oct → Sun 1 Nov

**Scope of this repo:** backend patterns (labs) + LARP interview prep only. Project cards
(D01–D05) happen in your evenings and are tracked there, not here.

**What's being squeezed in:** the non-project parts of planner days Wed 28 – Sat 31
(L01, L02, Friday mock, LAB00), plus networking basics from zero so LAB00 actually makes sense.

Every session is **10–20 min** so it fits a break. Do them in order; tick as you go.
Long free stretch? Chain several. Only 10 minutes? Do one.

| ✓ | # | Day | Session | ⏱ | Type | File |
|---|---|---|---|---|---|---|
| ☐ | 1 | Thu 29 | How computers find each other (IP, ports, packets) | 10–15 | read + 3 commands | `net101/S01-how-computers-find-each-other.md` |
| ☐ | 2 | Thu 29 | TCP: reliable byte stream, handshake | 15 | read | `net101/S02-tcp-reliable-byte-stream.md` |
| ☐ | 3 | Thu 29 | Sockets hands-on: echo server | 15–20 | code along | `net101/S03-sockets-hands-on.md` |
| ☐ | 4 | Thu 29 | L01 Part A: concurrency vs parallelism, GIL | 15 | read + run | `larp/L01-async-await.md` |
| ☐ | 5 | Fri 30 | Framing: where does a message end? | 20–25 | exercise + tests | `net101/S04-framing.md` → `lessons/N01-framing/` |
| ☐ | 6 | Fri 30 | L01 Part B: event loop, await, blocking the loop | 20 | read + run | `larp/L01-async-await.md` |
| ☐ | 7 | Fri 30 | **L01 quiz** (9 Qs, graded) | 15 | `/quiz L01` | |
| ☐ | 8 | Fri 30 | HTTP is text on TCP | 15 | read + curl | `net101/S05-http-is-text-on-tcp.md` |
| ☐ | 9 | Sat 31 | **LAB00** part 1: `handle_request` | 20–30 | exercise | `lessons/A01-http-from-sockets/` |
| ☐ | 10 | Sat 31 | **LAB00** part 2: `run_server`, then `/check` break rounds (slow client → threads → asyncio) | 30–60 | exercise | same |
| ☐ | 11 | Sat 31 | L02 Part A: ASGI, Uvicorn, request lifecycle | 20 | read | `larp/L02-fastapi-internals.md` |
| ☐ | 12 | Sun 1 | L02 Part B: Depends, Pydantic, lifespan | 20 | read | `larp/L02-fastapi-internals.md` |
| ☐ | 13 | Sun 1 | **L02 quiz** (9 Qs, graded) | 15 | `/quiz L02` | |
| ☐ | 14 | Sun 1 | **Weekly mock**: L01 + L02 + LAB00 (Friday mock moved here) | 30–45 | `/quiz mock` | |
| ☐ | 15 | Sun 1 | Wrap-up: flashcards, Excel update, push | 10 | `/lesson wrap` | |

Optional if time is left on Sunday: "Tell me about yourself" v1 (90 s) as a `/quiz` behavioural drill.

**Rough load:** Thu ≈ 60 min · Fri ≈ 75 min · Sat ≈ 75–110 min · Sun ≈ 75–90 min.

## How to run a session
- Passive (reading): open the file, read, try the snippet, answer the "Check yourself"
  questions, either out loud or by pasting your answers to me for grading.
- Exercise: `/lesson` tells you what to do; `/check` when tests are green; `/hint` when stuck.
- Quiz: `/quiz L01` etc. I ask one question at a time and grade it.
- End of each sitting: say **"wrap up"**. I update `progress.md`, the Excel planner and
  flashcards, then commit and push, so your personal laptop is in sync.

## After Sunday
Week 2 follows the same pattern from the planner: L03–L06 LARP topics + LAB01 (caching),
pulled forward and done on breaks instead of waiting for Saturday.
