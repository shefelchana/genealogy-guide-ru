---
name: searching-archival-name
description: >-
  Searches archival.name — a free, AI-built name index for Central and Eastern Europe (Ukrainian Jewish metrical books, the 1897 census, 1926 Ukrainian SSR family cards, archive inventories with names in file titles, pogrom relief and resettlement files 1917–1938, merchants and town societies, directories, Congress Poland and Galician lists) with links to the scans on Wikimedia Commons. Covers checking coverage first on "Record books by place", the free sign-in (full record and scan link), account limits (4,000 records a day reset at 00:00 UTC, 8,000 rows an hour), search tips (asterisk for case endings, "sounds like", town plus gubernia radius, the 1897 census w= search that finds natives living elsewhere), the JSON endpoints, and the traps (HTTP 429 or parallel queries return an empty answer that is a false zero, an inventory row is not the file, AI misreads names). Use when the user mentions archival.name, wants to search many archive inventories or the 1897 census by surname or place at once, asks "where is a file about this family", "who from this town lived elsewhere in 1897", or an index row from archival.name needs checking. Also triggers on Russian requests: «archival.name», «архивал нейм», «указатель по описям», «перепись 1897 по фамилии», «уроженцы местечка в переписи», «семейные карточки 1926», «найти дело по фамилии в описях».
---

# archival.name: an AI index of archive records and inventories

archival.name (open since 8 October 2026, made by one person) gathers name indexes from many collections and links almost every row to a scan on Wikimedia Commons ("Скан" and "Дело" links). The indexes were **made by AI** and checked on samples; the author says that for now quantity comes before quality. Treat every row as a pointer to a page, not as a reading of it.

Related skills: `ukrainian-archives-on-commons` (opening the file the row points to), `reading-archive-scans` (reading it), `verifying-genealogy-findings` (index ≠ document, negative conclusions), `using-community-surname-indexes` (other indexes first), `orchestrating-genealogy-agents` (one agent per site).

## 1. What is indexed

| Collection type | What a row gives | Typical use |
|---|---|---|
| Jewish metrical books of Ukraine (1863–1922) | date, place, roles (child, father, mother, groom, bride, deceased, witness, mohel) | births and marriages outside the books you already read |
| 1897 census | name, age, household, place of birth / registration / residence, occupation | where the family actually lived, natives of a town living elsewhere |
| 1926 family cards (Ukrainian SSR) | household members | the family between the wars |
| Archive inventories (finding aids) | the file title with names, years, archive code and fond-opys-sprava | court, notarial, police, duma files that nobody has indexed by name |
| Pogrom relief and resettlement (1917–1938) | recipient, official, victim, place | see also `searching-pogrom-records` |
| Merchants and town societies, directories, conscription and war lists | name, status, town, year | status changes, moves, occupation |

New collections keep appearing and counts change from day to day (the same query gave different totals on two consecutive days in November 2026). Write the date next to every count.

## 2. Before searching: coverage and access

1. **Check coverage first.** The page "Record books by place" (`archival.name/books/`) lists all books and files on the site by gubernia, oblast, archive and record type, with links to scans. If your place is not covered, a zero by surname means nothing.
2. **Free sign-in.** Without it you see short rows; after signing in (free; the person signs in, not the agent) you see the full record text and the scan link.
3. **Limits** (read from `/api/me`, tested 20 November 2026): **4,000 records a day** (reset at **00:00 UTC**), **8,000 rows an hour**; also searches 10,000 a day, rows 25,000 a day, openings 1,500 a day. The counter counts **rows delivered**, so wide queries burn the limit. **There is no paid plan**; for a higher limit the person can write to the author (address on the About page). Do not work around the limit (second account, other cookies, other IP).
4. **One worker at a time.** Limits belong to the account, so parallel agents under one sign-in share them and trip HTTP 429 for each other. Give archival.name to one agent only.

## 3. How to search (tested November 2026)

- **Search by URL** (the site's own form builds it): `archival.name/ru/search/?q=<surname>&m=bm&t=<Town>&tr=g`. `m=bm` — "sounds like" (Beider–Morse groups); `m=exact` — exact form; `t` — town in Latin letters (`Vinnytsya`, `Tulchyn`); `tr=g` — "in its gubernia around 1900", `tr=t` — the town only. A row opens by clicking it.
- **`q` takes one surname.** "Two words" returns an error ("Type one surname"); filter the given name with `&g=<name>*`.
- **Asterisk for case endings.** Inventory titles are in Russian or Ukrainian with case endings: `Rosenthal*`-style searches are mandatory. In one test the stem with `*` gave 241 rows against 172 for the nominative form. The site itself merges some letters (Ю/У/И) and, in inventories, double letters.
- **"Sounds like" is noisy.** It brings Galician, Viennese and Latvian look-alikes. Use it for discovery, then confirm with `exact` and the place filter.
- **Control query.** Before trusting a zero, run a common surname in the same town (or the same query that gave rows earlier today). If the control is empty too, the site is silent, not the archive.
- **1897 census: natives living elsewhere.** `w=<place>*` searches the census fields of place of birth, registration and residence, and combines with `q=` and `g=`. Example: `w=Tulchyn*` (spelled as the site writes the place) returns people born in or registered to the town but counted in Odessa, Uman or Berdychiv. In one test this returned about 1,900 rows across the whole census. **In inventories `w=` is ignored** (hundreds of rows were wasted finding this out).
- **Inventories by archive or year.** Filter by archive code `&a=<code>` (for example `a=DAKO`), by years `&y1=1880&y2=1889`, by place `pl=`. Split big totals by decade or archive instead of paging through everything.
- **Speed.** Rows of each collection load in 10–20 seconds. "Database busy or updating" usually clears after a retry in about 20 seconds.

## 4. JSON endpoints (for agents with a browser)

The site's pages call JSON endpoints; an agent can call the same ones **from a page of the site in the person's signed-in browser** (fetch in the page), one at a time, with pauses.
- **Catalogue of collections:** `/api/everything?q=<surname>&m=exact|bm[&t=<Town>&tr=t|g][&g=<name>*]` → for each collection its `id`, the count `n` and `aq` (the query string that collection expects).
- **Rows:** `/api/<id>/search?<aq>`. Take the parameter names from `aq`: they differ by collection (`q`/`g` in metrical books and the census; `nm`/`nmm`, `ng`/`ngm` for names in inventories). **Without `&evn=1` a page holds up to 200 rows** (with it, 25).
- **Paging:** `&off=`. The page size depends on the query (pages of 50 and of 200 rows were both seen): read it from the first answer and step `off` by exactly that number. Overlapping pages waste the limit (770 rows were lost this way in one run).
- **Inventories: use full text.** Searching inventories through `/api/everything` matches the name field only (53 rows against 84 with the inventory collection's own full-text `q=` in one test).
- Answers are large (10,000–25,000 characters). Compress them in the page (keep id, year, place, title, roles) before reading them out, and save each answer to a file.

## 5. Traps

1. **Empty is not zero.** An answer to an over-limit or parallel request can come back empty or as `{"error":"limit"}` with the message that the account "has seen its share of records"; the hourly limit resets within the hour, the daily one at midnight UTC. Check every answer for a `total`; rerun empty ones after a pause. Record a zero only with its control query.
2. **An inventory row is not the file.** It points to the inventory page with the title; the file itself may not be digitised. Then you have a reference (fond-opys-sprava), not a document: check Commons and the other portals (`ukrainian-archives-on-commons`) before thinking of a request to the archive (`requesting-records-from-ukrainian-archives`).
3. **AI misreads names.** The card may show one form and the scan another; surnames come in Polish-style Latin (sz, cz, w); inventory titles may be machine-translated into English. Quote from the scan, never from the row.
4. **Archive codes on rows** (prefixes such as `daoo.`, `davo.`) are the site's own; check which archive they mean on the scan's Commons page before citing.
5. **A zero of the index** is a zero of this index on this date, not of the archive (`verifying-genealogy-findings`).

## 6. Worked example (invented family)

Question: where did the Feldgauz family of Tulchyn go after 1890?
1. "Record books by place": Podolia has metrical books for Tulchyn 1900–1911 and the 1897 census for several towns. → Coverage exists, but not for the 1880s.
2. `/api/everything?q=Feldgauz*&m=exact&t=Tulchyn&tr=g` → census 3, inventories 5, pogrom relief 2, metrical books 0. Control `q=Shapiro*` with the same filter → hundreds of rows, so the site answers; the metrical zero is real for this index.
3. Census with `w=Tulchyn*&q=Feldgauz*` → 2 rows: "Feldgauz Moishe Itskov, 41, registered to Tulchyn, living in Odessa". → A lead to Odessa, not yet a fact.
4. Inventories, full text `q=Фельдгауз*` → "О перечислении мещанина Фельдгауза в одесские мещане", 1899, with fond-opys-sprava. → The file is the document that would date the change of registration; it is not on Commons → next step is the archive.
5. Every row is opened on the scan before it goes into the dossier; the inventory reference goes into the case list with "not digitised, checked on Commons and Inspector on <date>".
Levels: residence in Odessa in 1897 🟡 (census row read on the scan; one person, family not yet linked); change of registration ⚪ until the file is read.

## Answer format

1. Coverage: what "Record books by place" shows for the place, with the date.
2. Each query: the URL or endpoint with parameters, `total`, rows read out of total, the control query and its result.
3. Each row: collection, the site's record id, date, place, roles; whether the scan was opened (quote from the scan with the Commons file name and page) or "index only".
4. Zeros with controls; empty answers and 429s that were rerun; rows of the daily limit spent (estimate).
5. Next step: which scan to read, which reference to find on Commons, which file is not online.
