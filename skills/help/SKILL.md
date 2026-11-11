---
name: help
description: "What should I do next? Use when stuck or you don't know what to do."
# Source argument-hint: "[optional: what you just finished, e.g. 'finished design-review' or 'stuck on ADRs']"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Bash(bash "*/<plugin-root>/skills/help/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash "*/<plugin-root>/skills/help/../../scripts/story-status.sh"), Bash(bash <plugin-root>/shared/scripts/story-status.sh*), Bash(bash <plugin-root>/shared/scripts/artifact-check.sh *), Bash(bash "<plugin-root>/shared/scripts/artifact-check.sh" *), Bash(bash ./<plugin-root>/shared/scripts/artifact-check.sh *), Bash(git log *)
# Source model: haiku
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
