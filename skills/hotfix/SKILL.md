---
name: hotfix
description: "Emergency fix bypassing normal sprint process — hotfix branch, approvals tracked, backport verified, full audit trail."
# Source argument-hint: "[bug-id or description]"
# Source user-invocable: true
disable-model-invocation: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, Agent, ask the user when needed, Bash(git rev-parse *), Bash(git tag --list*), Bash(git branch --list *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
