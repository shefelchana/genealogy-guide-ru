#!/usr/bin/env python3
"""Expected ethnicity shares from a documented tree, with the usual spread.

Usage:
    python3 expected_share.py tree.json [--test test.json] [--json]

tree.json:
{
  "tested": "Елена Петровна",
  "ancestors": [
    {"name": "Иван Савельев", "generation": 2, "origin": {"Русские": 1}},
    {"name": "Анна Михайловна", "generation": 2, "origin": {"Русские": 1}},
    {"name": "Остап Ткаченко", "generation": 2, "origin": {"Восточноевропейцы": 1}},
    {"name": "Ганна", "generation": 2, "origin": {"Восточноевропейцы": 1}}
  ],
  "legend": {"name": "Анна Михайловна", "origin": {"Восточноевропейцы": 1}}
}
generation: 1 = parent, 2 = grandparent, 3 = great-grandparent, 4, 5 ...
List every ancestor of ONE generation (or mix generations, but do not list
someone together with their own parents). "origin" fractions per ancestor add up to 1;
use the same component names as the test company does.
"legend" (optional): the same ancestor with the origin the family story claims;
the script then also gives the expectation if the legend were true ("alt").

test.json (optional): {"Русские": 44.8, "Восточноевропейцы": 46.3, ...}
The script prints observed − expected in units of the spread.

The spread is approximate: an individual's share from one ancestor varies
around the mean (parent: none; grandparent ≈ ±3.3 pp; great-grandparent ≈ ±3;
2× great ≈ ±2; deeper ≈ ±1.2). Spreads of independent ancestors add as
squares. Company models add their own error on top; shares under 2–5 % are noise.
Standard library only.
"""
import json
import math
import sys

SD = {1: 0.0, 2: 3.3, 3: 3.0, 4: 2.0}


def sd_for(gen):
    return SD.get(gen, 1.2)


def expect(ancestors):
    mean, var = {}, {}
    for a in ancestors:
        g = int(a['generation'])
        share = 100 * 0.5 ** g
        for comp, frac in a['origin'].items():
            mean[comp] = mean.get(comp, 0) + share * frac
            var[comp] = var.get(comp, 0) + (sd_for(g) * frac) ** 2
    return {c: (round(mean[c], 1), round(math.sqrt(var[c]), 1)) for c in mean}


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    with open(argv[0], encoding='utf-8') as fh:
        tree = json.load(fh)
    test = {}
    if '--test' in argv:
        with open(argv[argv.index('--test') + 1], encoding='utf-8') as fh:
            test = json.load(fh)
    anc = tree['ancestors']
    covered = sum(100 * 0.5 ** int(a['generation']) for a in anc)
    base = expect(anc)
    alt = None
    if tree.get('legend'):
        leg = tree['legend']
        alt_anc = [dict(a, origin=leg['origin']) if a['name'] == leg['name'] else a for a in anc]
        if not any(a['name'] == leg['name'] for a in anc):
            print(f'warning: legend ancestor "{leg["name"]}" is not in the list')
        alt = expect(alt_anc)
    comps = sorted(set(base) | set(alt or {}) | set(test), key=lambda c: -base.get(c, (0, 0))[0])
    if abs(covered - 100) > 0.5:
        print(f'warning: listed ancestors cover {covered:.1f} % of the tree, not 100 %')
    rows = []
    for c in comps:
        m, s = base.get(c, (0.0, 0.0))
        row = {'name': c, 'expected': m, 'sd': s}
        if alt:
            row['alt'] = alt.get(c, (0.0, 0.0))[0]
        if c in test:
            row['value'] = test[c]
            row['z'] = round((test[c] - m) / s, 1) if s else None
        rows.append(row)
    if '--json' in argv:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0
    print(f'tested: {tree.get("tested", "?")}')
    for r in rows:
        line = f'{r["name"]:<28} expected {r["expected"]:5.1f} ± {r["sd"]:.1f}'
        if 'alt' in r:
            line += f'   if legend true {r["alt"]:5.1f}'
        if 'value' in r:
            z = '' if r['z'] is None else f'  ({r["z"]:+.1f} spreads)'
            line += f'   observed {r["value"]:5.1f}{z}'
        print(line)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
