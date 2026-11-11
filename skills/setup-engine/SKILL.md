---
name: setup-engine
description: "Configure engine and version. Pins it in CLAUDE.md; WebSearch fills reference docs when the version is beyond LLM training data."
# Source argument-hint: "[engine] | [engine version] | refresh | upgrade [old-version] [new-version] | no args for guided selection"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, WebSearch, WebFetch, Agent, ask the user when needed, Bash(bash "*/<plugin-root>/skills/setup-engine/../../hooks/yaml-helper.sh" resolve_config *), Bash(godot --version), Bash(godot --headless --path . --import), Bash(command -v godot), Bash(uname -s), Bash(bash <plugin-root>/shared/scripts/project-coherence.sh*)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
