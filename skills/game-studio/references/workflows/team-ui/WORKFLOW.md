> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Team UI

When this skill is invoked, orchestrate the UI team through a structured pipeline.

## Team Composition
- **ux-designer** — User flows, wireframes, accessibility, input handling
- **ui-programmer** — UI framework, screens, widgets, data binding, implementation
- **art-director** — Visual style, layout polish, consistency with art bible
- **engine UI specialist** — Validates UI implementation patterns against engine-specific best practices (`specialists.ui` from `project.yaml`; if absent, the UI Specialist line of `## Engine Specialists` in `<skill-root>/references/studio/technical-preferences.md`)
- **accessibility-specialist** — Audits accessibility compliance at Phase 4

> **`specialists.ui: null` means UNSET.** Treat it as absent and skip the engine
> UI specialist; never spawn `null` as an agent name. The v1.0 migration writes
> the whole `specialists` block whenever any one member is set, so `null` here is
> ordinary — and the config reader returns it as the non-empty string `"null"`.

**Templates used by this pipeline:**
- `ux-spec.md` — Standard screen/flow UX specification
- `hud-design.md` — HUD-specific UX specification
- `interaction-pattern-library.md` — Reusable interaction patterns
- `accessibility-requirements.md` — Committed accessibility tier and requirements

## Pipeline

### Phase 1a: Context Gathering

Before designing anything, read and synthesize. Read each GDD by section: find the
headings you need with the Grep tool (pattern `^#`, content mode) and Read those
ranges with offset and limit.
- `design/gdd/game-concept.md` — platform targets and intended audience (or
  `design/game-brief.md`, the one-page brief that replaces it at `rigor: minimal` —
  its "Who it's for" line gives the audience; it names no platform)
- `design/player-journey.md` — player's state and context when they reach this screen
- All GDD UI Requirements sections relevant to this feature
- `design/ux/interaction-patterns.md` — existing patterns to reuse (not reinvent)
- `design/accessibility-requirements.md` — committed accessibility tier (Basic, Standard, Comprehensive or Exemplary)

**Report the status of every document above before designing anything.** Phase 1a
reads five inputs, and any of them can be absent. List each as
present or ABSENT.

**`design/accessibility-requirements.md` is the one that must not pass silently.**
It carries the committed accessibility tier, which **Phase 3 implements against**
and **Phase 4 gates on** ("verify compliance against the committed accessibility
tier … flag any violations as blockers"). If the file is missing there is no tier,
so that gate has no criterion and would pass while checking nothing — a gate made
of an absent standard, the same shape as an assertion that can never fail. When it
is absent:
- Say so here, and carry it forward: **Phase 4 must report
  `Accessibility: NOT ASSESSED — no committed tier (design/accessibility-requirements.md absent)`
  and must NOT report the accessibility gate as passed.**
- The ux-designer states which tier they designed against as an explicit
  assumption, so a later reader can see it was assumed rather than committed.
- Recommend `$game-studio ux-design accessibility` to establish the tier.

Absence of a concept doc (neither `design/gdd/game-concept.md` nor
`design/game-brief.md`), `design/player-journey.md` or `design/ux/hud.md` is not
blocking, but name each missing one in the brief you
pass to the ux-designer so they design knowing what context they lack, rather
than inferring it.

**If `design/ux/interaction-patterns.md` does not exist**, surface the gap immediately:
> "interaction-patterns.md does not exist — no existing patterns to reuse."

Do NOT invent or assume patterns from the feature name or GDD alone. If the user chooses (b), explicitly instruct ui-programmer in Phase 3 to treat all patterns as new and document them in `design/ux/interaction-patterns.md` when implementation is complete. Note the pattern library status (created / absent / updated) in the final summary report.

Summarize the context in a brief for the ux-designer: what the player is doing, what they need, what constraints apply, and which existing patterns are relevant.

### Phase 1b: UX Spec Authoring

Invoke `$game-studio ux-design [feature name]` skill OR delegate directly to ux-designer to produce `design/ux/[feature-name].md` following the `ux-spec.md` template.

If designing the HUD, use the `hud-design.md` template instead of `ux-spec.md`.

> **Notes on special cases:**
> - For HUD design specifically, invoke `$game-studio ux-design` with `argument: hud` (e.g., `$game-studio ux-design hud`).
> - For the interaction pattern library, run `$game-studio ux-design patterns` once at project start and update it whenever new patterns are introduced during later phases.

Output: `design/ux/[feature-name].md` with all required spec sections filled.

### Phase 1c: UX Review

After the spec is complete, invoke `$game-studio ux-review design/ux/[feature-name].md`.

A **NOT ASSESSED** verdict blocks the same way, and the user may override it the same way. Its fix is an input, not a revision: present the dimensions `$game-studio ux-review` could not assess and the missing input for each (e.g. `$game-studio ux-design accessibility` for an uncommitted tier). Re-running the review without that input returns the same verdict, so offer to produce the input first.

When the user proceeds past NEEDS REVISION or NOT ASSESSED, the final report records the override: the verdict, the concerns or unassessed dimensions left open, and that the user chose to proceed.

### Phase 2: Visual Design

Delegate to **art-director**:
- Review the full UX spec (flows, wireframes, interaction patterns, accessibility notes) — not just the wireframe images
- Apply visual treatment from the art bible: colors, typography, spacing, animation style
- Check that visual design preserves accessibility compliance: verify color contrast ratios, and confirm color is never the only indicator of state (shape, text, or icon must reinforce it)
- Specify all asset requirements needed from the art pipeline: icons at specified sizes, background textures, fonts, decorative elements — with precise dimensions and format requirements
- Ensure consistency with existing implemented UI screens
- Output: visual design spec with style notes and asset manifest

### Phase 3: Implementation

Before implementation begins, spawn the **engine UI specialist** (`specialists.ui` from `project.yaml`; if absent, the UI Specialist line of `## Engine Specialists` in `<skill-root>/references/studio/technical-preferences.md`) to review the UX spec and visual design spec for engine-specific implementation guidance:
- Which engine UI framework should be used for this screen? (e.g., UI Toolkit vs UGUI in Unity, Control nodes vs CanvasLayer in Godot, UMG vs CommonUI in Unreal)
- Any engine-specific gotchas for the proposed layout or interaction patterns?
- Recommended widget/node structure for the engine?
- Output: engine UI implementation notes to hand off to ui-programmer before they begin

If no engine is configured, skip this step. **Record ``Engine validation: NOT ASSESSED — no engine configured (`engine.name` unset in `project.yaml`)`` in this run's output.** A skipped check that says nothing is indistinguishable from a check that passed; the reader cannot tell engine guidance was never sought.

Delegate to **ui-programmer**:
- Implement the UI following the UX spec and visual design spec
- **Use patterns from `design/ux/interaction-patterns.md`** — do not reinvent patterns that are already specified. If a pattern almost fits but needs modification, note the deviation and flag it for ux-designer review.
- **UI NEVER owns or modifies game state** — display only; emit events for all player actions
- All text through the localization system — no hardcoded player-facing strings
- Support both input methods (keyboard/mouse AND gamepad)
- Implement accessibility features per the committed tier in `design/accessibility-requirements.md`
- Wire up data binding to game state
- **If any new interaction pattern is created during implementation** (i.e., something not already in the pattern library), add it to `design/ux/interaction-patterns.md` before marking implementation complete
- Output: implemented UI feature

### Phase 4: Review (parallel)

Delegate in parallel:
- **ux-designer**: Verify implementation matches wireframes and interaction spec. Test keyboard-only and gamepad-only navigation. Check accessibility features function correctly.
- **art-director**: Verify visual consistency with art bible. Check at minimum and maximum supported resolutions.
- **accessibility-specialist**: Verify compliance against the committed accessibility tier documented in `design/accessibility-requirements.md`. Flag any violations as blockers. **If that file is absent there is no committed tier, so this gate has no criterion: report `Accessibility: NOT ASSESSED — no committed tier (design/accessibility-requirements.md absent)` and do NOT report the gate as passed**. Carry forward whatever tier Phase 1a recorded as assumed, and say plainly that it was assumed.

All three review streams must report before proceeding to Phase 5.

### Phase 5: Polish

- Address all review feedback
- Verify animations are skippable and respect the player's motion reduction preferences
- Confirm UI sounds trigger through the audio event system (no direct audio calls)
- Test at all supported resolutions and aspect ratios
- **Verify `design/ux/interaction-patterns.md` is up to date** — if any new patterns were introduced during this feature's implementation, confirm they have been added to the library
- **Confirm all HUD elements respect the visual budget** defined in `design/ux/hud.md` (element count, screen region allocations, maximum opacity values)

## Quick Reference — When to Use Which Skill

- `$game-studio ux-design` — Author a new UX spec for a screen, flow, or HUD from scratch
- `$game-studio ux-review` — Validate a completed UX spec before implementation
- `$game-studio team-ui [feature]` — Full pipeline from concept through polish (calls `$game-studio ux-design` and `$game-studio ux-review` internally)
- `$game-studio quick-design` — Small UI changes that don't need a full new UX spec

## Error Recovery Protocol

**First, verify the artifact.** If the return contract named a path, check the
path exists before treating the phase as done — **a named artifact that is not
on disk is a failed phase, however fluent the response reads.** An agent can
burn a full phase and return a plausible preamble having written nothing, which
is neither BLOCKED nor an error nor "cannot complete", so the trigger below
never fires. Resume it naming the unmet contract; the context is
usually still there.

If any spawned agent returns BLOCKED, errors, or cannot complete: **surface it
immediately, don't proceed past a dependency it blocks, and always produce a
partial report.** A skipped agent's section stays a named gap — never fill it with content of your own. Full procedure: `<skill-root>/references/studio/error-recovery-protocol.md`.

Common blockers:
- Input file missing (story not found, GDD absent) → redirect to the skill that creates it
- ADR status is Proposed → do not implement; once it is decided, accept it with `$game-studio architecture-decision accept ADR-NNNN`
- Scope too large → split into two stories via `$game-studio create-stories`
- Conflicting instructions between ADR and story → surface the conflict, do not guess

## Output

A summary report covering: UX spec status, UX review verdict, visual design status, implementation status, accessibility compliance, input method support, interaction pattern library update status, and any outstanding issues.

Verdict: **COMPLETE** — UI feature delivered through full pipeline (UX spec → visual → implementation → review → polish).

If the accessibility gate (no committed tier) or the engine validation (no engine
configured) was NOT ASSESSED, the verdict names each one — never a plain COMPLETE:

Verdict: **COMPLETE — [accessibility | engine validation] NOT ASSESSED ([reason])** — UI feature delivered; the named check could not run.

Verdict: **BLOCKED** — pipeline halted; surface the blocker and its phase before stopping.

## Next Steps

- Run `$game-studio ux-review` on the final spec if not yet approved.
- Run `$game-studio code-review` on the UI implementation before closing stories.
- Run `$game-studio team-polish` if visual or audio polish pass is needed.
