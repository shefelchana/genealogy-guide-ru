# Archives, file names, catalogues

Read before the first query to a new archive: here are the abbreviations, how they are written in Commons file names, and where to get inventories.

## 1. Archive abbreviations in Commons file names

Checked with a `list=allimages` prefix query (October 2026): files with these prefixes exist. Letter case matters ("ДАХмО", not "ДАХМО").

| Prefix | Archive | Notes |
|---|---|---|
| ЦДІАК | Central State Historical Archive of Ukraine, Kyiv (TsDIAK) | the form `ЦДІАК 0256_0002_0101` also occurs (numbers with zeros joined by underscores) |
| ЦДІАЛ | Central State Historical Archive of Ukraine, Lviv (TsDIAL) | Galicia |
| ДАК | State Archive of the City of Kyiv | city fonds, Kyiv ZAGS (R-1654) |
| ДАКО | State Archive of Kyiv Oblast (DAKO) | `ДАКО - Фонд N Опис N Справа N` also occurs |
| ДАХмО | State Archive of Khmelnytskyi Oblast (DAKhmO; the former Podolia guberniya, Kamianets) | revisions fond 226, Jewish metrical books fond 227, district ZAGS R-6435…R-6453 |
| ДАВіО | State Archive of Vinnytsia Oblast (DAViO) | `ДАВіО - …` and `ДАВіО -…` occur |
| ДАЖО | State Archive of Zhytomyr Oblast (Volhynia guberniya) | `ДАЖО - …` occurs |
| ДАОО | State Archive of Odesa Oblast (DAOO) | |
| ДАЧвО | State Archive of Chernivtsi Oblast (Bukovina) | |
| ДАЧО | State Archive of Chernihiv Oblast | |
| ДАЧкО | State Archive of Cherkasy Oblast | |
| ДАКрО | State Archive of Kirovohrad Oblast | |
| ДАПО | State Archive of Poltava Oblast | |
| ДАХО | State Archive of Kharkiv Oblast | |
| ДАХеО | State Archive of Kherson Oblast | |
| ДАМО | State Archive of Mykolaiv Oblast | |
| ДАДнО, ДАДО | State Archive of Dnipropetrovsk Oblast | both forms occur |
| ДАДоО | State Archive of Donetsk Oblast | |
| ДАЛуО | State Archive of Luhansk Oblast | |
| ДАЗпО | State Archive of Zaporizhzhia Oblast | |
| ДАСО | State Archive of Sumy Oblast | |
| ДАЛО | State Archive of Lviv Oblast | |
| ДАТО | State Archive of Ternopil Oblast | |
| ДАІФО | State Archive of Ivano-Frankivsk Oblast | |
| ДАРО | State Archive of Rivne Oblast | |
| ДАВоО | State Archive of Volyn Oblast | |
| ДАЗО | State Archive of Zakarpattia Oblast | |
| ДАВО | ⚠️ **Voronezh (Russia)**, not Volyn | Volyn is ДАВоО |

If a prefix gives nothing, search with `list=search` by the reference without a prefix: uploaders write the abbreviation in different ways.

## 2. Sample file names

| What | Sample |
|---|---|
| file, "dotted" form | `ДАХмО 227-1-137. 1800-1804. Про порушення прав міщан м. Бар ….pdf` [On the violation of the rights of townspeople of the town of Bar …] |
| file, hyphen form | `ДАХмО - 226-80-639 Відомості про … 1816-1820.pdf` [Information on … 1816-1820] |
| file with the year in brackets | `ДАЛО Р-3321-1-10 Книга державної реєстрації шлюбу (1940).pdf` [Book of state registration of marriage (1940)] |
| file with a letter | `ЦДІАК 127-1012-1197а. 1801. Метричні книги церков Уманського повіту.pdf` [Metrical books of the churches of Uman uezd] |
| paper inventory | `ДАХмО фонд 227 опис 1.pdf` [fond 227 inventory 1]; additions such as "поновлено" [renewed] occur |
| consolidated catalogue | `ЗВЕДЕНИЙ КАТАЛОГ МЕТРИЧНИХ КНИГ, ЩО ЗБЕРІГАЮТЬСЯ В ДЕРЖАВНИХ АРХІВАХ УКРАЇНИ міжархівний довідник. Т. N.pdf` [Consolidated catalogue of metrical books held in the state archives of Ukraine, inter-archive reference book, vol. N] |
| catalogue of a single archive | `Державний архів Одеської області. Зведений каталог метричних книг. Випуск 1. ….pdf` [State Archive of Odesa Oblast. Consolidated catalogue of metrical books. Issue 1] |

In the API, spaces and underscores in names are equivalent; in an `allimages` response names come with underscores.

## 3. Paper inventories on Commons

- Continuous series of inventories: for DAKhmO about a thousand files, for DAViO about two hundred (2026). To list a fond's inventories: `list=allimages`, `aiprefix=<ARCHIVE> фонд <N> опис`.
- For large fonds the inventory is split into volumes (`опис 1 том 1–5`) and supplements (`1д`, `2д` …): check them all.
- Not all inventories are digitised: for example, for DAKhmO fond 226 Commons has no inventories 1–30. Their files are available only in the archive: this is a limit of the source, not "no files".
- An inventory of hundreds of MB is often not served whole (HTTP 429); read it page by page with thumbnails at 3840 px width.

## 4. Wikisource: the structure of the "Архів:" namespace

- `Архів:Архіви`: the list of archives.
- `Архів:<ARCHIVE>`: the archive's fonds; `Архів:<ARCHIVE>/Р`: Soviet fonds (convenient for finding "метричні книги" [metrical books] for ZAGS).
- `Архів:<ARCHIVE>/<fond>/<opys>`: the listing of an inventory: a template with title, years and a link in the notes to the file of the paper inventory; a table of files.
- `Архів:<ARCHIVE>/<fond>/<opys>/<sprava>`: the file's subpage with a link to the Commons file.
- ⚠️ A listing is a sample (sometimes 3% of the inventory's files) and is sometimes wrong in titles. It is not suitable for negative conclusions.

## 5. Consolidated catalogue of metrical books: the volumes

Checked against the volume title pages on Commons (October 2026):

| Volume | Oblasts (state archives) | Year |
|---|---|---|
| 1 | Volyn, Dnipropetrovsk, Zakarpattia | 2009 |
| 2 | Kyiv, Mykolaiv, Rivne, Sumy | 2012 |
| 3 | Ternopil, Cherkasy, Chernivtsi; city of Kyiv, city of Sevastopol | 2010 |
| 4 | Donetsk, Ivano-Frankivsk, Luhansk, Odesa, Poltava | 2012 |
| 5, bks. 1–2 | Kharkiv | 2012 |
| 6 | Autonomous Republic of Crimea, Zaporizhzhia, Kherson | 2012 |
| 7 | Vinnytsia, Kirovohrad | 2012 |
| 8, bks. 1–2 | Khmelnytskyi | 2013 |
| 9, bks. 1–2 | Zhytomyr | 2018 |
| 10, bks. 1–3 | Chernihiv | 2019–2021 |

Lviv oblast is not in volumes 1–10. The Odesa oblast archive also has its own catalogue of metrical books (issues 1–2, also on Commons).

The volumes are digital PDFs with a text layer; the whole catalogue (15 books) is about 30 million characters, and a text search takes seconds. TsDIAK is not itemised in the catalogue at all.

## 6. Where else to look for a reference in Ukraine

- The Inter-archival search portal (searcharchives.net.ua): 13 archives, search by names of fonds and files, annotations and indexes.
- The archium sites of the archives (for example archium.cdiak.archives.gov.ua, archium.dahmo.gov.ua): search by file titles; coverage is incomplete.
- FamilySearch: films of metrical books of TsDIAK, TsDIAL and the oblast archives (skill `searching-familysearch-films`).
