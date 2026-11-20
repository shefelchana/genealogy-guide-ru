---
name: searching-familysearch-films
description: >-
  Finds and reads digitised microfilms on FamilySearch — locates a book inside a film (catalog → film number → DGS → frame), finds item boundaries with a thumbnail mosaic, reads frames at full resolution, uses regional collections with a partial name index, keeps a coverage log, and paces requests to avoid hCaptcha. Use whenever the task involves FamilySearch films, "Moldova Church Books", "Russia, Tver, Church Books", Kishinev/Bessarabia metrical books, revision lists on film, a JewishGen index entry that cites a microfilm, a DGS number, an ark link, or a frame number — even if the user only says "look at the film", "find the frame", "read the birth book on FamilySearch". Also triggers on Russian requests: «посмотри плёнку», «найди кадр», «прочитай книгу рождений на FamilySearch».
---

# FamilySearch films: find the book, reach the frame, read it

## When to use
The document was photographed on microfilm and is on FamilySearch (metrical books, revision lists, censuses). A typical starting point: a JewishGen index with the fields "Microfilm / Item / Image", an archive file number (for example ANRM 211-3-…, National Archives of the Republic of Moldova), or an ark link.

## Terms
- **Film number (FHL)** — the film's number in the catalog (7 digits, e.g. 2373291).
- **DGS** — digital film number (9 digits with zeros, e.g. 005783060) — the viewer opens by this number.
- **Item** — a separate book within a film. One film may hold 5–10 different books, often of different places and even faiths.
- **Frame (image)** — a photograph; a spread of the book is often photographed **twice in a row** (a duplicate) — check.

## From the archival reference to the frame
1. **Catalog**: find the collection (search by place, e.g. "Russia, Bessarabia, Izmail") or by film number. In the catalog entry each film has: film number, DGS, a list of items with file references and years.
   ⚠️ The book you need may be **hidden in another collection**: a Jewish birth book of 1883 turned up inside a set of Orthodox metrical records of the uezd (district).
   ⚠️ **The "Jewish" label in the catalog is incomplete.** According to E. Kogan (Bessarabia SIG, 2018), of 292 Bessarabian revision-list films, Jewish records are certainly present on 30, and only the Bender ones are labelled Jewish in the catalog. Do not filter the catalog by "Jewish" — go through all films of the uezd.
   🔑 Search the place **in all spellings** and separately by uezd and guberniya (province): "Nezhin" finds sets that "Nizhin" does not (Lara Diamond). The Item number in the catalog entry shows where on the film the book you need lies.
   ⚠️ **New filming is not in the Catalog.** Since 2022, filming in Ukrainian archives goes to **Images** (familysearch.org/records/images), searched by place at town, uezd and guberniya level; details and a checked state — `ukrainian-archives-on-commons`.
   ⚠️ FamilySearch's indexed Ukrainian collections hold more than 100 million records, the largest being the confessional lists (*ispovednye vedomosti*) of Kyiv guberniya; **there are no Jewish records among them** [from the search results]. The search understands `*`; when searching in Latin letters, do not tick "exact" (lostrussianfamily.wordpress.com, 18.07.2026).
2. **Viewing the film**: `familysearch.org/search/film/<DGS>?i=<frame-1>` (the parameter `i` counts from zero).
3. **The frame number**: take it from the index (JewishGen "Image"); otherwise find the item by step 4.
4. **Item boundaries**: between books there are targets and "END OF ITEM N" cards, then the title of the next file (a stamp with fond/inventory/file). A fast way is a **thumbnail mosaic**: open the thumbnails of every 20th frame, find the black cards and titles, then refine in steps of 2–3.

## Reading
- First read the **printed table header** (what is in which column), then the column you need (usually "father/parents").
- Output not the whole frame but a **strip of the column you need** at large size; 1–2 pages at a time.
- Every hit is **frame + record number + verbatim quotation** + crop.
- **Control record**: before continuous reading, find one record that certainly exists (from the index) — this checks that you are reading correctly.
- **Coverage log**: "frame N: records m. X–Y, f. Z–W; month boundaries". Without it a negative conclusion has no force.
- **Duplicates**: if a spread was photographed twice, read one frame of the pair, but check that the second really is the same spread.

## Pace and protection (experience of October 2026)
- hCaptcha ("Additional security check") appears after roughly **45–150 opened frames (more often around 130 in 40 minutes; earlier as time goes on)**, even with pauses of 10–12 s.
- Pulling a whole film (a thousand frames in minutes) causes freezes and errors for **all** tabs of the same account.
- Rules: **one worker on FamilySearch at a time**; no more than 1 frame per 5–10 s; batches of 4 frames; breaks; on a captcha, stop — a human passes the captcha.
- Some films are available only in FamilySearch centers or serve frames only up to a certain number — record this as a limitation of the source, not as "not found".

## For advanced users
After logging in, frame images and thumbnails can be fetched by a script in the same browser tab (with the session token, which is never printed and never sent anywhere). This is faster than navigating, but **the pace and limits are the same**.

## Regional indexed collections (experience of November 2026)
- There are collections of metrical books by province (for example "Russia, Tver, Church Books, 1722–1918": parish books and consistory copies by district) with a **partial name index**.
- From an index entry: Document Information → Digital Folder Number (DGS) and image number → catalog `q.filmNumber=<DGS>` → parish and district → image.
- **Cross-check siblings:** export all children with a given name and father in the target years and all their presumed sisters (brothers) with the same parents; a match of the parent pair **on both patronymics** is a candidate family. Confirm or reject each candidate on the image (the village in the record).
- A zero in a partial index means "not in the indexed part"; next — page through the parishes.

## Pitfalls
- Index ≠ document: dates in the index may be shifted (Old/New Style), fields mixed up.
- A registration note instead of a surname: «Рашковскій мещ.» [“Rashkovsky meshch.”] = a meshchanin (townsman) of the shtetl of Rashkov.
- A bad frame — look for a second copy of the book (consistory/rabbinate copy) or a second photographing.

See also: `reading-archive-scans`, `verifying-genealogy-findings`.
