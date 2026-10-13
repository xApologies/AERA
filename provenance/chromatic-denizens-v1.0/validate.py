"""Read-only Chromatic Denizens v1.0 publication checks (Python 3 standard library).

Run --local-bytes before publication; --staged checks the actual index.
--repo and --overlay allow a read-only preview of prepared files over the baseline.
This frozen release validator supplements, not replaces, the reverse semantic audit.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse
import difflib
import hashlib
import json
import posixpath
import re
import subprocess

BASE = '40e3482b9ea8339ad2c6a9166f3324fa30f42a12'
ARCHIVE = 'provenance/chromatic-denizens-v1.0/'
EDITED = {'FRAMEWORK_INDEX.md', 'L2/README.md', 'L2/GENESIS_BIOLOGY.md',
          'CHANGELOG.md', 'NEXT_THREAD_HANDOFF.md'}
PAYLOADS = {
    'L2/BIOLOGY/00_READ_FIRST.md', 'L2/BIOLOGY/01_VAELITH.md',
    'L2/BIOLOGY/02_SPRITES.md', 'L2/BIOLOGY/03_BLACK_SPRITE_CRYSTAL.md',
    'L2/BIOLOGY/04_MIGRATION_BOUNDARIES.md',
    'provenance/CHROMATIC_DENIZENS_DECISION_RECORD_v1.0.md',
    'visuals/chromatic_denizens/VAELITH_ACCEPTED_CONCEPT.png',
    'visuals/chromatic_denizens/SPRITE_NATIVE_AND_BLACK_REFERENCE.jpg',
    'visuals/chromatic_denizens/BLACK_SPRITE_CRYSTAL_LOCKED.jpg',
}
ADDED = PAYLOADS | {
    'visuals/chromatic_denizens/README.md',
    'provenance/CHROMATIC_DENIZENS_PUBLICATION_AUDIT_v1.0.md',
    ARCHIVE + 'Executable.md', ARCHIVE + 'MANIFEST.json',
    ARCHIVE + 'PRESERVATION_BASELINE.json', ARCHIVE + 'validate.py',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def anchors(text):
    found, counts = set(), {}
    fenced = False
    for line in text.splitlines():
        if re.match(r'^\s*(\x60{3}|~~~)', line):
            fenced = not fenced
            continue
        if fenced:
            continue
        heading = re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not heading:
            continue
        value = re.sub(r'<[^>]*>', '', heading.group(1)).lower()
        slug = re.sub(r'[^\w\- ]', '', value).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(slug if not count else f'{slug}-{count}')
    return found


def links(md, files):
    broken, count = set(), 0
    for path, content in md.items():
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            target = target.strip('<>')
            parts = urlsplit(target)
            if parts.scheme or target.startswith('//'):
                continue
            rel = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(parts.path))) if parts.path else path
            if rel not in files and not any(p.startswith(rel.rstrip('/') + '/') for p in files):
                broken.add((path, target))
            elif parts.fragment and rel in md and unquote(parts.fragment) not in anchors(md[rel]):
                broken.add((path, target))
            count += 1
    return broken, count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument('--overlay', type=Path)
    ap.add_argument('--staged', action='store_true')
    ap.add_argument('--local-bytes', action='store_true')
    args = ap.parse_args()
    root = args.repo.resolve()
    assert not (args.staged and (args.overlay or args.local_bytes))

    def git(*items):
        return subprocess.check_output(['git', *items], cwd=root)

    def git_blobs(refs):
        names = list(refs)
        if not names:
            return {}
        proc = subprocess.run(['git', 'cat-file', '--batch'], cwd=root,
                              input=('\n'.join(names)+'\n').encode(),
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        output, offset, result = proc.stdout, 0, {}
        for name in names:
            end = output.index(b'\n', offset)
            header = output[offset:end].split()
            assert len(header) == 3 and header[1] == b'blob', (name, header)
            size = int(header[2])
            offset = end + 1
            result[name] = output[offset:offset+size]
            assert output[offset+size:offset+size+1] == b'\n'
            offset += size + 1
        assert offset == len(output)
        return result

    assert not git('ls-files', '-u'), 'Unmerged entries'
    oldfiles = set(git('ls-tree', '-r', '--name-only', BASE).decode().splitlines())
    assert len(oldfiles) == 119
    gitpaths = ('ls-files', '-z') if args.staged else ('ls-files', '-z', '--cached', '--others', '--exclude-standard')
    files = set(git(*gitpaths).decode().strip('\0').split('\0'))
    overlay = args.overlay.resolve() if args.overlay else None
    overlay_files = {p.relative_to(overlay).as_posix() for p in overlay.rglob('*') if p.is_file()} if overlay else set()
    files |= overlay_files
    assert oldfiles <= files, 'Prior path removed'
    assert files-oldfiles == ADDED, f'New-file scope mismatch: {(files-oldfiles)^ADDED}'
    assert all('_inbox' not in Path(p).parts and not p.lower().endswith('.zip') for p in files)
    old_blobs = git_blobs(BASE + ':' + p for p in sorted(oldfiles))
    prior = {p: old_blobs[BASE + ':' + p] for p in oldfiles}
    if args.staged:
        staged = git_blobs(':' + p for p in sorted(files))
        current = {p: staged[':' + p] for p in files}
    else:
        current = {p: ((overlay/p) if p in overlay_files else (root/p)).read_bytes() for p in files}
    snapshot = json.loads(current[ARCHIVE+'PRESERVATION_BASELINE.json'])
    assert snapshot['baseline'] == BASE
    before = {r['path']: r for r in snapshot['files']}
    assert set(before) == oldfiles
    for p in oldfiles:
        old, now, recorded = prior[p], current[p], before[p]
        assert sha(old) == recorded['git_sha256'] and len(old) == recorded['git_bytes'], p
        if p in EDITED:
            oldlines = normalized(old).decode('utf-8').splitlines()
            newlines = normalized(now).decode('utf-8').splitlines()
            changes = difflib.SequenceMatcher(a=oldlines, b=newlines, autojunk=False).get_opcodes()
            assert all(tag in {'equal','insert'} for tag,*_ in changes), f'Previous text altered: {p}'
            assert oldlines != newlines, f'Expected addition absent: {p}'
        else:
            textual = Path(p).suffix.lower() in {'.md','.json','.txt','.csv','.py','.yml','.yaml'} or p in {'.gitattributes','.gitignore'}
            equal = now == old if args.staged or not textual else normalized(now) == normalized(old)
            assert equal, f'Protected Git content changed: {p}'
            if args.local_bytes:
                assert sha(now) == recorded['sha256'] and len(now) == recorded['bytes'], f'Protected local bytes changed: {p}'

    manifest_data = current[ARCHIVE+'MANIFEST.json']
    assert sha(manifest_data) == '360568d11d3cd554f1b20decac19241adf9636a96ff4bc5efc834dd778b4ec0b'
    assert sha(current[ARCHIVE+'Executable.md']) == 'e99f1fac342881627007d8e565d0da7ec8a85419f01f3b9fa4f45933d1b3460c'
    manifest = json.loads(manifest_data)
    assert manifest['target'] == 'https://github.com/xApologies/AERA'
    assert len(manifest['files']) == 9
    assert {e['path'].removeprefix('payload/') for e in manifest['files']} == PAYLOADS
    for entry in manifest['files']:
        path = entry['path'].removeprefix('payload/')
        assert len(current[path]) == entry['size'] and sha(current[path]) == entry['sha256'], f'Payload changed: {path}'

    md = {p: b.decode('utf-8') for p,b in current.items() if p.endswith('.md')}
    oldmd = {p: b.decode('utf-8') for p,b in prior.items() if p.endswith('.md')}
    for path, content in md.items():
        assert '\ufffd' not in content, path
        assert not any(ord(c) < 32 and c not in '\r\n\t' for c in content), path
        assert not re.search(r'^(?:<<<<<<< |=======\s*$|>>>>>>> )',content,re.M), path
    oldbroken, _ = links(oldmd, oldfiles)
    broken, link_count = links(md, files)
    assert not broken-oldbroken, f'New broken local links: {sorted(broken-oldbroken)}'

    intro = md['L2/BIOLOGY/00_READ_FIRST.md']
    mapping = [(c,re.sub(r'\*','',n).strip()) for c,n in re.findall(
        r'^\| (Red|Orange|Yellow|Green|Blue|Violet) \| ([^|]+) \|',intro,re.M)]
    assert len(mapping) == 6
    assert [c for c,_ in mapping] == ['Red','Orange','Yellow','Green','Blue','Violet']
    for (_,actual), expected in zip(mapping,['Dragons','Vaelith','Primordials','Sprites','Leviathans','Unicorns']):
        assert actual.startswith(expected), (actual,expected)
    assert 'White is their superposition' in intro and 'Authors may substitute' in intro
    assert 'process' in intro.lower() and 'not necessarily aquatic' in intro
    sprite = md['L2/BIOLOGY/02_SPRITES.md']
    assert all(s in sprite for s in ('not actual combustion','dark-gray recursive shadow',
        'Green dominates','genuine tree','genuine dragon','locally admissible',
        'not a green glowing shadow imitation','not automatically ELDRIS',
        'does not automatically grant','not Green-dominant leakage'))
    vaelith = md['L2/BIOLOGY/01_VAELITH.md']
    assert all(s in vaelith for s in ('not one indispensable core','not armor plating',
        'No head ribbons/tendrils','NOT accepted','not necessarily individually conscious'))
    crystal = md['L2/BIOLOGY/03_BLACK_SPRITE_CRYSTAL.md']
    assert all(s in crystal for s in ('not canonically locked','proposed replacement',
        'until explicitly changed','seemingly static / suspended','does not project as free exterior flames'))
    for p in ('L2/GENESIS_BIOLOGY.md','NEXT_THREAD_HANDOFF.md'):
        text = md[p]
        assert all(s in text for s in ('Vaelith','Sprite','Process','proposed, not enacted','White'))
    assert 'BIOLOGY/00_READ_FIRST.md' in md['L2/README.md']
    assert 'L2/BIOLOGY/00_READ_FIRST.md' in md['FRAMEWORK_INDEX.md']
    new_prose = '\n'.join(md[p] for p in PAYLOADS if p.endswith('.md'))
    assert not re.search(r'\bVaelithe\b',new_prose)
    audit = md['provenance/CHROMATIC_DENIZENS_PUBLICATION_AUDIT_v1.0.md']
    ids = re.findall(r'^\| CD-(\d\d) \|',audit,re.M)
    assert ids == [f'{i:02}' for i in range(1,29)]

    manuscripts = sorted(p for p in oldfiles if re.match(r'^prophecies/0[1-8]_',p))
    examples = sorted(p for p in oldfiles if p.startswith('examples/MK231/'))
    assert len(manuscripts) == 8 and len(examples) == 5
    assert not any(re.search(r'\b(?:phoenix|eggs?)\b',md[p],re.I) for p in manuscripts)
    assert 'Black Phoenix Egg' in md['PROPHECIES.md'], 'Historical story account lost'
    for p in manuscripts + examples + ['CONSTITUTION.md','chat-thread/CHAT_THREAD_CONSTITUTION.md']:
        assert (current[p] == prior[p]) if args.staged else (sha(current[p]) == before[p]['sha256']), p

    # Preserve the exact author payload, including its one supplied trailing space.
    # Accept only this exact diagnostic/content; all other whitespace errors fail.
    source_line = intro.splitlines()[17]
    assert source_line.endswith('species. ')
    expected_whitespace = ('L2/BIOLOGY/00_READ_FIRST.md:18: trailing whitespace.\n'
                           + '+' + source_line + '\n')

    def diff_check(staged=False):
        command = ['git', 'diff'] + (['--cached'] if staged else []) + ['--check']
        result = subprocess.run(command, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            assert result.returncode in {1,2}, result.stderr.decode('utf-8')
            assert normalized(result.stdout).decode('utf-8') == expected_whitespace, result.stdout.decode('utf-8')
            assert not result.stderr, result.stderr.decode('utf-8')

    diff_check()
    if args.staged:
        diff_check(staged=True)
        changed = set(git('diff','--cached','--name-only',BASE).decode().splitlines())
        assert changed == EDITED | ADDED, 'Staged scope mismatch'
    print(json.dumps({
        'result':'PASS','mode':'staged' if args.staged else 'overlay' if overlay else 'working',
        'baseline_files_retained':len(oldfiles),'protected_unchanged_files':len(oldfiles)-len(EDITED),
        'additive_existing_files':len(EDITED),'new_files':len(ADDED),'exact_payload_files':len(PAYLOADS),
        'unchanged_prophecy_manuscripts':len(manuscripts),'unchanged_mk231_examples':len(examples),
        'unchanged_constitutions':2,'exact_reference_images':3,'semantic_groups':len(ids),
        'markdown_files':len(md),'local_links_and_fragments':link_count,
        'preexisting_broken_links':sorted(broken),'new_broken_links':0,
        'retained_source_whitespace':['L2/BIOLOGY/00_READ_FIRST.md:18 (original trailing space; exact manifest hash retained)'],
        'original_local_bytes_checked':args.local_bytes
    },indent=2))


if __name__ == '__main__':
    main()
