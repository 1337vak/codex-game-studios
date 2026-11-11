---
name: game-studio
description: Coordinate game design, engine implementation, art, animation, audio, and evidence-based QA using focused studio roles and workflows. Use for building or reviewing games and playable prototypes.
---

# Game Studio

Use the user's existing game, engine, approved art direction, and authorization.
Read [compatibility](references/compatibility.md) once before using the port.
`<skill-root>` means this folder; `<project-root>` means the actual game repository,
which can be different from the toolkit repository. `<plugin-root>` is two
directories above this skill folder.

Choose the smallest useful workflow and role set. Search `catalog.json`, or run:

```sh
python3 <skill-root>/scripts/studio.py catalog polish
```

Read only the returned workflow and role references needed for the task. The
catalog preserves 74 workflows and 49 role briefs from the MIT-licensed upstream
studio. Workflows are native, explicitly invoked skills (for example `$game-studio:prototype`
or `$game-studio:asset-audit`); the catalog resolves their installed locations. Role briefs
are references used with the host's native delegation tools, not registered
agents or separate models.

For current work:

- Visual identity, staging and animation: read [visual review](references/visual-review.md), then the `art-director` or `technical-artist` brief as needed.
- Asset import correctness and measurements: use [asset audit](references/asset-audit.md) and the read-only helper below.
- Coordinated fixes: use [polish](references/polish.md), assigning explicit ownership and observable acceptance conditions.
- Other game work: select a catalog workflow by name, such as `prototype`, `design-system`, `unity-specialist`, `qa-plan` or `release-checklist`.

```sh
python3 <skill-root>/scripts/studio.py inspect --project <project-root>
python3 <skill-root>/scripts/studio.py asset-audit --root <asset-root> --output <temporary-report.json>
```

Use native subagent tools when available. Give each selected specialist the
relevant brief, current constraints, owned files, expected artifact, and evidence
needed. Respect current concurrency limits and inherit the current model. Carry
out short or dependent tasks directly. A role title is expertise guidance, not a
reason to stop an authorized implementation because a different title owns it.

Finish with the actual result, evidence inspected, unresolved defects and limits.
Do not turn an art or animation request into documentation-only work. Preserve
user approvals across phases; do not import upstream per-file approval prompts.
Do not claim a hook, test, render, playback, or specialist pass ran unless it did.

Attribution, the upstream pin, conversion decisions, and build provenance are in
`<plugin-root>/README.md`, `COMPATIBILITY.md`, `provenance.json`, and `LICENSE`.
