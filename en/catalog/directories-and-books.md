# Directories and books

What this section covers: where to look for old directories (address calendars, "Vsya Rossiya" [All Russia], medical lists, memorial books of guberniyas [*pamyatnye knizhki*]), books and place directories — and how to search inside them when the recognized text is full of errors. Surname dictionaries and encyclopedias are in [../reading/dictionaries-and-encyclopedias.md](../reading/dictionaries-and-encyclopedias.md). Markers are in [README.md](README.md).

The main rules for all scanned books:
- search **without the first letter** and in both spellings (pre-reform and modern);
- be sure to run a **control** — a known rare surname or name that is certainly in the book; if it is not found, the search is broken and the person is not absent;
- check the **title page**: the year of publication in the description is sometimes wrong.

---

## Place directories (where it is, what it belonged to)

- **JewishGen Communities Database and Gazetteer** (jewishgen.org/Communities): over 6,000 Jewish communities with name variants, population and affiliation by era; about 2.4 million localities in 54 countries, radius search. Free [checked].
- **Radzima.org** — a directory of places in Belarus with historical maps [per FamilySearch].
- **Bessarabia Geographical Dictionary** (Bessarabia SIG) — places of Bessarabia where Jews lived or traded; Excel or PDF [per FamilySearch].
- **bessarabia.ru** — a description of the types of documents in the archives of Moldova, a forum; there is an English version [per FamilySearch].
- **easteurotopo.org** — topographic maps of Eastern Europe [per FamilySearch].
- **"Spiski naselennykh mest Rossiiskoi imperii" (Lists of populated places of the Russian Empire)**; an example for Podolia — "Spiski naselennykh mest Podolskoi gubernii… po evreiskim obshchestvam" (Lists of populated places of Podolia guberniya… by Jewish communities) in the Presidential Library (prlib.ru/item/466841), "Spisok naselennykh mest Podolskoi gub. 1905" (List of populated places of Podolia guberniya 1905) on familio.org [from search results]. (Russian-language)
- **Where Once We Walked** (Mokotoff & Sack) — over 23,500 shtetls with a Jewish population and 17,500 alternative names [page: avotaynu.com, 2026-10-07]; the book is paid.
- **Steve Morse One-Step** (stevemorse.org): Russian ↔ English transliteration, conversion of Jewish calendar dates, Soundex, old telephone directories of Moscow and St. Petersburg [checked].

---

## Libraries and collections

### archive.org (Internet Archive)
- **What is there:** the collection `russianempiregenealogyresources` (840 items): "Rossiiskii meditsinskii spisok" (Russian Medical List) year by year 1810–1925, "Vsya Moskva" (All Moscow) 1846–1936, memorial books of Podolia guberniya (9 volumes, 1859–1911) and Ekaterinoslav guberniya (1864–1917), inventories of personal files of students of Moscow University 1872–1917. As separate books — "Vsya Rossiya" (1899, 1900, 1902), "Fabrichno-zavodskie predpriyatiya Rossiiskoi imperii na 1909 god" (Factory and plant enterprises of the Russian Empire for 1909). Also here is M. Weiner's book *Jewish Roots in Ukraine and Moldova*.
- **Access:** Free, no registration. When downloading from the command line — `curl -L` (otherwise an empty file).
- **How to search:** every volume has a ready text — the file `<identifier>_djvu.txt`; download it and search on your own computer. The built-in "search inside the book" returned nothing.
- **Traps:** the years in the description get confused (of four checked editions of "Vsya Moskva", three turned out to be Soviet); some files are empty or truncated; in the text of the 1911 Podolia memorial book the OCR is poor.
- **Noise:** a short fragment without the first letter finds a lot of extraneous material (for "абай" — Zabaikalye, Babailov, Karabaev).
- **What the "Medspisok" (Medical List) gives:** name, patronymic, year of birth, year of receiving the title, place of service — year by year, a ready biography of a doctor for 20–30 years. The Soviet list of 1924 often gives the Russian form of a name next to the Jewish one (Gersh Shlyumovich = Grigory Solomonovich).
- **For advanced users:** if `grep` does not work on Cyrillic, a regular expression in Python helps.

### Genealogy Indexer (genealogyindexer.org)
- **What is there:** a free full-text search of the recognized text of 2.24 million pages: address calendars, "Vsya Rossiya", "Ves Yugo-Zapadnyi Krai" (The Whole South-Western Region), Galician schematisms, memorial books (yizkor), **World War I loss lists**, school reports. No login and no CAPTCHA.
- **The main rule:** **search in Cyrillic.** Russian directories are recognized in Cyrillic: "Shefel" in Latin letters — 1 match in the whole database, "Шефель" — 15, "Шеффель" — 92. The `ocr` mode is tolerant of recognition errors.
- **Trap:** the "Podolia Gubernia" filter is stuffed with Soviet telephone directories; a zero from it proves nothing — check through "Ukraine" and "Russian Empire+".
- **Experience:** the owner of a sawmill in a village (1895, 30 workers), a merchant in Berdichev (1913).
- **For advanced users:** the form is a POST to `https://genealogyindexer.org/` **without www**; region codes: 19800 — Podolia, 19500 — Kyiv, 19300 — Volhynia, 19000 — Ukraine, 1100 — Galicia. A ready script — the skill `verifying-genealogy-findings` in [../../skills/](../../skills/).

### Google Books (books.google.com)
- **What is there:** scans and snippets of old editions.
- **Example:** a search with a **phrase in pre-reform spelling** ("Вайнбергъ Моисей") found "Lichnyi sostav Imperatorskogo Yuryevskogo universiteta" (Personnel of the Imperial Yuryev University) of 1893 — a line with the student number, name and patronymic. This closed a task that had stood for two weeks.
- **Limitations:** programmatic access quickly exhausts the quota; work by hand.

### HathiTrust (babel.hathitrust.org)
- Full-text search across the shared corpus, full view of editions before 1929. As of 04.10.2026 automated requests are blocked by Cloudflare; it is worth trying by hand in an ordinary browser.

### GPIB — State Public Historical Library (elib.shpl.ru) (Russian-language)
- **What is there:** books of the 18th–20th centuries; **full-text search** (tick "Search in texts"). Open access, books can be downloaded. OCR was not done for all editions.
- **Technique:** for editions without text, look at the table of contents and the index, then the page you need. This is how I. Kamanin's edition "Perepisi evreiskogo naseleniya… 1765–1791" (Censuses of the Jewish population… 1765–1791; Archive of South-Western Russia) is read: it has only a count of souls and households by kahal, **no lists by name**, but it indicates in which town court books (TsDIAK [Central State Historical Archive of Ukraine, Kyiv]) the originals lie.
- **Network:** it opened from abroad too.

### NEB — National Electronic Library (rusneb.ru) (Russian-language)
- **What is there:** books and journals, whole PDFs (for example, V. Guldman, "Podolskii adres-kalendar" [Podolia address calendar], with a text layer).
- **Access statuses (checked 27.09.2026):** "**svobodnyi**" (free) — the scan exists and is open; "**tolko opisanie**" (description only) — **there is no scan at all**, registration will not help; login is needed only for "restricted" access. The status is visible in the results in the "Доступ" (Access) line.
- **Network:** may not open from abroad.
- **For advanced users:** huge files (hundreds of MB) need not be downloaded whole: the server serves chunks (HTTP Range), and the text is extracted from a truncated file. It is more convenient to search by **mask** (the surname with any first letter).

### RGB — Russian State Library (search.rsl.ru) (Russian-language)
- Search **by catalog only**, not by the text of books. The "Rossiiskii meditsinskii spisok" (Russian Medical List) 1809–1916 is digitized, but a surname inside cannot be found through the catalog — you have to page through the volume. May not open from abroad.

### RNB — National Library of Russia (nlr.ru, reading room vivaldi.nlr.ru) (Russian-language)
- "Ves Leningrad" (All Leningrad; 1926, 1931, 1935), memorial books of Podolia guberniya (1859, 1885, 1895, 1900, 1904, 1909, 1911). The pages open without a login.
- **Technique:** the letter you need in a directory is found by the running heads of the pages; a table of contents with page numbers by letter is at nlr.ru/cont/v_l/oglav.php.
- May not open from abroad.

### history.org.ua / LiberUA
- Direct PDFs: "Ves Yugo-Zapadnyi Krai" 1913 (1,177 pages, **images only, no text**), V. Guldman "Podolskii adres-kalendar" 1895. The index of "Ves Yugo-Zapadnyi Krai" on JewishGen is incomplete: the needed surnames sometimes appear in the book itself and not in the index. (Ukrainian-language site)

### Polona (polona.pl) — National Library of Poland
- Full-text search across digitized editions through an open programming interface (for editions under copyright the snippets are empty). The browser version in September 2026 did not load everywhere.

### "Runivers" (runivers.ru) (Russian-language)
- An electronic library on the history of Russia: monographs, atlases, documentary publications; free [checked].

### Presidential Library (prlib.ru) (Russian-language)
- Over 1 million items; open materials are read on the site, the rest — in electronic reading rooms [from search snippet]. May not open from abroad.

### KehilaLinks (kehilalinks.jewishgen.org) and memorial books
- Sites of individual shtetls: histories, photos, lists of surnames, maps. On the Krasilov page — the introduction and the tables of contents of all four volumes of the "Knyha skorboty Ukrainy" (Book of Sorrow of Ukraine) for Khmelnytskyi oblast (name lists of civilian victims 1941–1944 by district).
- **What is online:** only Krasilov (vol. I) and Starokostyantyniv (vol. II); the other districts were not found online. The old shtetlinks address does not work.
- Memorial books (yizkor) — see [../reading/dictionaries-and-encyclopedias.md](../reading/dictionaries-and-encyclopedias.md).

---

**See also:** [press.md](press.md) · [archive-file-scans.md](archive-file-scans.md) · [../reading/dictionaries-and-encyclopedias.md](../reading/dictionaries-and-encyclopedias.md) · [Names, surnames, spellings](../guide/2-reference/03-names-spellings.md)
