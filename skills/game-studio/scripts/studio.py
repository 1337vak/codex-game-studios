#!/usr/bin/env python3
"""Dependency-free studio discovery and read-only asset observations."""
import argparse
import json
import re
import struct
import sys
import wave
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]


def catalog(query):
    data = json.loads((SKILL / 'catalog.json').read_text())
    terms = query.lower().split()
    entries = []
    curated = {'asset-audit': 'references/asset-audit.md', 'team-polish': 'references/polish.md', 'art-bible': 'references/visual-review.md', 'technical-artist': 'references/visual-review.md', 'art-director': 'references/visual-review.md'}
    for group, rows in data.items():
        for row in rows:
            if all(t in (row['name'] + ' ' + row['description']).lower() for t in terms):
                item = dict(row, kind=group)
                item['absolute_path'] = str(SKILL / row['path'])
                if row['name'] in curated:
                    item['native_guide'] = str(SKILL / curated[row['name']])
                entries.append(item)
    return {'matches': entries}


def inspect(project):
    root = Path(project).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Project must be a directory')
    engines = []
    excludes = {'.git', 'Library', 'Temp', 'node_modules', 'build', 'Build', '.venv'}
    for file in root.rglob('ProjectVersion.txt'):
        if not any(p in excludes for p in file.relative_to(root).parts):
            engines.append({'engine': 'Unity', 'project': str(file.parent.parent), 'version_evidence': file.read_text().strip()})
    for file in root.rglob('project.godot'):
        if not any(p in excludes for p in file.relative_to(root).parts):
            engines.append({'engine': 'Godot', 'project': str(file.parent), 'version': 'Inspect installed editor; project format does not prove editor version'})
    for file in root.rglob('*.uproject'):
        if not any(p in excludes for p in file.relative_to(root).parts):
            engines.append({'engine': 'Unreal', 'project': str(file.parent), 'descriptor': str(file)})
    return {'project': str(root), 'engines': engines, 'project_instructions': str(root / 'AGENTS.md') if (root / 'AGENTS.md').is_file() else None, 'note': 'Project metadata is evidence of the project pin; installed engine versions require a separate check.'}


def audit(root):
    root = Path(root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Asset root must be a directory')
    files = []
    errors = []
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix.lower() not in {'.png', '.wav', '.json'}:
            continue
        record = {'path': str(p.relative_to(root)), 'bytes': p.stat().st_size, 'format': p.suffix[1:].lower()}
        try:
            if p.suffix.lower() == '.png':
                with p.open('rb') as handle:
                    h = handle.read(33)
                if h[:8] != b'\x89PNG\r\n\x1a\n' or h[12:16] != b'IHDR':
                    raise ValueError('Invalid PNG signature/IHDR')
                width, height, depth, color = struct.unpack('>IIBB', h[16:26])
                record.update(width=width, height=height, bit_depth=depth, alpha_channel=color in {4, 6}, power_of_two=width > 0 and height > 0 and width & (width - 1) == 0 and height & (height - 1) == 0)
                meta = p.with_name(p.name + '.meta')
                if meta.is_file():
                    source = meta.read_text()
                    found = re.search(r'^\s*nPOTScale:\s*(\d+)', source, re.M)
                    record['unity_npot_scale'] = int(found[1]) if found else None
                    record['unity_meta'] = str(meta.relative_to(root))
            elif p.suffix.lower() == '.wav':
                with wave.open(str(p)) as w:
                    record.update(channels=w.getnchannels(), sample_rate=w.getframerate(), sample_width_bytes=w.getsampwidth(), frames=w.getnframes(), duration=w.getnframes()/w.getframerate())
            elif p.suffix.lower() == '.json':
                content = json.loads(p.read_text())
                record['json_type'] = type(content).__name__
                record['schema_validation'] = 'Not assessed; no schema supplied'
        except (ValueError, OSError, EOFError, struct.error, wave.Error) as exc:
            record['error'] = str(exc)
            errors.append({'path': record['path'], 'error': str(exc)})
        files.append(record)
    return {'root': str(root), 'files_scanned': len(files), 'files': files, 'parse_errors': errors, 'not_assessed': ['Naming and size budgets unless a project standard is supplied', 'Runtime appearance, motion and audio audition', 'Complete Unity reference graph and orphan status', 'PNG indexed transparency chunks; alpha_channel reports IHDR channel type only'], 'note': 'Measurements only. Non-power-of-two images are not automatically defects. No asset was changed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    c = sub.add_parser('catalog'); c.add_argument('query', nargs='*')
    i = sub.add_parser('inspect'); i.add_argument('--project', required=True)
    a = sub.add_parser('asset-audit'); a.add_argument('--root', required=True); a.add_argument('--output')
    args = parser.parse_args()
    if args.command == 'catalog': result = catalog(' '.join(args.query))
    elif args.command == 'inspect': result = inspect(args.project)
    else: result = audit(args.root)
    payload = json.dumps(result, indent=2) + '\n'
    if getattr(args, 'output', None):
        output = Path(args.output).expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('x') as handle:
            handle.write(payload)
        print(json.dumps({'report': str(output.resolve()), 'files_scanned': result['files_scanned'], 'parse_errors': len(result['parse_errors'])}))
    else:
        print(payload, end='')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(2)
