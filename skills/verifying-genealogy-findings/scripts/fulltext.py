#!/usr/bin/env python3
"""Полнотекстовый поиск по genealogyindexer.org — справочники, адрес-календари,
книги памяти, именные списки потерь Первой мировой. Логина не требует.

  python3 fulltext.py Шефель --scope 19800
  python3 fulltext.py Вайнберг --scope any --match ocr --collection military
  python3 fulltext.py Людмирский --counts      # только счётчики по регионам

⚠️ Искать КИРИЛЛИЦЕЙ: русские справочники распознаны кириллицей,
латинская транслитерация по ним не ищется.
⚠️ Ноль по этому инструменту НЕ доказывает отсутствия — OCR теряет записи.
"""
import argparse, html, re, sys, urllib.parse, urllib.request

# Форма живёт на домене БЕЗ www: адрес с www отдаёт 301, и POST при этом теряется.
ENDPOINT = "https://genealogyindexer.org/"
# Сервер отдаёт форму ботам без узнаваемого UA.
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"

SCOPES = {
    "podolia": "19800", "kiev": "19500", "volhynia": "19300",
    "ukraine": "19000", "galicia": "1100", "russia": "12000",
    "empire": "17500", "any": "any",
}


def search(term, scope="any", match="regular", collection="any", date="any"):
    data = urllib.parse.urlencode({
        "term": term, "scope": SCOPES.get(scope, scope), "match": match,
        "sort": "alpha", "collection": collection, "date": date, "search": "Search",
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8", "replace")
    except Exception as exc:
        print(f"запрос не прошёл: {exc}", file=sys.stderr)
        return ""


def lines(page):
    page = re.sub(r"<(script|style|select).*?</\1>", "", page, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", page))
    return [l.strip() for l in text.split("\n") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term")
    ap.add_argument("--scope", default="any", help="|".join(SCOPES) + " или код")
    ap.add_argument("--match", default="regular", choices=["regular", "dm", "ocr"])
    ap.add_argument("--collection", default="any",
                    choices=["any", "directories", "yizkor", "military", "history", "school"])
    ap.add_argument("--date", default="any")
    ap.add_argument("--counts", action="store_true", help="только счётчики по регионам")
    a = ap.parse_args()

    page = search(a.term, a.scope, a.match, a.collection, a.date)
    if not page:
        sys.exit(1)
    L = lines(page)
    idx = [i for i, l in enumerate(L) if l == "Filter Matches"]
    L = L[(idx[0] + 1 if idx else 0):]

    counts = [l for l in L if re.match(r"^[A-Z][\w .+-]* \(~?\d+\)$", l)]
    print("── совпадений по регионам:")
    for c in dict.fromkeys(counts):
        print("   ", c)
    if a.counts:
        return

    print("── источники и фрагменты:")
    for l in L:
        if re.match(r"^\d{4} ", l):
            print("\n  ИСТОЧНИК:", l[:120])
        elif l.startswith("Original Title") or l.startswith("image "):
            print("    ", l[:120])
        elif a.term.lower() in l.lower():
            print("    »", l[:200])


if __name__ == "__main__":
    main()
