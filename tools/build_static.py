#!/usr/bin/env python3
"""Build static HTML pages and sitemap.xml for search engines.

The guide is read through docsify (index.html, hash URLs like #/guide/...).
Search engines treat hash URLs as one page, so this script renders every
content .md file to a plain .html file next to it, with its own <title>,
meta description, canonical URL and ru/en alternates, plus sitemap.xml.

Run from the repository root after editing the guide:
    pip install markdown          # once
    python3 tools/build_static.py

Generated files: <same path>.html for each page (README.md -> index.html;
the root README.md -> home.html, because index.html is docsify), sitemap.xml.
Do not edit generated .html by hand: edit the .md and rebuild.
"""
import html
import os
import re
import subprocess
import sys
import unicodedata
from datetime import date
from urllib.parse import quote

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://shefelchana.github.io/genealogy-guide-ru/'
REPO = 'https://github.com/shefelchana/genealogy-guide-ru/blob/main/'
INCLUDE = ['README.md', 'about.md', 'guide', 'catalog', 'reading', 'examples', 'templates',
           'en/README.md', 'en/about.md', 'en/GLOSSARY.md', 'en/guide', 'en/catalog', 'en/reading',
           'en/examples', 'en/templates', 'en/articles']
SITE = {'ru': 'Поиск предков', 'en': 'Tracing Your Ancestors'}
UI = {
    'ru': {'home': 'Поиск предков', 'interactive': 'Открыть в интерактивной версии', 'other': 'English',
           'license': 'Текст — CC BY 4.0. Составитель — Анна Шефель.', 'contents': 'Оглавление',
           'skills': 'Навыки для ИИ-агентов'},
    'en': {'home': 'Tracing Your Ancestors', 'interactive': 'Open in the interactive version', 'other': 'Русский',
           'license': 'Text — CC BY 4.0. Compiled by Anna Shefel.', 'contents': 'Contents',
           'skills': 'Skills for AI agents'},
}


def collect():
    files = []
    for item in INCLUDE:
        p = os.path.join(ROOT, item)
        if os.path.isfile(p):
            files.append(item)
        elif os.path.isdir(p):
            for d, _, fs in os.walk(p):
                for f in sorted(fs):
                    if f.endswith('.md') and not f.startswith('_'):
                        files.append(os.path.relpath(os.path.join(d, f), ROOT))
    return sorted(set(f.replace(os.sep, '/') for f in files))


def out_path(md):
    if md == 'README.md':
        return 'home.html'
    if md.endswith('README.md'):
        return md[:-len('README.md')] + 'index.html'
    return md[:-3] + '.html'


def url_of(rel):
    return BASE + quote(rel)


def lang_of(md):
    return 'en' if md.startswith('en/') else 'ru'


def pathmap():
    pairs = {}
    p = os.path.join(ROOT, 'en', 'PATHMAP.tsv')
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            parts = line.rstrip('\n').split('\t')
            if len(parts) == 2 and not parts[0].startswith('('):
                pairs[parts[0]] = parts[1]
                pairs[parts[1]] = parts[0]
    return pairs


def slugify(value, separator='-'):
    value = unicodedata.normalize('NFKC', value).strip().lower()
    value = re.sub(r'[^\w\s-]', '', value, flags=re.U)
    return re.sub(r'[\s_-]+', separator, value, flags=re.U).strip('-')


def plain(md_text):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md_text)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'[*_`>#|]', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def describe(text):
    """First ordinary paragraph after the H1, about 155 characters."""
    body = re.split(r'^# .*$', text, maxsplit=1, flags=re.M)
    body = body[1] if len(body) > 1 else text
    for para in re.split(r'\n\s*\n', body):
        p = para.strip()
        if not p or p.startswith(('#', '|', '-', '*', '>', '```', '<', '!', '1.')):
            continue
        s = plain(p)
        s = re.sub(r'^(О чём раздел|What this section covers|Что в разделе)\s*:\s*', '', s)
        s = s[:1].upper() + s[1:]
        if len(s) < 40:
            continue
        if len(s) > 158:
            s = s[:155].rsplit(' ', 1)[0].rstrip(',;:—–-') + '…'
        return s
    return ''


def title_of(text, md):
    m = re.search(r'^# (.+)$', text, flags=re.M)
    t = plain(m.group(1)) if m else os.path.basename(md)[:-3]
    return t


def normalize_lists(text):
    """docsify (marked) accepts lists right after a paragraph and 2-space nesting;
    Python-Markdown needs a blank line before a list and 4-space nesting."""
    out, prev, fence = [], '', False
    item = re.compile(r'^(\s*)([-*+]|\d+[.)])\s+')
    for line in text.split('\n'):
        if line.strip().startswith('```'):
            fence = not fence
        if not fence:
            m = item.match(line)
            if m:
                n = len(m.group(1).expandtabs(4))
                if n and n % 4:
                    line = ' ' * (n * 2) + line.lstrip()
                if prev.strip() and not item.match(prev) and not prev.lstrip().startswith(('|', '>')) and n == 0:
                    out.append('')
        out.append(line)
        prev = line
    return '\n'.join(out)


def rewrite_links(htm, md, pages):
    src_dir = os.path.dirname(md)

    def target_for(href):
        if re.match(r'^(https?:|mailto:|#(?!/))', href):
            return None
        frag = ''
        if '#' in href and not href.startswith('#/'):
            href, frag = href.split('#', 1)
            frag = '#' + frag
        if href.startswith('#/'):
            path = href[2:]
        elif href.startswith('/'):
            path = href[1:]
        else:
            path = os.path.normpath(os.path.join(src_dir, href)).replace(os.sep, '/')
        path = path.split('?')[0]
        if path in ('', '.'):
            path = 'README.md'
        if path.endswith('/'):
            path += 'README.md'
        if not path.endswith('.md') and (path + '/README.md') in pages:
            path += '/README.md'
        if path in pages:
            target = out_path(path)
            rel = os.path.relpath(target, src_dir or '.').replace(os.sep, '/')
            return quote(rel) + frag
        if os.path.exists(os.path.join(ROOT, path)):
            return REPO + quote(path) + frag
        return None

    def sub(m):
        new = target_for(html.unescape(m.group(2)))
        return m.group(1) + (html.escape(new, quote=True) if new else m.group(2)) + m.group(3)

    return re.sub(r'(<a href=")([^"]+)(")', sub, htm)


CSS = """
:root{--ink:#1F3454;--muted:#5a6475;--gold:#9a6b25;--paper:#fbf9f4;--line:#e3dccd;--code:#f3efe6}
@media (prefers-color-scheme:dark){:root{--ink:#e6e9ef;--muted:#a9b1bf;--gold:#d6a75a;--paper:#16191f;--line:#2c313b;--code:#1f232b}}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
header,main,footer{max-width:860px;margin:0 auto;padding:0 20px}
header{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;justify-content:space-between;padding-top:18px;padding-bottom:14px;border-bottom:1px solid var(--line);font-size:15px}
header a{color:var(--ink);text-decoration:none}header .site{font-weight:700;font-family:Georgia,serif;font-size:19px}
nav a{margin-left:14px;color:var(--gold)}main{padding-top:10px;padding-bottom:40px;overflow-wrap:anywhere}html,body{max-width:100%}
h1,h2,h3{font-family:Georgia,"Times New Roman",serif;line-height:1.25}h1{font-size:32px;margin:22px 0 14px}
a{color:var(--gold)}code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:.92em}
pre{background:var(--code);padding:12px;border-radius:8px;overflow:auto}pre code{padding:0}
blockquote{margin:16px 0;padding:6px 16px;border-left:4px solid var(--gold);background:var(--code);border-radius:6px}
.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px}
th,td{border:1px solid var(--line);padding:6px 9px;vertical-align:top;text-align:left;overflow-wrap:normal;min-width:6em}th{background:var(--code)}
img{max-width:100%}footer{border-top:1px solid var(--line);padding-top:14px;padding-bottom:30px;color:var(--muted);font-size:14px}
"""


def render(md, pages, pairs, today):
    text = open(os.path.join(ROOT, md), encoding='utf-8').read()
    lang = lang_of(md)
    ui = UI[lang]
    title = title_of(text, md)
    desc = describe(text) or title
    conv = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists', 'toc'],
                             extension_configs={'toc': {'slugify': slugify}})
    body = conv.convert(normalize_lists(text))
    body = rewrite_links(body, md, pages)
    body = re.sub(r'<table>', '<div class="table-wrap"><table>', body).replace('</table>', '</table></div>')
    out = out_path(md)
    depth = out.count('/')
    up = '../' * depth
    home = up + ('en/index.html' if lang == 'en' else 'home.html')
    alts = [(lang, url_of(out))]
    other = pairs.get(md)
    other_link = ''
    if other and other in pages:
        olang = lang_of(other)
        alts.append((olang, url_of(out_path(other))))
        other_link = f'<a href="{up}{quote(out_path(other))}" hreflang="{olang}">{ui["other"]}</a>'
    alt_tags = '\n'.join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alts)
    if len(alts) > 1:
        ru_url = dict(alts).get('ru')
        alt_tags += f'\n<link rel="alternate" hreflang="x-default" href="{ru_url}">'
    hash_path = md if not md.endswith('README.md') else md[:-len('README.md')]
    interactive = f'{up}index.html#/{quote(hash_path)}'
    full_title = title if (SITE[lang].lower() in title.lower() or len(title) > 55) else f'{title} — {SITE[lang]}'
    skills = up + quote(out_path('en/guide/1-ai-search/06-skills.md' if lang == 'en' else 'guide/1-поиск-с-ии/06-навыки.md'))
    page = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{url_of(out)}">
{alt_tags}
<meta property="og:title" content="{html.escape(full_title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:url" content="{url_of(out)}">
<meta property="og:type" content="article">
<style>{CSS}</style>
</head>
<body>
<header><a class="site" href="{home}">{ui['home']}</a>
<nav>{other_link}<a href="{skills}">{ui['skills']}</a><a href="{interactive}">{ui['interactive']}</a></nav></header>
<main>
{body}
</main>
<footer>{ui['license']} <a href="{REPO.replace('/blob/main/', '')}">GitHub</a></footer>
</body>
</html>
"""
    with open(os.path.join(ROOT, out), 'w', encoding='utf-8') as fh:
        fh.write(page)
    return out


def lastmod(md):
    try:
        d = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', md], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
        return d or date.today().isoformat()
    except OSError:
        return date.today().isoformat()


def main():
    pages = collect()
    pairs = pathmap()
    today = date.today().isoformat()
    outs = []
    for md in pages:
        outs.append((render(md, set(pages), pairs, today), md))
    urls = [f'<url><loc>{BASE}</loc><lastmod>{today}</lastmod></url>']
    for out, md in sorted(outs):
        urls.append(f'<url><loc>{url_of(out)}</loc><lastmod>{lastmod(md)}</lastmod></url>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                 + '\n'.join(urls) + '\n</urlset>\n')
    print(f'{len(outs)} pages, sitemap.xml with {len(urls)} URLs')


if __name__ == '__main__':
    sys.exit(main())
