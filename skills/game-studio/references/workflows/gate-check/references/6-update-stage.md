> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio gate-check — Section 6: Update Stage on PASS

> Part of `$game-studio gate-check`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## 6. Update Stage on PASS

When the verdict is **PASS** and the user confirms they want to advance, write the
new stage to BOTH `project.yaml` and the legacy `production/stage.txt`.

### 6.1 Write the stage

After the yes, write both stage files with one command (quote a two-word stage):

It sets `project.stage` in `project.yaml`: it edits the `stage:` line, adds a
`project:` block after `framework:` when there is none, or creates the file from
the minimal template when there is no `project.yaml`. It keeps comments, other
keys and line endings. It also writes the legacy `production/stage.txt`, so hooks
that have not migrated still work, then reads both files back. It never seeds
`modes.review_mode`: `modes.rigor` supplies that, and an explicit value would pin
the review mode whatever the project's rigor.

### 6.2 Verify both writes

Show its `stage_yaml` and `stage_txt` rows. Exit 0 means both files hold the new
stage. Exit 4 means they disagree after writing: report the discrepancy to the
user and stop, because a split stage indicator corrupts future auto-detection.
Exit 5 means `project.yaml` has a layout the script will not edit (`project:` as
a one-line value): nothing was written, so say so and edit `project.yaml` with
the user's yes. Any other non-zero exit: report the message and stop.

### 6.3 Rigor-fit check (advisory — never affects the verdict)

After the stage advance is confirmed, apply the raise trigger in
`<skill-root>/references/studio/settings-guidance.md § 4`: if the new stage is **Production** (or
later) while the resolved `modes.workflow` is `minimal` (the `rigor: minimal`
posture, from the config block above), add one line:

> "You're entering [stage] on `rigor: minimal` — most projects this size run
> `standard`. Revisit with `$game-studio settings modes.rigor=standard`?"

Offer it **once**, here at the gate. Route to `$game-studio settings` — never change the
setting yourself.

---
