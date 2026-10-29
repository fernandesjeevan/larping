# LARP as a Backend Dev — the Backend Patterns Course

You learn every pattern the way it was invented: someone wrote the obvious version, it broke in
production, and the fix got a name. Each lesson goes like this:

```
 0 Brief        theory of the problem + runnable snippets  -> answer 2 check questions
 1 Brute force  implement the simplest thing that works    -> test_stage1.py green
 2 Break it     I ask "what happens when...?", then write a test that FAILS on your code
                with a measured number; you fix it your way (1-3 rounds)
 3 Pattern      the pattern gets its name: structure, trade-offs, when NOT to use it;
                you refactor to it
 4 LARP         interview questions + a "prod is broken" scenario, graded 0-2 -> flashcards
```

## Commands
| Type | What happens |
|---|---|
| `/lesson` | start or continue where you left off (`/lesson A01`, `/lesson next`) |
| `/check` | run the tests on your attempt, critique it, break it |
| `/hint` | escalating hints (nudge → concept → shape → near-solution) |
| `/quiz` | interview drill (`/quiz review` for flashcards, `/quiz mock` for Friday mock) |
| "show me" | full reference solution (no shame; you retype it from memory after) |

Run tests yourself: `python -m pytest lessons/<lesson-folder> -q`

## Course map
**What to do today is in `PLAN.md`.** This map is the full course; `PLAN.md` pulls from it week by week.
Titles name the *problem*. The pattern behind each one gets its name at stage 3.

**0. Networking from zero** (`net101/`, 10–20 min reads)
- S01 IP, ports, packets · S02 TCP · S03 Sockets hands-on · S04 Framing (+ exercise N01) · S05 HTTP/HTTPS

**A. How a backend actually serves a request**
- A01 Serving HTTP with nothing but a socket · *LAB00, L01*
- A02 Every endpoint needs logging, auth and timing · *L02*
- A03 Handlers that create their own database connection · *L45, L54*

**B. Code patterns backends lean on**
- B01 Supporting three LLM providers · *L11, L49*
- B02 Two payment gateways with incompatible APIs · *L54*
- B03 Adding retry/logging/caching without touching 20 functions · *L54*
- B04 SQL sprinkled through request handlers · *L28, L45*
- B05 "When an order is placed, also email, stats, audit, Slack" · *L56*

**C. Data correctness**
- C01 Listing 1,000,000 rows to a client · *LAB04, L27*
- C02 Showing 50 posts with their authors · *L27*
- C03 Two requests update the same balance · *LAB07, L28*
- C04 The client retried and the customer got charged twice · *LAB03, L08*

**D. Performance**
- D01 A query that takes 800 ms on every request · *LAB01, L24*
- D02 The cache expired and the database fell over · *LAB01*
- D03 Attackers requesting IDs that don't exist · *LAB16*
- D04 One client is hammering the API · *LAB02, L25*

**E. Talking to things that fail**
- E01 Calling a flaky third-party API · *LAB05, L11*
- E02 The dependency is completely down · *LAB05, L58*
- E03 One slow dependency takes down every endpoint · *LAB18*
- E04 A page that calls four services · *LAB09, LAB23*

**F. Async work and messaging**
- F01 Uploading a 200-page PDF times out the request · *L07, L40*
- F02 The producer is faster than the workers · *LAB06*
- F03 The worker crashed halfway through a job · *L37*
- F04 Saved to the DB but the event never got published · *LAB08*
- F05 A message must reach users on a different server instance · *LAB10, L48*
- F06 Notifying customers' servers when something happens · *LAB21*
- F07 Book flight + hotel + car; the car booking failed · *L32*
- F08 "Why is this account balance wrong?" · *L57, LAB17*

**G. Distributed systems**
- G01 Spreading keys over cache servers · *LAB11*
- G02 Sending traffic to 3 backends · *LAB12*
- G03 Only one worker should run the nightly job · *LAB13*
- G04 Exactly one scheduler must be active · *LAB15*
- G05 Generating unique IDs on 3 machines · *LAB26*
- G06 "I saved my profile but the page shows the old one" · *LAB20*
- G07 Is that server dead or just slow? · *LAB28*

**H. The API surface**
- H01 Designing the DocuLens public API · *L31*
- H02 Who is calling, and what may they do? · *L15*
- H03 Live progress for a long job · *L48*
- H04 Mobile and web need different shapes of the same data · *LAB27*

**Capstones:** CAP/PACELC · queues vs streams · system design drills (rate limiter, job
scheduler, notification system, RAG platform for 10k users)

Where a lesson lists a LAB, finishing it covers that Saturday lab in the roadmap. Labs that
name Redis/Postgres also need the optional ⚙ extra, which you run from WSL with Docker.
