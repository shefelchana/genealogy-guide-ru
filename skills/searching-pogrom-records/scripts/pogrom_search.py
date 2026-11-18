#!/usr/bin/env python3
"""Search two open databases of victims and sufferers of the 1917-1921 pogroms
without a browser. Prints a table (TSV) and the number of records found.

1) jewishpogroms.info (N. Lipes's database, ~77,777 records; Latin-letter search only)
   python3 pogrom_search.py lipes Rabinovich
   python3 pogrom_search.py lipes "Rabin*"            # asterisk = any letters
   python3 pogrom_search.py lipes Rabinovich --soundslike
   python3 pogrom_search.py lipes "" --city Pavoloch  # all records for a city

2) pogrom.amhazikaron.org (Am HaZikaron, ~7,900 victims; substring search, Cyrillic)
   python3 pogrom_search.py amh Проскуров
   python3 pogrom_search.py amh Рабинович --all      # all pages, not just the first 100

Courtesy: one database - one worker; a pause between requests (3 s by default).
The script does not bypass CAPTCHAs and does not log in to accounts. A response that
does not look like a table (a placeholder page, 403/429) is printed as an ERROR - it
is not "0 found".
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0 Safari/537.36")
LIPES_URL = "https://jewishpogroms.info/wp-admin/admin-ajax.php"
AMH_URL = "https://pogrom.amhazikaron.org/wp-json/wp/v2/victims"
FIELDS = ["Region", "City", "Record type", "Family name", "Name", "Patronymic", "Age",
          "Incident", "Is Alive", "Notes", "Found", "Register", "Case", "Page", "Archive"]


def fetch(url, data=None, headers=False):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read().decode("utf-8", errors="replace")
        return (body, dict(r.headers)) if headers else body


def lipes(surname, soundslike=False, city=None):
    form = {"action": "pogroms_search", "family_name": surname}
    if soundslike:
        form["soundslike"] = "yes"
    if city:
        form["city"] = city
    body = fetch(LIPES_URL, urllib.parse.urlencode(form).encode())
    m = re.search(r"pogroms-persons-info'>([^<]*)<", body)
    if not m:
        print("ERROR: the response does not look like a results table:", body[:200].replace("\n", " "))
        sys.exit(2)
    print("#", m.group(1), "| query:", form)
    print("\t".join(FIELDS) + "\tRecord URL")
    for row in re.findall(r"<tr>(.*?)</tr>", body, re.S)[1:]:
        cells = dict(
            (k.strip(), html.unescape(re.sub(r"<[^>]+>", "", v)).strip())
            for k, v in re.findall(r"<strong>([^<]*)</strong>\s*<span>(.*?)</span>", row, re.S)
        )
        link = re.search(r"href='([^']+)'", row)
        print("\t".join(cells.get(f, "") for f in FIELDS) + "\t" + (link.group(1) if link else ""))


def amh(query, all_pages=False, pause=3.0):
    page, total_pages = 1, 1
    while page <= total_pages:
        qs = urllib.parse.urlencode({"search": query, "per_page": 100, "page": page,
                                     "_fields": "id,title,content,categories,link"})
        try:
            body, hdr = fetch(f"{AMH_URL}?{qs}", headers=True)
        except Exception as e:  # noqa: BLE001
            print("ERROR:", e)
            sys.exit(2)
        total = hdr.get("X-WP-Total") or hdr.get("x-wp-total")
        total_pages = int(hdr.get("X-WP-TotalPages") or hdr.get("x-wp-totalpages") or 1)
        if page == 1:
            print(f"# found {total} records, pages of 100: {total_pages} | query: {query!r}")
            print("id\trecord\ttext (with source)")
        for rec in json.loads(body):
            title = html.unescape(rec["title"]["rendered"])
            text = html.unescape(re.sub(r"<[^>]+>", " ", rec["content"]["rendered"]))
            flat = re.sub(r'\s+', ' ', text).strip()  # hoisted out of the f-string for older Python versions
            print(f"{rec['id']}\t{title}\t{flat}")
        if not all_pages:
            if total_pages > 1:
                print(f"# only the first hundred shown; add --all")
            break
        page += 1
        time.sleep(pause)


def main():
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in ("lipes", "amh"):
        print(__doc__)
        sys.exit(1)
    if a[0] == "lipes":
        city = a[a.index("--city") + 1] if "--city" in a else None
        lipes(a[1], soundslike="--soundslike" in a, city=city)
    else:
        amh(a[1], all_pages="--all" in a)


if __name__ == "__main__":
    main()
