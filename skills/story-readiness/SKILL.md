---
name: story-readiness
description: "Checks whether a story is ready to implement: clear acceptance criteria, no open questions, valid ADR and dependencies. Use when the user asks if a story, or the sprint's stories, are ready to start or build."
# Source argument-hint: "[story-file-path or 'all' or 'sprint'] [--review full|lean|solo]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, ask the user when needed, Agent, Bash(bash "*/<plugin-root>/skills/story-readiness/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/story-facts.sh *), Bash(bash <plugin-root>/shared/scripts/adr-status.sh *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
