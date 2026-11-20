---
name: searching-jewishgen
description: >-
  Searches JewishGen databases (Ukraine, Romania/Bessarabia/Moldova, Lithuania, Belarus, Poland via JRI, JOWBR burials, Holocaust and refugee lists) efficiently and reads results correctly — chooses phonetic vs exact search, narrows queries past the 50-row display limit, decodes ambiguous fields, goes from the index row to the archival image (film number vs archive reference, item, frame range, "M18"), and dates every zero so it can be rerun. Use whenever the user wants to find a Jewish ancestor by surname, town or given name in Eastern Europe, or says "search JewishGen", "my great-grandfather came from Bessarabia/Ukraine", "JewishGen Ukraine database", JOWBR, revision lists, metrical records indexes, or Tashkent refugee cards — even if JewishGen is not named. Also triggers on Russian requests: «поищи в JewishGen», «база Бессарабии», «база по Украине», «ташкентские карточки».
---

# JewishGen: searching and reading the indexes correctly

## Access
- Registration is free; without logging in the search partly works, but detailed records open only under an account.
- The databases are split by region (Ukraine, Romania — this includes Bessarabia, Lithuania, Belarus…) and by topic (JOWBR — cemeteries, Holocaust, KehilaLinks, Communities/Gazetteer).

## How to search
1. **Surname — phonetic** (Daitch-Mokotoff) for the first pass; then **exact** to cut out noise.
2. **Given name — "starts with"** (Ber… catches Berko, Berl, Ber-Itsko).
3. **Town** — as a separate field; mandatory for large result sets.
4. "Any field" — for patronymics and parents' names ("Duvid" in any field).
5. **Search a region wider than the shtetl.** First look at results for the whole uezd (district) or guberniya (province), not for a single shtetl: this shows the family's moves and all brothers and sisters (advice of N. Lipes).

## The databases are updated every month
The Ukraine Research Division posts new records monthly (by announcements — 100 to 150 thousand records a month in 2026; news archive — jewishgen.org/ukraine/ABT_newsArchive.asp). So "not found" is true only as of the search date: write the **date of every zero** in the log and **rerun old zeros** every few months and after each upload for the place you need. The announcements advise checking results in "Ukraine Group 2", "Ukraine Group 3" and in records with no group.

## Display limit
Only the **first page (~50 rows)** is shown for each dataset. If it says "276 matching records" but you see 50, narrow the query: town, years, given name, record type. Otherwise you will miss the one you need.

## How to read a row
- In revision lists (*revizskie skazki*) one family = several rows (head, wife, children); age "of the previous revision | of this one".
- In marriages the father's/mother's fields may sit in one cell with separators ("Duvid////") — **the first position may refer to the groom rather than the bride**. Check against the scan.
- The columns "Archive/Fond", "Microfilm", "Image/Page" are the address of the original. **Open every key record on the scan** (FamilySearch, data.jewishgen.org): in a check in November 2026 the index twice disagreed with the image (a different surname; a "second copy" that was the same file).
- Dates: Old Style/New Style shift and indexer errors are possible (example: the index says "8.VI", the scan says "15 June O.S. = 7 Tammuz").
- A registration note (*pripiska*) can look like a surname: "Rashkovsky meshch." = a meshchanin (townsman) of Rashkov.
- In a source reference you may see a form like «ЦДІАК/W/1162/1/15» (TsDIAK, Central State Historical Archive of Ukraine, Kyiv): according to a discussion on the JewishGen mailing list, the letter W comes from the source data and does not mean an error [not verified]. To find the scan, use fond — inventory (*opis*) — file (*delo*).
- For Ukrainian archives, a scan for a reference from the index is conveniently found through the combined index "Качиний Інспектор" (skill `ukrainian-archives-on-commons`).

## From the index row to the frame
After E. Vance, RootsTech 2023, "Using a JewishGen or JRI-Poland Index to Locate the Original on FamilySearch" (recorded talk) [rule from the talk, not verified]:
1. A number of up to seven digits in the source column is the **FamilySearch film number**. The archive reference (fond–inventory–file) is **not** a film number: the FamilySearch catalog does not find a film by it.
2. **Item** = one book on the film. Each item begins with a **black card with its number**: for item 8, skip items 1–7.
3. A **range of frames** (for example 994–1008) is the span of the book for that year, not the size of the record: start at the first frame of the range.
4. **"M18"** = the 18th entry in the **male** column: a metrical book has two runs of numbers, male and female.
5. No frame number? Use the thumbnail mosaic and item boundaries (`searching-familysearch-films`). No film at all? Search the catalog by the place: there may be two entries, "town in uezd" and "uezd" — check both.
6. After the find, compare: the image may add parents and an exact date that the index left out, or may add nothing. The check is still required.
Indexers often take only the identifying data; the original holds much more (L. E. Diamond, BCGS 2025, "JewishGen, JRI Poland & Gesher Galicia").

## What is useful besides names
- Tashkent cards of evacuees from 1942 (patronymic, occupation, pre-war address, scan of the card).
- JOWBR — years of life and photos of gravestones (in Hebrew — the father's name).
- KehilaLinks — pages of shtetls, links to sources.
- ViewMate — volunteers help read and translate a scan.
- JGFF — who else is searching the same surname and shtetl.

## What to record
The dataset, the query (exactly how you searched), the number found, the row verbatim, the link to the scan, the result of checking against the scan.

See also: `searching-familysearch-films`, `verifying-genealogy-findings`.
