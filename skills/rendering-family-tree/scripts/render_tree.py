#!/usr/bin/env python3
"""Render a pedigree chart (and an optional line ladder) to a standalone SVG/HTML file.

Usage:
    python3 render_tree.py tree.json OUT.html     # HTML page with the SVG, light/dark aware
    python3 render_tree.py tree.json OUT.svg      # bare SVG (for print or a document)

tree.json uses the showcase keys:
  "lines":    [{"id": "a", "name": "Шапиро"}, ...]          up to 5, colours in fixed order
  "pedigree": {"generations": [[root], [father, mother], [4], [8], [16]]}
              Ahnentafel order: in generation g, positions 2i and 2i+1 are the father
              and mother of person i of generation g-1; null = unknown ("?").
              Each person: {"name": "...", "sub": "SURNAME · years", "line": "a", "level": "💭"}
  "ladder":   {"title": "...", "steps": [{"name": "...", "note": "...", "level": "🟢"}]}
Up to 5 generations are drawn. Standard library only.
"""
import html
import json
import sys

COLORS = ['#2a78d6', '#eb6834', '#1baf7a', '#6250d6', '#e87ba4']
W, H, GAP, ROW = 212, 58, 22, 71


def esc(s):
    return html.escape(str(s or ''), quote=True)


def pedigree_svg(data):
    gens = (data.get('pedigree') or {}).get('generations') or []
    gens = gens[:5]
    if not gens:
        return ''
    color = {l['id']: COLORS[i] for i, l in enumerate((data.get('lines') or [])[:5])}
    n = len(gens)
    rows = 2 ** (n - 1)
    col_w = W + GAP
    width, height = n * col_w, rows * ROW + 30
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
           f'font-family="PT Sans, Arial, sans-serif" role="img" aria-label="pedigree chart">']
    pos = []
    for g in range(n):
        cnt, span = 2 ** g, rows / 2 ** g
        pos.append([(6 + g * col_w, 8 + (i * span + span / 2) * ROW - H / 2) for i in range(cnt)])
    for g in range(n - 1):
        for i, (x, y) in enumerate(pos[g]):
            for j in (2 * i, 2 * i + 1):
                qx, qy = pos[g + 1][j]
                x1, y1, x2, y2 = x + W, y + H / 2, qx, qy + H / 2
                mx = (x1 + x2) / 2
                out.append(f'<path d="M{x1} {y1} H{mx} V{y2} H{x2}" fill="none" class="ln" stroke-width="2"/>')
    for g in range(n):
        people = gens[g] + [None] * (2 ** g - len(gens[g]))
        for (x, y), p in zip(pos[g], people):
            p = p or {'name': '?', 'sub': ''}
            dash = ' stroke-dasharray="4 4"' if p.get('name') == '?' else ''
            c = color.get(p.get('line'), '#5B6676')
            name = p['name'] + (' ' + p['level'] if p.get('level') else '')
            out.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="8" class="card"{dash}/>')
            out.append(f'<rect x="{x}" y="{y}" width="5" height="{H}" rx="2" fill="{c}"/>')
            out.append(f'<text x="{x + 14}" y="{y + 24}" font-size="14" font-weight="700" class="ink">{esc(name)}</text>')
            out.append(f'<text x="{x + 14}" y="{y + 44}" font-size="12" class="mut">{esc(p.get("sub"))}</text>')
    out.append('</svg>')
    return '\n'.join(out)


def ladder_html(data):
    lad = data.get('ladder')
    if not lad:
        return ''
    items = ''.join(f'<li><b>{i + 1}.</b> {esc(s.get("name"))} <span class="mut">{esc(s.get("note"))}</span> {esc(s.get("level"))}</li>'
                    for i, s in enumerate(lad.get('steps') or []))
    return f'<h2>{esc(lad.get("title"))}</h2><ol class="ladder">{items}</ol>'


STYLE = """
:root{--paper:#EEF1EF;--card:#FBFCFB;--ink:#18212F;--muted:#5B6676;--line:#CBD3D6}
@media (prefers-color-scheme:dark){:root{--paper:#121821;--card:#1A2230;--ink:#E6EAF0;--muted:#9AA5B5;--line:#2C3747}}
body{margin:0;padding:24px 16px;background:var(--paper);color:var(--ink);font:16px/1.5 "PT Sans",Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto}.box{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px}
svg{display:block;min-width:720px;width:100%;height:auto}.card{fill:var(--card);stroke:var(--line)}.ln{stroke:var(--line)}
.ink{fill:var(--ink)}.mut{fill:var(--muted);color:var(--muted)}.ladder{list-style:none;padding:0}.ladder li{padding:6px 0;border-bottom:1px dashed var(--line)}
"""


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 1
    with open(argv[0], encoding='utf-8') as fh:
        data = json.load(fh)
    svg = pedigree_svg(data)
    if argv[1].endswith('.svg'):
        svg = svg.replace('class="card"', 'fill="#FBFCFB" stroke="#CBD3D6"').replace('class="ln"', 'stroke="#CBD3D6"') \
                 .replace('class="ink"', 'fill="#18212F"').replace('class="mut"', 'fill="#5B6676"')
        with open(argv[1], 'w', encoding='utf-8') as fh:
            fh.write(svg)
    else:
        title = esc(data.get('title') or 'Родословная таблица')
        page = (f'<!doctype html><html lang="{esc(data.get("lang", "ru"))}"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>'
                f'<style>{STYLE}</style></head><body><div class="wrap"><h1>{title}</h1>'
                f'<div class="box">{svg}</div>{ladder_html(data)}</div></body></html>')
        with open(argv[1], 'w', encoding='utf-8') as fh:
            fh.write(page)
    print(f'written {argv[1]}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
