> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio architecture-review — Phase 9: Handoff

> Part of `$game-studio architecture-review`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## Phase 9: Handoff

After completing the review and writing approved files, present:

1. **Immediate actions**: List the top 3 ADRs to create (highest-impact gaps first,
   Foundation layer before Feature layer)
2. **Pre-gate checklist**: Check whether these exist via Glob and mark each ✅ or ❌:
   - the engine's test root — `tests/unit/` and `tests/integration/` (Godot), `Assets/Tests/EditMode/` and `Assets/Tests/PlayMode/` (Unity), `Source/<Module>/Private/Tests/` (Unreal) — if ❌: run `$game-studio test-setup`
   - `.github/workflows/tests.yml` — if ❌: run `$game-studio test-setup`
   - `design/accessibility-requirements.md` — if ❌: run `$game-studio ux-design`
   - `design/ux/interaction-patterns.md` — if ❌: run `$game-studio ux-design`
   Present ❌ items as required steps before gate-check. Do not offer `$game-studio gate-check`
   as an option if any item is ❌ — offer the missing skill to run instead.
3. **Rerun trigger**: "Re-run `$game-studio architecture-review` after each new ADR is written
   to verify coverage improves"

---
