---
name: dev-story
description: "Implements one story in code with tests, following its ADRs. Use when the user says to build, implement or start working on a story. Not for checking readiness beforehand or closing the story after."
# Source argument-hint: "[story-path]"
# Source user-invocable: true
disable-model-invocation: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, Agent, ask the user when needed, Bash(bash "*/<plugin-root>/skills/dev-story/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/story-facts.sh *), Bash(bash <plugin-root>/shared/scripts/adr-status.sh *), Bash(bash <plugin-root>/shared/scripts/md-section.sh *), Bash(bash <plugin-root>/shared/scripts/session-state.sh *), Bash(bash <plugin-root>/shared/scripts/review-receipts.sh hash *), Bash(godot *), Bash(mkdir -p production/qa/evidence/*)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
