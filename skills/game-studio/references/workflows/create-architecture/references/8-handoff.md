> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio create-architecture — Phase 8: Handoff

> Part of `$game-studio create-architecture`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## Phase 8: Handoff

**Step 1 — Update session state**: Write a summary to `production/session-state/active.md` covering: artifact written, TD/LP sign-off verdicts, any blockers, required ADRs remaining, and next step.

**Step 2 — Output the handoff** using exactly this template (no freeform prose, no rephrasing of section titles):

---

## Architecture Complete

`docs/architecture/architecture.md` v[N] — [TD-ARCHITECTURE: APPROVE / CONCERNS (accepted) / REVISED after CONCERNS / REVISED after REJECT / NOT ASSESSED / skipped — [mode] mode]. [One sentence on what the architecture covers.]

---

## Run These ADRs Next

**1. `$game-studio architecture-decision "[Title]"` → ADR-[XXXX]**
[One sentence: what it defines and what it unblocks.]

**2. `$game-studio architecture-decision "[Title]"` → ADR-[XXXX]**
[One sentence.]

**3. `$game-studio architecture-decision "[Title]"` → ADR-[XXXX]**
[One sentence.]

**Then:** `$game-studio architecture-review`, and `$game-studio create-control-manifest` once it passes and those ADRs are Accepted — it turns them into the layer rules manifest.

List top 3 from Phase 6 in priority order. If fewer than 3 remain, list only what's outstanding.

---

## Gate-Check Readiness

> **Required before `$game-studio gate-check pre-production`:**
> - [ ] Accept ADRs: [list Proposed ADR IDs that must be Accepted]
> - [ ] Write ADRs: [list ADR IDs that must still be written]
> - [ ] Run `$game-studio architecture-review` — writes the review report and the traceability index (`docs/architecture/requirements-traceability.md`) the gate reads
> - [ ] Run `$game-studio test-setup` — scaffolds `tests/unit/`, `tests/integration/`, CI workflow, and an example test file
> - [ ] Run `$game-studio ux-design` — creates `design/ux/interaction-patterns.md` and `design/accessibility-requirements.md`
>
> Run `$game-studio gate-check pre-production` when all boxes are checked.

If nothing is blocking, write instead:
> No blockers — run `$game-studio gate-check pre-production` now.

---

## Open Questions to Watch

| ID | Summary | Priority | Resolution Path |
|----|---------|----------|-----------------|
| QQ-XX | [short description] | High / Medium / Low | [ADR or system that resolves it] |

Omit this section entirely if there are no open QQs.

---

(End of handoff. Do not add trailing commentary after the closing rule.)

---
