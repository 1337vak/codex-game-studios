> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Team Combat

**Argument check:** If no combat feature description is provided, output:
> "Usage: `$game-studio team-combat [combat feature description] [--review full|lean|solo]` — Provide a description of the combat feature to design and implement (e.g., `melee parry system`, `ranged weapon spread`)."
Then stop immediately without spawning any subagents or reading any files.

When this skill is invoked with a valid argument, orchestrate the combat team through a structured pipeline.

## Team Composition
- **game-designer** — Design the mechanic, define formulas and edge cases
- **gameplay-programmer** — Implement the core gameplay code
- **ai-programmer** — Implement NPC/enemy AI behavior for the feature
- **technical-artist** — Create VFX, shader effects, and visual feedback
- **sound-designer** — Define audio events, impact sounds, and ambient combat audio
- **engine specialist** (primary) — Validate architecture and implementation patterns are idiomatic for the engine (the primary specialist is `<engine>-specialist` from `engine.name` — Godot→`godot-specialist`, Unity→`unity-specialist`, Unreal→`unreal-specialist`; fall back to the Primary line of `## Engine Specialists` in `technical-preferences.md`)
- **qa-tester** — Write test cases and validate the implementation

## Pipeline

### Phase 1: Design
Delegate to **game-designer**:
- Create or update the design document for `design/gdd/[feature].md` from `<skill-root>/references/studio/templates/game-design-document.md`, with `## Summary` and the sections `workflow` requires (Phase 0) — at `full`: mechanic overview, player fantasy, detailed rules, formulas with variable definitions, edge cases, dependencies, tuning knobs with safe ranges, and acceptance criteria
- Output: completed design document, drafted to `production/combat/[feature]-gdd-draft.md`

### Phase 2: Architecture
Delegate to **gameplay-programmer** (with **ai-programmer** if AI is involved):
- Review the design document, reading it by section: find the headings you need with the Grep tool (pattern `^#`, content mode) and Read those ranges with offset and limit
- Design the code architecture: class structure, interfaces, data flow
- Identify integration points with existing systems
- Output: architecture sketch with file list and interface definitions

Then spawn the **primary engine specialist** to validate the proposed architecture:
- Is the class/node/component structure idiomatic for the pinned engine? (e.g., Godot node hierarchy, Unity MonoBehaviour vs DOTS, Unreal Actor/Component design)
- Are there engine-native systems that should be used instead of custom implementations?
- Any proposed APIs that are deprecated or changed in the pinned engine version?
- Output: engine architecture notes — incorporate into the architecture before Phase 3 begins

If no engine is configured, skip the specialist spawn. **Record ``Engine validation: NOT ASSESSED — no engine configured (`engine.name` unset in `project.yaml`)`` in this run's output.** A skipped check that says nothing is indistinguishable from a check that passed.

Only spawn implementation agents if user selects [A]. (In `guided`/`autonomous`
mode this architecture gate is a normal phase transition — proceed to
implementation unless the architecture sketch came back BLOCKED, recording the
decision via `log_decision` in autonomous mode. The gate is not a release-
critical or irreversible decision, so it follows the standard pipeline rule.)

### Phase 3: Implementation (parallel where possible)
Delegate in parallel:
- **gameplay-programmer**: Implement core combat mechanic code
- **ai-programmer**: Implement AI behaviors (if the feature involves NPC reactions)
- **technical-artist**: Create VFX and shader effects
- **sound-designer**: Define audio event list and mixing notes, drafted to `production/combat/[feature]-audio-events.md`

### Phase 4: Integration
- Wire together gameplay code, AI, VFX, and audio
- Ensure all tuning knobs are exposed and data-driven
- Verify the feature works with existing combat systems

### Phase 5: Validation
Delegate to **qa-tester**:
- Write test cases from the acceptance criteria
- Test all edge cases documented in the design
- Verify performance impact is within budget
- File bug reports for any issues found

### Phase 6: Sign-off
- Collect results from all team members
- Report feature status: COMPLETE / NEEDS WORK / BLOCKED
- List any outstanding issues and their assigned owners

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

A summary report covering: design completion status, implementation status per team member, test results, and any open issues.

Verdict: **COMPLETE** — combat feature designed, implemented, and validated.

If the engine validation was skipped (Phase 2, no engine configured), the verdict
says so — never a plain COMPLETE:

Verdict: **COMPLETE — engine validation NOT ASSESSED ([reason])** — combat feature designed, implemented, and validated; the engine specialist never reviewed the architecture.

Verdict: **NEEDS WORK** — every phase ran, but Phase 5 validation left failures or open bugs unresolved; the report lists each with its owner.

Verdict: **BLOCKED** — one or more phases could not complete, or an agent was skipped (`<skill-root>/references/studio/error-recovery-protocol.md` step 5); partial report produced with unresolved items listed.

## Next Steps

- Run `$game-studio code-review` on the implemented combat code before closing stories.
- Run `$game-studio balance-check` to validate combat formulas and tuning values.
- Run `$game-studio team-polish` if VFX, audio, or performance polish is needed.
