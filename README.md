# Codex Game Studios

An unofficial Codex adapter for [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios), pinned to upstream commit [`05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418`](https://github.com/Donchitos/Claude-Code-Game-Studios/tree/05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418). The upstream author created the studio's game development procedures, 49 specialist roles, and 74 workflows. This repository maintains the Codex adaptation and a small read-only asset helper.

## Install the plugin

The `release` branch contains the generated, self-contained plugin and its Codex marketplace. With a current Codex CLI:

```sh
codex plugin marketplace add 1337vak/codex-game-studios --ref release
codex plugin add game-studio@codex-game-studios
```

Start a new Codex session after installation. Review the asset-validation hook through Codex's hook trust flow before expecting it to run. Installation does not automatically trust hooks. The plugin includes a lifecycle hook, so this distribution targets GitHub marketplaces and manual Codex installation rather than OpenAI's public directory.

If you used the old `install_codex.py` skill installer, inspect `~/.agents/skills/game-studio` before upgrading. Remove only an adapter-owned legacy symlink after checking its target, which may point to an old source skill or generated build, to avoid loading both installations; preserve unrelated user content. The new plugin build does not update that legacy standalone-skill directory.

## Use

Ask Codex to use `$game-studio:game-studio` for game design, engine implementation, art, animation, audio, or evidence-based QA. It finds the relevant workflow and role brief without loading the entire studio. Each upstream workflow can also be invoked directly, for example `$game-studio:prototype`, `$game-studio:asset-audit`, or `$game-studio:release-checklist`; those 74 skills are explicit-only to avoid accidental activation.

The authored helper measures PNG, WAV, and JSON assets without modifying them. Its observations do not prove visual quality, animation smoothness, audio quality, or compliance with a budget the project has not supplied. It reports malformed files and checks it did not assess. The adapted PostToolUse hook reuses that parser to report invalid changed JSON asset data.

## Rebuild and test

```sh
python3 scripts/port.py build
python3 scripts/port.py verify
```

The bootstrap reads the tool pin in `port.json`. Builds fetch the exact source and converter revisions, apply transformations and maintained overrides, and write the result under `build/`. Python 3.11+, Git, and network access for pinned dependencies are required. The converter uses Bun; when it is absent the build can provision the pinned runtime locally through npm. The converter is [EveryInc's Compound Engineering converter](https://github.com/EveryInc/compound-engineering-plugin/tree/4ba48871919650d43a412e3faf0374272fdc209d); the shared build/publishing tool is [claude-to-codex-plugin-port](https://github.com/1337vak/claude-to-codex-plugin-port).

`tests/verify.py` exercises actual helper and hook processes against disposable valid and malformed PNG/WAV/JSON assets. It also checks that source prototype and audit decisions survive conversion, including `NOT ASSESSED` for missing evidence. Fixture execution, native Codex discovery, and model-driven workflow behavior are separate checks; the generated test report records their actual status.

## How this adapter stays small

`port.json` locks the source, converter, and shared port tool and records the transformation recipe and compatibility decisions. `overrides/` contains the small Codex-specific router, guides, helper, and hook shim. Generated upstream files are not maintained in this checkout. Update the pin deliberately, rebuild, inspect the transformation report, and run tests before publishing a new release.

All 74 workflow entrypoints retain their reference trees. The 49 roles become local prompt briefs for native subagents rather than registered agents with hardcoded models or permissions. Shared source docs/rules remain references; original project-template scripts and hooks are preserved for inspection without activation. The generated plugin's `COMPATIBILITY.md` records every adaptation and limitation. The original broad paragraph-removal converter has been replaced by a pinned converter plus count-checked textual patches, preserving the domain decisions inside source paragraphs.

## Attribution and license

The studio guidance and generated source resources are MIT-licensed work by Donchitos. [LICENSE](LICENSE) preserves the original notice. The generated package records its exact origin and converter pins in `provenance.json`; source hashes and compatibility decisions make the adaptation reviewable. This is an independent adaptation, not affiliated with Donchitos, EveryInc, or OpenAI.
