---
name: reading-archive-scans
description: Reads digitised archival files — revision lists (revizskie skazki), censuses, metrical books, family lists (posemeinye spiski) — from Wikimedia Commons or a downloaded PDF. Extracts the original embedded image instead of a re-compressed preview, judges scan quality before work starts, enhances faded handwriting, detects out-of-focus pages, and maps a volume that has no index. Use when reading scanned historical documents, Ukrainian or Russian archive PDFs (DAKhmO, DAKO, DAViO, TsDIAK files), old handwriting, or when a scan seems unreadable, a name "is not found", or you need to work out which page holds which family. Also triggers on Russian requests: «посемейные списки», «ревизские сказки», «ДАХмО», «ДАКО», «ДАВіО», «ЦДІАК», «прочитай скан», «карта тома».
---

# Reading archive scans

## Scripts

**`scripts/pagetool.py`** — pulls out pages without re-encoding. Run it, do not read it.
```bash
python3 scripts/pagetool.py info  FILE.pdf                  # pages, sizes, MB per page
python3 scripts/pagetool.py sharp FILE.pdf 55,57,59         # defective shots
python3 scripts/pagetool.py sheet FILE.pdf 241,243,245 s.jpg --crop 0.04 0.40 0.10 0.99 --w 1840
python3 scripts/pagetool.py page  FILE.pdf 128 p.jpg --rot 270
```
**`scripts/mapvolume.py`** — finds title pages in a file with no table of contents.
```bash
python3 scripts/mapvolume.py FILE.pdf --mode both
```
⚠️ Both need `pypdf`, `Pillow`, `numpy`.

("FILE.pdf" is the archival file (*delo*) as a PDF.)

## Order of work

```
- [ ] 1. Download the whole file (not a preview)
- [ ] 2. info — judge whether it is readable at all
- [ ] 3. mapvolume — build the volume map
- [ ] 4. Determine the spread parity ON THE SPOT
- [ ] 5. sheet of the names column, keep a log of numbers
```

### 1. Download it whole

Wikimedia previews are over-compressed and on faded ink they destroy exactly what you need to read; a request for an arbitrary thumbnail width gets HTTP 400 from the server.

```bash
curl -s -A "<browser User-Agent>" -X POST "https://commons.wikimedia.org/w/api.php" \
  --data-urlencode "action=query" --data-urlencode "format=json" \
  --data-urlencode "prop=imageinfo" --data-urlencode "iiprop=url|size" \
  --data-urlencode "titles=File:<exact name>.pdf"
```
POST only: GET runs into rate limits. **The directory prefix in the URL (`a/ab`, `6/68`) is different for every file** — take it from the response; a guessed one gives 404. Find the exact name with the same `api.php`: `list=search` with `srnamespace=6`.

The register of digitised holdings of Ukrainian archives is on `uk.wikisource.org`, in the **`Архів:`** ("Archive:") namespace, with the structure `Архів:<ARCHIVE>/<fond>/<inventory>`. It can be exported via `?action=raw` and grepped.

### 2. Judge the quality in advance

`info` divides the file size by the number of pages:

| MB/page | Resolution | Conclusion |
|---|---|---|
| 2.5–3 | 4000×3000 | handwriting is easy |
| 0.9–1.6 | ~2000×1600 | readable, cropping helps |
| 0.25–0.5 | 690×920 … 840×1120 | only by cropping columns |

⚠️ For files in the bottom row, previews of 1920 and 3840 px are **upscaled**: that is the ceiling of the file, not a viewing setting.

### 3. Volume map

Printed title pages are much blacker than handwritten ones — `--mode printed` catches them by the share of ink and the number of long ruled lines. **If the titles in the file are handwritten, the printed criterion does not work**: `--mode written` picks up a concentration of ink in the top third with an empty bottom.

⭐ **First check whether there is a running header** with the name of the place on every spread: many revision lists have one, and then the map is built by sampling every 20th–40th page along the top strip, with no statistics at all.

### 4. The spread trap — the main cause of false "not found"

It comes in two forms, and **you must check on the spot by opening two neighbouring pages**:
* **PDF page = one sheet**: the columns are split between sheets, names appear on every second page. The parity **gets shifted** wherever an extra sheet is bound in — three times in one file, nineteen in another. Determine it afresh after every title; the control is the archival foliation in the corner.
* **PDF page = a whole spread**: the male side on the left, the female side on the right, household numbers run consecutively across all pages. Here viewing "every other page" loses exactly half of the households.

### 5. Reading a small scan

**Do not output the whole page** — cut out a strip with the columns you need and stretch it: the letters get three to four times more pixels. No more than 3–4 pages per sheet.

`sharp` objectively separates "I read it badly" from a defective shot: if the variance of the Laplacian is three times lower than the median, the shot is out of focus and cannot be rescued. This turns "could not read" into a precise request for a re-shoot.

## Proof of completeness

**Continuity of household numbering.** Keep a log "page NNN: Nos. X–Y" and check the joins.
⚠️ Read numbering with care: for some scribes a leading "5" is indistinguishable from "3", "2" from "4"; three-digit numbers at the spine are distorted by the curvature ("290" reads as "190"). Compare with neighbouring pages — the series must be monotonic. If the numbering is disputed, completeness rests on **page-by-page coverage**.

## ⚠️ If a scan is damaged or empty — look for ANOTHER copy, do not give up

This is a mandatory step, not an optional one. A document that is missing in one copy is often intact in another.

**Revision lists (*revizskie skazki*) were written in several copies**, and they lie in different fonds:
· the copy of the **treasury chamber** (*kazennaya palata*) — usually this is the digitised fond;
· the copy of the **city duma, town hall (*ratusha*) or volost board** — its own fond in the same archive;
· the copy of the **district treasury**;
· summaries and extracts in the files of the **revision commission**.
The same goes for metrical books: the parish copy and the consistory copy are two different books about the same people.

**The same file is sometimes shot twice** — by the archive and by the Mormons (FamilySearch microfilm). A spoiled frame in one shoot may be intact in the other. A sign of a film shoot is perforation along the edge of the frame.

**Order of action in case of a defect:**
```
- [ ] 1. Name the defect exactly: which sheets, what kind (break in numbering, protective sheet, out of focus)
- [ ] 2. Check the fond's inventory: is there a duplicate of the same year and district
- [ ] 3. Check other holding fonds (duma, town hall, treasury, commission)
- [ ] 4. Check whether there is a second shoot of the same file
- [ ] 5. Check adjacent sources in which the same family must surface:
       recruit lists, family lists, metrical books, kahal tax registers
- [ ] 6. Only after that — a request to the archive, and a targeted one
```
A targeted request ("двори 193–292 відсутні, розрив між стор. 450 і 454" [households 193–292 are missing, gap between pp. 450 and 454]) is cheaper and faster than a thematic one ("find the Feigel family").

## ⚠️ The inventory must be a paper one. Electronic itemisations are not good for negative conclusions

The itemisations in the `Архів:` namespace on uk.wikisource are **a sample, not an inventory**. Verified: `Архів:ДАХмО/226/79` itemises **308 files out of 9,288** and moreover gets the titles wrong. Three false conclusions in a row were born from it.

✅ **On Commons there is a continuous series of genuine archival inventories** — typewritten, complete:
`ДАХмО фонд N опис N.pdf` — **964 files** · `ДАВіО фонд N опис N.pdf` — 211.
(DAKhmO = State Archive of Khmelnytskyi Oblast; DAViO = State Archive of Vinnytsia Oblast; "фонд" = fond, "опис" = inventory.)
To get the list: POST to `commons.wikimedia.org/w/api.php`, `list=allimages&aiprefix=ДАХмО фонд 227 опис`.

**Reading recipe (not obvious).** An inventory file may weigh 275 MB and **cannot be downloaded whole** — upload.wikimedia.org returns **HTTP 429** for the whole endpoint. Page by page it can be read freely:
```
https://thumb.wikimedia.org/wikipedia/commons/thumb/<pr/prefix>/<NAME>/pageN-3840px-<NAME>.jpg
```
· the width is **only 1280 or 3840**, otherwise HTTP 400;
· from the URL that api.php returns, **cut off the tail `?utm_source=…`** — with it the server answers with an error.
· **⚠️ Do not trust the width the API reports.** On 21 November 2026 api.php (`iiurlwidth=1920`) answered `thumbwidth: 1920`, while the `thumburl` itself pointed to `pageN-500px-…`: agents read 500-px pages and could report a false zero. → **Put the width into the path yourself** (`/pageN-1920px-<NAME>.jpg`, or 1280 / 3840 — use a width the server actually serves; 2000 gave an error page), drop `?utm…`, and **after downloading check the real width of the JPEG** (and its size: a 3 KB "page" is an error page). A page narrower than requested is not "no entry" — download it again at the right width.
· **A 429 on `upload.` may not apply to `thumb.`**: the limit is on the host, not on the volume, so range requests to `upload.` get the same 429; try the same `/thumb/` path on `thumb.wikimedia.org` before writing "unavailable".

## 🔑 Film or copy stand — determined by frame width

Before looking for a "second shoot" or a security negative, determine the method of shooting:
· **film** — the frame width at a given height is **constant**;
· **copy stand** — the width jumps (example: 1485 / 1950 / 911 px at a height of 2000). No negative exists, so there is no point looking for the security fond.
⚠️ "Perforation" along the edge of a frame may be an **artefact of contrast stretching** on a uniform background. Check the edge profile numerically for periodicity, not by eye on the processed picture.

## ⚠️ Low sharpness ≠ defective shot. Confirm by eye

On a **blank sheet** the variance of the Laplacian is just as low as on one shot out of focus: there is nothing sharp to be had. This was learned expensively — two of three "defective" sheets turned out to be blank pages, and they went into the re-shoot request for nothing.
✅ `sharp` only **selects candidates**. Open and look at every candidate: is there any text on it at all, and if there is, is it blurred or bleached out by overexposure (the latter also cannot be rescued by enhancement; the data is not in the file).

## ⚠️ Determine the viewing step on the spot — by family numbers

The spread trap springs again and again, and each time in a new way. The only defence:
✅ Open **four pages in a row** and write out the family numbers on each. If the series runs 9–11, 12–15, 16–19, 22 — **page = spread**, and viewing "every other page" loses half, "every fourth page" loses three quarters.
A real case: a volume was read at every fourth page, coverage came out at **25%**, and the negative conclusion "the surname is not there" had no basis whatsoever.

## 🔑 Check a disputed letter against known letters of the same pen

Do not stare at the disputed sign by itself. Find, on **neighbouring lines of the same hand**, words with a letter known for certain, cut them out together with the disputed spot **in one column at one scale** and compare the shape.
A working example: "Ли[д/б]еръ" (Li-d/b-er) was resolved by comparison with "А**б**рамко" (Abramko) and "Мен**д**ель" (Mendel) on neighbouring lines — in that hand the "б" makes a tall loop up and to the left with no descender, while the "д" goes in a loop **below the line**. The answer: **Либеръ** (Liber).

## 🔑 A name outside the onomasticon = a misreading, not a rare name

Jewish given names of the Russian Empire are **a closed list of a few hundred**. If the name read is found in no onomasticon (Beider, the JewishGen Given Names DB), that is a **signal of a reading error**, not a find.
This is how these were caught: "Лидеръ" (Lider) → **Либеръ** (Liber) · "Маiорновъ" (Maiornov) → **Маiорковъ** (Maiorkov) (from **Меиръ**, Meir).
✅ Run every unfamiliar name through a name dictionary **before** putting it in the result.

## 🔑 Reading handwriting with AI — in two passes

AI models read the printed part of a form well, but handwritten names and places with errors (a JewishGen mailing-list case is described of "Ломжа" [Lomzha] instead of "Ловича" [Lowicz] [unverified]; in Louis Kessler's 2024 test all three models misread the father's name).
1. **First pass — without the expected names.** Give the model the type of document, the year and the place, but not the surnames and names you are looking for: otherwise it will "see" them. Supply a **fragment in high resolution** (the column you need), not the whole frame reduced. Ask it to keep the original spelling and to write "(?)" or "illegible" for what cannot be read.
2. **Second pass — comparison with hypotheses**: compare the reading with your own versions and resolve the discrepancies by the letters of the same pen (section above).
An AI reading is a hint; only what has been checked by eye against the scan goes into the result.
Before reading it is useful to see what the surname you seek looks like in cursive: Steve Morse's "printed ↔ handwritten Cyrillic" tool (stevemorse.org/russian/cyrprintcurs.html).

## ⚠️ In `pagetool.py` the crop is applied AFTER rotation

When working with `--rot`, the `--crop` coordinates are given **in the coordinate system of the already rotated image**, not the original. Recalculate in advance, or the wrong area is cut out.

## 🔑 Before looking for "where he came from" — read the table header

In a block of "arrivals" there may be no origin column at all. This is checked in a minute: read the **column headings** verbatim.
A real case: in the census of 1811 there are exactly three columns ("по послѣдней ревизiи состояли" [stood per the last revision] · "изъ того числа выбыли" [of these, left] · "нынѣ налицо съ причисленными и вновь рожденными" [now present, with those added and newly born]), and the origin is recorded for nobody.
⚠️ A vertical inscription across empty columns is usually **a stroke cancelling the unused columns**, not text about a person. Signs: one per page, not per family; too short for a formula with a place name; **identical on different sheets**.

## 🔑 How to find title pages: measure INK, not file weight

The weight of a compressed frame is **no good** — it reflects the texture of the paper, not the amount of ink (verified: the "light" frames merged into one lump instead of pointing to the titles).

✅ **A working method, entirely local:**
1. decode the JPEG in **`draft` mode (1/8 resolution)** — fast;
2. take the paper level as the **80th percentile** of the frame's brightness;
3. count the **share of pixels darker than it** — this is the share of ink.

A title gives a share noticeably **below** the median for the file. Real numbers on a file of 2,862 frames: median **0.3156**, threshold **0.2253**, below the threshold 229 frames in 140 groups, **scattered throughout the file** — that is, the criterion really does point to the structure. The run took **~6 minutes, no network needed**.

⚠️ And do not judge the language of the file from a sample: in one and the same file **the tables may be in Hebrew while the titles, extracts and certifying inscriptions are in Russian**. It is the certifications that name the community, district, kind of records and year.

## ⚠️ A page may be NOT a JPEG but a raw raster under FlateDecode

`pagetool.py` fails with "cannot identify image file" when a page is stored not as `/DCTDecode` (JPEG) but as a **raw raster under `/FlateDecode`** (ICCBased, 1600×1200, is encountered). PIL does not recognise such a stream.

✅ **Workaround:** decompress with zlib, determine the number of components as `len(raw) // (width*height)`, and assemble with `Image.frombytes`:
```python
raw = zlib.decompress(stream_bytes)
comp = len(raw) // (w*h)                      # 1 = L, 3 = RGB
img = Image.frombytes("L" if comp==1 else "RGB", (w,h), raw)
```
Take the width and height from `/Width` and `/Height` of the image object.
⚠️ Such frames often lie **on their side** — check and apply `--rot 270`.

## ⚠️ Frame orientation varies WITHIN one series — and frame 1 is no guide

Within the same series of books the orientation changes from file to file: portrait 1500×2000 (no rotation needed), landscape 1600×1200 and landscape 4000×3000 (`--rot 270` needed).
⚠️ **The cover is often portrait even in a landscape book** — you cannot judge by frame 1.
✅ **Look at `/Width` and `/Height` of FRAME 2.** Wider than tall → `--rot 270`, otherwise no rotation. Check **each file separately**.

## ⚠️ In bilingual metrical books the parity of the Russian frames is its own in EACH book

In one series: in two files the Russian entries are on **even** frames, in three others on **odd** ones. A rule derived from one file **does not work** on the next.
✅ Determine afresh **in each file**, by opening two or three frames in a row.

## ⚠️ Captions on Commons can be false — read the cover BEFORE working

Verified on one batch three times running: a fond code that is not in the archive's finding aids; a file number missing from the digitisation; and a **substitution of contents** — the file is captioned "family list by districts of the guberniya", and inside is an ordinary list of Christians of a single town.
✅ **Before investing in a file: open the cover and one frame from the middle.** Five minutes against hours of work on the wrong document.
✅ Check not only the title but the **age column** — it names the year of the previous revision and at once shows which year the file belongs to.

## 🔑 Large files from upload.wikimedia.org can be downloaded whole with range requests

A file of 774 MB can be taken **whole** (HTTP 206, range requests) — page-by-page previews are not needed, and you get the **native resolution**.
If previews are nevertheless needed: `page<N>-1280px-<NAME>.jpg`; the width is **only 1280 or 3840**, intermediate values give HTTP 400. When `upload.` answers 429 to everything, range requests are refused too: take the pages from `thumb.wikimedia.org`, with the width written into the path and checked after download (see the inventory recipe above).

## ⚠️ The enhancement coefficient depends on the scan's resolution

`DEFAULT_K = 1.6` is calculated for ~2000 px in width. On large scans (**6883×5539**) even `k = 1.4` gives "embossing" — a false relief instead of a stroke. For such frames use **k = 0.8–1.0**.
✅ Rule: the more pixels per letter, the **less** enhancement is needed.

## 🔑 The register of submitted returns — an index to what is lost

If the returns (*skazki*) of a community are neither in the digitisation nor in the inventory, look for the **summary registers of the revision commission**: "Вѣдомость … поданнымъ въ Коммиссiю Сказкамъ по N Ревизiи" [Register of the returns submitted to the Commission for the Nth Revision]. They give the **number of the source file, the name of the community and the number of souls** — that is, they prove that the return existed, and give its reference code.
With such a register a request to the archive becomes targeted instead of thematic.

## Printed editions in library readers (no OCR)

An old edition is often digitised only by a library, with no recognised text and no PDF. It can still be read — the readers serve pages as pictures at predictable addresses.

**Recipe (verified on GPIB `elib.shpl.ru`):**
1. Open the HTML of the book page and pull out **all** the preview paths (`/system/pages/NNN/NNN/NN/images/...`). **Page identifiers run consecutively** — from them build a full list, even if the reader loads them in by script.
2. Find the maximum zoom: `…/pages/<id>/zooms/<N>`, N from 0 to 8. The eighth is usually ~2000×3200 — more than enough for nineteenth-century printed text.
3. Check whether there is a text layer: `…/pages/<id>/read`. The answer `{"text":null}` means there is no OCR, read by eye.
4. **Derive the formula `scan = constant + page number`** from two or three known pages and check it on a fourth. After that any page is obtained by direct calculation, with no trial and error.
⚠️ In a multi-volume work **each issue has its own constant** — covers and unnumbered sheets shift the count.

**Navigating an alphabetical index — by binary search, not in sequence.**
Take 5 pages at wide intervals, cut from each the **top strip with the first lines**, join them into one contact sheet and read it as one picture. Two or three such probes lead to the right letter. This is an order of magnitude cheaper than leafing through.

## ⚠️ When a site does not deliver: tell a bot wall from a geoblock

- **Bot wall** (Imperva/Incapsula, Cloudflare): curl gets 403 with `_Incapsula_Resource` or a challenge page. Sometimes **a real browser gets through**.
- **Geoblock by IP**: the browser sees the same as curl — "Access denied", an error code and its own IP in the text. A browser **will not help**, nor will the user's Chrome: it has the same address.
- Verified: `szukajwarchiwach.gov.pl` (the catalogue of Polish archives) **blocks Israeli IPs entirely** — Imperva "Error 16". `cdiak.archives.gov.ua` — Akamai 403, bypassed via `archium.cdiak.archives.gov.ua`.
📌 Before asking the user to "open it on your side", work out which case this is. Asking a person to repeat what will certainly not work wastes their time.

## ⚠️ What cannot be read from a reduced preview

Ages and personal names can be made out on a preview ~1280 px wide, **place names cannot**. A real case: "Проскуровъ" (Proskurov) and "**Проскуровкъ**" (Proskurovka) are indistinguishable on the preview, and yet one is a town and the other a village in **different districts** — and a conclusion was almost built on that, that the file was captioned wrongly.

**Rule: any place name that is going into a report or conclusion must be reread at maximum resolution.** Age and name — a preview will do; a place name — never.

## Files below the readability threshold: catch the form covers, do not read in sequence

There are files with **0.04–0.11 MB/page at 1024 px**, and no wider preview exists. A continuous viewing is pointless: 2,000 pages cannot be read, and the line you need is one per household.

**Technique (verified on the 1897 census, DAKO fond 384 inventory 4):**
1. Find out whether the file has a **printed form with fixed layout**. In the census sheets a PDF page is a spread, and **the right half-sheet is always the form's cover** with the single line you need, "Name, patronymic and surname of the head of the household".
2. Catch the cover **by a printed element, not by text**: coat of arms, frame, large typeface. Count the share of dark pixels in a fixed box (for this form — `x 0.66–0.80 / y 0.04–0.14`). Control: headings 0.172–0.220, non-headings 0.092–0.120 — a clean separation.
3. ⚠️ **Take the threshold from the median of the specific file**: exposure differs between files, and the absolute value does not carry over.
4. From each cover found cut out **one line**, put them 25 to a contact sheet and read as one picture.
➜ 2,021 pages are viewed in **nine images** instead of hundreds.
(DAKO = State Archive of Kyiv Oblast.)

## ⚠️ Distinguish "it is not in the source" from "there is no source"

The certifying inscription of a file says **how many sheets are bound in it**. If a register lists sheets Nos. 1–36 and the file has "підшито 2 аркуші" [2 sheets bound], then **the sheets themselves are missing**, and the negative result concerns the **availability of the source**, not its content.
📌 Word it like this: "the household was not found because the city counting district is not digitised", and **not** "there is no such household in the shtetl". This is the same error as taking someone else's itemisation for an inventory.
