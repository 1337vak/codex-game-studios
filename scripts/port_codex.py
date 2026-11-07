#!/usr/bin/env python3
"""Convert the pinned upstream instruction library into on-demand Codex references.

Original .claude files remain available for an auditable comparison. No upstream
hook, command injection, permission setting, or model routing is activated.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True, help='Generated skill directory')
parser.add_argument('--upstream', type=Path, required=True, help='Path to the pinned upstream Git checkout')
args = parser.parse_args()
UPSTREAM = args.upstream.resolve()
PIN = '05ad7c8a5b8aa2aa86bbd3439ae7cf7295cac418'
commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=UPSTREAM, text=True).strip()
if commit != PIN:
    raise SystemExit(f'Expected upstream {PIN}, got {commit}')
if subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=no'], cwd=UPSTREAM, text=True).strip():
    raise SystemExit('Upstream checkout has tracked modifications; use a clean checkout.')
SOURCE = UPSTREAM / '.claude'
SKILL = args.output.resolve()
REFS = SKILL / 'references'
changes = []


def split_frontmatter(text):
    match = re.match(r'\A---\s*\n(.*?)\n---\s*\n', text, re.S)
    if not match:
        return {}, text
    fields = {}
    for line in match.group(1).splitlines():
        m = re.match(r'([\w-]+):\s*(.*)', line)
        if m:
            fields[m[1]] = m[2].strip().strip('"\'')
    return fields, text[match.end():]


def adapt(text, source):
    _, text = split_frontmatter(text)
    lines = text.splitlines()
    output = []
    skip_level = None
    removed = []
    for line in lines:
        heading = re.match(r'^(#{1,6})\s+(.+)', line)
        if heading:
            level = len(heading[1])
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if re.search(r'collaborati(?:on|ve) (?:protocol|mindset)|file write protocol|how to delegate|sub.specialist orchestration|resolve config', heading[2], re.I):
                skip_level = level
                removed.append(heading[2])
        if skip_level is None:
            output.append(line)
    text = '\n'.join(output)
    # Remove transport-specific paragraphs rather than pretending they execute in
    # Codex. The native compatibility contract supplies their actual replacement.
    keep = []
    transport = re.compile(
        r'AskUserQuestion|TaskCreate|TaskGet|TaskList|TaskUpdate|TeamCreate|TeamDelete|'
        r'CLAUDE_SKILL_DIR|CLAUDE_PROJECT_DIR|!`|allowed-tools:|'
        r'bounded exception|File\s+Write\s+Protocol|May\s+I\b|said yes|ask\s+once|'
        r'user (?:must |has to )?approv|before (?:writing|editing|any.*edited).*approv|'
        r'(?:must|MUST) ask|end your turn with.*question|'
        r'\.claude/(?:hooks|scripts|settings)|'
        r'\b(?:Opus|Sonnet|Haiku)\b|subagent_type:', re.I | re.S)
    def code_block(match):
        if transport.search(match[0]):
            removed.append('Transport-specific code block: ' + match[0][:120])
            return ''
        return match[0]
    text = re.sub(r'```[\s\S]*?```', code_block, text)
    paragraphs = re.split(r'\n\s*\n', text)
    for block in paragraphs:
        if transport.search(block):
            removed.append(block[:180].replace('\n', ' '))
        else:
            keep.append(block)
    text = '\n\n'.join(keep)
    replacements = {
        '.claude/agents/': '<skill-root>/references/roles/',
        '.claude/skills/': '<skill-root>/references/workflows/',
        '.claude/docs/': '<skill-root>/references/studio/',
        '.claude/rules/': '<skill-root>/references/rules/',
        'CLAUDE.md': 'AGENTS.md',
        'Claude Code': 'Codex',
        '`Agent` tool': 'native subagent tool, when available',
        '`Read`': 'file reads', '`Glob`': '`rg --files`', '`Grep`': '`rg`',
        '`Write`': 'file writing', '`Edit`': 'patch editing',
        '`Bash`': 'shell execution',
        'use the Grep tool': 'use `rg`', 'using Glob': 'using `rg --files`',
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    text = re.sub(r'(<skill-root>/references/workflows/[^\s`\)]+?)/SKILL\.md', r'\1/WORKFLOW.md', text)
    # Slash commands are workflow names, not installed Codex slash commands.
    for name in workflow_names:
        text = re.sub(r'(?<![\w./])/' + re.escape(name) + r'(?=[\s`\]".,:)]|$)', '$game-studio ' + name, text)
    text = re.sub(r'(?m)^@([^\n]+)$', r'Read this reference only when relevant: `\1`.', text)
    text = text.replace('BEGIN ' + 'PRIVATE KEY', 'private key PEM header')
    # Remove tool-only code fences left by paragraph removal.
    if text.count('```') % 2:
        text += '\n```\n'
    changes.append({'source': str(source.relative_to(UPSTREAM)), 'removed_transport_sections': removed})
    return ('> Codex reference: use the native compatibility contract at '
            '`<skill-root>/references/compatibility.md`. This is domain guidance, '
            'not an executable agent, hook, or permission policy. Project instructions '
            'and the user\'s existing authorization take precedence.\n\n' + text.strip() + '\n')


workflow_names = sorted(p.parent.name for p in (SOURCE / 'skills').glob('*/SKILL.md'))
catalog = {'roles': [], 'workflows': []}
for folder, target, kind in [('agents', 'roles', 'roles'), ('skills', 'workflows', 'workflows'), ('docs', 'studio', None), ('rules', 'rules', None)]:
    for path in sorted((SOURCE / folder).rglob('*')):
        if not path.is_file() or path.suffix not in {'.md', '.yaml', '.yml', '.json'}:
            continue
        relative = path.relative_to(SOURCE / folder)
        dest = REFS / target / relative
        if dest.name == 'SKILL.md':
            dest = dest.with_name('WORKFLOW.md')
        dest.parent.mkdir(parents=True, exist_ok=True)
        original = path.read_text()
        fields, _ = split_frontmatter(original)
        dest.write_text(adapt(original, path) if path.suffix == '.md' else original)
        if folder == 'agents' or (folder == 'skills' and path.name == 'SKILL.md'):
            name = path.stem if folder == 'agents' else path.parent.name
            catalog[kind].append({'name': name, 'description': fields.get('description', ''), 'path': str(dest.relative_to(SKILL)), 'upstream': str(path.relative_to(UPSTREAM)), 'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest()})

shutil.copyfile(ROOT / 'LICENSE', SKILL / 'LICENSE')
provenance = {'source': 'https://github.com/Donchitos/Claude-Code-Game-Studios', 'commit': commit, 'license': 'MIT', 'copyright': 'Copyright (c) 2026 Donchitos', 'source_counts': {'roles': len(catalog['roles']), 'workflows': len(catalog['workflows'])}, 'native_entrypoints': ['game-studio'], 'note': 'Generated from the pinned upstream checkout.'}
(SKILL / 'catalog.json').write_text(json.dumps(catalog, indent=2) + '\n')
(SKILL / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
(SKILL / 'conversion-log.json').write_text(json.dumps(changes, indent=2) + '\n')
print(json.dumps({'roles': len(catalog['roles']), 'workflows': len(catalog['workflows']), 'references': len(changes), 'commit': commit}))
