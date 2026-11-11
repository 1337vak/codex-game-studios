---
name: start
description: "Guides a first-time user through onboarding and picks the right workflow. Use when the user is new, just cloned or installed the studio, has no idea or engine yet, asks where to begin, or wants to bring in an existing game."
# Source argument-hint: "[no arguments]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, ask the user when needed, Bash(bash <plugin-root>/shared/scripts/project-state.sh*), Bash(bash <plugin-root>/shared/scripts/set-stage.sh *), Bash(bash <plugin-root>/shared/scripts/config-set.sh *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
