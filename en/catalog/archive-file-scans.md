# Archive file scans: the documents themselves

What this section covers: where digitized archive files are kept — FamilySearch films, Wikimedia Commons, archive sites, catalogs and inventories, Yandex "Archive Search". How to find the file you need, how to read it, and where the traps are. Markers are in [README.md](README.md).

---

### What an archival reference is and why you need it
Fond–inventory–file (for example, 226-79-5224 — DAKhmO [State Archive of Khmelnytskyi Oblast], fond 226, inventory (*opis*) 79, file (*delo*) 5224). An inventory shows the title of a file but not its content; an index shows that a surname is in the file. This is not the same as reading the record. Distinguish: **inventory · index · database index · scan · your transcription**. In detail — [Documents of the Russian Empire and the USSR](../guide/2-reference/01-records-empire-ussr.md).

---

## FamilySearch — films and frames (familysearch.org)
- **What is there:** digitized microfilms of metrical books, revisions, records from the archives of Moldova (NARM [National Archives of the Republic of Moldova]: Chisinau, Cahul, Bolgrad, Izmail), Ukraine (TsDIAK [Central State Historical Archive of Ukraine, Kyiv], TsDIAL [Central State Historical Archive of Ukraine, Lviv], oblast archives [from search snippet]), Poland, Belgium, the USA.
- **Access:** Free, registration: yes. Many films are available only at FamilySearch centers.
- **Pace (from experience 01–07.10.2026):** hCaptcha **after ~45–150 opened frames (more often about 130 in 40 minutes; earlier as time goes on)**. Loading too fast (1,052 frames in 4 minutes) — a freeze and error 429. Safe is no more often than **one frame every 5–10 seconds**, with breaks; one thread (one worker per site); **do not download a film whole**. At a CAPTCHA — stop and pass it yourself.
- **Techniques:**
  - find the film you need by number through the catalog (search "film number"), then open the viewer and page by frame number;
  - one film can hold several different books (items), sometimes of different places and confessions. The book you need may be **hidden in someone else's collection**: the Jewish birth book of Izmail for 1883 is listed in the collection of Orthodox metrical books of the uezd;
  - find the boundaries of the books by thumbnails at an interval (for example, every 20th frame), then refine;
  - with double-frame filming (a spread on two frames) the father's and mother's columns are on different frames; a spread is sometimes shot twice;
  - sometimes a film gives only the first frames;
  - check against a **control record** from a known metrical record to make sure you are looking at the same volume.
- **Experience:** records of Chisinau, revisions of Izmail 1824–1854, revision lists of Akkerman 1835 and 1859, an emigrant's file in Antwerp. A marriage of 1869 was found only in the index; the record itself is not on FamilySearch — **an index ≠ a document**.
- **For advanced users:** the frame address is built from the digital film number (DGS); do not pull films down with a script. Detailed method — the skill `searching-familysearch-films` in [../../skills/](../../skills/).

## Wikimedia Commons (commons.wikimedia.org) — whole files of Ukrainian archives
- **What is there:** the project of Alex Krakovsky. After the court victory of 3 October 2019 (the court ruled unlawful the ban on private individuals copying archival documents), Commons holds **metrical books, revision lists, censuses, fond inventories** of DAKhmO (Khmelnytskyi oblast), DAViO (State Archive of Vinnytsia Oblast), DAZhO (State Archive of Zhytomyr Oblast), DAKO (State Archive of Kyiv Oblast) and other archives. **Also here are the ZAGS books 1919–1944**: Proskurov (DAKhmO R-6450), Kyiv (DAK R-1654), rural districts of Khmelnytskyi oblast (R-6435–R-6453).
- **Access:** Free, no registration.
- **Important:** these are **scans without indexing by name** — access, not search. You have to read sheet by sheet. The ZAGS books have no search by surname; the Proskurov forms of 1924–1935 and the Kyiv forms of 1922 do not give parents or place of birth.
- **The main technique:** **download the PDF of the file whole and read it on your own computer.** The previews on the site are over-compressed (faded ink is lost). Assess quality in advance: file size ÷ number of pages. 2.5–3 MB per page — reads freely; 0.25 MB — with difficulty, only if you crop the columns.
- **Traps:**
  - a file of hundreds of megabytes sometimes will not download whole (error 429) — take the pages one at a time;
  - household numbers in spread books run into the gutter ("290" reads as "190") — check against neighboring pages;
  - sheets are sometimes torn out of files (22 sheets in one file of 1834): check by a break in the numbering and the page count.
- **For advanced users:** the file address and size — by a request to the site's API (`prop=imageinfo`); the original JPEG is extracted from the PDF without re-encoding; enhancing faded ink — subtracting the blurred background and stretching the contrast (a coefficient no higher than 1.8). Ready-made scripts — the skill `reading-archive-scans` in [../../skills/](../../skills/).

## Vikidzherela — Ukrainian Wikisource (uk.wikisource.org, the "Архів:" section) (Ukrainian-language)
- **What is there:** breakdowns of fonds ("Архів:ДАХмО/226/79"), subpages of files with a link to the Commons file if the file is digitized. The page "Архів:Архіви" gathers the inventories of central and oblast archives.
- **The main warning:** a breakdown is a **sample, not an inventory**. For example, the breakdown of fond 226 inventory 79 of DAKhmO covers 308 files out of 9,288 and sometimes names a file wrongly. In one study three false conclusions in a row were drawn from it ("the only file for the uezd", "there is no 1795 revision", "there is no duplicate"). **It is not suitable for negative conclusions.**
- **What is good:** a file's subpage gives a link to the scan; adding `&action=raw` to the address returns the inventory as text. The scans have no text layer.
- **The right order:** first the register of inventories on the archive's own site, then the real paper inventory (its scan is sometimes on Commons), and only then the Vikidzherela breakdown.

## Websites of Ukrainian archives (Ukrainian-language)
- **DAKhmO** (dahmo.gov.ua, archium.dahmo.gov.ua): the "Анотований реєстр описів" (Annotated register of inventories; 389 pages with a text layer) describes **the whole fond**. Through it a class of files was found that was in neither Vikidzherela nor the digitization (files on assignment to the tax-paying estates 1846–1851, 1,312 files). archium — a search by file titles; **coverage is incomplete** (titles are entered mostly for church metrical books, prosecutors' fonds and Soviet ZAGS). Inventories 1–30 of fond 226 are not on Commons — those files are only in the archive.
- **DAViO** (davio.gov.ua): the inventories of fond 172 are PDFs with a text layer; the inventories of some other fonds are images only, and a zero from them is false.
- **Note:** in the archives.gov.ua zone the sites returned a 403 error to automated requests; in an ordinary browser they often open.
- **Oblast archives** post digitization in "Електронний архів" (Electronic archive) sections [from search snippet].

## Interarchive search portal — Міжархівний пошуковий портал (searcharchives.net.ua) (Ukrainian-language)
- 13 archives of Ukraine: 65,406 fonds, 1,276,033 files, over 25 million digital images. Full-text search by names of fonds and files, annotations and indexes, with morphology; free [checked].

## TsDIAK (Kyiv): cdiak.archives.gov.ua and archium.cdiak.archives.gov.ua (Ukrainian-language)
- **What is there:** the Central State Historical Archive of Ukraine: metrical books of the 18th–20th centuries, police materials. A **geographical index** and the section **"Рабинати"** (Rabbinates) — a list of surviving rabbinates of Kyiv guberniya with references and years (Berdichev, Ruzhin, Skvira and about 70 others). Files that are not digitized can be ordered to the reading room through a personal account [checked].
- **Access:** the main site returns 403 to automated requests, but opens in an ordinary browser; the main page is very heavy — go in by direct links. archium.cdiak: a search by file titles `/search?q=<word>`.
- **Note:** TsDIAK is **not included** in the consolidated catalog of metrical books. "Not catalogued" ≠ "did not survive".

## "Zvedenyi katalog metrychnykh knyh" — Consolidated Catalog of Metrical Books (on Commons) (Ukrainian-language)
- **What is there:** 10 volumes (15 books, 2009–2021) of the catalog of metrical books of the state archives of Ukraine (Lviv oblast is not in volumes 1–10) — **digital PDFs with a text layer**. Any village is searched across all oblasts in seconds.
- **Map of the volumes:** vol. 2 — Kyiv oblast, vol. 3 — the city of Kyiv, vol. 4 — Odesa, vol. 7 — Vinnytsia, vol. 8 — Khmelnytskyi, vol. 9 — Zhytomyr, vol. 10 — Chernihiv.
- **Technique:** search the name in several spellings (Ukr./Rus.: "Білилівка / Белиловка"), bearing in mind the cases. Not in the catalog ≠ no metrical books: the catalog does not cover TsDIAK, duplicate copies and ZAGS records. The right wording: "not found in a full-text search of the 15 volumes".
- **Note:** the official site returned 403 — take the volumes from Commons.

## Russian oblast archives and EAIS (example: State Archive of Lipetsk Oblast) (Russian-language)
- **What is there:** a section "Электронные описи" (Electronic inventories) with PDFs of fond inventories and **inter-fond indexes**: metrical books (village → church → fond/inventory/years), revision lists, service records (*formulyarnye spiski*), household books (*pokhozyaistvennye knigi*); a guide to the fonds. Some fonds have **name indexes** — a surname is searched straight through without ordering files. **Check whether an index exists before ordering files.**
- **Techniques:** inventories are PDFs with a text layer. The letter case in the address matters — take links from the site's page rather than guessing. In some indexes the text layer is "scattered" into single letters — glue the single-letter lines together before searching. Check the file numbers from the index against the file titles in the inventory.
- **Paid:** EAIS (remote viewing of digitized files) — in this archive since November 2025 it is 60 ₽ an hour or 110 ₽ for 2 hours; the mark "ОЦ ФП" in an inventory = the file is digitized. From abroad EAIS and a number of oblast archive sites did not open (September 2026).
- Other regions have their own conditions: for example, in Kuzbass part of the documents is in free open access after registration [checked]. See [russian-language-resources.md](russian-language-resources.md).

## Yandex "Archive Search" (Poisk po arkhivam) (yandex.ru/archive) (Russian-language)
- **What is there:** full-text search — **even handwritten text is recognized** — across more than 23 million pages: about 30 Russian archives (Central State Archive of Moscow, TsGAMO [Central State Archive of Moscow Oblast], Orenburg, Omsk, Astrakhan, Irkutsk and others), **periodicals** ("Kommersant" 1909–1917, "Senatskie ob"yavleniya" [Senate announcements], guberniya gazettes, "Vechernyaya Moskva", "Pravda"), **directories** ("Vsya Moskva", "Vsya Rossiya", "Rossiiskii meditsinskii spisok", loss lists of 1914–1917). **There are no Ukrainian archives** — the absence of Podolian documents proves nothing. But there are **Moscow metrical books**: residents of many guberniyas married and died in Moscow.
- **Access:** Free, no login.
- **Pace:** after about **25 rapid requests in a row** connections are dropped. Safe is **one request every 8–9 seconds**. In October 2026 the search did not work for several days, then worked again. Work in the active tab.
- **Techniques:**
  - the search understands cases and pre-reform spelling;
  - the recognized text of the page lies right on the document page — you can read the paragraph you need without opening the scan;
  - the resolution in viewing mode is low — for small text you need the full scan;
  - the OCR of directories confuses columns: check the heading against the scan;
  - for Jewish provincial lines **periodicals** are more valuable: "Kommersant" printed a provincial chronicle with obituaries and trade news, "Senatskie ob"yavleniya" — auctions, pledges and summonses of heirs with full names and patronymics.
- **Experience:** an obituary of a provincial timber dealer (1914); pledges of family members at auctions in Uman (1917) with patronymics; inventories of personal files in the Central State Archive of Moscow.
- **The trap of look-alikes:** namesakes and similar words fill the results (Shefel / Sheffel / Shepel; "shefel" is a grain measure). Check initials, address, telephone.
- Under the service's rules you may not build your own database from its materials [checked].

---

**See also:** [indexed-databases.md](indexed-databases.md) · [directories-and-books.md](directories-and-books.md) · [Archives by country](../guide/2-reference/07-archives-by-country.md) · skills `reading-archive-scans`, `searching-familysearch-films` in [../../skills/](../../skills/)
