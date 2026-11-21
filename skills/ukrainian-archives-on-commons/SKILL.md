---
name: ukrainian-archives-on-commons
description: >-
  Finds and downloads whole files of Ukrainian state archives published on Wikimedia Commons (metrical books, revision lists, censuses, court files, inventories, ZAGS registers of 1919–1944) and the fond listings on Ukrainian Wikisource (the «Архів:» namespace). Checks where a file is online (Duck Inspector, babynyar.org, FamilySearch Images), searches the inter-archive portal searcharchives.net.ua by place, and goes from an archival reference (archive, fond, inventory, file) or a place name to the exact Commons file name via the MediaWiki API (POST), handles naming variants and duplicates, measures scan quality, downloads the PDF whole and hands reading to reading-archive-scans. Wikisource listings cover a small share of each inventory: never use them for negative conclusions. Use when the user mentions DAKhmO, DAViO, DAZhO, DAKO, DAOO, TsDIAK or another Ukrainian archive, a reference like 227-1-137, or asks for a metrical book or 1920s–30s ZAGS records. Also triggers on Russian requests: «ДАХмО», «ДАВіО», «ДАЖО», «ДАКО», «ЦДІАК», «дело на Commons», «межархивный портал», «FamilySearch Images», «Архів на Вікіджерелах», «скачай метрическую книгу из украинского архива», «найди ЗАГС 1920-х или 1930-х».
---

# Files of Ukrainian archives on Wikimedia Commons

## What is there and when to use it

Commons holds **whole digitised files** from dozens of Ukrainian archives: metrical books, revision lists (*revizskie skazki*), censuses, family lists (*posemeinye spiski*), court files, **genuine typescript inventories of fonds**, and **ZAGS books of 1919–1944** (Soviet civil registry, *ZAGS*). These are scans without a name index: Commons gives access, not search.

Use it when you have an archival reference (archive — fond — inventory (*opis*) — file (*delo*)) or when you need to understand what survives for a place and whether it is digitised. Reading a downloaded file: skill `reading-archive-scans`; revisions: `tracing-revision-records`; identifying a place: `identifying-places`.

Archive abbreviations, sample file names and the volume map of the consolidated catalogue are in `references/archives-and-naming.md`. Read it before building the first query to a new archive.

## Workflow

```
- [ ] 0. Have a reference? → check it in the "Duck Inspector" (Качиний Інспектор): is the file online and where (Commons, FamilySearch, babynyar.org)
- [ ] 1. Have a reference? → step 3. Only a place and years? → step 2
- [ ] 2. Find the reference: inter-archive portal by place → consolidated catalogue of metrical books → the archive's register of inventories → paper inventory on Commons → Wikisource listing; FamilySearch Catalog and Images
- [ ] 3. Find the exact file name (Wikisource subpage or the Commons API, all name variants)
- [ ] 4. Metadata: size, page count → MB/page; duplicates
- [ ] 5. Open the cover and one page from the middle: is it the right file
- [ ] 6. Download the PDF whole → reading-archive-scans
```

## Step 0. Reference → "Duck Inspector" (Качиний Інспектор)

The "Duck Inspector" (inspector.duckarchive.com) is a volunteer consolidated index of Ukrainian archive files published anywhere: Commons, FamilySearch, archive websites. You search by reference or by title; there is an open API:
```bash
curl -s -X POST https://inspector.duckarchive.com/api/search -H "Content-Type: application/json" \
  -d '{"archive":"ДАХмО","fond":"226","inventory":"80","file":"639"}'
```
The response gives the file title, years and an `is_online` flag; the file card is at `inspector.duckarchive.com/archives/<ARCHIVE>/<fond>/<opys>/<sprava>`. Checked 07.10.2026.
Other endpoints: `GET /api/catalog/<archive>/<fond>/<opys>/<sprava>` for one file; text search only in Cyrillic; about 5 requests per 10 seconds; instructions for agents at `inspector.duckarchive.com/llms.txt`. A search by place and years gives a summary of everything digitised for a shtetl (Catholic, Orthodox, confessional lists), so you see at once what is missing for Jews. Checked November 2026: in minutes it showed which of the needed files were online nowhere.
⚠️ The index is **incomplete**: an empty response, a 404 or `is_online: false` means "not found", not "does not exist". It was verified that some files already uploaded to Commons are marked there as not online. Go on to step 3 on Commons.

**babynyar.org/archive** (the portal of the Babyn Yar project; part of the Inspector's results lead there) holds whole files of some archives (for example DAZhO revisions) in colour. It is a **mirror of scans, not an index**: there is no name index to the revisions (its "Імена" section is the database of Babyn Yar victims). It opens in an ordinary browser; scripts get 403. Previews are small: take full size through the viewer. Checked November 2026.

## Step 2. From a place to a reference

**Start with the inter-archive portal, by place.** searcharchives.net.ua (13 archives, DAKhmO among them) searches titles of fonds and files, annotations and name indexes: `https://searcharchives.net.ua/search/?Search=<word>&Digitized=1` (`Digitized=1` = only digitised, `0` = everything). **Search by the place name, not by surname**: one query shows the fonds of a shtetl by type (magistrate, notaries, pogrom reports, Soviet ZAGS), and digitised files have a "Переглянути" [View] link to the archive's viewer. By surname the search is fuzzy (similar-sounding and merely similar words, quotation marks do not help), and name indexes exist only for some fonds: **a zero by surname means nothing**. **For a place name, open the tab «Географічний покажчик періоду до 1917 року фондів „давніх актів“» (geographical index) and the «Іменний покажчик» (name index) tabs**, not only the general results: the general search works by stem, and a village whose name is the stem of a common word (for example «Старовичі» → «старовини», "antiquities") is buried under unrelated files while the count looks large. Check that the first three rows actually name the place. Works without login and from a script. Checked November 2026. Source: M. T. Chubenko, RootsTech 2026, "Click Into Ukraine".

Then for metrical books, the order matters: each following source is **less complete** than the previous one.

1. **The "Consolidated Catalogue of Metrical Books" (*Зведений каталог метричних книг*)**: 10 volumes in 15 books (2009–2021), covering the oblast state archives and the archive of the city of Kyiv; Lviv oblast is not in volumes 1–10. The volumes on Commons are **digital PDFs with a text layer** (a few MB for hundreds of pages): download the needed volume and search for the place name by text search. Search in several spellings (Ukrainian and Russian, "Білилівка / Белиловка" [Bilylivka]) and allow for case endings.
   ⚠️ The catalogue **does not cover TsDIAK** (Central State Historical Archive, Kyiv), second copies, or ZAGS records. The correct wording of a negative result: "not found by text search of all 15 books of the catalogue".
   ⚠️ **The catalogue errs and is incomplete** (checked November 2026): one file was listed under a shtetl it does not contain, and a whole inventory of late Jewish metrical books read by us was absent. "Not in the catalogue" does not mean "no book"; check a catalogue reference against the file's cover. The hub metrics.tilda.ws/ukraine links all volumes.
2. **The register of inventories on the archive's website** (for example DAKhmO's "Анотований реєстр описів" [Annotated register of inventories], with a text layer) describes **the whole fond**. It reveals whole classes of files that are in neither the listings nor the digitisation.
3. **A paper inventory on Commons**: files of the form "<ARCHIVE> фонд N опис N.pdf" [fond N inventory N]. This is the full list of the fond's files with titles.
4. **A listing on Wikisource** (`uk.wikisource.org`, pages "Архів:<ARCHIVE>/<fond>/<opys>", the Ukrainian Wikisource "Archive:" namespace): convenient because a file's subpage leads straight to the file on Commons, and the inventory page links in its notes to the file of the paper inventory.

⚠️ **A Wikisource listing is a sample, not an inventory.** A verified case: the listing of one inventory itemises 308 files out of 9,288 and in places names a file wrongly. Three false conclusions in a row were born from it ("the only file for the uezd", "no such revision exists", "there is no duplicate"). **Never use it for negative conclusions**: only the paper inventory or the register.

**FamilySearch: Catalog and Images are different stores.** Films of the 1990s–2000s are in the Catalog; filming in Ukrainian archives **since 2022** is published in **Images** (familysearch.org/records/images), not in the Catalog. Search Images by place at three levels — town or village, uezd, guberniya — under old and modern names (place IDs differ, results differ); the `keyword` filter matches the file number (several numbers = OR). Control: search a file you know is there. A checked state (November 2026): for Podolia, Images held consistory, Orthodox church, court, bank, notary, magistrate and town-council fonds, but **no files of DAKhmO fonds 226, 227 and 277** (treasury chamber revisions, copies of Jewish metrical books). Repeat such a zero every few months. Viewing needs the person's FamilySearch login; reading frames: `searching-familysearch-films`. Source: E. Vance, RootsTech 2023, "Tracing Your Jewish Roots in Ukraine".

For TsDIAK, instead of the catalogue: the "Архів:ЦДІАК" listing on Wikisource and a search of file titles at archium.cdiak.archives.gov.ua (the archive's main site answers automated requests with 403 but opens in an ordinary browser).

⚠️ **A shtetl's metrical books may not lie in the rabbinate fond.** When there was no crown rabbi (*kazyonny ravvin*), books were handed to the *zemsky sud* (district court), sometimes **of a neighbouring uezd** (N. Lipes: the Cherkasy ones went to Lipovets). If the book is not in the expected fond, check the court fonds. Look for revision lists in the fonds of the **treasury chamber** (*kazyonnaya palata*) too.
🔑 **Files sometimes contain alphabetical indexes and name lists**: look for them first. For some of Krakovsky's files the JewishGen Ukraine Research Division has made a transliterated index and keeps copies of the scans. The order is: the index inside the file → the JewishGen index for that file → page-by-page reading.
⚠️ **Browser auto-translation spoils the terms**: «ревізькі казки» → "tales-revisions", «фонд» → "stock", «опис» → "description", «справа» → "affairs". Read file titles in the original.

## Step 3. The exact file name

File names on Commons are **not uniform**. For one archive these forms occur:
- `ДАХмО 226-80-639. 1816-1820. Відомості про ….pdf`
- `ДАХмО - 226-80-639 Відомості про … 1816-1820.pdf`
- `ДАЛО Р-3321-1-10 Книга державної реєстрації шлюбу (1940).pdf`
- `ДАКО - Фонд 782 Опис 1 Справа 7622 - ….pdf`
- `ЦДІАК 0256_0002_0101.pdf`

So a name cannot be guessed. Three ways, from the reliable to the wide:

1. **The file's subpage on Wikisource** (`Архів:<ARCHIVE>/<fond>/<opys>/<sprava>`) contains a link to the file. Get the page text through the Wikisource API (`action=query`, `prop=revisions`, content of the latest revision): the ordinary page address with `action=raw` sometimes returns an error.
2. **A file list by prefix**: `list=allimages` with `aiprefix=<ARCHIVE> <fond>-<opys>-<sprava>`. The prefix "…-1-12" will also return files 12, 120, 1203: select those where a full stop, space or bracket follows the number. Repeat with the form `<ARCHIVE> - <fond>-…`.
3. **Search in file titles**: `list=search`, namespace 6 (files), a query like `intitle:"226-80-639"`: it catches all variants of the name, including those with a different separator.

**Make all requests to the Commons and Wikisource APIs with the POST method** to `api.php`: GET runs into rate limits sooner. Set a meaningful User-Agent. Pause 2–3 seconds between requests: with frequent requests the API starts answering with an error page instead of JSON.

⚠️ **One file may have been uploaded twice** under different names (with a full stop and with a hyphen). Compare the size and page count of both and take the better scan; if they differ in the set of pages, you need both.

## Step 4. Metadata and quality: before downloading

A `prop=imageinfo` query with the fields `url|size` returns the direct address, the file size and the **page count**. Divide the size by the page count:

| MB per page | What to expect |
|---|---|
| 2.5–3 | ~4000×3000, handwriting reads freely |
| 0.9–1.6 | ~2000×1600, readable, cropping helps |
| 0.25–0.5 | 700–1100 px, only by cropping columns |
| under 0.15 | below the threshold for straight-through reading: see the techniques in `reading-archive-scans` |

⚠️ **The catalogue prefix in the file address** (`a/ab`, `b/bc` …) is different for each file. Take the address from the API response, do not assemble it by hand. Cut off the `?utm_source=…` tail from the address.

## Step 5. Is it the right file

**Page images: check the width you got.** The API may report the width you asked for while its `thumburl` points to a 500-px page (seen 21 November 2026). Write the width into the path yourself (`/pageN-1920px-…`), drop `?utm…`, and check the real JPEG width after download; a page narrower than requested is re-downloaded, never read as "no entry" (`reading-archive-scans`).

Captions on Commons are sometimes wrong: a wrong reference, different content, a different year. **Before working, open the cover and one page from the middle** (page thumbnail: `iiurlparam=page<N>-1280px`; the permitted widths are only 1280 and 3840, otherwise HTTP 400). For revisions, check the column "по последней ревизии" [per the last revision]: it names the year of the previous revision and so gives away the year of the file. Five minutes of checking against hours of work on the wrong document.

## Step 6. Download whole

- **Download the PDF whole** and read locally: the page-by-page previews are over-compressed and, on faded ink, destroy exactly what has to be read.
- A very large file (hundreds of MB) is sometimes not served whole (HTTP 429): then download in parts (range requests) or take individual pages at 3840 px width.
- After that, the skill `reading-archive-scans`: extraction of the original images without re-encoding, the volume map, parity of spreads, enhancement of faded text.
- Downloading means a file on the person's disk: name the file, source and size, if the session requires confirmation of downloads.

## ZAGS books 1919–1944

- Commons holds the fonds of district and city ZAGS offices of a number of oblasts (example: the district ZAGS offices of Khmelnytskyi oblast, DAKhmO fonds R-6435…R-6453; the city books of Proskuriv and Kyiv). The letter **Р** (R) in a fond number = the Soviet period.
- The Wikisource listing of such an inventory often lists the **village councils and villages** for each file: look for the village in several spellings (a village council might be named after a neighbouring village).
- **There is no search by surname**: you read page by page by place and year.
- Forms of the 1920s–1930s often **lack parents and place of birth**; the form changes even within one file; there are two records on a page or one record across two pages. First read the header of the form in this file.
- Records less than 75 years old are personal confidential data; Commons holds what the archive has opened. Do not spread other people's personal data beyond what the research needs.

## Pace and limits

- Commons and Wikisource work without login and without CAPTCHA; the limits are on frequency. One worker per site, a pause between requests.
- The archives' own sites in the archives.gov.ua zone sometimes answer automated requests with 403 and open in an ordinary browser. If it is a geo-block (the browser sees the same), do not circumvent it: look for the same file on Commons or FamilySearch.
- Ordering undigitised files, letters to archives and payment are only for a person.

## What counts as a find and as a negative conclusion

A find = an **address** (archive — fond — inventory — file — PDF page and folio by the archival foliation, the file name on Commons) + a **verbatim quotation** + **checking against the scan** at full resolution.

A negative conclusion has force only if a source with limits is named: "the paper inventory of fond N inventory M was looked through whole, no files on village X for the 1850s" or "the file was looked through from page A to page B, no records of …". "Did not find on Wikisource" and "not in the consolidated catalogue" are **not** negative conclusions but a reason to go to the inventory and the register.
