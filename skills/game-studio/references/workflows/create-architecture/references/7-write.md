> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio create-architecture — Phases 7 and 7b: Write and Sign-Off

> Part of `$game-studio create-architecture`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## Phase 7: Write the Master Architecture Document

**In this file:**

- Phase 7: the master architecture document template, then the write
- Phase 7b: Technical Director Sign-Off + Lead Programmer Feasibility Review: review mode check, presenting both assessments, recording the sign-off

Once all sections are approved, write the complete document to
`docs/architecture/architecture.md`.

In an update (Phase 0e `[A]`, or a focus-area argument), write only the chosen
sections instead, replacing each in place with patch editing, and raise `Version`; the
ask below then names those sections and the version change.

The document structure:

```markdown
# [Game Name] — Master Architecture

## Document Status
- Version: [N]
- Last Updated: [date]
- Engine: [name + version]
- GDDs Covered: [list]
- ADRs Referenced: [list]

## Engine Knowledge Gap Summary
[Condensed from Phase 0d inventory — HIGH/MEDIUM risk domains and their implications]

## System Layer Map
[From Phase 1]

## Module Ownership
[From Phase 2]

## Data Flow
[From Phase 3]

## API Boundaries
[From Phase 4]

## ADR Audit
[From Phase 5]

## Required ADRs
[From Phase 6]

## Architecture Principles
[3-5 key principles that govern all technical decisions for this project,
derived from the game concept, GDDs, and technical preferences]

## Open Questions
[Decisions deferred — must be resolved before the relevant layer is built]
```

---

## Phase 7b: Technical Director Sign-Off + Lead Programmer Feasibility Review

After writing the master architecture document, perform an explicit sign-off before handoff.

**Review mode check** — apply before spawning either gate:
- `solo` → skip both. Note: "TD-ARCHITECTURE and LP-FEASIBILITY skipped — Solo mode." Go to Step 4 and record both as skipped, then Phase 8.
- `lean` → skip both (neither is a PHASE-GATE). Note: "TD-ARCHITECTURE and LP-FEASIBILITY skipped — Lean mode." Go to Step 4 and record both as skipped, then Phase 8.
- `full` → spawn both, in parallel.

**Step 1 — Spawn `technical-director` via `Agent` using gate TD-ARCHITECTURE (`<skill-root>/references/studio/director-gates/td-architecture.md`):**

Pass: the architecture document path (`docs/architecture/architecture.md`), the Technical Requirements Baseline (TR-IDs and count), the ADR list with statuses, and the Engine Knowledge Gap Inventory from Phase 0d. Issue this call and Step 2's before waiting for either result.

**Step 2 — Spawn `lead-programmer` via `Agent` using gate LP-FEASIBILITY (`<skill-root>/references/studio/director-gates/lp-feasibility.md`):**

Pass: architecture document path, technical requirements baseline summary, ADR list.

**Step 3 — Present both assessments to the user:**

Show the TD-ARCHITECTURE verdict (APPROVE / CONCERNS / REJECT) and the LP-FEASIBILITY verdict (FEASIBLE / CONCERNS / INFEASIBLE) side by side.

**Step 4 — Record sign-off in the architecture document:**

Update the Document Status section:
```
- TD-ARCHITECTURE: [date] — APPROVE / CONCERNS (accepted) / REVISED after CONCERNS / REVISED after REJECT / NOT ASSESSED — [missing input] / skipped — [mode] mode
- LP-FEASIBILITY: [date] — FEASIBLE / CONCERNS (accepted) / REVISED after CONCERNS / REVISED after INFEASIBLE / NOT ASSESSED — [missing input] / skipped — [mode] mode
```

---
