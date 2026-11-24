# The j-roots forum ("Jewish Roots"): how to get surname indexes

Checked 07.10.2026. The forum runs on phpBB.

## What is there

- **Topics by shtetl and uezd (district)** (for example, "СКВИРА и СКВИРСКИЙ уезд" [Skvyra and Skvyra uezd]). In the first posts volunteers itemise files: "1858. Revision list of the Jews of Skvyra uezd (*Ревизская сказка евреев Сквирского уезда*). State Archive of Kyiv Oblast. Fond 280, inventory 2, file 1490" → link to the PDF → "frames 82–128 — ПАВОЛОЧЬ [Pavoloch]" → under a spoiler, the list of surnames in the section. This is how the lists by Krakovsky, Finkelstein and other compilers are built.
- **Topics "ГАКО, фонд 280_ревизские сказки"** (GAKO, fond 280, revision lists), "ГАКО, разные фонды, поиск и находки" (GAKO, various fonds, searches and finds), "Перепись 1897" (1897 census) by uezd: summary indexes by fond.
- **Family navigator**: `viewtopic.php?f=20&t=1384` (the "Фамильный указатель" [Surname index] link in the forum header). It is a table of contents of the **family topics** opened by researchers themselves ("what we know, what we are looking for"). It is not an index to files but an index to people who have already searched for the surname.
- The topic "архивные документы, которые участники форума просят отснять" (archival documents that forum members ask to have photographed): what was photographed recently and under which reference code.

## Access

| What | Without login | Checked |
|---|---|---|
| `viewtopic.php?t=…`, `viewtopic.php?p=…` | opens | yes, 07.10.2026 |
| `search.php?keywords=…` | **"Извините, но вам запрещено пользоваться поиском"** [Sorry, you are not allowed to use search] | yes, 07.10.2026 |
| links from search results with `hilit=`/`sid=` | sometimes 403; the direct topic address opens | from the work log |

- Forum search works only under an account. A person logs in in their own browser; the agent may read the results in their tab, without posting anything.
- Without a login: a search engine restricted to the domain, for example the query "Паволочь ревизия 1858 фонд 280" [Pavoloch revision 1858 fond 280] filtered to `forum.j-roots.info`. This finds topics and topic pages (checked 07.10.2026).
- Under an account the search form is `search.php?keywords=SURNAME&terms=all&sf=all&sr=posts` (all words, in text and titles, results as posts). Search each form of the surname separately and with an asterisk (`Фамил*`).
- The site's certificate fails verification in some clients; `curl -k` is acceptable **only** for reading public pages without logging in: do not send cookies, passwords or forms with such a request. If the site redirects to a block page or does not respond because of the network (VPN, geo-restrictions), **do not circumvent it**; tell the person.

## How to fetch a whole post

Surname lists are hidden in "► Показать" (Show) spoilers (`div.spoilcontent` with style `display:none`). **The browser's innerText and "copy text" skip them**, and then a surname appears to be "absent" where it is in fact present.

1. Save the page HTML:
   ```
   curl -sk -A "GenealogyGuideTool/1.0 (personal family research)" \
     "https://forum.j-roots.info/viewtopic.php?p=NNNNNN" -o post-NNNNNN.html
   ```
   In the browser, use `textContent` or `outerHTML` of the needed `div.post`, not innerText.
2. Parse locally:
   ```
   python3 scripts/forum_post_index.py post-NNNNNN.html Surname Variant --loose
   ```
   The script prints the post, the line, the nearest document header above (fond-inventory-file), the section (a line in capitals, usually a shtetl or volost) and the nearest PDF link above.
3. **Check by eye**: the header is chosen automatically. One post often holds 5–15 files in a row (1795, 1816, 1850, 1858, 1875, 1888…), and the surname occurs in several of them.
4. A topic page gives 10–20 posts; a long topic continues at `&start=20`, `&start=40`.

## From post to scan

- PDF links in posts are truncated in the visible text ("upload.wikimedia.org/wikipedia/ … .pdf"); the full address is in the `href` attribute (the script takes and decodes it itself).
- If there is no link: find the file through the Commons API (`list=search`, `srnamespace=6`). Files are named in different ways ("ДАКО 280-2-365. 1816…", "ГАКО 280 1490 1491 1858 Сквирский уезд", "1858 год. Ревизская сказка евреев Сквирского уезда"), so search by **words**, not by a single reference-code string: `280 1490 1858` finds the file, `intitle:"280-2-1490"` does not (checked 07.10.2026). Then the file's inventory entry on uk.wikisource (`Архів:ДАКО/280/2`). Skill `ukrainian-archives-on-commons`.
- The "frame" numbers in the post are PDF pages; the file's folio numbers are on the scan itself. In the findings log (FINDINGS-LOG.md) write both.

## What an index will not give

Given names, ages, family numbers and folios. Only "the surname is in this section of this file". The rest comes from the scan.
