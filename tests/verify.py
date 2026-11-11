#!/usr/bin/env python3
"""Exercise the built helper, hook protocol, and retained domain contract.

These tests run helper/hook processes against disposable data. They do not claim
that Codex activated a hook or that a model followed an entire workflow.
"""
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import wave
import zlib


def run_json(*args):
    return json.loads(subprocess.check_output([sys.executable, *map(str, args)], text=True))


def png(width, height):
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    header = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    pixels = b''.join(b'\x00' + b'\xff\x00\x00\xff' * width for _ in range(height))
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', header) + chunk(b'IDAT', zlib.compress(pixels)) + chunk(b'IEND', b'')


def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


def main():
    plugin = Path(sys.argv[1]).resolve(strict=True)
    assert not list(plugin.rglob('*.pyc')), 'Interpreter caches must not enter the release'
    package_before = snapshot(plugin)
    router = plugin / 'skills/game-studio'
    catalog = json.loads((router / 'catalog.json').read_text())
    assert len(catalog['roles']) == 49, 'Missing role briefs'
    assert len(catalog['workflows']) == 74, 'Missing native workflows'
    for group in catalog.values():
        for row in group:
            file = (router / row['path']).resolve(strict=True)
            assert file.is_relative_to(plugin), row
            assert len(row['source_sha256']) == 64, row
    skills = {p.name for p in (plugin / 'skills').iterdir() if (p / 'SKILL.md').is_file()}
    assert len(skills) == 75 and 'game-studio' in skills, skills
    for row in catalog['workflows']:
        policy = (plugin / 'skills' / row['name'] / 'agents/openai.yaml').read_text()
        assert 'allow_implicit_invocation: false' in policy, row['name']

    # Domain evidence decisions must survive transport conversion.
    prototype = plugin / 'skills/prototype'
    body = '\n'.join(p.read_text() for p in prototype.glob('*.md'))
    assert 'Prototype code must NEVER import from production source files' in body
    assert 'Production code must NEVER import from prototype directories' in body
    assert 'Test ONE mechanic' in body and '1 day' in body
    assert 'real peers or simulated latency' in body
    debrief = (prototype / 'references/6-debrief.md').read_text()
    assert 'NOT ASSESSED — built, not' in debrief and 'played' in debrief
    director = (prototype / 'references/8-cd-review.md').read_text()
    assert 'PIVOT' in director and 'KILL' in director and 'not an approval' in director
    asset_body = '\n'.join(p.read_text() for p in (plugin / 'skills/asset-audit').glob('*.md'))
    assert 'NOT ASSESSED — NO DATA' in asset_body and 'zero assets scanned' in asset_body
    assert 'at least one asset scanned, every section assessed, no findings' in asset_body

    helper = router / 'scripts/studio.py'
    matches = run_json(helper, 'catalog', 'prototype')['matches']
    assert any(Path(row['absolute_path']).resolve() == prototype / 'SKILL.md' for row in matches)
    with tempfile.TemporaryDirectory(prefix='game-studio-fixture-') as folder:
        project = Path(folder)
        assets = project / 'assets/data'
        assets.mkdir(parents=True)
        (assets / 'sprite.png').write_bytes(png(3, 5))
        (assets / 'sprite.png.meta').write_text('TextureImporter:\n  nPOTScale: 2\n')
        (assets / 'broken.png').write_bytes(b'not a PNG')
        with wave.open(str(assets / 'voice.wav'), 'wb') as audio:
            audio.setnchannels(1)
            audio.setsampwidth(2)
            audio.setframerate(24000)
            audio.writeframes(b'\x00\x00' * 24000)
        (assets / 'valid.json').write_text('\ufeff{"ok":true}', encoding='utf-8')
        (assets / 'broken.json').write_text('{broken')
        before = snapshot(project)
        report = run_json(helper, 'asset-audit', '--root', assets)
        assert report['files_scanned'] == 5
        assert {row['path'] for row in report['parse_errors']} == {'broken.json', 'broken.png'}
        rows = {row['path']: row for row in report['files']}
        assert rows['sprite.png']['width'] == 3 and rows['sprite.png']['height'] == 5
        assert rows['sprite.png']['power_of_two'] is False
        assert rows['sprite.png']['alpha_channel'] is True
        assert rows['sprite.png']['unity_npot_scale'] == 2
        assert rows['voice.wav']['duration'] == 1 and rows['voice.wav']['sample_rate'] == 24000
        assert 'error' not in rows['valid.json'], 'UTF-8 BOM JSON must remain valid'
        assert report['not_assessed'], 'Measurements must retain coverage limitations'
        assert snapshot(project) == before, 'Read-only audit changed assets'

        hook = plugin / 'hooks/validate_assets.py'
        def invoke(payload, tool_name='Write'):
            event = {'hook_event_name': 'PostToolUse', 'tool_name': tool_name,
                     'cwd': str(project), 'tool_input': payload}
            return subprocess.run([sys.executable, str(hook)], input=json.dumps(event),
                                  capture_output=True, text=True, cwd=project)
        bad = invoke({'file_path': str(assets / 'broken.json')})
        assert bad.returncode == 2 and 'assets/data/broken.json' in bad.stderr, bad
        good = invoke({'file_path': str(assets / 'valid.json')})
        assert good.returncode == 0 and not good.stderr, good
        patch = invoke({'input': '*** Begin Patch\n*** Update File: assets/data/broken.json\n*** End Patch'})
        assert patch.returncode == 2 and 'broken.json' in patch.stderr, patch
        native_patch = invoke({'command': '*** Begin Patch\n*** Add File: assets/data/broken.json\n+{broken\n*** End Patch'}, 'apply_patch')
        assert native_patch.returncode == 2 and 'Asset JSON invalid' in native_patch.stderr, native_patch
        absent = invoke({'command': 'echo unrelated'})
        assert absent.returncode == 0 and 'NOT ASSESSED' in absent.stdout, absent
        assert snapshot(project) == before, 'Hook changed assets'

        # A symlink to non-asset project data must not expand this hook's scope.
        outside = project / 'outside.json'
        outside.write_text('{broken')
        linked = assets / 'linked.json'
        linked.symlink_to(outside)
        unrelated = invoke({'file_path': str(linked)})
        assert unrelated.returncode == 0 and not unrelated.stderr, unrelated
    assert snapshot(plugin) == package_before, 'Helpers/hooks modified the installed package'
    print('PASS: 49 roles, 74 native workflows, prototype/audit decisions, real PNG/WAV/JSON measurements, read-only assets/package, and hook process feedback. Codex runtime activation is a separate check.')


if __name__ == '__main__':
    main()
