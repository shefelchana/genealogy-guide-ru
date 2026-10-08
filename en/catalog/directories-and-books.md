# Directories and books

What this section covers: where to look for old directories (address calendars, "All Russia", medical lists, memorial books (*pamyatnye knizhki*)), books and place directories — and how to search inside them when the recognized text is full of errors. Surname dictionaries and encyclopedias are in [dictionaries-and-encyclopedias.md](../reading/dictionaries-and-encyclopedias.md). Markers and interface-language notes are in [README.md](README.md).

The main rules for all scanned books:
- search **without the first letter** and in both spellings (pre-reform and modern);
- always run a **control** — a known rare surname or a name that is certainly in the book; if it is not found, the search is broken, not the person absent;
- check the **title page**: the year of publication in the description is sometimes wrong.

Don't read Russian? Most of the books below are in Russian and are searched in Cyrillic — see [For English speakers](../guide/0-start/08-for-english-speakers.md).

---

## Place directories (where it is, what it belonged to)

- **JewishGen Communities Database and Gazetteer** (jewishgen.org/Communities) (English interface): more than 6,000 Jewish communities with name variants, population and affiliation by period; about 2.4 million localities in 54 countries, radius search. Free [checked].
- **Radzima.org** — a directory of places in Belarus with historical maps [per FamilySearch].
- **Bessarabia Geographical Dictionary** (Bessarabia SIG) — places of Bessarabia where Jews lived or traded; Excel or PDF [per FamilySearch].
- **bessarabia.ru** — a description of the types of documents in the archives of Moldova, a forum; there is an English version [per FamilySearch].
- **easteurotopo.org** — topographic maps of Eastern Europe [per FamilySearch].
- **"Lists of inhabited places of the Russian Empire"** (Списки населённых мест Российской империи); an example for Podolia — "Lists of inhabited places of Podolia guberniya… by Jewish societies" in the Presidential Library (prlib.ru/item/466841), "List of inhabited places of Podolia gub. 1905" on familio.org [from search snippet].
- **Where Once We Walked** (Mokotoff & Sack) — more than 23,500 shtetls with a Jewish population and 17,500 alternative names [checked: avotaynu.com, 2026-10-07]; the book is paid.
- **Steve Morse One-Step** (stevemorse.org): Russian ↔ English transliteration, conversion of Jewish-calendar dates, Soundex, old telephone books of Moscow and St Petersburg [checked].

---

## Libraries and collections

### archive.org (Internet Archive) (English interface)
- **What is there:** the collection `russianempiregenealogyresources` (840 items): the "Russian Medical List" (Российский медицинский список) by year 1810–1925, "All Moscow" (Вся Москва) 1846–1936, memorial books of Podolia guberniya (9 volumes, 1859–1911) and Ekaterinoslav (1864–1917), inventories of personal files of Moscow University students 1872–1917. Separate books — "All Russia" (Вся Россия) (1899, 1900, 1902), "Factory and plant enterprises of the Russian Empire for 1909". Also here is M. Weiner's book *Jewish Roots in Ukraine and Moldova*.
- **Access:** Free, no registration. When downloading from the command line use `curl -L` (otherwise an empty file).
- **How to search:** every volume has a ready text — the file `<identifier>_djvu.txt`; download it and search on your own computer. The built-in "search inside the book" returned nothing.
- **Traps:** the years in the description get confused (of four checked issues of "All Moscow" three turned out to be Soviet); some files are empty or truncated; in the text of the Podolia memorial book of 1911 the OCR is bad.
- **Noise:** a short fragment without the first letter finds a lot of junk (for "абай" — Zabaikalye, Babailov, Karabaev).
- **What the "Medical List" gives:** name, patronymic, year of birth, year the title was received, place of service — year by year, a ready biography of a doctor over 20–30 years. The Soviet list of 1924 often gives the Russian form of a name next to the Jewish one (Gersh Shlyumovich = Grigory Solomonovich).
- **For advanced users:** if `grep` does not work on Cyrillic, a regular expression in Python helps.

### Genealogy Indexer (genealogyindexer.org)
- **What is there:** free full-text search through the recognized text of 2.24 million pages: address calendars, "All Russia", "The Whole South-Western Region" (Весь Юго-Западный край), Galician schematisms, memorial (yizkor) books, **World War I casualty lists**, school reports. No login and no CAPTCHA.
- **The main rule:** **search in Cyrillic.** Russian directories were recognized in Cyrillic: "Shefel" in Latin letters — 1 match in the whole database, "Шефель" — 15, "Шеффель" — 92. The `ocr` mode is tolerant of recognition errors.
- **Trap:** the "Podolia Gubernia" filter is stuffed with Soviet telephone books; a zero from it proves nothing — check through "Ukraine" and "Russian Empire+".
- **Experience:** the owner of a sawmill in a village (1895, 30 workers), a merchant in Berdychiv (1913).
- **For advanced users:** the form is a POST to `https://genealogyindexer.org/` **without www**; region codes: 19800 — Podolia, 19500 — Kyiv, 19300 — Volhynia, 19000 — Ukraine, 1100 — Galicia. A ready script — the skill [`verifying-genealogy-findings`](../../skills/verifying-genealogy-findings/SKILL.md) (in Russian).

### Google Books (books.google.com)
- **What is there:** scans and snippets of old editions.
- **Example:** a search by a **phrase in pre-reform spelling** ("Вайнбергъ Моисей") found "The Personnel of the Imperial Yuryev University" of 1893 — a line with the student's number, name and patronymic. That closed a question that had stood open for two weeks.
- **Limits:** programmatic access quickly exhausts the quota; work by hand.

### HathiTrust (babel.hathitrust.org)
- Full-text search across the common corpus, full view of editions up to 1929. On 04.10.2026 automated requests were blocked by Cloudflare; it is worth trying by hand in an ordinary browser.

### GPIB — State Public Historical Library (elib.shpl.ru) (in Russian)
- **What is there:** books of the 18th–20th centuries; **full-text search** (tick "Search in texts"). Open access, books can be downloaded. OCR has not been done for all editions.
- **Technique:** for editions without text, look at the table of contents and the index, then the page you need. This is how I. Kamanin's edition "Censuses of the Jewish population… 1765–1791" (Archive of South-Western Russia) is read: it has only the count of souls and households by kahal, **no lists by name**, but it states in which municipal court books (TsDIAK — Central State Historical Archive of Ukraine) the originals lie.
- **Network:** it opened from abroad too.

### NEB — National Electronic Library (rusneb.ru) (in Russian)
- **What is there:** books and journals, whole PDFs (for example, V. Guldman, "Podolia Address Calendar", with a text layer).
- **Access statuses (checked 27.09.2026):** "**free**" — the scan exists and is open; "**description only**" — **there is no scan at all**, registration will not help; a login is needed only for "restricted" access. The status is visible in the results in the line "Access".
- **Network:** may not open from abroad.
- **For advanced users:** huge files (hundreds of MB) need not be downloaded whole: the server serves them in pieces (HTTP Range), and the text is extracted from a truncated file. It is more convenient to search with a **mask** (the surname with any first letter).

### RGB — Russian State Library (search.rsl.ru) (in Russian)
- Search **by catalog only**, not by the text of books. The "Russian Medical List" 1809–1916 is digitized, but a surname inside it cannot be found through the catalog — you have to page through the volume. May not open from abroad.

### RNB — National Library of Russia (nlr.ru, reading room vivaldi.nlr.ru) (in Russian)
- "All Leningrad" (Весь Ленинград) (1926, 1931, 1935), memorial books of Podolia guberniya (1859, 1885, 1895, 1900, 1904, 1909, 1911). Pages open without a login.
- **Technique:** the letter you need in a directory is found from the running heads of the pages; a table of contents with page numbers by letter is at nlr.ru/cont/v_l/oglav.php.
- May not open from abroad.

### history.org.ua / LiberUA
- Direct PDFs: "The Whole South-Western Region" 1913 (1,177 pages, **images only, no text**), V. Guldman, "Podolia Address Calendar" 1895. The index of "The Whole South-Western Region" on JewishGen is incomplete: in the book itself the surnames you need are sometimes there, but in the index they are not.

### Polona (polona.pl) — National Library of Poland
- Full-text search across digitized editions through an open programming interface (for editions under copyright the snippets are empty). The browser version did not load everywhere in September 2026.

### "Runiverse" (Руниверс; runivers.ru) (in Russian)
- An electronic library on Russian history: monographs, atlases, document publications; free [checked].

### Presidential Library (prlib.ru) (in Russian)
- More than 1 million items; open materials are read on the site, the rest in electronic reading rooms [from search snippet]. May not open from abroad.

### KehilaLinks (kehilalinks.jewishgen.org) and memorial books
- Sites of individual shtetls: histories, photos, lists of surnames, maps. The Krasilov page has an introduction and the tables of contents of all four volumes of the "Book of Sorrow of Ukraine" (Книга скорботи України) for Khmelnytskyi oblast (lists by name of civilian victims 1941–1944 by district).
- **What is online:** only Krasilov (vol. I) and Starokostiantyniv (vol. II); the other districts were not found online. The old shtetlinks address does not work.
- Memorial (yizkor) books — see [dictionaries-and-encyclopedias.md](../reading/dictionaries-and-encyclopedias.md).

---

**See also:** [press.md](press.md) · [archive-file-scans.md](archive-file-scans.md) · [dictionaries-and-encyclopedias.md](../reading/dictionaries-and-encyclopedias.md) · [Names, surnames, spellings](../guide/2-reference/03-names-spellings.md)
