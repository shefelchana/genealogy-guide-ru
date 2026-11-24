#!/bin/sh
# blockade_address_probe.sh — house pages of the consolidated Leningrad siege
# memorial book (blockade.spb.ru).
#
# The site has a page per house: https://blockade.spb.ru/address/<id>/
# ("Список жителей дома по адресу: …"). It lists the residents of that house
# who are in the book (mostly those who died in the siege), with flat numbers,
# about 10 per page, paged with ?page=N. The house id is not shown by the name
# search, so it has to be found by trying ids. Ids are grouped by street (not
# strictly alphabetical): once one house of a street is found, try the
# neighbouring ids.
#
# Usage:
#   blockade_address_probe.sh 12345            # address of one house id
#   blockade_address_probe.sh 12300 12500      # probe a range, print houses found
#   blockade_address_probe.sh -r 12345         # all residents of house 12345 (TSV)
#
# Output:
#   probe:     id | district | street, house
#   residents: flat <TAB> name <TAB> birth year <TAB> card URL
#              (card URL form: /card/?id=N&source=external&docs=simple)
#
# Politeness: one request at a time, DELAY seconds between requests
# (default 2; e.g. DELAY=3 blockade_address_probe.sh 12300 12500).
# Do not run several copies in parallel against the site. The script does not
# pass captchas or log in; if the site starts refusing, stop and wait.
#
# Notes:
# - An id that prints nothing is either empty or not a house page; that is not
#   a "zero" for a person.
# - A house page shows only people who are in the book. Survivors and evacuees
#   are mostly not there, so a missing flat says nothing about its residents.
# - The site's name search fills its results with a script, so a plain curl of
#   the search page comes back empty; use a browser for name search.
# - The parsing follows the page layout seen in November 2026 (blocks with
#   class "address-result"). If the site changes its layout, residents mode
#   prints nothing — check one page in a browser before trusting a zero.
#
# Requires: curl, python3.

BASE="https://blockade.spb.ru"
UA="GenealogyGuideTool/1.0 (personal family research)"
DELAY="${DELAY:-2}"

fetch() {
  curl -sL -m 20 -A "$UA" "$1"
}

probe_one() {
  h=$(fetch "$BASE/address/$1/")
  a=$(printf '%s' "$h" | grep -o "Список жителей дома по адресу: [^,<]*,[^,<]*" | head -1)
  d=$(printf '%s' "$h" | grep -o "г.Санкт-Петербург, [^,<]*" | head -1)
  [ -n "$a" ] && echo "$1 | $d | ${a#Список жителей дома по адресу: }"
  return 0
}

residents() {
  id="$1"
  page=1
  last=1
  while [ "$page" -le "$last" ] && [ "$page" -le 300 ]; do
    h=$(fetch "$BASE/address/$id/?page=$page")
    if [ "$page" -eq 1 ]; then
      probe_line=$(printf '%s' "$h" | grep -o "Список жителей дома по адресу: [^,<]*,[^,<]*" | head -1)
      if [ -z "$probe_line" ]; then
        echo "id $id: not a house page (or the site did not answer)" >&2
        return 1
      fi
      echo "# ${probe_line}" >&2
      last=$(printf '%s' "$h" | grep -o "page=[0-9]*" | sed 's/page=//' | sort -n | tail -1)
      [ -z "$last" ] && last=1
      echo "# pages: $last" >&2
    fi
    printf '%s' "$h" | python3 -I -c '
import sys, re, html
h = sys.stdin.read()
n = 0
for block in h.split("class=\"address-result\"")[1:]:
    m = re.search(r"/card/\?id=(\d+)[^\"]*\"[^>]*>(.*?)</a>", block, re.S)
    if not m:
        continue
    name = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
    t = re.search(r"address-result__text\"[^>]*>(.*?)<", block, re.S)
    year = re.sub(r"\s+", " ", html.unescape(t.group(1))).strip() if t else ""
    r = re.search(r"address-result__room\"[^>]*>(.*?)<", block, re.S)
    flat = re.sub(r"\s+", " ", html.unescape(r.group(1))).strip() if r else ""
    url = "https://blockade.spb.ru/card/?id=%s&source=external&docs=simple" % m.group(1)
    print("\t".join([flat, name, year, url]))
    n += 1
if n == 0:
    print("# page %s: no rows" % sys.argv[1], file=sys.stderr)
' "$page"
    page=$((page + 1))
    [ "$page" -le "$last" ] && sleep "$DELAY"
  done
  return 0
}

case "$1" in
  -r)
    [ -n "$2" ] || { echo "usage: $0 -r <house id>" >&2; exit 2; }
    residents "$2"
    ;;
  ''|-h|--help)
    sed -n '2,40p' "$0"
    ;;
  *)
    if [ -n "$2" ]; then
      i="$1"
      while [ "$i" -le "$2" ]; do
        probe_one "$i"
        i=$((i + 1))
        [ "$i" -le "$2" ] && sleep "$DELAY"
      done
      exit 0
    else
      probe_one "$1"
    fi
    ;;
esac
