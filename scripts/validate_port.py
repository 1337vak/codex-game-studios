#!/usr/bin/env python3
"""Check port resources and exercise its measurements/installer in isolation."""
from pathlib import Path
import json
import struct
import subprocess
import sys
import tempfile
import wave

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'build/game-studio'
catalog = json.loads((SKILL / 'catalog.json').read_text())
assert len(catalog['roles']) == 49 and len(catalog['workflows']) == 74
for entries in catalog.values():
    for entry in entries:
        file = SKILL / entry['path']
        assert file.is_file(), file
        assert file.resolve().is_relative_to(SKILL.resolve()), file
        assert file.stat().st_size > 250, file
assert (SKILL / 'LICENSE').read_text() == (ROOT / 'LICENSE').read_text()
for file in (SKILL / 'references').rglob('*.md'):
    text = file.read_text()
    for forbidden in ['AskUserQuestion', 'CLAUDE_SKILL_DIR', 'subagent_type:', 'TaskCreate', 'May I ']:
        assert forbidden not in text, (file, forbidden)

with tempfile.TemporaryDirectory(prefix='codex-studio-test-') as folder:
    p = Path(folder)
    # Real PCM audio and valid JSON exercise parsing; malformed data must remain
    # an error observation, not disappear into a clean verdict.
    with wave.open(str(p / 'voice.wav'), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000)
        w.writeframes(b'\x00\x00' * 24000)
    (p / 'valid.json').write_text('{"ok":true}')
    (p / 'broken.json').write_text('{broken')
    tool = SKILL / 'scripts/studio.py'
    result = json.loads(subprocess.check_output([sys.executable, str(tool), 'asset-audit', '--root', str(p)], text=True))
    assert result['files_scanned'] == 3 and len(result['parse_errors']) == 1
    audio = next(f for f in result['files'] if f['format'] == 'wav')
    assert audio['duration'] == 1 and audio['sample_rate'] == 24000
    installer = [sys.executable, str(ROOT / 'scripts/install_codex.py'), '--skills-dir', str(p / 'skills')]
    first = json.loads(subprocess.check_output(installer, text=True))
    second = json.loads(subprocess.check_output(installer, text=True))
    assert first['status'] == 'installed' and second['status'] == 'already installed'
    other = p / 'collision/game-studio'; other.mkdir(parents=True)
    (other / 'keep.txt').write_text('existing user content')
    refusal = subprocess.run([sys.executable, str(ROOT / 'scripts/install_codex.py'), '--skills-dir', str(other.parent)], capture_output=True, text=True)
    assert refusal.returncode != 0 and (other / 'keep.txt').read_text() == 'existing user content'
print('PASS: 49 roles, 74 workflows, attribution, forbidden transport, audio/JSON observations, idempotent install and collision protection')
