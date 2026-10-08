# Archive file scans: the documents themselves

What this section covers: where digitized archival files are kept — FamilySearch films, Wikimedia Commons, archive websites, catalogs and inventories, Yandex "Archive Search". How to find the file you need, how to read it, and where the traps are. Markers and interface-language notes are in [README.md](README.md). Don't read Russian? See [For English speakers](../guide/0-start/08-for-english-speakers.md).

---

### What an archival reference is and why you need it
Fond–inventory–file (for example, 226-79-5224 — DAKhmO, fond 226, inventory (*opis*) 79, file (*delo*) 5224; DAKhmO is the State Archive of Khmelnytskyi Oblast). An inventory shows the title of a file but not its contents; an index shows that the surname is in the file. That is not the same as reading the record. Distinguish: **inventory · index · database index · scan · your transcription**. In detail — [Records of the Russian Empire and the USSR](../guide/2-reference/01-records-empire-ussr.md).

---

## FamilySearch — films and frames (familysearch.org) (English interface)
- **What is there:** digitized microfilms of metrical books, revisions, civil records from the archives of Moldova (ANRM, the National Archives of the Republic of Moldova: Chișinău, Cahul, Bolgrad, Izmail), Ukraine (TsDIAK — Central State Historical Archive of Ukraine in Kyiv, TsDIAL — in Lviv, oblast archives [from search snippet]), Poland, Belgium, the USA.
- **Access:** Free, registration: yes. Many films are available only in FamilySearch centers.
- **Pace:** a CAPTCHA after about 45–150 opened frames; no more than **one frame per 5–10 seconds**, one worker per site, **do not download a whole film**, a human passes the CAPTCHA. Figures and cases — [Access, CAPTCHAs, pace](../guide/2-reference/19-access-captchas-pace.md).
- **Techniques:**
  - find the film you need by number through the catalog (search "film number"), then open the viewer and page by frame number;
  - one film can hold several different books (items), sometimes of different places and confessions. The book you need may be **hidden in someone else's collection**: the Jewish birth book of Izmail for 1883 is listed in the collection of Orthodox metrical books of the uezd;
  - find the boundaries of books by thumbnails at a step (for example, every 20th frame), then refine;
  - with double-frame filming (a spread on two frames) the father's and mother's columns lie on different frames; a spread is sometimes shot twice;
  - sometimes a film gives only the first frames;
  - check a **control record** from a known metrical book to make sure you are looking at the same volume.
- **Experience:** civil records of Chișinău, revisions of Izmail 1824–1854, revision lists of Akkerman 1835 and 1859, an emigrant's file in Antwerp. A marriage of 1869 turned up only in the index; the record itself is not on FamilySearch — **an index ≠ a document**.
- **For advanced users:** the address of a frame is built from the number of the digital film (DGS); do not pull films down with a script. The detailed method is in the skill [`searching-familysearch-films`](../../skills/searching-familysearch-films/SKILL.md) (in Russian).

## Wikimedia Commons (commons.wikimedia.org) — whole files of Ukrainian archives
- **What is there:** the project of Alex Krakovsky. After the court victory on 3 October 2019 (the court found unlawful the ban on private persons copying archival documents), Commons holds **metrical books, revision lists, censuses, fond inventories** of DAKhmO (Khmelnytskyi oblast), DAViO (Vinnytsia), DAZhO (Zhytomyr), DAKO (Kyiv) and other archives. **Also here are the ZAGS (Soviet civil registry) books of 1919–1944**: Proskurov (DAKhmO R-6450), Kyiv (DAK R-1654), the rural districts of Khmelnytskyi oblast (R-6435–R-6453).
- **Access:** Free, no registration.
- **Important:** these are **scans without name indexing** — access, not search. You have to read sheet by sheet. The ZAGS books have no surname search; the Proskurov forms of 1924–1935 and Kyiv 1922 lack parents and place of birth.
- **The main technique:** **download the file's PDF whole and read it on your own computer.** The previews on the site are over-compressed (faded ink is lost). Judge the quality in advance: file size ÷ number of pages. 2.5–3 MB per page — readable freely; 0.25 MB — with difficulty, only if you cut out the columns.
- **Traps:**
  - a file of hundreds of megabytes sometimes does not download whole (error 429) — take the pages one by one;
  - household numbers in spread-format books run into the gutter ("290" is read as "190") — check against neighboring pages;
  - sheets are sometimes torn out of files (22 sheets in one file of 1834): check by gaps in the numbering and the number of pages.
- **For advanced users:** the file address and size — by a request to the site's API (`prop=imageinfo`); the original JPEG is extracted from the PDF without re-encoding; enhancing faded ink — subtracting a blurred background and stretching the contrast (a factor not above 1.8). Ready scripts — the skill [`reading-archive-scans`](../../skills/reading-archive-scans/SKILL.md) (in Russian).

## Wikisource (Вікіджерела; uk.wikisource.org, section "Архів:") (in Ukrainian)
- **What is there:** itemized listings (*rospis*) of fonds ("Архів:ДАХмО/226/79"), subpages of files with a link to the Commons file if the file is digitized. The page "Архів:Архіви" collects the inventories of central and oblast archives.
- **The main warning:** a listing is a **selection, not an inventory**. For example, the listing of fond 226 inventory 79 of DAKhmO covers 308 files out of 9,288 and sometimes names a file wrongly. In one research project it led to three false conclusions in a row ("the only file for the uezd", "there is no revision of 1795", "there is no duplicate"). **It is not suitable for negative conclusions.**
- **What is good:** a file's subpage gives a link to the scan; adding `&action=raw` to the address returns the inventory as text. The scans have no text layer.
- **The right order:** first the register of inventories on the archive's own site, then the real paper inventory (its scan is sometimes on Commons), and only then the Wikisource listing.

## Websites of Ukrainian archives (in Ukrainian)
- **DAKhmO** (dahmo.gov.ua, archium.dahmo.gov.ua): the "Annotated register of inventories" (Анотований реєстр описів; 389 pages with a text layer) describes the **whole fond**. It revealed a class of files that was neither on Wikisource nor in the digitization (files on assignment to tax-paying estates 1846–1851, 1,312 files). archium — search by file titles; **the coverage is incomplete** (titles have been entered mostly for church metrical books, prosecutors' fonds and Soviet ZAGS). Inventories 1–30 of fond 226 are not on Commons — these files exist only in the archive.
- **DAViO** (davio.gov.ua): inventories of fond 172 are PDFs with a text layer; inventories of some other fonds are images only, and a zero from them is false.
- **Caveat:** in the archives.gov.ua zone the sites returned error 403 to automated requests; in an ordinary browser they often open.
- **Oblast archives** post digitization in the sections "Електронний архів" (electronic archive) [from search snippet].

## Inter-archival search portal (Міжархівний пошуковий портал; searcharchives.net.ua) (in Ukrainian)
- 13 archives of Ukraine: 65,406 fonds, 1,276,033 files, more than 25 million digital images. Full-text search over the names of fonds and files, annotations and indexes, with morphology; free [checked].

## TsDIAK (Kyiv): cdiak.archives.gov.ua and archium.cdiak.archives.gov.ua (in Ukrainian)
- **What is there:** the Central State Historical Archive of Ukraine: metrical books of the 18th–20th centuries, police materials. A **geographical index** and the section **"Rabynaty"** (Рабинати) — a list of surviving rabbinates of Kyiv guberniya with archival references and years (Berdychiv, Ruzhyn, Skvyra and about 70 others). Files that are not digitized can be ordered to the reading room through a personal account [checked].
- **Access:** the main site returns 403 to automated requests, but opens in an ordinary browser; the home page is very heavy — go by direct links. archium.cdiak: search by file titles `/search?q=<word>`.
- **Caveat:** TsDIAK is **not part of** the consolidated catalog of metrical books. "Not itemized" ≠ "not preserved".

## "Consolidated catalog of metrical books" (Зведений каталог метричних книг; on Commons)
- **What is there:** 10 volumes (15 books, 2009–2021) of the catalog of metrical books of the state archives of Ukraine (Lviv oblast is not in volumes 1–10) — **digital PDFs with a text layer**. Any village can be looked up across all oblasts in seconds.
- **Map of volumes:** vol. 2 — Kyiv oblast, vol. 3 — the city of Kyiv, vol. 4 — Odesa, vol. 7 — Vinnytsia, vol. 8 — Khmelnytskyi, vol. 9 — Zhytomyr, vol. 10 — Chernihiv.
- **Technique:** search the name in several spellings (Ukrainian/Russian: "Білилівка / Белиловка"), remembering the case endings. Not in the catalog ≠ no metrical books: the catalog does not cover TsDIAK, second copies and ZAGS records. The right wording: "not found in a full-text search of the 15 volumes".
- **Caveat:** the official site returned 403 — take the volumes from Commons.

## Russian oblast archives and EAIS (example: the State Archive of Lipetsk Oblast) (in Russian)
- **What is there:** a section "Electronic inventories" (Электронные описи) with PDFs of fond inventories and **inter-fond indexes**: metrical books (village → church → fond/inventory/years), revision lists, service record lists (*formulyarnye spiski*), household books (*pokhozyaistvennye knigi*); a guide to the fonds. Some fonds have **name indexes** — a surname is searched through without ordering files. **Check for an index before ordering files.**
- **Techniques:** inventories are PDFs with a text layer. The letter case in the address matters — take the links from the site's page, do not guess. In some indexes the text layer is "scattered" into letters — join the single-letter lines before searching. Check the file numbers from the index against the file titles in the inventory.
- **Paid:** EAIS (EAIS is the unified archival information system; remote viewing of digitized files) — in this archive since November 2025, 60 ₽ per hour or 110 ₽ for 2 hours; the mark "ОЦ ФП" in an inventory = the file is digitized. From abroad EAIS and a number of oblast archive sites did not open (September 2026).
- Other regions have their own terms: for example, in Kuzbass part of the documents is freely available after registration [checked]. See [russian-language-resources.md](russian-language-resources.md).

## Yandex "Archive Search" (yandex.ru/archive) (in Russian)
- **What is there:** full-text search — **even handwritten text is recognized** — across more than 23 million pages: about 30 Russian archives (the Central State Archive of Moscow, TsGAMO, Orenburg, Omsk, Astrakhan, Irkutsk and others), **periodicals** ("Kommersant" 1909–1917, "Senate announcements", guberniya gazettes, "Vechernyaya Moskva", "Pravda"), **directories** ("All Moscow", "All Russia", "Russian Medical List", casualty lists 1914–1917). **There are no Ukrainian archives** — the absence of Podolian documents proves nothing. But there are **Moscow metrical books**: residents of many guberniyas married and died in Moscow.
- **Access:** Free, no login.
- **Pace:** after about **25 quick requests in a row** connections drop. Safe — **one request every 8–9 seconds**. In October 2026 the search did not work for several days, then worked again. Work in the active tab.
- **Techniques:**
  - the search understands case endings and pre-reform spelling;
  - the recognized text of a page lies right on the document page — the paragraph you need can be read without opening the scan;
  - in viewing mode the resolution is low — for small text you need the full scan;
  - OCR of directories confuses columns: check the heading against the scan;
  - for Jewish provincial lines **periodicals** are more valuable: "Kommersant" printed a provincial chronicle with obituaries and trade news, "Senate announcements" — auctions, mortgages and summonses to heirs with full names and patronymics.
- **Experience:** an obituary of a provincial timber dealer (1914); mortgages of a family member at an auction in Uman (1917) with patronymics; inventories of personal files in the Central State Archive of Moscow.
- **The trap of look-alikes:** namesakes and similar words fill the results (Shefel / Sheffel / Shepel; "shefel" is a measure of grain). Check initials, address, telephone.
- By the service's rules you may not build your own database from its materials [checked].

---

**See also:** [indexed-databases.md](indexed-databases.md) · [directories-and-books.md](directories-and-books.md) · [Archives by country](../guide/2-reference/07-archives-by-country.md) · skills [`reading-archive-scans`](../../skills/reading-archive-scans/SKILL.md), [`searching-familysearch-films`](../../skills/searching-familysearch-films/SKILL.md) (in Russian)
