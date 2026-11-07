> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

Resolved above; use as-is. No block → the defaults in `<skill-root>/references/studio/config-resolution.md`
(`workflow: minimal`, `review_mode: solo`, `automation: collaborative`, `docs.density: terse`), and
say that the settings were not read.

# Brainstorm

Turns no idea, or a rough one, into a written design the next step builds from. How much it writes
depends on `workflow`:

- **`minimal`:** the Lean Brief flow below: a one-page `design/game-brief.md`, then stop. No
  discovery questions, pillars, director gates or `game-concept.md`, and do not load
  `references/full-concept.md`.
- **`standard` or `full`:** read `references/full-concept.md` and follow it. It writes
  `design/gdd/game-concept.md` from `<skill-root>/references/studio/templates/game-concept.md`. Its gates follow
  `<skill-root>/references/studio/director-gates.md`; each director agent is given its own gate file,
  `<skill-root>/references/studio/director-gates/<gate-id in lower case>.md` (`cd-pillars.md`,
  `ad-concept-visual.md`, `td-feasibility.md`, `pr-scope.md`), and you do not read those files
  yourself.

`--review` in the text typed after the skill name overrides `review_mode` for this run.
`docs.density` sets each section's depth: `terse` = bullets; `balanced` = with brief rationale;
`thorough` = rationale and alternatives. Questions follow `<skill-root>/references/studio/automation-modes.md`
(collaborative asks, guided asks only for major decisions, autonomous logs and proceeds; the
always-ask categories always ask).

Ask with the question tool. Without one, list the options numbered and end your turn to wait. The
question is the last thing in the reply: no advice or lean after it. A skipped or dismissed
question is not an answer: ask again in plain text.

## Lean Brief flow (`workflow: minimal`)

A few exchanges, not fifteen: capture the thinking that carries the game on one page, then get to
code. Write from the template `<skill-root>/references/studio/templates/game-brief.md` (six required fields, three
one-liners). If `design/game-brief.md` exists, read it and refine it instead of starting over.

   Then one summary line: the pitch, the number of MVP items, and `design/game-brief.md`. End with
   the line `Verdict: COMPLETE — game brief written; next stop is code.`

If the user stops before the write, say the brief was not written, so it lives only in this
conversation.
