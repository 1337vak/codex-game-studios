> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio prototype — Phase 8: Creative Director Review

> Part of `$game-studio prototype`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## Phase 8: Creative Director Review

**Review mode check:**
- `solo` → skip. Note: "CD-PLAYTEST skipped — Solo mode."
- `lean` → skip. Note: "CD-PLAYTEST skipped — Lean mode."
- `full` → spawn `creative-director` via `Agent` using gate **CD-PLAYTEST** if
  `design/gdd/game-concept.md` exists with game pillars defined, or
  `design/game-brief.md` exists (the `rigor: minimal` brief has no pillars — its
  pitch and "what they feel" line stand in). If neither is available, note:
  "CD-PLAYTEST skipped — game pillars not yet defined at concept prototype stage."

Pass: the full REPORT.md content, the original hypothesis, and game pillars /
core fantasy from `design/gdd/game-concept.md` (or the brief's pitch and "what
they feel" line from `design/game-brief.md`). Read the concept by section: find the
headings you need with the Grep tool (pattern `^#`, content mode) and Read those
ranges with offset and limit.

The creative director evaluates the result against the game's creative vision and
returns one of the gate's verdicts — APPROVE, CONCERNS or REJECT — or NOT
ASSESSED when it could not judge. Apply it to the recommendation:

---
