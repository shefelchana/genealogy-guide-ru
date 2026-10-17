#!/usr/bin/env python3
"""Поиск по двум открытым базам жертв и пострадавших от погромов 1917–1921 гг.
без браузера. Печатает таблицу (TSV) и число найденных записей.

1) jewishpogroms.info (база Н. Липес, ~77 777 записей; поиск только латиницей)
   python3 pogrom_search.py lipes Rabinovich
   python3 pogrom_search.py lipes "Rabin*"            # звёздочка = любые буквы
   python3 pogrom_search.py lipes Rabinovich --soundslike
   python3 pogrom_search.py lipes "" --city Pavoloch  # все записи по городу

2) pogrom.amhazikaron.org («Ам а-Зикарон», ~7 900 жертв; поиск подстрокой, кириллица)
   python3 pogrom_search.py amh Проскуров
   python3 pogrom_search.py amh Рабинович --all      # все страницы, а не первые 100

Вежливость: одна база — один исполнитель; между запросами пауза (по умолчанию 3 с).
Скрипт не обходит капчи и не входит в аккаунты. Ответ, не похожий на таблицу
(страница-заглушка, 403/429), печатается как ОШИБКА — это не «0 найдено».
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
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
        print("ОШИБКА: ответ не похож на таблицу результатов:", body[:200].replace("\n", " "))
        sys.exit(2)
    print("#", m.group(1), "| запрос:", form)
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
            print("ОШИБКА:", e)
            sys.exit(2)
        total = hdr.get("X-WP-Total") or hdr.get("x-wp-total")
        total_pages = int(hdr.get("X-WP-TotalPages") or hdr.get("x-wp-totalpages") or 1)
        if page == 1:
            print(f"# найдено {total} записей, страниц по 100: {total_pages} | запрос: {query!r}")
            print("id\tзапись\tтекст (с источником)")
        for rec in json.loads(body):
            title = html.unescape(rec["title"]["rendered"])
            text = html.unescape(re.sub(r"<[^>]+>", " ", rec["content"]["rendered"]))
            print(f"{rec['id']}\t{title}\t{re.sub(r'\s+', ' ', text).strip()}")
        if not all_pages:
            if total_pages > 1:
                print(f"# показана только первая сотня; добавь --all")
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
