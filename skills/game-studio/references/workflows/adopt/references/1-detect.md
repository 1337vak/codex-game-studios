> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio adopt — Phase 1: Detect Project State

> Part of `$game-studio adopt`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## Phase 1: Detect Project State

Emit one line before reading: `"Scanning project artifacts..."` — this confirms the
skill is running during the silent read phase.

Then read silently before presenting anything else.

### Existence check
- `project.stage` in `project.yaml` (fallback `production/stage.txt`) — if either is present, use that value (authoritative phase)
- `design/gdd/game-concept.md` (or, at the minimal tier, `design/game-brief.md`) — concept exists?
- `design/gdd/systems-index.md` — systems index exists?
- Count GDD files: `design/gdd/*.md` (excluding game-concept.md and systems-index.md)
- Count ADR files: `docs/architecture/adr-*.md`
- Count story files: `production/epics/**/*.md` (excluding EPIC.md)
- `project.yaml` (`engine.name`) / `<skill-root>/references/studio/technical-preferences.md` — engine configured?
- `docs/engine-reference/` — engine reference docs present?
- Glob `docs/adoption-plan-*.md` — note the filename of the most recent prior plan if any exist

### Infer phase (if no project.stage / stage.txt)
Use the same heuristic as `$game-studio project-stage-detect`:
- 10+ source files in the code root → Production
- Stories in `production/epics/` → Pre-Production
- ADRs exist → Technical Setup
- systems-index.md exists → Systems Design
- game-concept.md (or `design/game-brief.md`) exists → Concept
- Nothing → Fresh (not a brownfield project — suggest `$game-studio start`)

`$game-studio start` and Cancel end this skill: say which, and stop.

**If they pick "help me find them"**, search before asking anything else:

Report: "Detected phase: [phase]. Found: [N] GDDs, [M] ADRs, [P] stories."

---
