#!/usr/bin/env python3
"""Fetch the pinned upstream revision and build the Codex skill locally."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
pin = '05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418'
url = 'https://github.com/Donchitos/Claude-Code-Game-Studios.git'
output = root / 'build' / 'game-studio'
with tempfile.TemporaryDirectory(prefix='codex-studio-upstream-') as temp:
    upstream = Path(temp) / 'upstream'
    subprocess.run(['git', 'init', '--quiet', str(upstream)], check=True)
    subprocess.run(['git', '-C', str(upstream), 'fetch', '--quiet', '--depth=1', url, pin], check=True)
    subprocess.run(['git', '-C', str(upstream), 'checkout', '--quiet', '--detach', 'FETCH_HEAD'], check=True)
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(root / 'skills/game-studio', output)
    subprocess.run([sys.executable, str(root / 'scripts/port_codex.py'), '--upstream', str(upstream), '--output', str(output)], check=True)
