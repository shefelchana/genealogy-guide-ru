---
name: using-community-surname-indexes
description: >-
  Uses surname indexes compiled by the genealogy community as the first step before reading archival files page by page — the j-roots forum lists (surname → archive, fond, inventory, file → shtetl or section), its family-topic navigator, JewishGen databases and JGFF, genealogyindexer full text, the AI-built archival.name index. Gives a no-login recipe for reading forum posts including hidden spoilers, maps each surname to the right document header and PDF, moves on to the scan on Commons, and keeps a registry of unread sections so a file read for one surname is not forgotten for the next. Use whenever the user is about to read a revision list, census or metrical book by surname, asks "which file has my family", "is there an index", gets a new surname to check, or says a file was only partly read — even if no index is named. Also triggers on Russian requests: «в каком деле искать фамилию», «есть ли указатель», «посмотри на j-roots», «фамильный указатель», «Краковский», «Финкельштейн».
---

# Community surname indexes: index first, page-by-page reading second

## When to use

- Before reading a revision list (*revizskaya skazka*), census, family list (*posemeinyi spisok*) or metrical book straight through, looking for a surname.
- When a **new surname** appears in the research (a wife's family, a brother-in-law, a neighbouring branch).
- When a file was already read for another surname and it is unclear whether all its sections were looked at.

An index tells you in a minute **which file and which shtetl** a surname appears under. Paging through without an index costs hours, and a partly read file later passes itself off as "checked". An index is a pointer, not a document: it usually gives no page numbers and no given names, and every hit is verified against the scan.

## Workflow

### Step 1. The registry of unread sections comes first

Open the project registry (template: `assets/unread-sections-registry.md`). If the new surname could appear in a file that has already been read in part, **finish reading that section first**: it is the cheapest find there is. A typical case: a revision file was in hand, but only the section for one shtetl was read, and the index later shows the needed surname in a neighbouring section of the same file.

### Step 2. List of spellings

All forms of the surname: Cyrillic and Latin, with a different root vowel, with "-ский/-цкий" (-sky/-tsky), "-ман/-манн" (-man/-mann), **without the first letter** (indexes and OCR lose it), without "й". Details: the `verifying-genealogy-findings` skill, section on spellings.

### Step 3. Indexes, one by one

1. **The j-roots forum** ("Jewish Roots", *Evreiskie korni*): topics by shtetl and uezd (district), where volunteers (lists by A. Krakovsky, Finkelstein and others) have itemised files as "fond-inventory-file → frames by shtetl → surnames". Recipe: `references/j-roots.md`; post parsing: `scripts/forum_post_index.py`.
2. **JewishGen**: databases for Ukraine and other regions, JGFF (who else is researching this surname and where; check it before any forum post), the shtetl's KehilaLinks page. For Poland, the JRI-Poland town surname list; for Israel, IGRA (it shows counts from both JewishGen and Gesher Galicia). Skill `searching-jewishgen`.
3. **genealogyindexer.org**: full text of directories and lists. The script is in the `verifying-genealogy-findings` skill.
4. Pogrom databases for 1917–1922: skill `searching-pogrom-records`.
5. Yandex "Search in Archives" (*Poisk po arkhivam*): recognised handwritten text for some archives, skill `searching-yandex-archives`.

What each index provides and its traps: `references/other-indexes.md`.

### Step 4. From the index to the file

1. Match the surname to the **document header** under which it stands in the post ("Fond 280, inventory 2, file 1012" → section "СКВИРА" [SKVYRA]). The script takes the nearest header above: check it by eye, since one post may hold a dozen files in a row.
2. Find the file: the PDF on Commons via the link in the post (take the address from the `href`; the visible link text on the forum is truncated) or by title through the Commons API; the inventory is on uk.wikisource, on pages like `Архів:ДАКО/280/2` (the Ukrainian Wikisource "Archive:" namespace, here the DAKO inventories). Skill `ukrainian-archives-on-commons`.
3. The frames for a section are often given in the post ("82–128 ПАВОЛОЧЬ" [Pavoloch]). Read the **whole section**, not just the frame with the surname. Skills `reading-archive-scans`, `tracing-revision-records`.
4. Record in the registry what was read, what was not, and for which surname the search was made.

## Traps

- **The index loses letters**: the first letter, "й", the soft sign; "е/э", "и/ы". Search truncated forms too.
- **A surname may be a given name.** The index holds a word that in the document is the given name or nickname of a person with a different surname. Check against the scan.
- **A patronymic or a registration note instead of a surname**: "…ский мещ." (…sky, *meshch.*) means a meshchanin (townsman) of that shtetl, not a surname.
- **The same list is repeated** across topics (by uezd, by shtetl, by surname). A match in three topics is one piece of evidence, not three.
- **Index ≠ document**: no folio, no age, no household composition. A zero in the index does not mean the surname is absent from the file: the volunteer may have skipped a section or read the surname differently.
- **The index is incomplete by year**: it covers the files somebody photographed. A year missing from the index is a reason to check the inventory, not to conclude "did not survive".

## What counts as a find

- An index line with the surname is a **hint ⚪**: "the surname is in file X, section Y".
- A find is only a record read from the scan of that file: folio or frame, verbatim, with ages and household composition. After that, assemble the whole family using the `reconstructing-family-clusters` skill.

## If nothing is found

1. Run a control: was a surname that is certainly there found in the same post or topic? If not, the parsing is broken (for example, the spoiler text did not make it into the download).
2. Check the forms: without the first letter, with a different vowel, Latin.
3. Search by **place**, not by surname: the topic for the shtetl and uezd will tell you which files have been itemised at all; the unitemised files are candidates for straight-through reading.
4. Write in the log: which indexes, which forms, which topics and posts, and what they do not cover.

## Access and courtesy

- j-roots topic and post pages open without logging in; **forum search is forbidden to guests** (checked 07.10.2026). Only a person logs in; without a login, search through a search engine restricted to `forum.j-roots.info`.
- If the site does not open because of the network (geo-blocking, VPN, redirect to a block page), **do not circumvent it**. Tell the person: it is their decision (for example, switching the VPN off).
- CAPTCHAs, logins, payments and letters are done only by a person. One site, one worker; pause several seconds between requests.
- Do not suggest letters to researchers or archives as a search step.

## See also

`verifying-genealogy-findings` · `tracing-revision-records` · `ukrainian-archives-on-commons` · `reading-archive-scans` · `searching-jewishgen` · `searching-yandex-archives` · `searching-pogrom-records` · `reconstructing-family-clusters` · `search-logic-navigator` · `orchestrating-genealogy-agents` · `research-session-handoff`
