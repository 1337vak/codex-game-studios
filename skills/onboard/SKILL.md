---
name: onboard
description: "Onboarding doc for a new contributor or agent — project state, conventions, priorities relevant to the specified role."
# Source argument-hint: "[role|area]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Bash(bash "*/<plugin-root>/skills/onboard/../../hooks/yaml-helper.sh" resolve_config *)
# Source model: haiku
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.


Source-only preprocessing (not executed): `bash "<plugin-root>/shared/source-hooks/yaml-helper.sh" resolve_config --keys automation`

**Automation mode**: Resolve `modes.automation` (`project.local.yaml` →
`project.yaml` → default `collaborative`). Every `ask the user when needed` call and
every file write follows `<plugin-root>/shared/docs/automation-modes.md`
(collaborative asks always · guided major-only · autonomous logs and proceeds;
`automation_always_ask` categories always prompt).

# Onboard

## Insufficient input — check this before producing any report

**If the inputs this skill needs do not exist, the answer is "could not run" —
not a filled-in report.** Check first, and stop if the check fails.

1. List the inputs this skill reads (data files, prior reports, profiler output,
   test results, registries, source code).
2. For each, record `FOUND` or `ABSENT` — not "assumed present".
3. If any input required for a section is ABSENT, that section is
   **`NOT ASSESSED — NO DATA`**. Do not estimate it, do not infer it from an
   adjacent artifact, and do not leave a mandated cell to be filled by whoever
   reads the template next.
4. If **every** required input is ABSENT, stop and report
   **`NOT ASSESSED — NO DATA`** as the whole verdict, naming what was missing and
   which skill produces it.

**A verdict of `NOT ASSESSED` is a success.** It is the correct, useful answer to
"what does the data say?" when there is no data. The failure mode this prevents is
specific: a report whose verdict enum has no "could not run" state produces
**false clean passes** — an asset audit returning COMPLIANT on a project with no
assets and no standards, or a performance profile reporting ">99% headroom against
a 16.67ms budget" with zero profiler data and no budget ever set.

**Absence of evidence is never evidence of absence.** A scan that finds no
matches because there are no files to scan has not verified anything. Say which of
the two happened — a reader cannot tell from a green result.

---

## Phase 1: Load Project Context

Read CLAUDE.md for project overview and standards.

Read the relevant agent definition from `<plugin-root>/skills/game-studio/references/roles/` if a specific role is specified.

`CLAUDE.md` and `<plugin-root>/skills/game-studio/references/roles/` ship with the framework — no skill creates them. If either is missing, report it as missing from the install.

---

## Phase 2: Scan Relevant Area

- For programmers: scan the code root (resolve per `<plugin-root>/shared/docs/code-root-resolution.md`) for architecture, patterns, key files. An unresolved root means the scan did not run: the sections it feeds read `NOT ASSESSED — code root unresolved`, never a guess at `src/`
- For designers: scan `design/` for existing design documents
- For narrative: scan `design/narrative/` for world-building and story docs
- For QA: scan `tests/` for existing test coverage (`the test-setup skill` creates it)
- For production: scan `production/` for current sprint and milestone
- **No role or area given**: a general orientation — list the top level of `design/`,
  `docs/architecture/`, `production/` and the code root, read
  `production/session-state/active.md` if it exists, and say that a role would
  focus the next pass (e.g. `the onboard skill programmer`)

Read recent changes (git log if available) to understand current momentum.

---

## Phase 3: Generate Onboarding Document

```markdown
# Onboarding: [Role/Area]

## Project Summary
[2-3 sentence summary of what this game is and its current state]

## Your Role
[What this role does on this project, key responsibilities, who you report to]

## Project Architecture
[Relevant architectural overview for this role]

### Key Directories
| Directory | Contents | Your Interaction |
|-----------|----------|-----------------|

### Key Files
| File | Purpose | Read Priority |
|------|---------|--------------|

## Current Standards and Conventions
[Summary of conventions relevant to this role from CLAUDE.md and agent definition]

## Current State of Your Area
[What has been built, what is in progress, what is planned next. Name what
Phase 2 found by path — for a designer, each existing GDD and design doc — or
say it found none]

## Current Sprint Context
[What the team is working on now and what is expected of this role]

## Key Dependencies
[What other roles/systems this role interacts with most]

## Common Pitfalls
[Things that trip up new contributors in this area]

## First Tasks
[Suggested first tasks to get oriented and productive]

1. [Read these documents first]
2. [Review this code/content]
3. [Start with this small task]

## Questions to Ask
[Questions the new contributor should ask to get fully oriented]
```

---

## Phase 4: Save Document

Present the onboarding document to the user.

Ask: "May I write this to `production/onboarding/onboard-[role]-[date].md`?"

If yes, write the file, creating the directory if needed.

---

## Phase 5: Next Steps

Verdict: **COMPLETE** — onboarding document generated.

- Share the onboarding doc with the new contributor before their first session.
- Run `the sprint-status skill` to show the new contributor current progress.
- Run `the help skill` if the contributor needs guidance on what to work on next.
