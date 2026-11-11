---
name: story-done
description: "Closes a finished story: verifies each acceptance criterion, checks for design or ADR deviations and updates its status. Use when the user says a story is done, finished or ready to close."
# Source argument-hint: "[story-file-path] [--review full|lean|solo]"
# Source user-invocable: true
disable-model-invocation: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, ask the user when needed, Agent, Bash(bash "*/<plugin-root>/skills/story-done/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/story-facts.sh *), Bash(bash <plugin-root>/shared/scripts/story-status.sh*), Bash(bash <plugin-root>/shared/scripts/adr-status.sh *), Bash(bash <plugin-root>/shared/scripts/md-section.sh *), Bash(bash <plugin-root>/shared/scripts/review-receipts.sh check *), Bash(bash <plugin-root>/shared/scripts/session-state.sh *), Bash(git status --porcelain*)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
