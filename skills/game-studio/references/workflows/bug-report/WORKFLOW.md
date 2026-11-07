> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Bug Report

**Drafts only.** This skill writes reports to `production/qa/bugs/`. When the
cause is in the engine, a plugin or another vendor's code, add a draft for their
tracker under **Notes** and stop there: never file, open or comment on an issue
or pull request in their repository. The user submits it.

## Phase 1: Parse Arguments

Determine the mode from the argument:

- No keyword → **Description Mode**: generate a structured bug report from the provided description
- `analyze [path]` → **Analyze Mode**: read the target file(s) and identify potential bugs
- `verify [BUG-ID]` → **Verify Mode**: confirm a reported fix actually resolved the bug
- `close [BUG-ID]` → **Close Mode**: mark a verified bug as closed with resolution record

If no argument is provided, ask the user for a bug description before proceeding.

---

## Phase 2A: Description Mode

1. **Parse the description** for key information: what broke, when, how to reproduce it, and what the expected behavior is.

2. **Search the codebase** for related files using Grep/Glob to add context (affected system, likely files).

3. **Draft the bug report**:

```markdown
# Bug Report

## Summary
**Title**: [Concise, descriptive title]
**ID**: BUG-[NNNN]
**Severity**: [S1-Critical / S2-High / S3-Medium / S4-Low]
**Priority**: [P1-Fix this sprint / P2-Fix soon / P3-Backlog / P4-Won't fix]
**Status**: Open
**Reported**: [Date]
**Reporter**: [the reporter's name as the user gives it, else `—`; never an email address or account ID taken from the session]

## Classification
- **Category**: [Gameplay / UI / Audio / Visual / Performance / Crash / Network]
- **System**: [Which game system is affected — when the bug spans systems, the one whose code must change; the others go under Related systems]
- **Frequency**: [Always / Often (>50%) / Sometimes (10-50%) / Rare (<10%)]
- **Regression**: [Yes/No/Unknown -- was this working before?]

## Environment
- **Build**: [Version or commit hash]
- **Platform**: [OS, hardware if relevant]
- **Scene/Level**: [Where in the game]
- **Game State**: [Relevant state -- inventory, quest progress, etc.]

## Reproduction Steps
**Preconditions**: [Required state before starting]

1. [Exact step 1]
2. [Exact step 2]
3. [Exact step 3]

**Expected Result**: [What should happen]
**Actual Result**: [What actually happens]

## Technical Context
- **Likely affected files**: [List of files based on codebase search]
- **Related systems**: [What other systems might be involved]
- **Possible root cause**: [If identifiable from the description]

## Evidence
- **Logs**: [Relevant log output if available]
- **Visual**: [Description of visual evidence]

## Related Issues
- [Links to related bugs or design documents]

## Notes
[Any additional context or observations]
```

The **Severity** and **Priority** labels use `$game-studio bug-triage`'s S and P numbers and
names, which it parses out of this file. `P4-Won't fix` is its `P4 — Won't fix /
Deferred` (an accepted risk), not a wishlist. If you change either ladder, change
`<skill-root>/references/workflows/bug-triage/WORKFLOW.md` too.

---

## Phase 2B: Analyze Mode

1. **Read the target file(s)** specified in the argument.

2. **Identify potential bugs**: null references, off-by-one errors, race conditions, unhandled edge cases, resource leaks, incorrect state transitions.

3. **For each potential bug**, generate a bug report using the template above, with the likely trigger scenario and recommended fix filled in.

---

## Phase 2C: Verify Mode

**Find the bug file by its number**, here and in close mode: Glob
`production/qa/bugs/BUG-*.md` and take the file whose number matches `[BUG-ID]`,
whatever its zero-padding — an older three-digit file with a slug is found by
its number too. If none
matches, stop: "No bug [BUG-ID] in `production/qa/bugs/`." Verdict: **BLOCKED**
— no such bug.

Read that file. Extract the reproduction steps and expected result.

Produce a verification verdict:

- **VERIFIED FIXED** — the bug is gone by every check that applies: any related test ran and passed, and, where step 4 asked, the user answered `[No longer occurs]` for a named build. With no test run, that play alone is the verification — a manual one, recorded as such: `[user], manual, build [X]`. A changed code path on its own is never a pass
- **STILL PRESENT** — a related test fails on the bug's case, or the user answered `[Still occurs]`; the fix did not resolve the issue
- **CANNOT VERIFY** — step 4 was answered `[Not played yet]`: name what is missing or could not run (no related test, `commands.test` unset, a run that did not complete, a Visual or UI bug), and say that playing the reproduction steps settles it — run `$game-studio bug-report verify [BUG-ID]` again once played

If STILL PRESENT: reopen the bug, set Status back to Open, and suggest re-running `$game-studio hotfix [BUG-ID]`.

---

## Phase 2D: Close Mode

Read the bug file, found by its number as in verify mode. Confirm Status is `Verified Fixed` before closing. If status is anything else, stop: "Bug [ID] must be Verified Fixed before it can be closed. Run `$game-studio bug-report verify [BUG-ID]` first."

On yes, append the closure record to the bug file:

```markdown
## Closure Record
**Closed**: [date]
**Resolution**: Fixed — [one-line description of what was changed]
**Fix commit / PR**: [if known]
**Verified by**: [the verify record's `**Verified by**:` line — the test that ran and passed, or "[user], manual, build [X]"]
**Closed by**: [user]
**Regression test**: [test file path, or "Manual verification" when verify recorded a manual play]
**Status**: Closed
```

Then update the top-level `**Status**:` field to `**Status**: Closed`.

After closing, check `production/qa/bug-triage-*.md` — if the bug appears in an open triage report, note: "Bug [ID] is referenced in the triage report. Run `$game-studio bug-triage` to refresh the open bug count."

---

## Phase 3: Save Report

Present the completed bug report(s) to the user.

**Allocate the ID** before asking: Glob `production/qa/bugs/BUG-*.md`, take the
highest number and add 1, zero-padded to four digits (`BUG-0001` when there are
none). Several reports in one run (analyze mode) take consecutive IDs from
there, one each — never the same ID twice.

If yes, write the file, creating the directory if needed. Verdict: **COMPLETE** — bug report filed.

If no, stop here. Verdict: **BLOCKED** — user declined write.

---

## Phase 4: Next Steps

After saving, suggest based on mode:

**After filing (Description/Analyze mode):**
- Run `$game-studio bug-triage` to prioritize alongside existing open bugs
- If S1 or S2: run `$game-studio hotfix [BUG-ID]` for emergency fix workflow

**After fixing the bug (developer confirms fix is in):**
- Run `$game-studio bug-report verify [BUG-ID]` — confirm the fix actually works before closing
- Never mark a bug closed without verification — a fix that doesn't verify is still Open

**After verify returns CANNOT VERIFY:**
- Play the reproduction steps on a build with the fix, then run `$game-studio bug-report verify [BUG-ID]` again and answer its question

**After verify returns VERIFIED FIXED:**
- Run `$game-studio bug-report close [BUG-ID]` — write the closure record and update status
- Run `$game-studio bug-triage` to refresh the open bug count and remove it from the active list
