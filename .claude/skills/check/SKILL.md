---
name: check
description: Review the learner's attempt for the current Backend Patterns lesson. Use when the learner says /check, "check my code", "review my solution", or "I'm done". Runs the tests, critiques the brute force Socratically, writes a failing break-test that proves the flaw, or advances to the pattern reveal.
argument-hint: "[lesson id, optional]"
---

# /check — review the learner's attempt

1. Read `progress.md` to find the current lesson and stage, then read that lesson's entry in
   `../lesson/references/curriculum.md` and the learner's `solution.py`.
2. Run all tests in the lesson folder: `python -m pytest lessons/<dir> -q` (timeout 120 s).
   Report the real result; never claim green if it isn't.

## Then act on the stage

**Stage 1 (brute force), tests failing:** point to the *first* failing behaviour, quote the
assertion, and ask a guiding question. Don't fix it for them. Offer `/hint`.

**Stage 1 passing → open stage 2:**
1. Say what's genuinely good (1–2 specific lines, no filler).
2. Code review notes that aren't the lesson's main flaw (naming, error handling, missing
   edge cases) as a short bullet list labelled "Minor".
3. Socratic probe: ask ONE question that points at the next curriculum break round
   ("What happens to client B if client A connects and never finishes sending?").
   **Stop and wait for their answer.**
4. After they answer (next turn, or immediately if they ran /check again): grade the
   reasoning, then write `test_stage2_break.py` (or add a test to it) that demonstrates the
   flaw, run it, and show that it fails against their code with the measured number.
   Ask them to fix it their own way. Update `progress.md` to "stage 2, round N".

**Stage 2, break test now passing:** acknowledge, then do the next break round from the
curriculum. When the rounds are done (or their fix has already arrived at the pattern),
move to stage 3: append the pattern section to the lesson `README.md` (template in
`../lesson/references/lesson-template.md`), and ask them to refactor to the clean pattern.

**Stage 3 passing:** review the pattern implementation against the canonical form (are the
trade-offs handled? edge cases?). If solid, run stage 4 (LARP) as described in the
`lesson` skill: 3 interview questions + 1 scenario, one at a time, graded 0–2.

## Review style
- Line-referenced (`solution.py:42`), concrete, specific.
- Distinguish **bug** (wrong behaviour now), **flaw** (breaks under load/concurrency/failure,
  which is the lesson), and **style**.
- If they found the pattern early on their own, say so and skip ahead; don't make them
  sit through break rounds they've already solved.
- If they ask "show me", show a clean reference solution, explain it line by line, and
  have them retype it from memory afterwards (their own words, not copy-paste).
- Always update `progress.md` and end with the next action.
