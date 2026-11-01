# Council verdicts (31 Oct 2026)

Three llm-council runs about the marathon plan. **What you actually decided overrides all three**
(top section). Live schedule: `evening-plan.md` and `Marathon_Daily_Planner_v5.xlsx`.
Rule: no more councils until 20 logged hours.

## What you decided (final, = planner v5)

- Keep the gym 5 days (trainer = physio friend; normal day 19:30, early day friend calls 18:00).
- Weekday: office breaks = Fundamentals FN01–FN15 + LARP flashcards (5–10 min) ·
  18:15–19:15 DSA at the office (skip on early-gym days) · 19:15–21:45 gym ·
  22:30–00:00 project card (personal laptop, home only) · 00:00–01:00 LARP · sleep 01:00–08:30.
- Weekend as in v4. Project never on the work laptop / personal laptop never at the office.
- Late cards are OK until their **Must finish by** date; SHIP weeks (W7, W13, W18, W24, W30) are catch-up.

## Council #3 (final): use the 18:15–19:20 gap

- Keep the gym. DSA at the office from **18:00** (not 17:30: that's company time).
- DocuLens only at home on the personal laptop.
- Ask the friend to confirm by 16:00 whether it's an early day; pack the gym bag every morning.
- Honest weekday total is about 8–9 h/week; don't plan more than that.

## Council #2: should I quit the gym?

- **No.** Timetable then: Block A 18:30, Block B 22:45 (later replaced by your v5 times).
- 14-day test, 1–14 Nov: ≥ 24 h logged → keep the gym as is; < 24 h because of gym tiredness →
  gym Mon/Wed/Fri only; < 24 h for other reasons → study at a café/the office instead.
- Weight goal 78 → 73 kg by mid-January (mostly a fixed dinner plate).
- Accountability: send a nightly screenshot of the ticked Daily Plan to one named person.

## Council #1: the 30-week plan (full text, moved here from the online doc)

Its "cut to 10 weeks" call was not adopted; you kept the full plan but added SHIP weeks and
must-finish-by dates. Its blind spots (notice periods, referrals, contract/IP clause, DSA) still apply.

### Council Verdict: 30-week Backend + AI Marathon

Oct 31, 2026 · @Jeevan Fernandes

#### The short answer

The plan isn't what's failing. Starting is. Cut it to 10 weeks, build one project deeply, and make your first commit now, not on Wednesday.

- **Plan reviewed:** the 30-week marathon (Wed 4 Nov 2026 to Sun 30 May 2027): the Excel planner, the roadmap .docx and `PLAN.md`.
- **How the council ran:** five advisors answered independently: the Contrarian, the First-Principles Thinker, the Expansionist, the Outsider and the Executor. Then five reviewers ranked their answers without knowing who wrote which. A chairman combined everything into this verdict.
- **Fact check:** two advisors said the plan has no "minimum day" rule. It does (25 min of the card + 15 min of questions aloud). It has never been used because Day 1 has never happened.

#### Where the council agrees

All five advisors reached the first point independently. These are the high-confidence findings.

- **The problem is starting, not the plan.** There have been three start dates, but no code yet. Meanwhile the planning grew to a 16-sheet Excel, a 30-page roadmap and 600 questions. Each restart made the plan bigger and harder to start.
- **The plan really only runs for 10 weeks.** You apply from week 3 and take the first good offer, so recruiters judge what exists in weeks 3 to 10. Weeks 12 to 30 will probably never happen.
- **Stage 1 alone is about 3 months of evenings.** Hybrid search, rerank, Celery, OCR, human approval steps, RBAC, tenancy, CI and Azure are too much in 6 weeks for someone without Docker who is new to networking.
- **Setup will eat week 1.** Docker isn't installed, Celery doesn't officially support Windows, and Python 3.14 may not have all the packages yet.
- **The 23:45 to 01:00 block will break first.** Bedtime at 1 AM four nights a week for 30 weeks, on top of a full-time job, won't last.
- **One deep project beats four shallow ones.** Interviewers keep asking follow-ups until your answer runs out. Interview practice only works if you actually built the thing.
- **Your current job is your strongest story.** Three advisors said this. "I put AI agents into production for enterprise users" is real experience, and the plan treats it as nothing.

#### Where the council clashes

Four real disagreements. Each row shows both sides and how the chairman settled it.

| Question | One side | Other side | Chairman's call |
| --- | --- | --- | --- |
| Add scope or cut it? | Expansionist: link DocuLens to your company's Copilot agents, focus on insurance/banking, post weekly on LinkedIn | The other four: cut hard. All five reviewers said adding work doesn't fix the restarts | Cut now. The market point is right: companies want people who know enterprise agents and pro-code backends |
| Can you claim "3 years"? | Contrarian: low-code years plus side projects won't pass as 3 years of backend | Expansionist: "I shipped enterprise agents and built the backend behind them" does pass | Only if the pro-code part is real and you can defend it in detail |
| When to take AI-102? | Expansionist: week 6 | Plan: week 16. Reviewers: may not matter for backend roles | Decide after reading 20 real job ads |
| Practise in office breaks? | Executor: yes, move interview practice there and stop nights at 23:45 | Outsider: studying on the work laptop during office hours is a risk | Stop at 23:45 and move interview practice to Saturday and Sunday |

#### Blind spots the council caught

None of the five advisors raised these. They came up when the reviewers compared the answers.

- **Notice periods of 60 to 90 days.** An offer in week 10 means you join around week 20 to 22. Ask about notice buyouts.
- **Background checks verify titles and dates.** An inflated "3 YOE backend" claim can get an offer withdrawn.
- **Moonlighting and IP clauses.** Read your employment contract before public repos, LinkedIn posts, or connecting anything to company agents or data.
- **Laptop RAM and money.** Docker, Postgres + pgvector, Celery and kind together can choke 8 GB of RAM. Cloud and LLM API bills add up on a personal budget.
- **Referrals beat cold applications.** 10 to 15 cold applications a week convert poorly in India. Start referral asks in week 1, not week 5.
- **Indian hiring filters.** DSA is a main filter, and "DSA in office time" has no protected slot. Many backend roles ask for Java or Go. You haven't read 20 real job ads or had a real interview yet.
- **Nobody asked why the earlier starts failed.** Outside accountability (a study partner, a public weekly commit) could help.

#### The recommendation

Cut it to a 10-week plan measured in hours you actually log, not hours you schedule. Re-plan only after 4 straight weeks of at least 10 real hours.

| Keep | Cut (or move to after the offer) |
| --- | --- |
| DocuLens core: FastAPI, Postgres + pgvector, hybrid search, evals, deployed on Azure with a URL | PDF Translator |
| Minimum-day and stop rules, and actually use them | AWS, Terraform, EKS (stay on Azure) |
| Applying from week 3 | Event sourcing and CQRS |
| AI-102, only if real job ads ask for it | GraphRAG, fine-tuning, A2A |
| One log line per day | Most of the 16 Excel sheets |
| About 100 of the questions | About 500 of the 600 questions |

*(10-week order: 4 phases, 2 gates. Not adopted.)*

Week 0 is now. Each gate proves a phase is done: first a pushed commit, then a live URL with your resume sent out.

- **Every day:** stop at 23:45 and move interview practice to Saturday and Sunday.
- **At work:** ask for pro-code tasks (custom connectors, Azure Functions, Semantic Kernel). Don't wire personal projects to company data.
- **Weekly test:** "What did I push and what did I send?" If the answer is nothing, cut scope that week. Don't re-plan.

#### The one thing to do first

**Today or tomorrow (not Wednesday), push a first commit of a tiny FastAPI app running on Python 3.12 inside WSL2, with Postgres + pgvector running in Docker.** That commit's timestamp is your real start date.

You already have WSL2, so what's left is Docker Desktop (with its WSL2 integration turned on), `uv` with Python 3.12 inside WSL, and one `docker compose up` for Postgres + pgvector.

This doesn't replace S01 to S05. Those networking basics stay as 10 to 20 minute break-time sessions. Evenings go to code that runs.

#### Appendix: each advisor's answer

Four of five reviewers rated the Contrarian's answer strongest; the other picked the First-Principles Thinker's. All five reviewers named the Expansionist's as the biggest blind spot, because it adds work without fixing the restarts.

##### The Contrarian

The fatal flaw is that the planning has become the procrastination. Three start dates passed with zero code shipped, and the plan grows each time execution fails. Moving the start to Wednesday is a fourth restart.

Week 3 is where it breaks. Weeks 1 to 6 of DocuLens are a quarter's work for an experienced backend engineer. Week 1 goes to setup, Gate 0 slips, and in your history a slipped gate leads to a restart.

The offer rule makes half the plan pointless: if it works, weeks 16 to 30 never happen. SQL depth, system design and Postgres internals, which 3-YOE interviews test first, have no time slot. Your years are low-code, so your real lever is the day job.

Cut the PDF Translator, the AWS stage, GraphRAG, fine-tuning, A2A, about 500 questions and most Excel sheets. Build one smaller DocuLens, live in 14 days. Put SQL and system design ahead of everything.

##### The First-Principles Thinker

You're solving the wrong problem. The plan isn't the bottleneck: planning has become the work because it feels productive and can't fail.

Getting hired needs three things: a resume that gets callbacks, one project you can defend in depth, and passing DSA, system design and backend rounds. Recruiters judge whatever exists in weeks 3 to 10. "You have a 10-week plan with 20 weeks of hopes attached."

Your job is your biggest asset, not a liability. Do pro-code work there now: custom connectors, Azure Functions, Semantic Kernel, Python APIs behind your Copilot agents.

Use one text file, one line per day. Build one project: DocuLens without the extras. Measure hours logged, and log 10 a week for 4 straight weeks before planning more.

##### The Expansionist

Copilot Studio is a way into an under-supplied market. GCCs, Microsoft partners and enterprise SaaS in India need people who know both enterprise agent rollout and pro-code backends. "I put agents into production and built the backend behind them" is a 3-YOE story.

Make DocuLens the backend your Copilot agents call through a custom connector or MCP. Look for an internal move to a pro-code AI team.

Pick a vertical: merge DocuLens and the PDF Translator into document AI for Indian insurance and banking. Post weekly on LinkedIn. Take AI-102 by week 6. Aim to be interview-ready by week 8 to 10.

##### The Outsider

Reading this cold: a huge planning setup and zero hours of work. Each restart produces a bigger plan, which is harder to start. Why start Wednesday when it's Saturday?

Bedtime at 1 AM for 30 weeks alongside a job breaks with one sick week, crunch or wedding. "LARP" means pretending, and interviewers keep asking until the pretending runs out. Back every answer with something you built.

Weeks 1 to 6 read like a job ad pasted into a calendar. A recruiter remembers one project you can explain deeply. Watch the risk of studying on the work laptop during office hours.

##### The Executor

Your first project will stall on setup: Postgres, Celery, Redis and OCR with no Docker, and Python 3.14 packages that may not install.

Today: get Docker running, install `uv`, pin Python 3.12, `docker compose up` Postgres with pgvector, write one ugly FastAPI endpoint under 200 lines (upload a PDF, chunk, embed, answer one question), and `git push`.

Ship a thin end-to-end version by week 2 and deepen it later. Stop at 23:45. Drop the Excel and keep one rule: a commit every scheduled day and a resume out this weekend. Each week ask: "What did I push and what did I send?"
