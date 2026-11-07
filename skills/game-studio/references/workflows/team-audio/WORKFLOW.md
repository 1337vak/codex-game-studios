> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Team Audio

When this skill is invoked with an argument, orchestrate the audio team through a structured pipeline.

## Next Steps

- Review the audio design doc with the audio-director before implementation begins.
- Use `$game-studio dev-story` to implement the audio manager and event system once the design is approved.
- Run `$game-studio asset-audit` after audio assets are created to verify naming and format compliance.
- If there was no sound bible, create one before the next audio pass: ask the
  `audio-director` agent to draft `design/audio/sound-bible.md` from
  `<skill-root>/references/studio/templates/sound-bible.md`, starting from this run's Step 1
  direction (it asks before writing under `design/`).

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
