---
name: searching-yandex-archives
description: >-
  Searches Yandex Archive Search (yandex.ru/archive): full text of machine-recognised handwriting in metrical books, confession and revision lists of Russian archives in 20+ regions (Moscow city and region, Astrakhan, Orenburg incl. 1942–1943 evacuee lists etc.), plus periodicals (Kommersant, Senate announcements) and directories (All Moscow, All Russia, Russian Medical List). Builds queries with spelling variants, operators, a dropped first letter and patronymic forms; keeps one query per 8–9 s; checks recognised text against the full scan. Needs the user's own Yandex login since November 2026. Use when an ancestor lived, married or died in a covered region, or for a surname in old newspapers or directories. Not for Ukrainian archives (use ukrainian-archives-on-commons). Also triggers on Russian requests: «поищи в Яндекс архивах», «Яндекс Поиск по архивам», «метрики Москвы или Подмосковья», «исповедные ведомости».
---

# Yandex Archive Search

## What it is and when to use it

The service has used a neural network to recognise the **handwritten** text of more than 23 million sheets of archival files of the 18th to early 20th century, and about 6 million pages of periodicals and directories (figures from the service's help page, October 2026). It is free. ⚠️ **Since November 2026 the search and the documents open only after logging in to a Yandex account**; without a login a query redirects to the home page. That is not a "zero" but a lack of access. The person logs in themselves in their own browser; the agent works in a tab of that browser.

Use it when:
- the ancestors lived, married, baptised children or died **in Moscow or Moscow guberniya**: people from many guberniyas ended up in Moscow metrical books;
- you need a region whose archives are in the service (the list and what is in each: `references/collections.md`; read it before the first query for a new region);
- you need **the press**: *Kommersant* (Коммерсантъ) of 1909-1917 printed provincial chronicle with obituaries and trade news; the "Senate announcements" (*Senatskie obyavleniya*) carry auctions, mortgages and summonses to heirs, with full names and patronymics;
- you need **directories**: *Vsya Moskva* ("All Moscow"), *Vsya Rossiya* ("All Russia"), the *Rossiiskii meditsinskii spisok* (Russian Medical List), casualty lists of 1914-1917;
- the person was **evacuated to Orenburg (Chkalov) in 1942–1943** or **wounded in the Russo-Japanese War of 1904–1905**: the lists of evacuees with a name index and the lists of the wounded in *Russky Invalid* are described in `references/collections.md`.

⚠️ **There are no Ukrainian, Belarusian or Moldovan archives in the service.** A zero on manuscripts for a Podolian or Bessarabian family proves nothing. For Jewish provincial lines the periodicals and directories are worth more than the archive section.

## Order of work

```
- [ ] 1. Find out whether the region and period are covered (references/collections.md)
- [ ] 2. Compile a list of spellings and forms BEFORE the first query
- [ ] 3. Choose the section: archives / periodicals / books and directories
- [ ] 4. Queries with an 8-9 s pause, a query log
- [ ] 5. Every hit: read the recognised text, then the scan
- [ ] 6. Screen out lookalikes, write up the find
```

## 1. How to build queries

**The service understands morphology and pre-reform orthography itself.** «Тимоѳей Михѣевъ» and «Тимофей Михеев» are searched alike; case forms («Рабиновича», «Рабиновичем» [of / by Rabinovich]) are found from the base form. So do not run through case forms; run through **spellings**.

**Operators** (from the service's help page; they are typed into the Russian-language search box as shown):
- `"…"`: exact phrase, e.g. `"Иванов Петр"`;
- `!слово`: only this form of the word, no morphology;
- `слово1 | слово2`: either of the words;
- `-слово`: exclude documents with this word;
- `*`: a skipped word inside a phrase, e.g. `"Петр * Иванов"`.

A multi-word query without quotation marks finds documents that contain **all** the words, though not necessarily next to each other. For metrical books this is convenient: surname + father's name + locality.

**Compile the list of variants beforehand** (why: recognised handwriting goes wrong in predictable ways, and the service searches by words, not fragments):
- doubled and single consonants, е/ѣ/и, о/а in unstressed syllables (the final ъ is already handled by the service);
- **letters that the neural network and the clerks confuse at the beginning of a word**: Б/В, Ш/Щ/Т, Р/К, Л/Д, Г/Т: make a separate query for each substitution;
- **without the first letter**: if the recognition tore off or lost the capital letter, the text holds the word «озенберг» instead of «Розенберг». A word search will find such an error only with a query for the stump itself;
- the "similar spelling" mode (a switch in the results) is for fuzzy matches; scan it by eye, it is noisy;
- for Jewish names, the forms of metrical books and directories: Мовша / Мошко / Моисей, Хаим / Ефим, Берко / Борис;
- **the patronymic in 19th-century metrical books** is often given in the form «Иванов сын» ("Ivan's son"), «Иванова дочь» ("Ivan's daughter"), «Ивановъ»: search for the father's name as a separate word next to the surname too.

**Filters** of the results: years, archive / fond / inventory / file, type of event (birth, marriage, death), type of document, place of search (title or full text). Narrow with a filter rather than by complicating the query: that way you can see exactly what is being cut off.

## 2. Pace

- **One query per 8-9 seconds.** After about 25 fast queries in a row the service starts to drop connections ("Failed to fetch", an error page); automated requests from outside the browser get a 403.
- **One worker per service.** Parallel searches from one address will all get dropped.
- Work in the **active tab**: the browser "freezes" background tabs and requests hang.
- Keep a **query log**: query, section, filters, number of results, date. Without it a negative conclusion cannot be formulated.

## 3. Reading the result

1. **The recognised text** of the page is right on the document page (the "More details" mode puts the scan next to the text). Find the paragraph with the word you need without paging through the whole document.
2. **The recognised text is a hint, not a reading.** The neural network confuses letters and, in directories, columns: neighbouring lines of the text may not be neighbours on the page. Determine the heading of a directory, the column of a metrical record and the record number **from the scan**.
3. **The full scan.** The viewer shows the image in low resolution (a preview of about 800 px); at maximum zoom small handwriting is blurred. The page gets the full resolution (about 2200 px) from the server through a **temporary permission for the specific image**: the browser first requests it, then downloads the original with this permission in the header. Do this only in the same tab where the scan page is open, using the page's own means; do not print, save or pass the permission anywhere. If that does not work, zoom in with the "+" button in the viewer several times and capture the area you need.
4. Re-read the place name and the surname that will go into a conclusion at maximum resolution. For difficult handwriting, the skill `reading-archive-scans`.
5. **Read the table header first**: in metrical books and confession lists the columns differ from guberniya to guberniya and from year to year.

## 4. Lookalikes and false hits

Results for a surname are almost always cluttered:
- namesakes of another faith and origin (Catholics, German colonists, merchants of another town);
- similar-sounding surnames that the neural network reduced to the one sought;
- **ordinary words** that coincide with a surname (measures, names of goods, place names).

Screen out by a second feature: given name and patronymic, estate and place of registration, address, profession, a telephone number in a directory. An entry "meshchanin of m. N" (townsman of shtetl N) is the **place of registration**, not a surname.

## 4a. Experience of November 2026

- **Paging** — parameter `pageNum=N`.
- **A year filter** set in the URL can return a false zero — repeat the query without the filter.
- When parsing the HTML you will meet service JSON fragments that echo the query; drop lines with `dateTo` / `reqId`, or you will get phantom "hits".
- **Where coverage is rich:** metrical books of the Central State Archive of Moscow and the Moscow Region (peasant migrants with province, district, volost and village — a way to find which district held the village of a family story), the State Archive of Vologda Region (fond 496 — district metrical books of Vologda and part of Novgorod province), the State Archive of Novgorod Region (fond 480), Smolensk, Mordovia, Omsk. **St Petersburg metrical books and civil registry are not indexed** — a zero for St Petersburg means nothing.
- **Villages with the same name:** the query "<village> <province>" over migrants' records lists every same-named village of the province with its district and volost — do this before choosing a parish.

## 5. If the service is unavailable

1. Tell your own dropped connections from a general breakdown: wait 10-15 minutes, open the service's home page in an ordinary tab. In October 2026 the search did not work at all for several days, then worked again.
2. Do not hammer it with repeated queries; that will prolong the block.
3. While the service is down, go to other full-text corpora: Genealogy Indexer (directories, search in Cyrillic), archive.org (ready text files of volumes), Google Books (a phrase in pre-reform orthography), newspapers of the Russian Empire at gpa.eastview.com, and for the Jewish press the skill `searching-nli-jewish-press`.
4. In the log write "source unavailable (date)", not "not found".

## 6. Rules

- Logging in to the Yandex account (required since November 2026), CAPTCHAs and any paid actions are done only by the human. The agent does not enter the password and does not create an account; if the login drops, stop and say so.
- **Do not download the service into your own database.** Under Yandex's terms, compiling a database from its materials is a violation. Save individual pages you find for your own research.
- The service had no geographic restrictions (it worked from abroad in October 2026); if any appear, do not bypass them.

## 7. The find

Write it up like this:
- **address**: archive, fond, inventory, file, folio (or publication, year, issue, page) and a link to the scan page;
- **a verbatim quotation** taken from the scan, not from the recognised text; mark discrepancies with the recognised text;
- **check against the scan**: yes / no, resolution, what remained illegible;
- why this is the same person (a second feature).

A negative conclusion: "Not found in the 'archives' section, filter: archive X, years Y-Z; spellings A, B, C, without the first letter, similar-spelling mode; date." A zero on its own proves nothing (see `verifying-genealogy-findings`).
