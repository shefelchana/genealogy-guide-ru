#!/usr/bin/env python3
"""Write the change log pages from git history.

Creates обновления.md (Russian) and en/changelog.md (English): every commit,
grouped by date, newest first, with a link to the commit on GitHub.
build_static.py calls this first, so the pages are refreshed on every build.
Run alone from the repository root:  python3 tools/build_changelog.py
"""
import os
import re
import subprocess
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMIT = 'https://github.com/shefelchana/genealogy-guide-ru/commit/'
SKIP = re.compile(r'verification file|пустые строки|^Merge ', re.I)
MONTHS_RU = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
             'сентября', 'октября', 'ноября', 'декабря']
MONTHS_EN = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
             'September', 'October', 'November', 'December']

HEAD = {
    'ru': ('# Обновления\n\n'
           '> Все правки руководства по датам, новые сверху, — из истории коммитов репозитория. '
           'Страница собирается автоматически при каждой сборке сайта. '
           'Описание по версиям — в разделах «Что нового» на [главной странице](README.md). '
           'Сообщения коммитов — на языке правки (русском или английском).\n'),
    'en': ('# Change log\n\n'
           '> Every change to the guide by date, newest first, taken from the repository\'s commit history. '
           'The page is rebuilt automatically with the site. '
           'A summary by version is in "What\'s new" on the [main page](README.md). '
           'Commit messages are in the language of the change (Russian or English).\n'),
}


def commits():
    out = subprocess.run(['git', 'log', '--format=%cs%x09%h%x09%s'], cwd=ROOT,
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split('\t', 2)
        if len(parts) == 3 and not SKIP.search(parts[2]):
            rows.append(parts)
    return rows


def esc(text):
    return re.sub(r'([\\*_<>\[\]`])', r'\\\1', text)


def day_title(iso, lang):
    d = date.fromisoformat(iso)
    months = MONTHS_RU if lang == 'ru' else MONTHS_EN
    return f'{d.day} {months[d.month - 1]} {d.year}'


def page(rows, lang):
    lines = [HEAD[lang]]
    current = None
    for iso, short, subject in rows:
        if iso != current:
            lines.append(f'\n## {day_title(iso, lang)}\n')
            current = iso
        lines.append(f'- {esc(subject)} ([{short}]({COMMIT}{short}))')
    return '\n'.join(lines) + '\n'


def main():
    rows = commits()
    if not rows:
        return
    for lang, rel in (('ru', 'обновления.md'), ('en', 'en/changelog.md')):
        with open(os.path.join(ROOT, rel), 'w', encoding='utf-8') as fh:
            fh.write(page(rows, lang))


if __name__ == '__main__':
    main()
