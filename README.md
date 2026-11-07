# Codex Game Studios

An unofficial Codex adapter for [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios), pinned to upstream commit `05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418`. It packages the upstream studio's game development guidance as one Codex skill, with 49 role briefs and 74 workflows loaded on demand.

## Install

Clone this repository, then run:

```sh
python3 scripts/validate_port.py
python3 scripts/install_codex.py
```

The installer links `~/.agents/skills/game-studio` to this checkout and refuses to replace existing content. Keep the checkout in place; restart Codex if the skill is not discovered. Use `--skills-dir` to choose another skill directory.

## Use

Ask Codex to use `$game-studio` for game design, implementation, art, animation, audio, or review. For example: “Use $game-studio to review this game's animation and fix visible defects.”

```sh
python3 skills/game-studio/scripts/studio.py catalog technical-artist
python3 skills/game-studio/scripts/studio.py inspect --project /path/to/game
python3 skills/game-studio/scripts/studio.py asset-audit --root /path/to/assets
```

The helper reports observations about PNG, WAV and JSON files; it does not replace viewing the game or listening to audio.

## How the adapter works

The shipped skill is a generated artifact plus Codex-specific guides and helpers. The converter removes Claude-specific transport instructions and rewrites references; the conversion log records removals. Roles are briefs, not automatically running agents. Claude hooks, model selection, permissions and tool allowlists are not installed. Some upstream automation therefore has no direct equivalent. See `skills/game-studio/references/compatibility.md` for the contract.

To regenerate, clone the upstream repository separately, check out the pinned commit, and run:

```sh
python3 scripts/port_codex.py --upstream /path/to/Claude-Code-Game-Studios
python3 scripts/validate_port.py
```

The converter requires a clean checkout at the pinned commit. Updating upstream requires reviewing conversion output and changing the pin deliberately. Generated references are shipped so normal use requires no upstream checkout.

## License

MIT. The upstream license and copyright notice are preserved in [LICENSE](LICENSE) and the skill. This project is an independent adaptation, not affiliated with the upstream author or OpenAI.
