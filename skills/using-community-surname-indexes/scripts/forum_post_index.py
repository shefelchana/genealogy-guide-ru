#!/usr/bin/env python3
"""Разбор сохранённой страницы темы форума phpBB (например, forum.j-roots.info)
с фамильными указателями к архивным делам.

Что делает:
  * делит страницу на посты (div id="pNNNN");
  * берёт текст поста ЦЕЛИКОМ из HTML, включая скрытые спойлеры «Показать»
    (innerText браузера их пропускает);
  * идёт по строкам и запоминает ближайший заголовок документа
    («Фонд N, опись N, дело N» / «ф. N оп. N д. N») и ближайший заголовок
    раздела (строка ЗАГЛАВНЫМИ буквами — обычно местечко);
  * печатает каждое попадание искомой фамилии вместе с постом, заголовком
    документа, разделом и ближайшей выше полной ссылкой на PDF.

Страницу сначала сохрани сам, например:
  curl -sk -A "Mozilla/5.0 ..." "https://forum.j-roots.info/viewtopic.php?p=NNNN" -o post.html

Запуск:
  python3 forum_post_index.py post.html Фамилия [Фамилия2 ...] [--loose]

--loose  дополнительно ищет форму без первой буквы и с заменой е/э, и/ы/й
         (указатели теряют буквы; см. SKILL.md, раздел «Ловушки»).

Ничего не скачивает и в сеть не ходит.
"""
import html
import re
import sys
from urllib.parse import unquote

HEADER_RE = re.compile(
    r"(фонд|ф\.)\s*[РрPR]?-?\s*\d+[^\n]{0,40}?(опись|оп\.)\s*\d+[^\n]{0,40}?(дело|д\.)\s*\d+",
    re.I,
)
CASE_ONLY_RE = re.compile(r"^\s*(дело|д\.)\s*№?\s*\d+", re.I)
SECTION_RE = re.compile(r"^[\d,\-\s]*([А-ЯЁІЇЄҐ][А-ЯЁІЇЄҐ\-\s\.\(\)]{2,})$")


def post_text(body: str) -> str:
    # ссылки на PDF превращаем в отдельную строку с полным адресом:
    # видимый текст ссылки на форуме обрезан («upload.wikimedia.org/... .pdf»)
    body = re.sub(r'<a[^>]+href="([^"]+\.pdf[^"]*)"[^>]*>.*?</a>',
                  lambda m: "\nPDF: " + unquote(html.unescape(m.group(1))) + "\n", body, flags=re.S)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"</(div|p|li|tr|h\d)>", "\n", body)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    lines = [re.sub(r"[ \t\xa0]+", " ", l).strip() for l in text.split("\n")]
    return "\n".join(l for l in lines if l)


def variants(name: str, loose: bool):
    out = {name.lower()}
    if loose:
        low = name.lower()
        out.add(low[1:])
        out.add(low.replace("е", "э"))
        out.add(low.replace("э", "е"))
        out.add(re.sub("[иыйі]", "и", low))
    return {v for v in out if len(v) >= 3}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    loose = "--loose" in sys.argv
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    page = open(args[0], encoding="utf-8", errors="replace").read()
    names = args[1:]
    title = re.search(r"<title>(.*?)</title>", page, re.S)
    print("Тема:", html.unescape(title.group(1)).strip() if title else "?")

    parts = re.split(r'<div id="p(\d+)" class="post', page)
    hits = 0
    for i in range(1, len(parts), 2):
        pid, body = parts[i], parts[i + 1]
        spoilers = len(re.findall(r'class="spoilcontent"', body))
        header, section, pdf = "—", "—", "—"
        for line in post_text(body).split("\n"):
            if line.startswith("PDF: "):
                pdf = line[5:]
                continue
            if HEADER_RE.search(line) or CASE_ONLY_RE.search(line):
                header, pdf = line[:160], "—"
                continue
            m = SECTION_RE.match(line)
            if m and len(line) < 60:
                section = m.group(1).strip()
                continue
            low = line.lower()
            for name in names:
                if any(v in low for v in variants(name, loose)):
                    hits += 1
                    print(f"\n[{name}] пост p={pid}  спойлеров в посте: {spoilers}")
                    print(f"  строка:   {line[:160]}")
                    print(f"  документ: {header}")
                    print(f"  раздел:   {section}")
                    print(f"  pdf:      {pdf}")
    print(f"\nВсего попаданий: {hits}. Каждое сверь с постом глазами: "
          "заголовок документа и PDF выбраны автоматически как ближайшие выше.")


if __name__ == "__main__":
    main()
