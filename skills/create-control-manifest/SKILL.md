---
name: create-control-manifest
description: "Builds a short list of must-do and never-do coding rules per system from accepted ADRs. Use when the user wants programmer rules or a cheat sheet from the ADRs, or needs it regenerated after ADR changes."
# Source argument-hint: "[update — regenerate from current ADRs] [--review full|lean|solo]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Agent, ask the user when needed, Bash(bash "*/<plugin-root>/skills/create-control-manifest/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/adr-status.sh*), Bash(bash <plugin-root>/shared/scripts/md-section.sh *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
