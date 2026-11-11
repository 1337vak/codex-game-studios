---
name: create-stories
description: "Breaks one epic into implementable stories with acceptance criteria. Use when the user wants stories for an epic or the next batch of work to build. Not for turning the whole design into epics."
# Source argument-hint: "[epic-slug | epic-path] [--review full|lean|solo]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, Agent, ask the user when needed, Bash(bash "*/<plugin-root>/skills/create-stories/../../hooks/yaml-helper.sh" resolve_config *), Bash(bash <plugin-root>/shared/scripts/adr-status.sh *), Bash(bash <plugin-root>/shared/scripts/md-section.sh extract *), Bash(bash <plugin-root>/shared/scripts/md-section.sh list *)
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
