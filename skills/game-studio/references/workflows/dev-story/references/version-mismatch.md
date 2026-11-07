> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Phase 2: When the ADR or the manifest changed after the story was written

Read only when Phase 2 found a version mismatch.

## The ADR

The ADR's `version` (from `adr-status.sh`: its Last Verified date, else its Date,
else `unversioned`) differs from the story's `ADR Version`, or the ADR is
`unversioned` while the story names a date. Its decision may have changed.

Ask: "Story was written against ADR v[story date]. The ADR is now v[current].
How do you want to go on?" Options:

## The control manifest

The story's `Manifest Version` differs from the manifest's. New rules may apply.

Ask: "Story was written against manifest v[story date]. The current manifest is
v[current]. How do you want to go on?" Options:

- **Update the story's manifest version and use the current rules (Recommended).**
  Set the story's `Manifest Version` to the current date, then read the layer's
  rules for the brief.
- **Use the old rules — I accept the risk.** Set `Manifest Version` to the current
  date and add `Manifest-Note: Proceeded with old manifest rules on [date] —
  non-compliance risk accepted.` to the story header. Note it under Deviations;
  `$game-studio story-done` carries the note into its deviations.
- **Stop — I want to review the manifest first.** No agent runs.

Each option names the story edit it makes, so choosing it is the ask.
