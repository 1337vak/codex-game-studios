> Codex reference: use the native compatibility contract at `<skill-root>/references/compatibility.md`. This is domain guidance, not an executable agent, hook, or permission policy. Project instructions and the user's existing authorization take precedence.

# $game-studio test-setup — Phase 6: Post-Setup Summary

> Part of `$game-studio test-setup`. `SKILL.md` names when to read this file; the settings it
> resolved and the rules under its later headings still apply here.

## Phase 6: Post-Setup Summary

After writing all files, report:

```
Test infrastructure created for [engine].

Files created:
- tests/README.md
- tests/unit/ and tests/integration/ (Godot) — or the engine's test root:
  Unity Assets/Tests/EditMode/ and PlayMode/, Unreal Source/<Module>/Private/Tests/
- tests/smoke/critical-paths.md
- production/qa/evidence/.gitkeep
[engine-specific files]
- .github/workflows/tests.yml

Next steps:
1. [Engine-specific install step, e.g., "Install GdUnit4 via the Asset Store (AssetLib before Godot 4.7)"]
2. Write your first test in the engine's test root:
   tests/unit/[system]/[system]_[feature]_test.gd (Godot),
   Assets/Tests/EditMode/[System]Tests.cs (Unity), or
   Source/<Module>/Private/Tests/[System]Test.cpp (Unreal)
3. Run `$game-studio qa-plan sprint` before your first sprint to classify stories and set
   test evidence requirements. At `workflow: minimal` — the default — skip
   this: there are no sprints. At `qa.level: minimal`, also the default, tests
   are waived, so `$game-studio dev-story` writes none. Raise `qa.level` with `$game-studio settings`
   to have it write them
4. `$game-studio smoke-check` before every QA hand-off

Gate note: $game-studio gate-check Technical Setup → Pre-Production now requires:
- the engine's test root: tests/unit/ and tests/integration/ (Godot),
  Assets/Tests/EditMode/ and Assets/Tests/PlayMode/ (Unity), or
  Source/<Module>/Private/Tests/ (Unreal)
- .github/workflows/tests.yml
- At least one example test file
Run $game-studio test-setup and write one example test before advancing.
(At `workflow: minimal` that gate requires only the engine.)

Verdict: **COMPLETE** — test framework scaffolded and CI/CD wired up.
```

---
