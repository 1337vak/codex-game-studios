> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# Hook: pre-commit-code-quality

## Trigger

Runs before any commit that modifies files under the code root — `src/`
(Godot), `Assets/` (Unity) or `Source/` (Unreal); see
`<skill-root>/references/studio/code-root-resolution.md`.

## Purpose

Enforces coding standards before code enters version control. Catches style
violations, missing documentation, overly complex methods, and hardcoded
values that should be data-driven.

## Implementation

## Agent Integration

When this hook fails:
1. For style violations: auto-fix with your formatter or invoke `lead-programmer`
2. For hardcoded values: invoke `gameplay-programmer` to externalize the values
3. For test failures: invoke `qa-tester` to diagnose and `gameplay-programmer` to fix
