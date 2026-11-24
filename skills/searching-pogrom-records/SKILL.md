---
name: searching-pogrom-records
description: >-
  Finds victims and survivors of the 1917–1922 pogroms in Ukraine and nearby regions — the Lipes database jewishpogroms.info (Latin-only search, wildcard, POST recipe), pogrom.amhazikaron.org (WordPress REST; Rosenthal's "Svitok rezni" and archival lists), the Kyiv relief committee fond DAKO R-3050 with about 900 scans on Commons, TsDAVO fond 2497, the YIVO Tcherikower archive. Covers the living too — 1922 relief recipients with addresses, orphans, refugees — and the path from a database row to the archival file and page. Use whenever a relative lived in a shtetl in 1917–1922 or died around 1919–1921, or the family speaks of a pogrom, a gang, orphans, refugees or help from America, even if no database is named. Not for 1941–1944 (use researching-holocaust-fates-ukraine). Also triggers on Russian requests: «погром», «банда», «петлюровцы», «убит в 1919», «сироты», «беженцы», «проверь базы погромов», «был ли он в списках жертв».
---

# Pogroms 1918–1922 (from late 1917): victims, the injured, orphans, refugees

## When to apply

- The family lived in a shtetl (*mestechko*) of Kyiv, Podolia, Volhynia, Kherson, Ekaterinoslav or Chernigov guberniya in 1917–1922.
- A person "vanished" or died around 1919–1921, and the family speaks of a pogrom, a gang, flight, an orphanage, money "from America".
- A standard check of the whole family for those years is needed (see `reconstructing-family-clusters`): the pogrom databases belong in the mandatory package for 1918–1922 alongside ZAGS (Soviet civil registry) and rabbinate books.

These sources hold not only the killed. They include the wounded, the robbed, widows, **recipients of money relief in 1922 with addresses**, **children in orphanages of the 1920s**, staff of children's institutions, refugees. So check living relatives too, not only those who died.

## Procedure

### Step 0. Identification set

Write down before the first query: the surname in all spellings (Cyrillic and Latin, with the root vowel in different variants, without the first letter), given names and patronymics (Jewish and Russian forms), age around 1919, the shtetl **and the neighbouring shtetls and the nearest large city** — people fled there and died there of typhus and hunger in the winter of 1919–1920.

### Step 1. The Lipes database, jewishpogroms.info

About 77,777 records, each with fond, inventory, file, folio and archive. The search is **Latin letters only**. The recipe without a browser and an explanation of the fields are in `references/databases.md`; the ready-made script is `scripts/pogrom_search.py lipes`.

1. First a **control query**: a surname that is certainly there (for example `Lipes` — 23–24 records, checked 07.10.2026). If there is no answer or a placeholder page comes back, the query is broken; it does not mean "the person is not there".
2. Try Latin forms one at a time: `Rabinovich`, `Rabinovitch`, `Rabinowicz`. **The asterisk works** and gives the most: `Rabin*`, `*binovich`. The "Sounds like" checkbox hardly widens the search (checked: `Libes` with it does not find `Lipes`), so go through the variants yourself.
3. Search **by shtetl without a surname** too (`--city Pavoloch`): this shows which lists for the place exist in the database at all, and catches distorted surnames.

### Step 2. Am HaZikaron (Am a-Zikaron), pogrom.amhazikaron.org

About 7,900 victims, each with a source: Rosenthal's "Свиток резни" ("Svitok rezni", the Scroll of Slaughter) in Russian translation, DAKO (State Archive of Kyiv Oblast) files R-3050, TsDAVO (Central State Archive of Supreme Bodies of Power of Ukraine) fond 2497, the Tcherikower archive (YIVO RG 80), TsDIAK (Central State Historical Archive of Ukraine, Kyiv) fond 1164, and others. The search is **in Cyrillic, by substring**, through the open REST: `scripts/pogrom_search.py amh Проскуров` (control: "Проскуров" — 284 records, 07.10.2026). One record often describes **a whole family** ("his wife…, their daughter…"), so search by the son-in-law's surname and by given name as well.

### Step 3. Cross-checking the two databases

The databases overlap but do not coincide: age and names "by different lists" diverge, and Am HaZikaron gives the **pages of the document** (the PDF frame number) beside the folios. A person matched in two databases with a reference to the same file is one piece of evidence, not two.

### Step 4. From the record to the file

1. Turn the fields into an archival reference: `Found / Register / Case / Page` = **fond / inventory / file / folio**, `Archive` = the archive (Dako = DAKO; State archive of Vinnytsia region = DAViO, the State Archive of Vinnytsia Oblast).
2. Find the file in the inventory: DAKO R-3050 is itemized file by file on Vikisource (Вікіджерела) (`Архів:ДАКО/Р-3050/1`, `/2`, `/3`). **Check the file title against the database record.** If the inventory has the file as being about another place, mark the discrepancy and do not draw a conclusion until you open the folio.
3. Find the scan: Commons, category `Funds of State Archive of Kyiv Oblast - Fund R-3050` (about 910 files, names like "ДАКО Р-3050-1-22. 1920. …pdf"; inventories are "ДАКО фонд Р-3050 опис 1.pdf", 2, 3). How to read the PDF: the skills `ukrainian-archives-on-commons` and `reading-archive-scans`.
4. Read the folio yourself. Copy word for word: name, age, what happened, the **address**, who submitted the information (often a relative — one more link), the sum of relief and from which hometown society.

A guide to the fonds and what to look for in them: `references/archives-and-fonds.md`.

### Step 5. Recording the result

Fill in the log from the template `assets/pogrom-search-log.md`: every database, every spelling variant, search mode, number of records, control. Without it "not in the pogrom databases" means nothing.

## What counts as a finding

- A **finding** is a database record **plus** a folio of the file read from the scan, where the surname, the given name and at least one more identifier match: patronymic, age, shtetl, names of relatives, address.
- A database row without an opened folio is a **hint ⚪**, not a fact. Fields in the database can be shifted (shifted columns are visible in the site's drop-down lists), and the file number can be inaccurate.
- A recipient of 1922 relief on a hometown-society list is a strong lead to the **American branch**: money was sent to specific people through the society of a specific shtetl (see `tracing-emigrants-to-origin`).
- A child on an orphanage list with a place of birth and the parents' names is often the only document about a "vanished" child; next look for the orphanage's Soviet documents and ZAGS.

## If nothing was found

1. Check whether the control query passed in each database. If not, repeat later: it is a technical zero.
2. Make sure all Latin forms and the asterisk have been tried, together with a search by shtetl and by neighbouring shtetls.
3. Remember the limits: the Lipes database is compiled from part of the fonds (mainly DAKO R-3050, DAViO, DAOO — State Archive of Odesa Oblast, TsDAVO); Am HaZikaron does not cover even the "Svitok rezni" in full. **Absence from the databases does not prove that the person was not harmed, and does not prove that he survived.**
4. Next, primary sources of the same time: rabbinate death books and ZAGS of 1918–1922 for the shtetl **and the nearest large city**. ZAGS records of these years usually have no column for nationality: look at the burial place (the Jewish cemetery) and the name. Read the cause of death in the rabbinate books "between the lines". See `soviet-era-records`, `ukrainian-archives-on-commons`.
5. Page through the R-3050 inventory by shtetl (search within the inventory page on Vikisource): files with "questionnaires" (*oprosnye listy*), "lists of those who suffered pogroms", "lists of children" by district. Enter unread sections in the register (skill `using-community-surname-indexes`).

Do not suggest letters and requests to archives as a step of the search. CAPTCHAs, logins and payment are done only by a human. One database — one worker at a time.

## See also

`verifying-genealogy-findings` (the four conditions of a negative conclusion, spellings) · `reconstructing-family-clusters` (the package of documents for a family) · `using-community-surname-indexes` (indexes before paging) · `ukrainian-archives-on-commons` · `reading-archive-scans` · `reading-hebrew-yiddish-sources` (about a third of the documents are in Yiddish) · `tracing-emigrants-to-origin` · `soviet-era-records` · `search-logic-navigator` · `orchestrating-genealogy-agents`
