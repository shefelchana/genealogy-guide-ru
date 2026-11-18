#!/usr/bin/env python3
"""Merge showcase data parts, validate them and render one interactive HTML page.

Usage:
    python3 build_showcase.py OUT.html part1.json [part2.json ...] [--forbid names.txt] [--check-only]

Each part is a JSON object with some of the top-level keys described in
references/data-schema.md (meta, lines, sources, people, profile, pedigree,
ladder, places, routes, dna, comparisons, story, surnames, library, ...).
Parts are merged: lists are concatenated, objects are merged key by key,
a scalar given twice with different values is an error.

--forbid FILE   one string per line (real names, archival references). If any
                of them occurs anywhere in the data, the build fails. Use it for
                public, anonymised versions.
--check-only    validate and print the report, do not write the page.

Exit code 0 = page written (warnings may be printed), 1 = errors.
Standard library only.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, '..', 'assets', 'showcase-template.html')
LEVELS = {'🟢', '🟡', '⚪', '💭', '🔴', 'zero', ''}
KNOWN = {'lang', 'title', 'description', 'kicker', 'lead', 'banner', 'footer', 'lines', 'sections',
         'cycle', 'methods', 'sources', 'people', 'profile', 'pedigree', 'ladder', 'places', 'routes',
         'offmap', 'dna', 'comparisons', 'story', 'surnames', 'library'}


def merge(into, part, path=''):
    for k, v in part.items():
        if k not in into:
            into[k] = v
        elif isinstance(into[k], list) and isinstance(v, list):
            into[k] = into[k] + v
        elif isinstance(into[k], dict) and isinstance(v, dict):
            merge(into[k], v, path + k + '.')
        elif into[k] != v:
            raise ValueError(f'conflicting values for "{path}{k}": {into[k]!r} vs {v!r}')


def validate(d):
    errors, warnings = [], []
    for k in d:
        if k not in KNOWN:
            warnings.append(f'unknown top-level key "{k}" is ignored by the template')
    lines = d.get('lines') or []
    ids = [l.get('id') for l in lines]
    if len(lines) > 5:
        errors.append('more than 5 lines: fold the rest into one ("other lines") — colours are fixed to 5')
    if len(set(ids)) != len(ids):
        errors.append('duplicate line ids')
    line_ids = set(ids)

    def check_line(where, v):
        if v not in line_ids and v not in (None, '', 'none'):
            errors.append(f'{where}: line "{v}" is not in "lines"')

    def check_level(where, v):
        if v is not None and v not in LEVELS:
            errors.append(f'{where}: level "{v}" — use one of 🟢 🟡 ⚪ 💭 🔴 or "zero"')

    for i, s in enumerate(d.get('sources') or []):
        w = f'sources[{i}]'
        for f in ('ref', 'type', 'who', 'gave', 'level'):
            if not s.get(f):
                errors.append(f'{w}: missing "{f}"')
        check_line(w, s.get('line'))
        check_level(w, s.get('level'))
    for i, p in enumerate(d.get('people') or []):
        w = f'people[{i}]'
        if not p.get('name'):
            errors.append(f'{w}: missing "name"')
        check_line(w, p.get('line'))
        check_level(w, p.get('level'))
    prof = d.get('profile')
    if prof:
        for i, r in enumerate(prof.get('timeline') or []):
            if not r.get('source'):
                warnings.append(f'profile.timeline[{i}] "{r.get("text", "")[:40]}" has no source')
            check_level(f'profile.timeline[{i}]', r.get('level'))
    ped = (d.get('pedigree') or {}).get('generations') or []
    for g, gen in enumerate(ped):
        if len(gen) > 2 ** g:
            errors.append(f'pedigree generation {g} has {len(gen)} people, at most {2 ** g}')
        for i, p in enumerate(gen):
            if p:
                check_line(f'pedigree[{g}][{i}]', p.get('line'))
    if len(ped) > 4:
        warnings.append('pedigree: only the first 4 generations are drawn')
    places = d.get('places') or {}
    for pid, p in places.items():
        try:
            float(p['lat']), float(p['lon'])
        except (KeyError, TypeError, ValueError):
            errors.append(f'places.{pid}: needs numeric "lat" and "lon"')
    for i, r in enumerate(d.get('routes') or []):
        check_line(f'routes[{i}]', r.get('line'))
        for pid in r.get('path') or []:
            if pid not in places:
                errors.append(f'routes[{i}]: place "{pid}" is not in "places"')
    if d.get('routes') and not places:
        errors.append('routes without places')
    dna = d.get('dna')
    if dna:
        total = sum(float(b.get('value', 0)) for b in dna.get('bars') or [])
        if total > 100.5:
            errors.append(f'dna bars add up to {total:.1f} % (> 100)')
        for i, b in enumerate(dna.get('bars') or []):
            check_line(f'dna.bars[{i}]', b.get('line'))
        if not any(b.get('expected') is not None for b in dna.get('bars') or []):
            warnings.append('dna: no bar has "expected" — the point of the format is comparing with the tree')
    for i, c in enumerate(d.get('comparisons') or []):
        n = len(c.get('columns') or [])
        for j, r in enumerate(c.get('rows') or []):
            if len(r) != n:
                errors.append(f'comparisons[{i}].rows[{j}]: {len(r)} cells, {n} columns')
        if not c.get('verdict'):
            warnings.append(f'comparisons[{i}] "{c.get("title", "")}" has no verdict')
    return errors, warnings


def forbidden_hits(d, path):
    with open(path, encoding='utf-8') as fh:
        words = [w.strip() for w in fh if w.strip() and not w.startswith('#')]
    text = json.dumps(d, ensure_ascii=False).lower()
    return [w for w in words if w.lower() in text]


def main(argv):
    args, forbid, check_only = [], None, False
    it = iter(argv)
    for a in it:
        if a == '--forbid':
            forbid = next(it)
        elif a == '--check-only':
            check_only = True
        else:
            args.append(a)
    if len(args) < 2:
        print(__doc__)
        return 1
    out, parts = args[0], args[1:]
    data = {}
    try:
        for p in parts:
            with open(p, encoding='utf-8') as fh:
                merge(data, json.load(fh))
    except (ValueError, json.JSONDecodeError) as e:
        print(f'ERROR {e}')
        return 1
    errors, warnings = validate(data)
    if forbid:
        hits = forbidden_hits(data, forbid)
        errors += [f'forbidden string found in data: "{h}"' for h in hits]
    for w in warnings:
        print('warning', w)
    for e in errors:
        print('ERROR', e)
    counts = {k: (len(v) if isinstance(v, (list, dict)) else 1) for k, v in data.items()}
    print('sections:', ', '.join(f'{k}={v}' for k, v in counts.items()))
    if errors:
        return 1
    if check_only:
        return 0
    with open(TEMPLATE, encoding='utf-8') as fh:
        html = fh.read()
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    esc = lambda s: str(s).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')
    html = (html.replace('/*DATA*/', blob)
                .replace('/*LANG*/', 'en' if data.get('lang') == 'en' else 'ru')
                .replace('/*TITLE*/', esc(data.get('title', 'Showcase')))
                .replace('/*DESCRIPTION*/', esc(data.get('description', data.get('lead', '')))[:300]))
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'written {out} ({len(html) // 1024} KB)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
