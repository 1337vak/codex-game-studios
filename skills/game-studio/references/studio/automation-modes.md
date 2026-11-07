> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Automation Modes — Shared Skill Pattern

**Companion spec**: `<skill-root>/references/studio/effects-map.md`
section `modes.automation` is the source of truth for behavior. This document
is the implementation pattern.

> **Do not read `effects-map.md` during a skill run** — it is a very large file, a
> reference for authoring the spec rather than a runtime input, and **this
> document is self-sufficient** for deciding what to ask and what to proceed on.
> If a case genuinely is not covered here, read only its `modes.automation`
> section, never the file.

---

## How to Use This Document

**Startup prelude** (add near Phase 0 / Phase 1):

```
Resolve automation mode (once, store for the run):
1. Read `modes.automation` from `project.local.yaml` (if present) → use that
2. Else read `modes.automation` from `project.yaml` → use that value
3. Else → default to `collaborative`

Pattern reference: `<skill-root>/references/studio/automation-modes.md`.
```

This resolution is automatic via `get_effective_yaml_key modes.automation` —
the helper deep-merges project.local.yaml on top of project.yaml.

---

## The Three Modes

**Default**: `collaborative`. New projects start here.

**Set by**: `$game-studio start`, `$game-studio settings`.

---

## Universal Rules per Mode

### Collaborative (current v1.0 behavior — no change)

### Guided

### Autonomous

### Every mode: a question with no answer

A question that comes back **skipped, dismissed or empty is not an answer**, in
every mode and on every tool: the user closing the question, a headless run that
returns every question as skipped, a reply that picks nothing.

- Do not write a file, change a mode or setting, or pick an option on its behalf.
- Ask again in plain text, say what is waiting on the answer, and wait.
- In `autonomous`, a question the mode did not require can be decided as usual:
  pick the recommended option and log it via `log_decision`. A question in an
  `automation_always_ask` category, or in an exempt skill, is the user's: ask
  again and wait.
- Where nobody can answer (CI, a headless run), stop and report what is waiting
  rather than choosing.

---

## Major vs Minor Decision Classification

Skills label each gated decision as **major** or **minor** before applying
the mode rules.

| Decision type | Example |
|---------------|---------|
| Choosing a system name or document path | "What should we call this system?" |
| Mutually exclusive design directions | "Real-time or turn-based?" |
| Any choice that gates downstream work | Engine choice, architecture approach |
| Scope changes | "Cut this feature or slip the deadline?" |
| Any decision that can't be changed without significant rework | Core loop mechanic |

### Minor — AI recommends and proceeds in guided mode

| Decision type | Example |
|---------------|---------|
| Which section to work on next | "Moving to Edge Cases next" |
| Optional section inclusion | "Adding a Visual Notes section — fits the system" |
| Formatting and structure choices | Heading levels, table vs prose |
| Adding detail to an already-decided direction | Sub-options within an approved approach |
| Next-step routing after a phase completes | "Running design-review now" |

---

## `automation_always_ask` Categories

**Default** (when unset): `[scope_changes, file_deletions, schema_changes]`.

### Recognized categories

**This table is the set you may configure, NOT the set that always asks.** Only
the categories actually listed in `modes.automation_always_ask` — the three
defaults above, unless the project overrides them — interrupt an `autonomous`
run. The other rows do nothing until a project opts into them. Read the resolved
list with `resolve_config` rather than assuming a row here is active. Treating a
category the project never configured, such as `architecture_decisions`, as
active reports rule violations the project never asked for.

| Category | Examples of decisions in this category |
|----------|----------------------------------------|
| `scope_changes` | Cutting a feature, slipping a deadline, splitting/merging an epic, removing acceptance criteria |
| `file_deletions` | Removing a story, deleting a GDD, removing a system, removing a test file |
| `schema_changes` | Changes to project.yaml, story template, control manifest, ADR template, GDD template |
| `architecture_decisions` | New ADR creation, ADR replacement, system boundary changes |
| `version_bumps` | Engine version change, framework version bump, dependency major version change |
| `external_calls` | Invoking external APIs (asset gen, AI services) when in autonomous mode |

### Helper

```bash
is_always_ask_category <category>
```

Returns 0 if the named category is in `modes.automation_always_ask`,
1 otherwise. Skills use this at decision points that fall into any
of the six categories above.

---

## Exemptions — Skills That Ignore the Automation Setting

These skills always behave as `collaborative` regardless of the setting:

These skills do NOT add the automation prelude described above. They keep
the v1.0 Q→O→D→Draft→Approval protocol exactly.

---

## Decision Log Format (Autonomous Mode)

```markdown
## [timestamp] — [skill-name]

**Decision point:** [what was being decided]
**Options considered:** [list of options that would have been presented]
**Chosen:** [what was picked]
**Reason:** [one-line rationale]
**Category:** [scope_changes | file_deletions | schema_changes | … or "minor"]
```

Written to `production/session-logs/decision-log.md` (append-only, never
truncated, created if absent). The user reviews the log post-session to
audit choices made.

### Helper

```bash
log_decision "<skill-name>" "<decision-point>" "<options>" "<chosen>" "<reason>" "<category>"
```

Wraps the format above. Skills call this at every decision point in
autonomous mode, including ones where the chosen value differs from
the recommended default (so the audit trail is complete).

### What to log, and at what granularity

These rules keep autonomous logs consistent across runs:

### Categorizing data-file writes

The most common categorization mistake is treating a data-file append as a
`schema_changes` decision:

- **Appending facts to a registry or index** — e.g.
  `design/registry/entities.yaml`, `design/gdd/systems-index.md` — is
  **`minor`**. It adds data without altering a *template*.
- **`schema_changes`** means editing the *structure* of `project.yaml` or a
  template (story / ADR / GDD / control-manifest template). These are
  always-ask.
- **When genuinely unsure** between `minor` and an always-ask category,
  prefer the always-ask category and prompt — failing safe.

---

This is the contract. Skills that follow this pattern produce
consistent behavior across all three automation modes.
