---
name: hint
description: Give an escalating hint for the current Backend Patterns lesson without giving away the solution. Use when the learner says /hint, "I'm stuck", or "give me a hint".
---

# /hint — escalating hints

Read `progress.md` (current lesson + stage), the lesson `README.md`, and `solution.py`.
Count prior hints for this stage in `progress.md` (field `hints:`) and give the next level:

1. **Nudge:** a question that reframes the problem ("What does `recv` return when the
   client has sent only part of the request?").
2. **Concept:** name the concept or stdlib tool to look at (`socket.settimeout`,
   `str.partition`, `threading.Lock`), with a link to the Python docs page.
3. **Shape:** pseudocode or a skeleton of the function with the key lines left as `...`.
4. **Near-solution:** a concrete snippet for the hardest 3–5 lines, explained. Tell them
   this is the last step before "show me".

Rules: one level per call; tailor it to *their* code (reference their lines), not generic
advice; increment the `hints:` counter in `progress.md`. If their code has a bug unrelated
to what they're stuck on, mention it in one line.
