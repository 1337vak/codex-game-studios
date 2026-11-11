#!/usr/bin/env python3
"""Report malformed JSON asset data after a write, without changing files.

Adapts the JSON check in the pinned studio's validate-assets.sh to a plugin
installed outside the game project. The shared studio helper owns file parsing.
"""
import importlib.util
import json
from pathlib import Path
import re
import sys

# Installed plugins can be read-only. Import the shared parser without leaving
# interpreter cache files beside the package's recorded source bytes.
sys.dont_write_bytecode = True


def context(message):
    print(json.dumps({'hookSpecificOutput': {
        'hookEventName': 'PostToolUse', 'additionalContext': message,
    }}))


def main():
    event = json.load(sys.stdin)
    if not isinstance(event, dict):
        raise ValueError('expected a JSON hook event object')
    project = Path(event.get('cwd') or Path.cwd()).resolve(strict=True)
    payload = event.get('tool_input', {})
    paths = []
    if isinstance(payload, dict):
        for key in ('file_path', 'path'):
            if isinstance(payload.get(key), str):
                paths.append(payload[key])
        patch = payload.get('patch') or payload.get('input') or ''
        # Codex's native apply_patch hook payload stores the patch in `command`.
        # An ordinary shell command must not be interpreted as a patch.
        command = payload.get('command')
        if not patch and isinstance(command, str) and command.startswith('*** Begin Patch'):
            patch = command
    else:
        patch = payload if isinstance(payload, str) else ''
    if isinstance(patch, str):
        paths.extend(re.findall(r'^\*\*\* (?:Add File|Update File|Move to): (.+)$', patch, re.M))
    if not paths:
        context('Asset JSON check NOT ASSESSED: this tool event supplied no file paths.')
        return 0

    candidates = set()
    for value in paths:
        file = (project / value).resolve()
        if not file.is_relative_to(project):
            continue
        parts = file.relative_to(project).parts
        if (file.is_file() and file.suffix.lower() == '.json' and len(parts) >= 3
                and parts[0] in {'assets', 'Assets', 'Content'}
                and any(part.lower() == 'data' for part in parts[1:-1])):
            candidates.add(file)
    if not candidates:
        return 0

    helper = Path(__file__).resolve().parents[1] / 'skills/game-studio/scripts/studio.py'
    spec = importlib.util.spec_from_file_location('game_studio_asset_checks', helper)
    studio = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(studio)
    observations = studio.audit(project, paths=candidates)
    if observations['parse_errors']:
        for error in observations['parse_errors']:
            print(f"Asset JSON invalid: {error['path']}: {error['error']}", file=sys.stderr)
        print('The write already happened; correct the malformed asset data before continuing.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, TypeError) as error:
        print(f'Asset JSON check NOT ASSESSED: {error}', file=sys.stderr)
        raise SystemExit(2)
