---
name: settings
description: "View or change project config — effective merged values, or set locally in project.local.yaml."
# Source argument-hint: "[key | key=value | --local key=value]"
# Source user-invocable: true
# Source allowed-tools (not enforced): Read, Glob, Grep, Write, Edit, ask the user when needed, Bash(bash "*/<plugin-root>/skills/settings/../../hooks/yaml-helper.sh" resolve_setting *), Bash(bash "*/<plugin-root>/skills/settings/../../hooks/yaml-helper.sh" get_yaml_key *), Bash(bash "*/<plugin-root>/skills/settings/../../hooks/yaml-helper.sh" validate_yaml_enum *), Bash(bash "*/<plugin-root>/skills/settings/../../hooks/yaml-helper.sh" validate_enum_value *), Bash(bash "*/<plugin-root>/skills/settings/../../hooks/yaml-helper.sh" is_locally_overridable *), Bash(bash <plugin-root>/shared/scripts/config-set.sh *), Bash(grep -B14 '^> ### RESERVED' <plugin-root>/shared/docs/effects-map.md), Bash(grep -E '^## ')
# Source model: sonnet
---

Read [Codex compatibility](../../COMPATIBILITY.md) before following this workflow.

Codex adaptation: `<plugin-root>` is two directories above this skill. Read `<plugin-root>/skills/game-studio/references/compatibility.md` before applying source procedures. Use the current host's tools and existing user authorization. Source per-file prompts do not reset that authorization. Source shell preprocessing is not executed: resolve needed project configuration explicitly. Shared source scripts and hooks are reference-only until separately reviewed; use the authored game-studio helper for supported asset observations. Preserve domain decision options and report missing evidence as NOT ASSESSED.

Read [the complete workflow](WORKFLOW.md) and only the supporting references relevant to this request.
