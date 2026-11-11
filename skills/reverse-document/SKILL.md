---
name: reverse-document
description: "Generate missing design or architecture docs from existing implementation — works backwards from code and prototypes."
# Source argument-hint: "<type> <path> (e.g., 'design src/gameplay/combat' or 'architecture Assets/Scripts/Core')"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, Bash(bash "*/<plugin-root>/skills/reverse-document/../../hooks/yaml-helper.sh" resolve_config *)
# Source model: sonnet
# Read-only diagnostic skill — no specialist agent delegation needed
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
