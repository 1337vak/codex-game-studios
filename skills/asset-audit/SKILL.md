---
name: asset-audit
description: "Audit assets against naming conventions, file size budgets, format standards. Finds orphaned assets, missing references."
# Source argument-hint: "[category|all]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Bash(stat *), Bash(file *), Bash(od *), Bash(wc *), Bash(du *)
# Source model: sonnet
# Read-only diagnostic skill — no specialist agent delegation needed
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
