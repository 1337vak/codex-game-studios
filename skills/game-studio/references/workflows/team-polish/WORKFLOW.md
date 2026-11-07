> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Team Polish

When this skill is invoked with an argument, orchestrate the polish team through a structured pipeline.

## Team Composition
- **performance-analyst** — Profiling, memory analysis, frame budget, and the optimisation list — it writes no game code
- **engine-programmer** — Implements the optimisation list's engine-level items: rendering pipeline, memory, resource loading, hot paths (invoke when performance-analyst identifies low-level root causes)
- **technical-artist** — VFX polish, shader optimization, visual quality
- **sound-designer** — Audio polish, mixing, ambient layers, feedback sounds
- **tools-programmer** — Content pipeline tool verification, editor tool stability, automation fixes (Phase 2, when Phase 1 traces a cause to a content authoring tool)
- **qa-tester** — Edge case testing, regression testing, soak testing

## Pipeline

### Phase 1: Assessment
Delegate to **performance-analyst**:
- Profile the target feature/area using `$game-studio perf-profile`
- Identify performance bottlenecks and frame budget violations
- Measure memory usage and check for leaks
- Benchmark against target hardware specs
- Output: performance report with the prioritized **optimisation list** — for each item, the change, its expected gain against the budget, and its owner (technical-artist for rendering-side changes, engine-programmer for engine systems and hot paths, tools-programmer for a content authoring tool, otherwise the programmer who owns the system)

### Phase 2: Optimization
performance-analyst writes no game code ("recommend and assign", its agent file),
so Phase 2 implements its Phase 1 list through the owners in the active set:
- **engine-programmer** — spawned only when Phase 1 identified engine-level root causes (rendering pipeline, resource loading, memory allocator, hot paths in core loops): implement those items, fix allocation pressure, verify gameplay behavior is unchanged. Output: engine-level fixes with before/after metrics and profiler validation
- **tools-programmer** — only when Phase 1 traced a cause to a content authoring tool: fix the tool. Output: tool fixes with before/after metrics
- **technical-artist** — rendering-side items (draw calls, overdraw, particles, shaders, LOD) join its Phase 3 brief

**An item whose owner is not in the active set is not implemented in this run.**
At `team.size: individual` that is every programmer item, since no programmer is
active; at any size it includes an item owned by a programmer this pipeline does
not name (e.g. gameplay-programmer for a gameplay-script hot spot). The report
lists those items with their owners under
"Optimisation list handed to `$game-studio dev-story`: `production/polish/[area]-report-[date].md`".
A metric they target that is over budget stays a known problem at Phase 6.

### Phase 3: Visual Polish (parallel with Phase 2)
Delegate to **technical-artist**:
- Review VFX for quality and consistency with art bible
- Optimize particle systems and shader effects
- Add screen shake, camera effects, and visual juice where appropriate
- Ensure effects degrade gracefully on lower settings
- Output: polished visual effects

### Phase 4: Audio Polish (parallel with Phase 2)
Delegate to **sound-designer**:
- Review audio events for completeness (are any actions missing sound feedback?)
- Check audio mix levels — nothing too loud or too quiet relative to the mix
- Add ambient audio layers for atmosphere
- Verify audio plays correctly with spatial positioning
- Output: audio polish list and mixing notes

### Phase 5: Hardening
Delegate to **qa-tester**:
- Test all edge cases: boundary conditions, rapid inputs, unusual sequences
- Soak test: run the feature for extended periods checking for degradation
- Stress test: maximum entities, worst-case scenarios
- Regression test: verify polish changes haven't broken existing functionality — each Phase 2–4 change by name, engine-level fixes included
- Test on minimum spec hardware (if available)
- Output: test results with any remaining issues

### Phase 6: Sign-off
- Collect results from all team members
- Compare performance metrics against budgets
- Report: READY FOR RELEASE / NOT ASSESSED / NEEDS MORE WORK
- List every remaining issue with its severity (S1–S4), the measured gap where there is one (e.g. "9 ms against a 6 ms budget — 3 ms over"), and a recommendation; a regression also names the broken behavior and the polish change that caused it

**NOT ASSESSED ranks above READY FOR RELEASE and below NEEDS MORE WORK.** A known
problem — a metric over budget, an unresolved regression — makes it NEEDS MORE
WORK whatever else went unchecked. Otherwise, if any part of the scope could not
be checked, the result is NOT ASSESSED, never READY FOR RELEASE, and the report
names each gap:
- A metric with no committed budget. `performance.target_framerate`,
  `performance.frame_budget_ms`, `performance.draw_call_limit` and
  `performance.memory_ceiling_mb` have no default, and `$game-studio perf-profile` reports an
  unset one as NOT ASSESSED — nothing was compared, so no budget was met.
- A phase that did not run: BLOCKED, skipped, or its agent outside the active set.
  At `team.size: individual`, sound-designer's audio polish and qa-tester's
  hardening are only consulted through the active agents, not run, and Phase 2's
  programmer items are handed to `$game-studio dev-story` rather than implemented.

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

A summary report covering: performance before/after metrics, visual polish changes, audio polish changes, test results, any optimisation list handed to `$game-studio dev-story`, and release readiness assessment.

## Next Steps

- If READY FOR RELEASE: run `$game-studio release-checklist` for the final pre-release validation.
- If NEEDS MORE WORK: schedule remaining issues in `$game-studio sprint-plan update` (at `workflow: minimal`, which has no sprints, add them to the brief's build order) and re-run `$game-studio team-polish` after fixes.
- If NOT ASSESSED: supply what was missing — commit the unset `performance.*` budgets in `project.yaml` (`$game-studio settings`), or run the phases that did not run (raise `team.size`) — then re-run `$game-studio team-polish`. Do not treat the area as release-ready.
- If the report handed an optimisation list to `$game-studio dev-story`: implement those items there, then re-run `$game-studio team-polish` to measure the gain.
- Run `$game-studio gate-check` for a formal phase gate verdict before handing off to release.
