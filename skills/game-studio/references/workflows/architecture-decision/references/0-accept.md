> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio architecture-decision — Acceptance Mode

> Part of `$game-studio architecture-decision`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

**If the argument starts with `accept` followed by an ADR id**

(e.g., `$game-studio architecture-decision accept ADR-0005`):

Enter **acceptance mode**. This is the *only* path in the framework that moves an
ADR from `Proposed` to `Accepted`. Authoring always produces `Proposed`
(Step 5), while
`$game-studio create-control-manifest`, `$game-studio create-epics`, `$game-studio create-stories` and `$game-studio gate-check`
all require `Accepted` — so without this mode an ADR would enter a state it
never leaves.

1. **Resolve the id to a file, then read it.** Glob
   `docs/architecture/adr-NNNN-*.md` for the given number. If **no** file matches,
   or **more than one** does, stop and say which — do not pick one. If the file
   has no `## Status` section, stop and say so; a missing Status is exactly what
   retrofit mode is for.
2. **Check the current status.** If it is already `Accepted`, say so and stop.
   If it is `Deprecated` or `Superseded`, refuse: reviving a superseded decision
   is a new ADR, not a status edit.
3. **Check its dependencies first.** Read `## ADR Dependencies`.

   **If that section is absent, empty, or reads `UNKNOWN`, do not read it as
   "no dependencies" — refuse and say which:**
   > "ADR-0005's dependency section is [absent / UNKNOWN], so I cannot tell what
   > this decision rests on. An empty dependency list and an unexamined one look
   > identical here, and only one of them is safe to accept. Run
   > `$game-studio architecture-decision retrofit <path>` to establish it."

   A dependency check reading a field that defaults to empty is the vacuous-pass
   shape this gate exists to prevent — the check would examine nothing and report
   clean.

   Feed the count into step 4's prompt so it reads *"3 stories become Ready"*
   rather than a generic claim: **the user is being asked to authorise an effect, and should be
   shown the effect.** If none match, say "no stories are waiting on this" — that
   is useful information, not an empty result to omit.
6. On confirmation, patch editing the `## Status` line to `Accepted`. Leave an existing
   `## Date` as it is: it records when the ADR was written, and `$game-studio create-stories`
   stamps stories with it (or `## Last Verified`), so rewriting it on acceptance
   would make every story drafted against the Proposed ADR look out of date to
   `$game-studio dev-story`. **If that section is absent, add it** with today's date — retrofit
   mode already owns this shape, and acceptance must not fail on a template that
   predates the field.
7. Then set each story found in step 5 from `Blocked` to `Ready`. Unblocking is a
   consequence of acceptance, never of authoring — see Step 6's note below.
8. Report what moved: the ADR (and its `## Date`, if one was added), and every
   story that became Ready.
