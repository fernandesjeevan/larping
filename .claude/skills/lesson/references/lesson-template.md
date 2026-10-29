# Lesson folder template

```
lessons/<ID>-<kebab-problem-name>/
  README.md              # stage 0 brief + stage 1 challenge; stage 3 pattern section appended later
  solution.py            # learner's file. You write ONLY stubs + docstrings.
  test_stage1.py         # proves the brute force works (functional spec)
  test_stage2_break.py   # written at /check time; proves the flaws (fails on brute force)
  test_stage3.py         # optional: pattern-specific behaviour
  notes.md               # optional: learner's own notes / measurements
```

Folder names use the *problem*, not the pattern (e.g. `D01-slow-reads`, not `D01-cache-aside`).

## README.md skeleton

```markdown
# <ID> — <Problem title>
> Maps to: LARP Lxx · Saturday LABxx · Project: <where this shows up in DocuLens/SRE/Translator>
> Time: ~<n> min · Stage: 0–1

## Why you care
<2–4 lines: a production story where this goes wrong>

## Theory
<short sections, each ≤ 6 lines, each followed by a snippet>

### Snippet: <name>
```python
# runnable, stdlib only
```

## Check yourself
1. <question>
2. <question>
(Answer in chat before starting the challenge.)

## Challenge — stage 1 (brute force)
Implement in `solution.py`:
- `def ...` — <behaviour>
Rules: simplest thing that works. Don't optimise. Don't google the pattern.

Run: `pytest lessons/<dir>/test_stage1.py -q`, then type `/check`.

<!-- STAGE 3 (pattern reveal) is appended below by the tutor after /check rounds -->
```

## Stage 3 section skeleton (appended later)

```markdown
## Stage 3 — The pattern: <Name>
**Intent:** one sentence.
**Structure:** ASCII diagram.
**Canonical snippet:** ...
**Trade-offs:** table (gain / cost).
**Don't use it when:** ...
**In the wild:** FastAPI / Celery / Redis / Postgres / Kafka / cloud examples.
**Say it in an interview (30 s):** a model answer in first person.
```

## Test conventions
- Import from `solution` (pytest's default rootdir import puts the lesson dir on sys.path).
- Every network/thread test has a timeout (socket `settimeout`, `thread.join(timeout=...)`).
- Measure, then assert: count calls, time durations, and print the numbers in the assertion
  message so the failure *teaches* (e.g. `assert db_calls == 1, f"DB was hit {db_calls} times"`).
