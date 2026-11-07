> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

Resolved above — use as-is; `--review` overrides `review_mode`. No block →
defaults in `<skill-root>/references/studio/config-resolution.md`.

# Create Architecture

This skill produces `docs/architecture/architecture.md` — the master architecture
document that translates all approved GDDs into a concrete technical blueprint.
It sits between design and implementation, and must exist before sprint planning begins.

**Distinct from `$game-studio architecture-decision`**: ADRs record individual point decisions.
This skill creates the whole-system blueprint that gives ADRs their context.

See `<skill-root>/references/studio/director-gates.md` for the full check pattern. Individual gate definitions live in `<skill-root>/references/studio/director-gates/[gate-id].md` — the spawned agent reads its own gate file; do not read it in the parent session.

**`docs.density`** — it controls per-section *depth*, where `workflow`
controls which sections exist. `modes.rigor` sets both together; set
`docs.density` explicitly to vary depth alone: `terse` (the default, via `rigor: minimal`) = layer diagrams + decision bullets,
no essays; `balanced` = diagrams + paragraph explanations of layer choices
(`rigor: standard`); `thorough` = full prose with rationale, trade-offs, and alternatives
considered per layer. Apply it to every section you author.

**`workflow`** (see `<skill-root>/references/studio/workflow-modes.md`):
- `full` — full architecture: all layers, module ownership, data flow, API
  boundaries, full ADR audit.
- `standard` — simplified: system layer map + critical ADR list only.
- `minimal` — not required. Can still be run voluntarily.

**Argument modes:**
- **No argument / `full`**: Full guided walkthrough — all sections, start to finish
- **`layers`**: Focus on the system layer diagram only
- **`data-flow`**: Focus on data flow between modules only
- **`api-boundaries`**: Focus on API boundary definitions only
- **`adr-audit`**: Audit existing ADRs for engine compatibility gaps only

---

## Phase 0: Load All Context

**Read `references/0-load-context.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 1: System Layer Mapping

**Read `references/1-layers.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 2: Module Ownership Map

**Read `references/2-module-ownership.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 3: Data Flow

**Read `references/3-data-flow.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 4: API Boundaries

**Read `references/4-api-boundaries.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 5: ADR Audit + Traceability Check

**Read `references/5-adr-audit.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 6: Missing ADR List

**Read `references/6-missing-adrs.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 7: Write the Master Architecture Document

**Read `references/7-write.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Phase 8: Handoff

**Read `references/8-handoff.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## Recommended Next Steps

- Run `$game-studio architecture-decision [title]` for each required ADR listed in Phase 6 — Foundation layer ADRs first
- Run `$game-studio architecture-review` — bootstraps the Requirements Traceability Matrix and TR registry from the ADRs just written, and gives each provisional TR-ID its permanent one. Required before the Pre-Production gate.
- Run `$game-studio test-setup` to scaffold `tests/unit/`, `tests/integration/`, CI workflow, and an example test (required for gate-check)
- Run `$game-studio ux-design` to initialize `design/ux/interaction-patterns.md` and `design/accessibility-requirements.md` (required for gate-check)
- Run `$game-studio create-control-manifest` once the required ADRs are written to produce the layer rules manifest
- Run `$game-studio gate-check pre-production` when all required ADRs, `$game-studio test-setup`, and `$game-studio ux-design` are complete
