#!/usr/bin/env python3
"""Full-text search on genealogyindexer.org: directories, address calendars,
memorial books, name lists of First World War casualties. No login required.

  python3 fulltext.py Фейгель --scope 19800
  python3 fulltext.py Розенберг --scope any --match ocr --collection military
  python3 fulltext.py Левин --counts      # only the per-region counts

⚠️ Search in CYRILLIC: the Russian directories are recognized in Cyrillic,
a Latin transliteration will not find anything in them.
⚠️ A zero from this tool does NOT prove absence: OCR loses records.
"""
import argparse, html, re, sys, urllib.parse, urllib.request

# The form lives on the domain WITHOUT www: the www address returns a 301 and the POST is lost.
ENDPOINT = "https://genealogyindexer.org/"
# The server serves the form to bots only without a recognizable bot UA.
UA = "GenealogyGuideTool/1.0 (personal family research)"

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
        print(f"request failed: {exc}", file=sys.stderr)
        return ""


def lines(page):
    page = re.sub(r"<(script|style|select).*?</\1>", "", page, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", page))
    return [l.strip() for l in text.split("\n") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term")
    ap.add_argument("--scope", default="any", help="|".join(SCOPES) + " or a code")
    ap.add_argument("--match", default="regular", choices=["regular", "dm", "ocr"])
    ap.add_argument("--collection", default="any",
                    choices=["any", "directories", "yizkor", "military", "history", "school"])
    ap.add_argument("--date", default="any")
    ap.add_argument("--counts", action="store_true", help="only the per-region counts")
    a = ap.parse_args()

    page = search(a.term, a.scope, a.match, a.collection, a.date)
    if not page:
        sys.exit(1)
    L = lines(page)
    idx = [i for i, l in enumerate(L) if l == "Filter Matches"]
    L = L[(idx[0] + 1 if idx else 0):]

    counts = [l for l in L if re.match(r"^[A-Z][\w .+-]* \(~?\d+\)$", l)]
    print("-- matches by region:")
    for c in dict.fromkeys(counts):
        print("   ", c)
    if a.counts:
        return

    print("-- sources and fragments:")
    for l in L:
        if re.match(r"^\d{4} ", l):
            print("\n  SOURCE:", l[:120])
        elif l.startswith("Original Title") or l.startswith("image "):
            print("    ", l[:120])
        elif a.term.lower() in l.lower():
            print("    »", l[:200])


if __name__ == "__main__":
    main()
