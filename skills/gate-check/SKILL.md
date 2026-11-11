---
name: gate-check
description: "Ready to advance between development phases? PASS/CONCERNS/NOT ASSESSED/FAIL with blockers and required artifacts. 'Can we move to production?'"
# Source argument-hint: "[target-phase: systems-design | technical-setup | pre-production | production | polish | release] [--review full|lean|solo]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, Agent, ask the user when needed, Bash(bash "*/<plugin-root>/skills/gate-check/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/artifact-check.sh *), Bash(bash <plugin-root>/shared/scripts/gdd-structure-check.sh*), Bash(bash <plugin-root>/shared/scripts/adr-dep-graph.sh*), Bash(bash <plugin-root>/shared/scripts/set-stage.sh *)
# Source model: opus
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
