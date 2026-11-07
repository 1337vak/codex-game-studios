# Codex Game Studios

An unofficial Codex adapter for [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios), pinned to upstream commit `05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418`. It packages the upstream studio's game development guidance as one Codex skill, with 49 role briefs and 74 workflows loaded on demand.

## Install

Clone this repository, then run:

```sh
python3 scripts/build.py
python3 scripts/validate_port.py
python3 scripts/install_codex.py
```

The installer links `~/.agents/skills/game-studio` to the generated `build/game-studio` directory and refuses to replace existing content. Keep the checkout in place; restart Codex if the skill is not discovered. Use `--skills-dir` to choose another skill directory.

## Use

Ask Codex to use `$game-studio` for game design, implementation, art, animation, audio, or review. For example: “Use $game-studio to review this game's animation and fix visible defects.”

```sh
python3 build/game-studio/scripts/studio.py catalog technical-artist
python3 build/game-studio/scripts/studio.py inspect --project /path/to/game
python3 build/game-studio/scripts/studio.py asset-audit --root /path/to/assets
```

The helper reports observations about PNG, WAV and JSON files; it does not replace viewing the game or listening to audio.

## How the adapter works

The build fetches the pinned upstream revision and generates a skill using the Codex-specific guides and helpers in this repository. The converter removes Claude-specific transport instructions and rewrites references; the conversion log records removals. Roles are briefs, not automatically running agents. Claude hooks, model selection, permissions and tool allowlists are not installed. Some upstream automation therefore has no direct equivalent. See `skills/game-studio/references/compatibility.md` for the contract.

To regenerate the skill, run:

```sh
python3 scripts/build.py
python3 scripts/validate_port.py
```

The build requires Git, Python 3, and network access to GitHub. Updating upstream requires reviewing conversion output and changing the pin deliberately in the build and converter scripts. Generated references and the conversion log live under `build/game-studio`.

## License

MIT. The upstream license and copyright notice are preserved in [LICENSE](LICENSE) and the skill. This project is an independent adaptation, not affiliated with the upstream author or OpenAI.
