---
name: searching-jewishgen
description: >-
  Searches JewishGen databases (Ukraine, Romania/Bessarabia/Moldova, Lithuania, Belarus, Poland via JRI, JOWBR burials, Holocaust and refugee lists) efficiently and reads results correctly — chooses phonetic vs exact search, narrows queries past the 50-row display limit, decodes ambiguous fields, and goes from the index row to the archival image. Use whenever the user wants to find a Jewish ancestor by surname, town or given name in Eastern Europe, or says "search JewishGen", "my great-grandfather came from Bessarabia/Ukraine", "JewishGen Ukraine database", JOWBR, revision lists, metrical records indexes, or Tashkent refugee cards — even if JewishGen is not named. Also triggers on Russian requests: «поищи в JewishGen», «база Бессарабии», «база по Украине», «ташкентские карточки».
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
The Ukraine Research Division posts new records monthly (by announcements — 100 to 150 thousand records a month in 2026; news archive — jewishgen.org/ukraine/ABT_newsArchive.asp). So "not found" is true only as of the search date: record the month of the search and repeat it after each upload for the place you need. The announcements advise checking results in "Ukraine Group 2", "Ukraine Group 3" and in records with no group.

## Display limit
Only the **first page (~50 rows)** is shown for each dataset. If it says "276 matching records" but you see 50, narrow the query: town, years, given name, record type. Otherwise you will miss the one you need.

## How to read a row
- In revision lists (*revizskie skazki*) one family = several rows (head, wife, children); age "of the previous revision | of this one".
- In marriages the father's/mother's fields may sit in one cell with separators ("Duvid////") — **the first position may refer to the groom rather than the bride**. Check against the scan.
- The columns "Archive/Fond", "Microfilm", "Image/Page" are the address of the original. **Open every key record on the scan** (FamilySearch, data.jewishgen.org).
- Dates: Old Style/New Style shift and indexer errors are possible (example: the index says "8.VI", the scan says "15 June O.S. = 7 Tammuz").
- A registration note (*pripiska*) can look like a surname: "Rashkovsky meshch." = a meshchanin (townsman) of Rashkov.
- In a source reference you may see a form like «ЦДІАК/W/1162/1/15» (TsDIAK, Central State Historical Archive of Ukraine, Kyiv): according to a discussion on the JewishGen mailing list, the letter W comes from the source data and does not mean an error [not verified]. To find the scan, use fond — inventory (*opis*) — file (*delo*).
- For Ukrainian archives, a scan for a reference from the index is conveniently found through the combined index "Качиний Інспектор" (skill `ukrainian-archives-on-commons`).

## What is useful besides names
- Tashkent cards of evacuees from 1942 (patronymic, occupation, pre-war address, scan of the card).
- JOWBR — years of life and photos of gravestones (in Hebrew — the father's name).
- KehilaLinks — pages of shtetls, links to sources.
- ViewMate — volunteers help read and translate a scan.
- JGFF — who else is searching the same surname and shtetl.

## What to record
The dataset, the query (exactly how you searched), the number found, the row verbatim, the link to the scan, the result of checking against the scan.

See also: `searching-familysearch-films`, `verifying-genealogy-findings`.
