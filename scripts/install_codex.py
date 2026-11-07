#!/usr/bin/env python3
"""Install only the native skill. Refuse to replace existing user content."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--skills-dir', type=Path, default=Path.home() / '.agents/skills')
args = parser.parse_args()
source = ROOT / 'build/game-studio'
destination = args.skills_dir.expanduser().resolve() / 'game-studio'
if not (source / 'SKILL.md').is_file():
    raise SystemExit('Native skill is missing; run scripts/build.py first.')
if destination.is_symlink() and destination.resolve() == source.resolve():
    status = 'already installed'
elif destination.exists() or destination.is_symlink():
    raise SystemExit(f'Refusing to replace existing content: {destination}')
else:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.symlink_to(source, target_is_directory=True)
    status = 'installed'
print(json.dumps({'status': status, 'path': str(destination), 'source': str(source), 'note': 'No account settings, hooks, model selection or permission settings changed.'}))
