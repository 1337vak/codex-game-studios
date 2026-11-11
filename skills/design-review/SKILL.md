---
name: design-review
description: "Reviews one design document for completeness, internal consistency, implementability, and design standards. Before handing to programmers."
# Source argument-hint: "[path-to-design-doc] [--review full|lean|solo]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, Agent, ask the user when needed, Bash(bash "*/<plugin-root>/skills/design-review/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/review-receipts.sh check *), Bash(bash <plugin-root>/shared/scripts/review-receipts.sh hash *), Bash(bash <plugin-root>/shared/scripts/gdd-structure-check.sh *), Bash(grep -E '^  - name:' design/registry/entities.yaml), Bash(grep -n -i -E *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
