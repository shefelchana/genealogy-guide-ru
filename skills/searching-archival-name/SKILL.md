---
name: searching-archival-name
description: >-
  Searches archival.name, a free AI-built name index for Central and Eastern Europe (Ukrainian Jewish metrical books, the 1897 census, 1926 family cards, inventories with names in file titles, pogrom relief files, directories, Polish and Galician lists) with links to scans on Commons. Covers the site terms (manual search only: no agents, scripts or bulk collection), coverage, sign-in and daily quotas (an endless "Searching…" means the quota is spent), tips (asterisk, "sounds like", the 1897 w= search for natives living elsewhere) and traps (an empty answer over the limit is a false zero; an inventory row is not the file). Use when the user mentions archival.name, wants to search many inventories or the 1897 census by surname or place, or a row from it needs checking. Not for j-roots and other community indexes (use using-community-surname-indexes). Also triggers on Russian requests: «archival.name», «указатель по описям», «перепись 1897 по фамилии», «уроженцы местечка в переписи».
---

# archival.name: an AI index of archive records and inventories

archival.name (open since 8 October 2026, made by one person) gathers name indexes from many collections and links almost every row to a scan on Wikimedia Commons ("Скан" and "Дело" links). The indexes were **made by AI** and checked on samples; the author says that for now quantity comes before quality. Treat every row as a pointer to a page, not as a reading of it.

**The search itself is done by the person, by hand** (section 4). The agent's part: plan the searches, read what the person brings back, open the scans on Commons, and check the rows.

Related skills: `ukrainian-archives-on-commons` (opening the file the row points to), `reading-archive-scans` (reading it), `verifying-genealogy-findings` (index ≠ document, negative conclusions), `using-community-surname-indexes` (other indexes first), `orchestrating-genealogy-agents` (stop when a task breaks a site's terms).

## 1. What is indexed

| Collection type | What a row gives | Typical use |
|---|---|---|
| Jewish metrical books of Ukraine (1863–1922) | date, place, roles (child, father, mother, groom, bride, deceased, witness, mohel) | births and marriages outside the books you already read |
| 1897 census | name, age, relation to the head of household, place of birth / registration / residence, occupation | where the family actually lived, natives of a town living elsewhere |
| 1926 family cards (Ukrainian SSR) | household members | the family between the wars |
| Archive inventories (finding aids) | the file title with names, years, archive code and fond-opys-sprava | court, notarial, police, duma files that nobody has indexed by name |
| Pogrom relief and resettlement (1917–1938) | recipient, official, victim, place | see also `searching-pogrom-records` |
| Merchants and town societies, directories, conscription and war lists | name, status, town, year | status changes, moves, occupation |

New collections keep appearing and counts change from day to day (the same query gave different totals on two consecutive days in November 2026). Write the date next to every count.

## 2. Before searching: coverage and access

1. **Check coverage first.** The page "Record books by place" (`archival.name/books/`) lists all books and files on the site by gubernia, oblast, archive and record type, with links to scans. If your place is not covered, a zero by surname means nothing.
2. **Free sign-in.** Without it you see short rows; after signing in (free; the person signs in, not the agent) you see the full record text and the scan link.
3. **Quotas.**
   - **Without sign-in: about 9 searches a day.** On the tenth the site says «Лимит поисков на сегодня исчерпан» ("today's search limit is used up"; reader's measurement, 18 November 2026). Plan the searches before the first one, the control query included; this is also the main reason to sign in.
   - **Signed-in account** (tested 20 November 2026): **4,000 records a day** (reset at **00:00 UTC**), **8,000 rows an hour**; also searches 10,000 a day, rows 25,000 a day, openings 1,500 a day. The counter counts **rows delivered**, so wide queries burn the limit.
   - **There is no paid plan.** For a higher limit the person writes to the author (address on the About page). Do not work around the limit (second account, other cookies, other IP).
4. **One person, one account.** The terms allow one account per person; the quotas belong to the account and to the connection.

## 3. How to search (tested November 2026)

- **Search by URL** (the site's own form builds it): `archival.name/ru/search/?q=<surname>&m=bm&t=<Town>&tr=g`. `m=bm` — "sounds like" (Beider–Morse groups); `m=exact` — exact form; `t` — town in Latin letters (`Vinnytsya`, `Tulchyn`); `tr=g` — "in its gubernia around 1900", `tr=t` — the town only. A row opens by clicking it. The agent can prepare such URLs as a list; the person opens them one by one.
- **`q` takes one surname.** "Two words" returns an error ("Type one surname"); filter the given name with `&g=<name>*`.
- **Asterisk for case endings.** Inventory titles are in Russian or Ukrainian with case endings: `Rosenthal*`-style searches are mandatory. In one test the stem with `*` gave 241 rows against 172 for the nominative form. The site itself merges some letters (Ю/У/И) and, in inventories, double letters.
- **"Sounds like" is noisy.** It brings Galician, Viennese and Latvian look-alikes. Use it for discovery, then confirm with `exact` and the place filter.
- **Control query.** Before trusting a zero, run a common surname in the same town (or the same query that gave rows earlier today). If the control is empty too, the site is silent, not the archive. Without sign-in the control costs one of the nine searches: budget for it.
- **Inventories by archive or year.** Filter by archive code `&a=<code>` (for example `a=DAKO`), by years `&y1=1880&y2=1889`, by place `pl=`. Split big totals by decade or archive rather than reading hundreds of rows.
- **Speed.** Rows of each collection load in 10–20 seconds. "Database busy or updating" usually clears after a retry in about 20 seconds.
- **An endless "Searching…" is usually a spent quota, not a slow site.** The sign: the page hangs or refuses **in the middle of a series of similar searches** that worked a moment ago. Stop; do not record a zero; continue after the reset or after signing in (reader's measurement, November 2026).

### 1897 census: search by registration with `w=`

**This is the main tool for the question "where were our people counted when they were not at home".** For Jewish families, registration (приписка) and residence were different places, and a search by the census place shows only those found at home. `w=<place>*` searches the census fields of **place of birth, registration and residence**, and combines with `q=` and `g=`.

- Example: `w=Tulchyn*` (spelled as the site writes the place) returns people born in or registered to the town but counted in Odessa, Uman or Berdychiv. In one test this returned about 1,900 rows across the whole census.
- Narrow it with `q=<surname>*`: without sign-in one wide `w=` search can be all you get for the day.
- **In inventories `w=` is ignored** (hundreds of rows were wasted finding this out).

## 4. Site terms — manual search only

The terms page `archival.name/ru/terms` (read 21 November 2026) says, word for word:

> «Не копируйте указатели массово: никаких скриптов, скраперов, ботов и другого автоматического доступа, никакого сбора записей с помощью множества поисковых запросов или множество учётных записей»

("Do not copy the indexes in bulk: no scripts, scrapers, bots or other automated access, no collecting of records through many search queries or many accounts.")

> «Учётные записи, нарушающие эти условия, могут быть ограничены или закрыты без предупреждения»

("Accounts that break these terms may be limited or closed without warning.")

Rules that follow:
- **Agents and scripts do not use archival.name** — neither searches nor the site's internal data requests, not even "one at a time from the person's browser": the terms are about the kind of access, not about the window it comes from. Paging through results with a program is collection by many queries.
- The person searches by hand. The agent prepares the list of searches (surname forms, place, mode, the control query), receives the rows the person copies out, and does everything after that: opens the scans on Wikimedia Commons, reads them, records zeros with their controls.
- **If manual search is not enough**, the way forward is a letter to the author asking for a higher limit (the address is on the About page), written and sent by the person — not a workaround.
- A task that asks for automated work on this site is refused with a quote of the terms (`orchestrating-genealogy-agents`). A technique found in someone else's guide is checked against the site's own terms, not against the guide's authority; an earlier version of this skill described the site's data endpoints and was corrected.

## 5. Traps

1. **Empty is not zero.** A search over the quota can hang on "Searching…" or come back empty, or with a message that the limit is used up; the hourly limit resets within the hour, the daily one at midnight UTC. Check that the page shows a count of results; rerun empty ones later. Record a zero only with its control query.
2. **An inventory row is not the file.** It points to the inventory page with the title; the file itself may not be digitised. Then you have a reference (fond-opys-sprava), not a document: check Commons and the other portals (`ukrainian-archives-on-commons`) before thinking of a request to the archive (`requesting-records-from-ukrainian-archives`).
3. **AI misreads names.** The card may show one form and the scan another; surnames come in Polish-style Latin (sz, cz, w); inventory titles may be machine-translated into English. Quote from the scan, never from the row.
4. **Archive codes on rows** (prefixes such as `daoo.`, `davo.`) are the site's own; check which archive they mean on the scan's Commons page before citing.
5. **A zero of the index** is a zero of this index on this date, not of the archive (`verifying-genealogy-findings`).
6. **A census role belongs to a head of household the row does not name.** Rows say «сынъ», «невѣстка», «внучка» ("son", "daughter-in-law", "granddaughter") — relative to the head of *that* household, and the index does not say which household. Rows come in the order of the results, not of the households. In one case seven rows with one surname from one village, assembled into one household, turned out on the scan to be three households: three people belonged to the man, three to his widowed mother (her son, her daughter-in-law, her granddaughter), and one was the daughter of a third brother. Such a reconstruction has no inner contradiction, so nothing but the scan can refute it (reader's case, November 2026). → **A household assembled from index rows is a conclusion, not a record**: mark it so and check it on the first scan. The same goes for notes in your own tables filled in by the order of the result rows. A record is a page, not a person — and a role is not a household.

## 6. Worked example (invented family)

Question: where did the Feldgauz family of Tulchyn go after 1890? The person is signed in; the agent prepares the searches, the person runs them and copies the rows.
1. "Record books by place": Podolia has metrical books for Tulchyn 1900–1911 and the 1897 census for several towns. → Coverage exists, but not for the 1880s.
2. Search page `archival.name/ru/search/?q=Feldgauz*&m=exact&t=Tulchyn&tr=g` → the results list census 3, inventories 5, pogrom relief 2, metrical books 0. Control `q=Shapiro*` with the same filter → hundreds of rows, so the site answers; the metrical zero is real for this index.
3. Census with `archival.name/ru/search/?q=Feldgauz*&w=Tulchyn*` → 2 rows: "Feldgauz Moishe Itskov, 41, registered to Tulchyn, living in Odessa". → A lead to Odessa, not yet a fact.
4. Inventories, full text `q=Фельдгауз*` → "О перечислении мещанина Фельдгауза в одесские мещане", 1899, with fond-opys-sprava. → The file is the document that would date the change of registration; it is not on Commons → next step is the archive.
5. Every row is opened on the scan before it goes into the dossier; the inventory reference goes into the case list with "not digitised, checked on Commons and Inspector on <date>".
Levels: residence in Odessa in 1897 🟡 (census row read on the scan; one person, family not yet linked); change of registration ⚪ until the file is read.

## Answer format

1. Coverage: what "Record books by place" shows for the place, with the date.
2. Each search: the search URL, who ran it (the person, by hand), the count shown, rows read out of total, the control query and its result.
3. Each row: collection, the site's record id, date, place, roles (and to whom the role refers, if the scan shows it); whether the scan was opened (quote from the scan with the Commons file name and page) or "index only".
4. Zeros with controls; empty answers and hangs that were rerun; searches used of the day's quota.
5. Next step: which scan to read, which reference to find on Commons, which file is not online.
