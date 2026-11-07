> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio dev-story — Handoff Contract

## Role in Pipeline
Bridges planning and code by loading the full context for a single story (story file, TR registry, ADR, control manifest, engine prefs), routing to the correct programmer agent, implementing source code and tests, and leaving the story ready for `$game-studio story-done` (with `$game-studio code-review` first at `standard`/`full`).

## Inputs Required

### Files That Must Exist
| File | Required Fields / Sections | Read-Only? |
|------|---------------------------|-----------|
| `production/epics/**/*.md` (the story file) | `Status: Ready`, `TR-ID`, `Governing ADR`, `Manifest Version`, `## Acceptance Criteria`, `## Test Evidence`, `## Dependencies`, `## Out of Scope` | **Partially mutable.** This skill sets `Status:` to `In Progress` and updates `Last Updated:` before any agent runs (Phase 3), and at the end replaces `## Files` with the files changed — at `minimal` the story file is the only record of progress, since `sprint-status.yaml` is absent. On an ADR version mismatch answered "Re-read the changed ADR" it sets `ADR Version` to the ADR's current version and refreshes `**ADR Decision Summary**` and `## Implementation Notes`; on a manifest mismatch answered "Update" or "Use the old rules" it sets `Manifest Version:` (and on the latter adds `Manifest-Note:`). Everything else in the story file is read-only to this skill |
| `docs/architecture/tr-registry.yaml` | Entry matching the story's TR-ID with current `requirement` text | Yes |
| `docs/architecture/adr-NNNN-[slug].md` (referenced ADR) | `## Status`, `## Last Verified` (else `## Date`) — from `adr-status.sh`; `## Decision` (with its `### Implementation Guidelines`), `## Engine Compatibility`, `## ADR Dependencies` — read only on a version mismatch answered "Re-read the changed ADR" | Yes — the ADR is never edited; a mismatch updates the story's stamp, not the ADR |
| `docs/architecture/control-manifest.md` | `Manifest Version:` header, layer rules (required patterns, forbidden patterns, performance guardrails) | Yes |
| `project.yaml` | `engine.name`, `engine.version`, `naming.*`, `performance.*` — the primary source for each of these fields | Yes |
| `<skill-root>/references/studio/technical-preferences.md` | Legacy fallback for any field above that is absent or empty in `project.yaml`; **sole** source for forbidden patterns and allowed libraries (deliberately never migrated), plus the `Engine Specialists` section | Yes — required only for fields absent from `project.yaml`, and always for forbidden patterns |
| `docs/engine-reference/[engine]/VERSION.md` | Engine version, LLM knowledge cutoff, post-cutoff risk levels | Yes |
| `production/session-state/active.md` | (read to find active story when no argument given; created if absent) | No |

> **Tier.** SKILL.md Phase 2 decides by `workflow`: the TR registry is required at
> `full`, optional at `standard` and not expected at `minimal`; a missing control
> manifest warns at `full`/`standard` and is not expected at `minimal`; an ADR
> blocks when the story references one that is missing, `Proposed`, `Deprecated`
> or `Superseded`.

### Preconditions
- The target story must have `Status: Ready` (validated by `$game-studio story-readiness` at `standard`/`full`; at `minimal`, `$game-studio create-stories` writes stories `Ready` and `$game-studio story-readiness` is not on the path)
- The ADR referenced in the story must have `Status: Accepted` — if `Status: Proposed`, do not implement; surface this as a blocker and direct user to `$game-studio architecture-decision accept [ADR-id]`; `Deprecated` or `Superseded` also blocks, naming the successor. A story whose ADR field reads `N/A` references none, at every tier
- All `## Dependencies` stories listed in the story file must already have `Status: Complete` (or `Status: Done`)
- An engine must be configured — `engine.name` in `project.yaml`, or as legacy fallback an `**Engine**:` value in `<skill-root>/references/studio/technical-preferences.md` that is not `[TO BE CONFIGURED]`
- At `full`, `docs/architecture/tr-registry.yaml` must contain the story's TR-ID (optional at `standard`, not expected at `minimal`)
- `docs/architecture/control-manifest.md` supplies the layer rules when present; a missing one warns and never stops the skill

## Outputs Produced

### Files Written
| File | Guaranteed Fields / Sections | Notes |
|------|------------------------------|-------|
| `<code root>/[system]/[file].[ext]` | Doc-commented public APIs; no hardcoded gameplay values; follows ADR Implementation Guidelines and control-manifest required patterns | created or modified by the programmer agent; code root resolved per `<skill-root>/references/studio/code-root-resolution.md` |
| `tests/unit/[system]/[story-slug]_test.[ext]` OR `tests/integration/[system]/[story-slug]_test.[ext]` | One test function per acceptance criterion (Logic/Integration stories only); naming per engine (`<skill-root>/references/rules/test-standards.md`); no random seeds; no external I/O | created by the programmer agent; path matches `## Test Evidence` in story |
| The story file's `## Files` section | The code and test files the programmer agent created or changed, one per line | replaced through `md-section.sh replace` (the section is added at the end when the story has none); named in the one In Progress ask, skipped when that ask is declined. `$game-studio story-done` checks scope against it |
| `production/session-state/active.md` | `<!-- CHECKPOINT -->` block: current task (story path), next step, blocker, files in progress, run result | written on every outcome by `session-state.sh checkpoint`: the block is replaced, never appended (the file is created from `<skill-root>/references/studio/templates/session-state.md` if absent) |

## Immutability Rules
- READS but does NOT modify: `project.yaml`, `docs/architecture/tr-registry.yaml`, `docs/architecture/adr-NNNN-[slug].md`, all GDD files in `design/gdd/`, `docs/architecture/control-manifest.md`, `<skill-root>/references/studio/technical-preferences.md` (legacy fallback), `docs/engine-reference/[engine]/VERSION.md`
- MODIFIES, through the programmer agents: `<code root>/**` (new/updated source files; code root resolved per `<skill-root>/references/studio/code-root-resolution.md`) and the engine's test root (the new test file; `tests/` on Godot)
- MODIFIES, itself, each after an ask that names the file (in `collaborative` mode; `<skill-root>/references/studio/automation-modes.md` governs the others): the story file's `Status:`, `Last Updated:`, `## Files`, `ADR Version`, `**ADR Decision Summary**`, `## Implementation Notes`, `Manifest Version:` and `Manifest-Note:` (see the story row above); the story's entry in `production/sprint-status.yaml` (`status: in-progress`, top-level `updated`); a dependency story's `Status:` (that dependency answer only); a Config/Data story's data file; on Unity, `Assets/Scripts/ScreenshotOnArg.cs`, written verbatim from `<skill-root>/references/studio/run-and-observe.md` when the project has none
- MODIFIES without an ask: `production/session-state/active.md` — its `<!-- CHECKPOINT -->` block is overwritten, never appended
- Sets the story file's own `Status` field to `In Progress` only (Phase 3, before
  any agent runs). Closing the story being implemented is the exclusive
  responsibility of `$game-studio story-done`; the one other `Status` this skill writes is a
  dependency's `Complete` under that dependency answer (Hard Constraints)

## Downstream Skill Expects
**Next skill:** `$game-studio story-done`
- It will read: the story file (to check `Status`, `## Acceptance Criteria`, `## Test Evidence` path, `Type:`, referenced ADR, TR-ID)
- It assumes: the test file declared in `## Test Evidence` already exists on disk (for Logic/Integration stories)
- It assumes: `production/session-state/active.md` records the story path and files changed (used to locate the in-progress story when no argument is given)
- It assumes: source files under the resolved code root are present and match the criterion descriptions, so Grep-based deviation checks can run

## Known Fragile Points
- If the story's embedded `Manifest Version` differs from the current `docs/architecture/control-manifest.md` header date, rules may have changed since the story was authored — the skill surfaces this, but silently proceeding would produce code that violates newer manifest rules
- The test file path in `## Test Evidence` must be exact: `$game-studio story-done` uses that literal path for Glob checks; a typo here causes a false BLOCKING result downstream
- If `docs/architecture/tr-registry.yaml` has a stale `requirement` text that diverges from the GDD, the implementation may satisfy the registry but fail the GDD — always treat the registry as authoritative per design, but flag if a visible discrepancy is noticed
- Agent failures are non-fatal by design (partial reports are surfaced), but a blocked programmer agent means no source files are written — `$game-studio story-done` will then fail its file-existence checks
- Config/Data stories produce no test file; `$game-studio story-done` must see `Type: Config/Data` in the story header to classify the story correctly — otherwise it resolves the test-evidence gate for the wrong type (e.g. Logic, which is BLOCKING by default) and may flag a missing test
