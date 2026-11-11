---
name: security-audit
description: "Security audit — save tampering, cheat vectors, network exploits, data exposure, input validation. Before public or multiplayer release."
# Source argument-hint: "[full | network | save | input | quick]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Agent, Bash(bash "*/<plugin-root>/skills/security-audit/../../hooks/yaml-helper.sh" resolve_config *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
