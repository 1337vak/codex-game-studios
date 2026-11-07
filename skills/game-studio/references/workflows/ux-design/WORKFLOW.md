> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

Resolved above — use as-is. No block → defaults in
`<skill-root>/references/studio/config-resolution.md`.

# UX Design

When this skill is invoked:

**Authoring guidance**: the skeletons below are self-contained — author from them
directly. When a section needs depth (worked examples, pattern catalogs,
accessibility criteria), the matching guide has it:

| Producing | Guide |
|---|---|
| UX spec | `<skill-root>/references/studio/templates/guidance/ux-spec-guide.md` |
| HUD design | `<skill-root>/references/studio/templates/guidance/hud-design-guide.md` |
| Interaction patterns | `<skill-root>/references/studio/templates/guidance/interaction-pattern-library-guide.md` (routes to three topic files) |
| Accessibility requirements | `<skill-root>/references/studio/templates/guidance/accessibility-requirements-guide.md` |

**Load a guide per-section, never whole** — each is organised by section and the
pointers in the templates name the exact section to read.

**`workflow`** (see `<skill-root>/references/studio/workflow-modes.md`):
- `full` — a UX spec is required per screen.
- `standard` — core screens only (main menu, HUD, primary game loop).
- `minimal` — not required. Can still be run voluntarily.

**`docs.density`** — it controls per-section *depth*, where `workflow`
controls which screens are specced. `modes.rigor` sets both together; set
`docs.density` explicitly to vary depth alone: `terse` (the default, via `rigor: minimal`) = wireframe descriptions +
interaction bullets; `balanced` = wireframes + paragraph descriptions of flows
(`rigor: standard`); `thorough` = full prose including user-research summaries and
alternative flow considerations. Apply it to every section you author.

## 1. Parse Arguments & Determine Mode

Four authoring modes exist based on the argument:

| Argument | Mode | Output file |
|----------|------|-------------|
| `hud` | HUD design | `design/ux/hud.md` |
| `patterns` | Interaction pattern library | `design/ux/interaction-patterns.md` |
| `accessibility` | Project-wide accessibility requirements | `design/accessibility-requirements.md` |
| Any other value (e.g., `main-menu`, `inventory`) | UX spec for a screen or flow | `design/ux/[argument].md` |
| No argument | Ask the user | (see below) |

> **`accessibility` is the only mode that writes outside `design/ux/`.** Its
> output is a project-wide standard the per-screen specs consult, not a spec for
> one screen — `<skill-root>/references/studio/workflow-catalog.yaml`, the Pre-Production and
> Polish gates, and `$game-studio architecture-review` all check
> `design/accessibility-requirements.md` at that exact path. Do not "tidy" it
> under `design/ux/`: every one of those checks would stop matching, and the
> Technical Setup → Pre-Production gate would become unpassable.

If the user selects "I'll name it" or types a screen name, normalize it to kebab-case
for the filename (e.g., "Main Menu" becomes `main-menu`).

---

## 2. Gather Context (Read Phase)

**Read `references/2-gather-context.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## 3. Create File Skeleton

**Read `references/3-file-skeleton.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## 4. Section-by-Section Authoring

**Read `references/4-authoring.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

### Section guidance — read the ONE file for the active mode

Per-section authoring guidance lives in its own file per mode. **When you reach
Phase 4, read only the file matching the mode resolved in Section 1; never load
the other two.**

| Mode | Guidance file |
|------|---------------|
| UX Spec (screen or flow) | `references/sections-ux-spec.md` |
| HUD Design | `references/sections-hud.md` |
| Interaction Pattern Library | `references/sections-patterns.md` |
| Accessibility Requirements | `<skill-root>/references/studio/templates/guidance/accessibility-requirements-guide.md` |

> The accessibility guidance lives under `templates/guidance/` rather than this
> skill's `references/` because the template it documents
> (`<skill-root>/references/studio/templates/accessibility-requirements.md`) is consumed by
> `$game-studio ux-review` and the gate files too. Same rule applies: load only the part
> covering the section you are authoring, never the whole file.

Apply `docs.density` (Section 1) to whatever that file tells you to author — it
controls the depth of each section, not which sections exist.

## 5. Cross-Reference Check

**Read `references/5-crossref-handoff.md` now and follow it** — this phase's steps are in that file, not here. Read it again if the conversation was compacted or resumed during this phase.

## 7. Recovery & Resume

If the session is interrupted (compaction, crash, new session):

1. Read `production/session-state/active.md` — it records the current screen
   and which sections are complete.
2. Read `design/ux/[filename].md` — sections with real content are done;
   sections with `[To be designed]` still need work.
3. Resume from the next incomplete section — no need to re-discuss completed ones.

This is why incremental writing matters: every approved section survives any
disruption.

---

## 8. Specialist Agent Routing

This skill uses `ux-designer` as the primary agent (set in frontmatter). For
specific sub-topics, additional context or coordination may be needed:

| Topic | Coordinate with |
|-------|----------------|
| Visual aesthetics, color, layout feel | `art-director` — UX spec defines zones; art defines how they look |
| Implementation feasibility (engine constraints) | `ui-programmer` — before finalizing component inventory |
| Gameplay data requirements | `game-designer` — when data ownership is unclear |
| Narrative/lore visible in the UI | `narrative-director` — for flavor text, item names, lore panels |
| Accessibility tier decisions | Recorded by this session (`$game-studio ux-design accessibility`; the user picks the tier) against the criteria `accessibility-specialist` defines and audits — consult it when a requirement's criterion is unclear |

When delegating to another agent via the native subagent tool, when available:
- Provide: screen name, game concept summary, the specific question needing expert input
- The agent returns analysis to this session
- This session presents the agent's output to the user
- The user decides; this session writes to file
- Agents do NOT write to files directly — this session owns all file writes

---

## Recommended Next Steps

- Run `$game-studio ux-review [filename]` to validate this spec before it enters the implementation pipeline
- Run `$game-studio ux-design [next-screen]` to continue designing remaining screens or flows
- Run `$game-studio gate-check production` once all key screens have approved UX specs
