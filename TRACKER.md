# Syllabus tracker: what's taught, what's left

This tracker **changes as we go**. It was generated in bulk, so it will have gaps. Whenever a
session shows that something is missing before or after a topic, it gets added here (marked ➕
and logged at the bottom) and taught at the point where it's needed.

Status: ⬜ not started · 🟡 in progress · ✅ taught (quiz/exercise done) · ➕ added later · ⏭ skipped (with reason)
Tutor: update this after every sitting. Detail on *how it went* goes in `JOURNAL.md`.

## 0. Networking from zero
| ID | Topic | Status | Taught on | Notes |
|---|---|---|---|---|
| S01 | IP addresses, ports, packets, DNS, layers | ⬜ | | |
| S02 | TCP: handshake, reliability, byte stream, close | ⬜ | | |
| S02b ➕ | Bytes vs text: `bytes`, `str`, UTF-8, encode/decode | ⬜ | | added 29 Oct, see log |
| S03 | Sockets hands-on: echo server, `recv` rules | ⬜ | | |
| S04 | Framing (delimiter / length prefix / close) + exercise N01 | ⬜ | | |
| S05 | HTTP/1.1 as text, status codes, keep-alive, HTTPS/TLS | ⬜ | | |

## 1. Backend pattern lessons (course, with Saturday-lab mapping)
| ID | Problem → pattern (pattern revealed at stage 3) | Lab | Status | Notes |
|---|---|---|---|---|
| A01 | Serving HTTP with a socket → concurrency models | LAB00 | ⬜ | |
| A02 | Logging/auth/timing everywhere → middleware chain | | ⬜ | |
| A03 | Handlers create own DB conn → dependency injection | | ⬜ | |
| B01 | Three LLM providers → strategy + factory | | ⬜ | |
| B02 | Incompatible payment APIs → adapter / ACL | | ⬜ | |
| B03 | Retry/log in 20 functions → decorator | | ⬜ | |
| B04 | SQL in handlers → repository + unit of work | | ⬜ | |
| B05 | Order side effects → observer / domain events | | ⬜ | |
| C01 | 1M rows to a client → cursor pagination | LAB04 | ⬜ | |
| C02 | Posts + authors → N+1 fix | | ⬜ | |
| C03 | Concurrent balance updates → locking | LAB07 | ⬜ | |
| C04 | Charged twice → idempotency keys | LAB03 | ⬜ | |
| D01 | 800 ms query → cache-aside, TTL, LRU | LAB01 | ⬜ | |
| D02 | Cache expiry kills DB → stampede protection | LAB01 | ⬜ | |
| D03 | Missing IDs → negative cache, Bloom filter | LAB16 | ⬜ | |
| D04 | Client hammering API → rate limiters | LAB02 | ⬜ | |
| E01 | Flaky API → timeouts, retries, backoff + jitter | LAB05 | ⬜ | |
| E02 | Dependency down → circuit breaker | LAB05 | ⬜ | |
| E03 | One slow dependency → bulkhead, load shedding | LAB18 | ⬜ | |
| E04 | Four services per page → fan-out/fan-in, hedging | LAB09, LAB23 | ⬜ | |
| F01 | PDF upload times out → job queue | | ⬜ | |
| F02 | Producer too fast → backpressure | LAB06 | ⬜ | |
| F03 | Worker crashed mid-job → ack, DLQ, idempotent consumer | | ⬜ | |
| F04 | DB saved, event lost → transactional outbox | LAB08, LAB24 | ⬜ | |
| F05 | Message to another instance → pub/sub fan-out | LAB10 | ⬜ | |
| F06 | Notify customer servers → webhooks | LAB21 | ⬜ | |
| F07 | Flight+hotel+car failure → saga | | ⬜ | |
| F08 | Why is balance wrong → event sourcing, CQRS | LAB17 | ⬜ | |
| G01 | Keys over cache servers → consistent hashing | LAB11 | ⬜ | |
| G02 | Traffic to 3 backends → load balancing | LAB12 | ⬜ | |
| G03 | One nightly job → distributed lock + fencing | LAB13 | ⬜ | |
| G04 | One active scheduler → leader election | LAB15 | ⬜ | |
| G05 | Unique IDs on 3 machines → Snowflake/ULID | LAB26 | ⬜ | |
| G06 | Stale read after save → read-your-writes | LAB20 | ⬜ | |
| G07 | Dead or slow → failure detection | LAB28 | ⬜ | |
| H01 | Public API design → REST conventions | | ⬜ | |
| H02 | Who is calling → auth, JWT, RBAC | | ⬜ | |
| H03 | Live job progress → SSE / WebSocket | | ⬜ | |
| H04 | Different clients → API gateway / BFF | LAB27 | ⬜ | |
| — | Labs without a lesson yet: LAB14 Kafka, LAB19 gRPC vs REST, LAB22 priority queues, LAB25 partitioning, LAB29 explain three | | ⬜ | add lessons when reached |

## 2. LARP topics (interview prep, from the roadmap's LARP bank)
| ID | Topic | Status | Quiz | Notes |
|---|---|---|---|---|
| L01 | Python async/await and the event loop | ⬜ | | |
| L02 | FastAPI internals: DI, Pydantic v2, sync vs async | ⬜ | | |
| L03 | Embeddings and vector search (ANN, HNSW vs IVFFlat) | ⬜ | | |
| L04 | BM25 and full-text search | ⬜ | | |
| L05 | Hybrid search, RRF, metadata filtering | ⬜ | | |
| L06 | Rerankers: bi-encoders vs cross-encoders | ⬜ | | |
| L07 | Task queues: Celery, Redis, delivery guarantees | ⬜ | | |
| L08 | Idempotency and de-duplication | ⬜ | | |
| L09 | Structured outputs and prompt engineering | ⬜ | | |
| L10 | Evaluating RAG systems | ⬜ | | |
| L11 | LLM routing, fallback, retries, timeouts, circuit breakers | ⬜ | | |
| L12 | Chunking strategies and query transformation | ⬜ | | |
| L13 | LangGraph core | ⬜ | | |
| L14 | Agentic patterns: ReAct, tools, HITL, multi-agent | ⬜ | | |
| L15 | AuthN/AuthZ, JWT, OAuth2/OIDC, RBAC, multi-tenancy | ⬜ | | |
| L16 | Docker in depth + CI/CD with GitHub Actions | ⬜ | | |
| L17 | Cloud fundamentals: Azure + AWS equivalents | ⬜ | | |
| L18 | Observability: logs, metrics, traces, OTel, LLM tracing | ⬜ | | |
| L71 | Intelligent document processing | ⬜ | | |
| L72 | Durable workflows and orchestration engines | ⬜ | | |
| L74 | Integrations and side effects: webhooks, outbox, retries, audit | ⬜ | | |
| L73 | Text-to-SQL agents and safe data access | ⬜ | | |
| L19 | Model Context Protocol (MCP) | ⬜ | | |
| L20 | Kubernetes core objects | ⬜ | | |
| L21 | Debugging containers and Kubernetes | ⬜ | | |
| L22 | Prometheus, PromQL, alerting | ⬜ | | |
| L23 | Redis in depth | ⬜ | | |
| L24 | Caching patterns (incl. LLM caching) | ⬜ | | |
| L25 | Rate limiting algorithms | ⬜ | | |
| L26 | Designing multi-agent systems | ⬜ | | |
| L27 | PostgreSQL indexes and query plans | ⬜ | | |
| L28 | Transactions, isolation, MVCC, locking | ⬜ | | |
| L29 | Evaluating agents and LLM apps in production | ⬜ | | |
| L30 | Cost and latency optimisation for LLM apps | ⬜ | | |
| L31 | REST API design | ⬜ | | |
| L32 | State machines, sagas, compensation | ⬜ | | |
| L33 | Guardrails and security for LLM apps | ⬜ | | |
| L34 | Kubernetes RBAC, ServiceAccounts, least privilege | ⬜ | | |
| L35 | Distributed systems fundamentals | ⬜ | | |
| L36 | Message queues vs event streams | ⬜ | | |
| L37 | Outbox, inbox, DLQ, poison messages | ⬜ | | |
| L38 | System design: RAG platform for 10k users | ⬜ | | |
| L39 | PDF internals and document parsing | ⬜ | | |
| L40 | Ingestion pipeline design at scale | ⬜ | | |
| L41 | Vector databases compared | ⬜ | | |
| L42 | Prompt injection through documents, data governance | ⬜ | | |
| L43 | Framework landscape (LangChain … Semantic Kernel) | ⬜ | | |
| L44 | Async Python deep dive, concurrency control | ⬜ | | |
| L45 | Testing backend and LLM systems | ⬜ | | |
| L46 | GraphRAG and knowledge graphs | ⬜ | | |
| L47 | Fine-tuning vs RAG vs prompting | ⬜ | | |
| L48 | Streaming: SSE, WebSockets, long polling | ⬜ | | |
| L49 | AI gateway design | ⬜ | | |
| L50 | Semantic caching and prompt caching | ⬜ | | |
| L51 | System design: document translation service | ⬜ | | |
| L52 | System design: AI support assistant with handoff | ⬜ | | |
| L53 | Behavioural: your story | ⬜ | | |
| L54 | Python design: OOP, typing, design patterns | ⬜ | | |
| L55 | Kafka in depth | ⬜ | | |
| L56 | Event-driven architecture patterns | ⬜ | | |
| L58 | Reliability patterns: breaker, bulkhead, shedding, hedging | ⬜ | | |
| L57 | Event sourcing and CQRS | ⬜ | | |
| L59 | OpenTelemetry deep dive | ⬜ | | |
| L60 | Terraform and IaC | ⬜ | | |
| L61 | AWS core for AI backends | ⬜ | | |
| L62 | EKS and Helm | ⬜ | | |
| L67 | System design: rate limiter as a service | ⬜ | | |
| L68 | System design: job scheduler / task queue | ⬜ | | |
| L63 | Azure AI stack | ⬜ | | |
| L66 | System design: notification system | ⬜ | | |
| L64 | MLflow and experiment tracking | ⬜ | | |
| L65 | A2A and agent platforms | ⬜ | | |
| L69 | SQL interview patterns | ⬜ | | |
| L70 | Voice and multimodal pipelines (overview) | ⬜ | | |

## 2b. ➕ Fundamentals (first-round basics, office micro-sessions, `Fundamentals` sheet)
| ID | Topic | Planned | Status | Quiz |
|---|---|---|---|---|
| FN01 | OOP: the four pillars | Wed 4 – Thu 5 Nov | ⬜ | |
| FN02 | Python OOP: ABC, MRO, super, methods, dunders, dataclasses | Fri 6 – Mon 9 Nov | ⬜ | |
| FN03 | Python data model: mutability, identity, copies, hashing | Tue 10 – Wed 11 Nov | ⬜ | |
| FN04 | Functions: *args/**kwargs, scope, closures, decorators | Thu 12 – Fri 13 Nov | ⬜ | |
| FN05 | Iterators, generators, context managers | Mon 16 – Tue 17 Nov | ⬜ | |
| FN06 | Composition vs inheritance, SOLID, DI | Wed 18 – Thu 19 Nov | ⬜ | |
| FN07 | Design patterns in Python | Fri 20 – Mon 23 Nov | ⬜ | |
| FN08 | Exceptions, memory, GIL, interpreter | Tue 24 – Wed 25 Nov | ⬜ | |
| FN09 | Big-O of Python data structures | Thu 26 Nov | ⬜ | |
| FN10 | DBMS: keys, normalisation, ACID, joins, indexes | Fri 27 – Mon 30 Nov | ⬜ | |
| FN11 | SQL basics: execution order, window functions, classics | Tue 1 – Wed 2 Dec | ⬜ | |
| FN12 | OS: processes, threads, deadlock, memory, scheduling | Thu 3 – Fri 4 Dec | ⬜ | |
| FN13 | Networking recap: layers, TCP/UDP, URL to page, HTTP | Mon 7 Dec | ⬜ | |
| FN14 | Git essentials | Tue 8 Dec | ⬜ | |
| FN15 | Testing basics: pyramid, pytest, fixtures, mocking | Wed 9 – Thu 10 Dec | ⬜ | |

Fri 11 Dec: review everything marked Revisit. Must-finish = Sunday of the following week.

## 3. ➕ Long-term CS foundations (5–10 year horizon, self-study after the course)
| ID | Subject | Best book | Best free course | Other materials | Status |
|---|---|---|---|---|---|
| F01 | Networking | *Computer Networking: A Top-Down Approach* (Kurose & Ross) | Stanford CS144 | Beej's Guide to Network Programming | ⬜ |
| F02 | Operating systems | *Operating Systems: Three Easy Pieces* (free) | MIT 6.1810 (6.S081) | xv6 book (free) | ⬜ |
| F03 | Databases | *Database Internals* (Petrov) | CMU 15-445 (Andy Pavlo, YouTube) | *Use The Index, Luke* (free site) | ⬜ |
| F04 | Distributed systems | *Designing Data-Intensive Applications* (Kleppmann) | MIT 6.5840 (6.824) | Raft paper; Kleppmann's Cambridge lectures | ⬜ |
| F05 | Algorithms & data structures | *The Algorithm Design Manual* (Skiena) | MIT 6.006 (OpenCourseWare) | NeetCode 150 | ⬜ |
| F06 | Discrete math | *Mathematics for Computer Science* (Lehman, Leighton, Meyer; free) | MIT 6.042J (OpenCourseWare) | — | ⬜ |
| F07 | Linear algebra | *Introduction to Linear Algebra* (Strang) | MIT 18.06 (OpenCourseWare) | 3Blue1Brown *Essence of Linear Algebra* | ⬜ |
| F08 | Probability & stats | *Introduction to Probability* (Blitzstein & Hwang; free) | Harvard Stat 110 | *Seeing Theory* (free site) | ⬜ |
| F09 | How LLMs work | *Build a Large Language Model (From Scratch)* (Raschka) | Karpathy *Neural Networks: Zero to Hero* | *The Illustrated Transformer* (Alammar) | ⬜ |
| F10 | Building & evaluating LLM systems | *AI Engineering* (Chip Huyen) | Anthropic courses (github.com/anthropics/courses) | Hamel Husain's posts on evaluating LLM apps | ⬜ |
| F11 | Data engineering | *Fundamentals of Data Engineering* (Reis & Housley) | DataTalksClub Data Engineering Zoomcamp | Kafka docs | ⬜ |
| F12 | Software design | *A Philosophy of Software Design* (Ousterhout) | MIT 6.031 / 6.1020 readings | *Refactoring* (Fowler) | ⬜ |
| F13 | Security | *Security Engineering* (Ross Anderson) | MIT 6.858 (OpenCourseWare) | PortSwigger Web Security Academy; OWASP Top 10 | ⬜ |
| F14 | Observability | *Observability Engineering* (Majors et al.) | Google SRE book (free online) | Brendan Gregg's site | ⬜ |
| F15 | Writing | *On Writing Well* (Zinsser) | Google Technical Writing courses | — | ⬜ |

## Added / changed topics log
Every insertion, reorder or skip, with the reason, so the plan's evolution is traceable.

| Date | Change | Why |
|---|---|---|
| 2026-10-29 | ➕ S02b Bytes vs text, inserted before S03 | S03–S05 and N01 use `b"..."`, `.encode()`, `.decode()` and byte-counted `Content-Length` without ever explaining them; a networking beginner would trip on that. |
| 2026-10-30 | ➕ Section 3: Long-term CS foundations F01–F15 (book, free course, materials per subject) | Learner asked for the subjects to master over the next 5–10 years; kept as a self-study reference list after the backend patterns + LARP course. |
| 2026-10-31 | ↪ Whole schedule moved +1 week: Excel marathon now Wed 4 Nov → Sun 30 May (L01 Wed 4, L02 Thu 5, LAB00 Sat 7); PLAN.md week 1 now Sun 1 – Sun 8 with S01–S05 as prep Sun 1 – Mon 2 | Nothing from the Thu 29 – Sun 1 catch-up was started. A +1 week shift keeps the weekly rhythm (weeknight project + LARP, Fri mock, Sat lab) intact. |
| 2026-10-31 | ➕ Section 2b: Fundamentals FN01–FN15 (OOP, Python core, SOLID, patterns, DBMS, SQL, OS, networking, Git, testing), 96 questions in a new `Fundamentals` sheet, office micro-sessions 4 Nov – 11 Dec | LARP bank assumed the basics (OOP only in L54 on 11 Feb); first-round interviews ask "what is an ABC / polymorphism" early. |
| 2026-10-31 | ↪ Planner v5: weeknights 22:30–00:00 project + 00:00–01:00 LARP (was 22:00/23:45), DSA 18:15–19:15 at the office, a SHIP week after stages 1–5, Stage 6 kept → ends Sun 4 Jul 2027; three dates per item (initial v4 / planned v5 / must finish by). LARP and lab dates unchanged. v4 in `archive/`. | Real evenings: gym with a friend-trainer, family until ~22:30, so 30 min/night less than v4 assumed. |
| 2026-11-01 | ↪ Roadmap docx synced to v5 (`Marathon_Roadmap_v5.docx`; v4 in `archive/`): new times, office-time section, SHIP weeks 7/13/18/24/30 inserted, project weeks renumbered per stage with must-by dates, stage + gate tables on v5 dates. LARP Quiz Book dates unchanged. Council write-ups moved to `council-verdicts.md` (online doc deleted). | Keep the companion doc consistent with the planner so nothing contradicts. |
