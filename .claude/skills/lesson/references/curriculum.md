# Instructor curriculum — Backend Patterns Course

Each entry: **Problem** (learner-facing) · **Brute-force ask** · **Break rounds** (flaws and
how to *prove* them with a test or a number) · **Pattern(s) reached** · **Maps to** (LARP topic /
Saturday lab / project). Pure Python + stdlib unless marked ⚙ (optional real-infra extra).

Source list: the learner's own `backend patterns.md.txt` (repo root). Its checklist levels map to
the planner's Theory 🟢 / Built 🔵 / Explain 🟣 / Design 🔴 columns. When a topic there isn't
covered below (e.g. LFU, cache avalanche, hot keys, refresh-ahead), fold it into the nearest
lesson's stage 3.

Order is by teaching dependency, not calendar. When a lesson matches a Saturday lab, finishing
the lesson (plus its ⚙ extra if the lab names Redis/Postgres) satisfies that lab's "Done when".

---

## Module 0 — Networking from zero (reading sessions in `net101/`)
S01 IP/ports/packets/DNS · S02 TCP (handshake, reliability, *byte stream not messages*) ·
S03 sockets hands-on (echo server; experiment 2 = blocking server preview) · S04 framing →
exercise **N01** (`recv_until`, `recv_exact`, `read_http_message` against a chunking FakeSocket;
brute force is fine here, no break rounds; it's a skill drill) · S05 HTTP/HTTPS as text on TCP.
A01 assumes all of these. In A01 break round 2 the learner should reuse their N01 functions.

## Module A — How a backend actually serves a request

### A01 Serving HTTP with nothing but a socket
- **Brute force:** single-threaded `accept → recv(1024) → parse → sendall → close` server.
  `handle_request(raw: bytes) -> bytes` + `run_server(host, port, ready)`.
- **Break rounds:**
  1. *Slow client* — client A connects and sends half a request, then stalls; client B's GET
     must answer within 2 s. Single-threaded server blocks → fails.
  2. *TCP is a stream* — send the request in 2 chunks 200 ms apart; send a 3 KB header. One
     `recv(1024)` gets a partial request → 400 or garbage. Fix: read until `\r\n\r\n`, cap size.
  3. *Thread explosion* — (after they go thread-per-connection) open 300 idle connections;
     count live threads. Unbounded. Fix: bounded pool, then contrast with asyncio.
- **Patterns:** concurrency models — thread-per-connection → bounded thread pool (worker pool)
  → event loop (reactor, `asyncio.start_server`). Framing (read-until-delimiter, max size).
- **Maps to:** LAB00, L01 (async/await, event loop), L44. Explains what uvicorn does under FastAPI.

### A02 Every endpoint needs logging, auth and timing
- **Brute force:** add 4 endpoints to a tiny framework with `if path == ...` chains; then
  "every endpoint must log, time itself, and reject missing `X-API-Key`".
- **Break rounds:** copy-paste in every branch → test adds 5th endpoint and forgets auth
  (a test hits it without a key and gets 200). Ordering bugs (timing excludes auth).
- **Patterns:** route table / dispatch dict; middleware chain (Chain of Responsibility);
  decorators. Show how Starlette/FastAPI middleware and `APIRouter` map to this.
- **Maps to:** L02, L31. DocuLens request-id + auth middleware.

### A03 Handlers that create their own database connection
- **Brute force:** handler opens `sqlite3.connect()` and constructs an `OpenAIClient()` inline.
- **Break rounds:** write a unit test without touching disk/network → impossible; count
  connections opened across 100 requests; swap provider for tests → monkeypatch hell.
- **Patterns:** Dependency Injection (constructor/parameter injection), composition root,
  FastAPI `Depends`, scoped lifetimes (per-request vs singleton), fakes over mocks.
- **Maps to:** L02, L45, L54.

## Module B — Code patterns backends lean on

### B01 Supporting three LLM providers (or three notification channels)
- **Brute force:** `def complete(provider, prompt)` with `if provider == "openai": ... elif ...`.
- **Break rounds:** add a 4th provider → edit 5 functions (show the diff size); per-provider
  tests require all SDKs; config typo `"opanai"` silently falls through.
- **Patterns:** Strategy (typing.Protocol), Factory/registry, fail-fast on unknown keys.
- **Maps to:** L11, L49, L54. DocuLens LLM router, shared AI gateway.

### B02 Two payment gateways with incompatible APIs
- **Brute force:** call vendor A and vendor B SDKs directly from business code.
- **Break rounds:** vendor B returns cents vs A returns decimal strings → amount bug test;
  vendor error types leak into business layer.
- **Patterns:** Adapter, Anti-Corruption Layer, domain error types.
- **Maps to:** L54, L74.

### B03 Adding retry/logging/caching without touching 20 functions
- **Brute force:** paste try/except-retry into each function.
- **Break rounds:** inconsistent behaviour across copies; decorator loses `__name__`/signature
  (test checks `func.__name__`); decorator on async function breaks (test with coroutine).
- **Patterns:** Decorator (functools.wraps, sync+async aware, parametrised decorators).
- **Maps to:** L54. Sets up E01.

### B04 SQL sprinkled through request handlers
- **Brute force:** handlers run raw `sqlite3` queries for orders + order_lines.
- **Break rounds:** second insert fails → half-written order remains (test asserts no orphan
  rows); string-formatted SQL → injection test with `name = "x'); DROP TABLE..."`;
  business logic untestable without DB.
- **Patterns:** Repository, Unit of Work (transaction boundary), parameterised queries,
  in-memory fake repo for tests.
- **Maps to:** L28, L45, L54. DocuLens persistence layer.

### B05 "When an order is placed, also email, update stats, audit, notify Slack"
- **Brute force:** `place_order()` calls all four directly.
- **Break rounds:** email service raises → order fails (test); adding a 5th side effect edits
  core code; slow Slack call adds latency (timed).
- **Patterns:** Observer / in-process domain events / event bus; then: "what if the process
  crashes after commit but before handlers?" → teaser for F04 outbox.
- **Maps to:** L56, L74.

## Module C — Data correctness

### C01 Listing 1,000,000 rows to a client
- **Brute force:** `GET /items` returns everything, then `?page=&size=` with OFFSET.
- **Break rounds:** memory/time of full dump (measured); page 5,000 OFFSET slower than page 1
  (time with sqlite + EXPLAIN QUERY PLAN); insert rows while paging → duplicate/skipped
  item (test).
- **Patterns:** Keyset/cursor pagination, opaque base64 cursor, stable sort with tiebreaker.
  ⚙ Postgres EXPLAIN ANALYZE numbers.
- **Maps to:** LAB04, L27, L31.

### C02 Showing 50 posts with their authors
- **Brute force:** loop, one query per author.
- **Break rounds:** count queries (51); add comments → 2,551 queries.
- **Patterns:** N+1 fix: JOIN / batched `WHERE id IN (...)` / DataLoader-style batching,
  ORM eager loading (`selectinload` vs `joinedload`).
- **Maps to:** L27.

### C03 Two requests update the same balance
- **Brute force:** read balance → add → write.
- **Break rounds:** 50 threads deposit 1 each → final balance < 50 (lost update, test);
  "just use a Python lock" → run 2 processes → still lost.
- **Patterns:** atomic `UPDATE ... SET x = x + ?`, optimistic locking (version column + retry),
  pessimistic locking (`SELECT ... FOR UPDATE`; sqlite `BEGIN IMMEDIATE`), isolation levels,
  MVCC theory, deadlocks and lock ordering.
- **Maps to:** LAB07, L28.

### C04 The client retried and the customer got charged twice
- **Brute force:** `POST /payments` inserts and charges.
- **Break rounds:** retry after timeout → 2 charges; naive "check if exists, then insert" →
  20 concurrent duplicates still produce >1 charge (race test); same key with different body
  → must 422; crash mid-processing → key stuck.
- **Patterns:** Idempotency keys (unique constraint, stored response, in-progress state,
  request fingerprint, TTL), idempotent consumers. ⚙ Redis SET NX version.
- **Maps to:** LAB03, L08. Celery tasks in DocuLens.

## Module D — Performance

### D01 A query that takes 800 ms on every request
- **Brute force:** memoise in a global dict.
- **Break rounds:** data changes → stale forever (test); 1M distinct keys → memory growth
  (measured); 2 worker processes → 2 caches disagree.
- **Patterns:** Cache-aside with TTL, LRU bound (`OrderedDict`), invalidation on write,
  write-through vs write-behind vs read-through; shared cache (⚙ Redis).
- **Maps to:** LAB01, L23, L24.

### D02 The cache expired and the database fell over
- **Brute force:** their D01 cache-aside.
- **Break rounds:** 100 threads hit an expired key at once → 100 DB calls (counted);
  all keys set with same TTL expire together (show synchronized expiry).
- **Patterns:** single-flight / request coalescing (lock per key; ⚙ Redis `SET NX PX`),
  TTL jitter, stale-while-revalidate, early probabilistic refresh.
- **Maps to:** LAB01, L24, L50 (semantic cache).

### D03 Attackers requesting IDs that don't exist
- **Brute force:** cache-aside that only caches hits.
- **Break rounds:** 10k random missing IDs → 10k DB calls.
- **Patterns:** negative caching with short TTL, Bloom filter (build one from scratch; measure
  false-positive rate vs size).
- **Maps to:** LAB16, L24.

### D04 One client is hammering the API
- **Brute force:** counter per client per minute (fixed window).
- **Break rounds:** 100 requests at 00:59 + 100 at 01:00 → 200 in 2 s pass (test);
  sliding log fix → memory per client measured; two processes → limits doubled.
- **Patterns:** fixed window → sliding log → sliding window counter → token bucket →
  leaky bucket; atomicity (⚙ Redis Lua), 429 + `Retry-After`, per-tenant/per-route limits,
  LLM token-based limits.
- **Maps to:** LAB02, L25, L67.

## Module E — Talking to things that fail

### E01 Calling a flaky third-party API
- **Brute force:** `urllib.request.urlopen(url)` against the provided flaky server
  (500s, 429s, slow responses, dropped connections).
- **Break rounds:** slow endpoint → call hangs (test with deadline); naive `for _ in range(5)`
  retry → hammering (count requests/second); retrying a non-idempotent POST double-writes;
  synchronized retries of 50 clients (plot timestamps).
- **Patterns:** timeouts (connect vs read, overall deadline), retry with exponential backoff +
  full jitter, retry only safe/retryable errors, `Retry-After`, retry budgets.
- **Maps to:** LAB05, L11.

### E02 The dependency is completely down
- **Brute force:** their E01 client.
- **Break rounds:** dependency down for 30 s → each request burns timeout × retries;
  measure p99 latency of your own API → you're down too.
- **Patterns:** Circuit breaker (closed/open/half-open, failure-rate window), fallback
  (cached/default/degraded), fail fast.
- **Maps to:** LAB05, L11, L58. LLM provider fallback in DocuLens.

### E03 One slow dependency takes down every endpoint
- **Brute force:** one shared thread pool / connection pool for all downstream calls.
- **Break rounds:** recommendations service slows → checkout endpoint also times out (test).
- **Patterns:** Bulkhead (pool/semaphore per dependency), load shedding by priority,
  503 + Retry-After, queue-time-based admission.
- **Maps to:** LAB18, L58.

### E04 A page that calls four services
- **Brute force:** call them sequentially.
- **Break rounds:** latency = sum (measured); one failure → whole page 500.
- **Patterns:** fan-out/fan-in with `asyncio.gather`/`TaskGroup`, per-call timeouts,
  partial responses, hedged requests (advanced: LAB23).
- **Maps to:** LAB09, LAB23, L44, L58.

## Module F — Async work and messaging

### F01 Uploading a 200-page PDF times out the request
- **Brute force:** process inside the request; then `threading.Thread(...).start()`.
- **Break rounds:** request duration measured; kill process mid-job → work lost, no status;
  no way to ask "is it done?".
- **Patterns:** job queue (producer/consumer), job table with status, 202 Accepted + polling
  endpoint, worker processes. Map to Celery/RQ.
- **Maps to:** L07, L40. DocuLens ingestion.

### F02 The producer is faster than the workers
- **Brute force:** unbounded `queue.Queue()` with N workers.
- **Break rounds:** producer 10× faster → queue length/memory grows without bound (measured).
- **Patterns:** bounded queue + backpressure, `asyncio.Queue(maxsize)`, semaphores, rejecting
  vs blocking vs dropping.
- **Maps to:** LAB06, L44.

### F03 The worker crashed halfway through a job
- **Brute force:** pop job → process → done.
- **Break rounds:** crash after pop → job lost (at-most-once); ack-after-work → duplicates
  on crash (at-least-once) → side effect twice; a poison job crashes worker forever.
- **Patterns:** ack after processing, visibility timeout/lease, idempotent consumer (inbox),
  max attempts + dead-letter queue, delivery guarantees vocabulary.
- **Maps to:** L07, L37. Celery `acks_late`.

### F04 Saved to the DB but the event never got published
- **Brute force:** `db.commit(); broker.publish(event)`.
- **Break rounds:** inject crash between the two → DB has order, no event (test); swap order
  → event published, DB rolled back (ghost event).
- **Patterns:** Transactional outbox + relay (polling), inbox dedup on consumer, CDC as
  alternative (LAB24). ⚙ Redis Streams relay.
- **Maps to:** LAB08, LAB24, L37, L74.

### F05 A message must reach users connected to a different server instance
- **Brute force:** in-memory list of connected clients per instance.
- **Break rounds:** two instances → client on instance B misses message sent via A (test).
- **Patterns:** pub/sub via broker, fan-out, SSE vs WebSocket vs long-poll, Redis pub/sub vs
  streams (delivery semantics).
- **Maps to:** LAB10, L48.

### F06 Notifying customers' servers when something happens
- **Brute force:** synchronous POST to the customer URL inside the request.
- **Break rounds:** customer endpoint slow/down → our request fails; spoofed webhook accepted
  by receiver (test); replayed webhook processed twice.
- **Patterns:** async webhook delivery with retries/backoff/DLQ, HMAC signature + timestamp
  (replay window), receiver dedup by event id, constant-time compare.
- **Maps to:** LAB21, L74. DocuLens signed webhooks.

### F07 Book flight + hotel + car; the car booking failed
- **Brute force:** sequential calls with try/except undo.
- **Break rounds:** crash after hotel booked → no record, can't compensate; compensation
  itself fails; retries double-book.
- **Patterns:** Saga (orchestrated vs choreographed), persisted state machine, compensating
  actions, idempotent steps; durable workflow engines (Temporal/Step Functions/LangGraph
  checkpoints).
- **Maps to:** L32, L72. SRE Copilot remediation + rollback.

### F08 "Why is this account balance wrong?"
- **Brute force:** `UPDATE accounts SET balance = ...` (+ maybe an audit table).
- **Break rounds:** answer "what was the balance last Tuesday?" → impossible; audit table
  drifts from state when a code path forgets to write it (test).
- **Patterns:** Event sourcing (append-only log, rebuild by replay, snapshots), CQRS (separate
  read models/projections), materialized views (LAB17), eventual consistency of reads.
- **Maps to:** L57, LAB17. SRE incident state.

## Module G — Distributed systems

### G01 Spreading keys over cache servers — `hash(key) % N`. Break: add a node → measure ~all
keys move. Pattern: consistent hashing + virtual nodes (~1/N move). LAB11, L35.
### G02 Sending traffic to 3 backends — random/round robin. Break: one backend slow/dead keeps
getting traffic. Pattern: round robin, least-connections, health checks, outlier ejection.
LAB12.
### G03 Only one worker should run the nightly job — check-then-set flag. Break: race (two run);
lock holder pauses (GC) past TTL and writes after expiry. Pattern: lock with TTL + owner token,
fencing tokens; when to avoid distributed locks. LAB13.
### G04 Exactly one scheduler must be active — "the first one wins". Break: leader dies → nobody
takes over. Pattern: lease-based leader election with renewals. LAB15, L35.
### G05 Generating unique IDs on 3 machines — auto-increment / random. Break: collisions or
coordination bottleneck, non-sortable UUID4 index fragmentation. Pattern: Snowflake, ULID/UUIDv7.
LAB26.
### G06 "I saved my profile but the page shows the old one" — reads from replica. Break: simulate
lag → read-after-write anomaly. Pattern: read-your-writes routing, session stickiness, LSN wait.
LAB20, L35.
### G07 Is that server dead or just slow? — single missed ping = dead. Break: latency spikes →
false positives (measured). Pattern: heartbeats + suspicion timeouts, phi-accrual idea. LAB28.

## Module H — The API surface

### H01 Designing the DocuLens public API — teach directly (no brute force): resources, status
codes, error envelope (RFC 9457), versioning, pagination link, ETags/conditional requests.
Exercise: critique a deliberately bad API spec. L31.
### H02 Who is calling, and what may they do? — brute: `?user_id=` param. Break: impersonation;
then stateful sessions across instances; then JWT can't be revoked. Pattern: sessions vs JWT,
access + refresh token rotation, RBAC, tenant isolation (row-level). L15.
### H03 Live progress for a long job — brute: client polls every 100 ms (measure load). Pattern:
long polling → SSE → WebSocket, choosing between them. L48.
### H04 Mobile and web need different shapes of the same data — brute: client calls 5 services.
Pattern: API gateway / BFF (auth, routing, rate limit, request id). LAB27, L49.

## Theory-only capstones (teach directly, then a design exercise)
- **T01** CAP / PACELC / consistency models (L35)
- **T02** Message queue vs event stream: RabbitMQ vs Kafka vs SQS (L36, L55)
- **T03** System design drills: rate limiter service (L67), job scheduler (L68), notification
  system (L66), RAG platform for 10k users (L38)
