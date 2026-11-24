#!/usr/bin/env python3
"""Parse a saved page of a phpBB forum topic (for example forum.j-roots.info)
that holds surname indexes to archival files.

What it does:
  * splits the page into posts (div id="pNNNN");
  * takes the post text IN FULL from the HTML, including the hidden "Show"
    spoilers (the browser's innerText skips them);
  * walks through the lines and remembers the nearest document header
    ("Фонд N, опись N, дело N" / "ф. N оп. N д. N", i.e. fond / inventory /
    file) and the nearest section header (a line in CAPITAL letters,
    usually a shtetl);
  * prints every hit of the searched surname together with the post, the
    document header, the section and the nearest full PDF link above it.

Save the page yourself first, for example:
  curl -sk -A "GenealogyGuideTool/1.0 (personal family research)" "https://forum.j-roots.info/viewtopic.php?p=NNNN" -o post.html

Usage:
  python3 forum_post_index.py post.html Surname [Surname2 ...] [--loose]

--loose  additionally searches the form without the first letter and with
         е/э and и/ы/й swapped (indexes lose letters; see SKILL.md,
         section "Traps").

Downloads nothing and makes no network requests.
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
    # turn PDF links into a separate line with the full address:
    # the visible link text on the forum is truncated ("upload.wikimedia.org/... .pdf")
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
    print("Topic:", html.unescape(title.group(1)).strip() if title else "?")

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
                    print(f"\n[{name}] post p={pid}  spoilers in post: {spoilers}")
                    print(f"  line:     {line[:160]}")
                    print(f"  document: {header}")
                    print(f"  section:  {section}")
                    print(f"  pdf:      {pdf}")
    print(f"\nTotal hits: {hits}. Check each one against the post by eye: "
          "the document header and PDF were chosen automatically as the nearest above.")


if __name__ == "__main__":
    main()
