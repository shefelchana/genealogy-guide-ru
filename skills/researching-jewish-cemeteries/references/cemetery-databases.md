# Cemetery and burial databases: what was checked and how to search

Markers: **[opened]** means the page was read when this was compiled (October 2026); **[from search results]** means only a search-result snippet was seen; **[did not open]** means the site is closed to automated access or did not respond from our network. A human handles logins, registration, CAPTCHAs and any requests. For a general overview see `catalog/кладбища.md` in the guide.

## Contents
1. Does a cemetery exist and does it survive
2. Name databases: the former USSR
3. Poland
4. Israel
5. USA and the rest of the world
6. Burial-society records
7. Dates: the converter

---

## 1. Does a cemetery exist and does it survive

### JewishGen Cemetery Discovery Project (cdp.jewishgen.org) [opened]
- The former **IAJGS International Jewish Cemetery Project**: the old addresses iajgscemetery.org and iajgs.org/cemetery redirect here.
- It is a catalogue of burial places, not a name search; for individuals it points to JOWBR.
- How to search: region → country → locality. For Eastern Europe, for example: Ukraine has 2,563 places, Belarus 385, Poland 1,578, Moldova 47, Russia 49.
- Each locality has the history of the community, location, sometimes contacts, condition and photos.

### ESJF: European Jewish Cemeteries Initiative (esjf-cemeteries.org) [opened]
- Surveys (including by drone): the home page shows **4,140 surveyed cemeteries in 10 countries** [opened 08.10.2026]. The survey database includes Poland, Ukraine, Slovakia, Hungary, Lithuania, Croatia, Serbia, Georgia, Moldova, Greece and **Bulgaria** [checked by searching the database, 08.10.2026]. **Belarus and Latvia were not found in the database** (Pinsk, Minsk, Brest, Daugavpils: 0 results). Plans for Latvia, Estonia and the former Yugoslavia in 2026-2027 are [not verified].
- **There is no name index.** Each cemetery has a page: region, GPS, address, whether it was demolished, fence, **number of stones, date of the oldest and the newest stone**, history of the community, sometimes a 3D model.
- Page address: `esjf-cemeteries.org/survey/<town>-jewish-cemetery/` (the town in Latin letters, Ukrainian spelling: chudniv, bratslav...). The map with a filter by country and region is at `/surveys-map/` (loaded by script).
- Statuses: demolished and built over; demolished, not built over; unfenced; Jewish section; fenced.

### Lo Tishkach (lo-tishkach.org) [opened: home page and the database page]
- A project of the Conference of European Rabbis and the Claims Conference: the database page lists **11,061 cemeteries and mass graves** in Europe.
- The database itself is embedded as a window from admin.lo-tishkach.org and **did not open** (error 503). Try again later; it has no data on individuals, only places.

## 2. Name databases: the former USSR

### Mitzvat Emet (mitzvatemet.com) [did not open: Cloudflare, 403]
- According to search results: a photo catalogue of more than 90-100 thousand burials in Belarus, Ukraine, Russia, Kazakhstan, Uzbekistan, Moldova and Lithuania; it includes Kyiv (Berkovtsy, Kurenivka), Lviv, Odesa (Third Jewish Cemetery) and Petersburg (Preobrazhenskoe) [from search results].
- Experience of the project: enter the **beginning** of the surname, **choose the suggestion** with the mouse, press «Поиск» ("Search"); the suggestion shows whether the surname is in the catalogue at all. 20 results per page. After about 5 searches in a row a reCAPTCHA appears and the form silently stops submitting. Do not bypass it; try again later. A chat window opens on the page by itself: do not write in it.

### Toldot, cemetery database (toldot.com/life/cemetery) [opened]
- More than 100,000 burials in **49 cemeteries** of Russia, Ukraine, Belarus and Uzbekistan (Moscow: Vostryakovo, Khovanskoe, Malakhovka, Saltykovka; Petersburg; Kazan; Kyiv: Baikove...).
- Fields: surname (required), given name, country / town / cemetery. No registration. The surname is searched as a **substring**. The site itself warns that many stones are in poor condition, so try different spellings.

### Moscow: hevra kadisha register (hevkad.com/burial) [opened]
- Vostryakovo Jewish, Vostryakovo Central, Malakhovka, Saltykovka.
- Search by number, full name, dates of birth and death, row and plot. No registration. The register has no photos; the data are incomplete.

### Petersburg: Preobrazhenskoe Jewish Cemetery [from search results]
- Burials of 1875-1968, about 80 thousand; according to search results about 97% are catalogued; search by surname, initials, years; photos and a plan of the plot.
- Sites: jekl.spb.ru, gravlov.com, aguterbeter.com **did not open** from our network (probably Russian sites being blocked while a VPN is on).

### Kyiv, Odesa, Lviv [from search results]
- Kyiv: the Lukyanivka Jewish cemetery was closed in 1962 and devastated; part of the burials were moved after closure to Berkovtsy, where a Jewish section appeared in the 1960s.
- Odesa: the First (Old) Jewish Cemetery was completely destroyed, so information is archival only; the Third Jewish Cemetery has about 50 thousand burials, with a photo catalogue at Mitzvat Emet.
- Photos of these cemeteries: Mitzvat Emet; a general search of burials in Ukraine: pomnim.online (did not open).

### JOWBR (jewishgen.org/databases/cemetery) [opened]
- More than 7 million records and 908,000 photos, about 9,500 cemeteries in 143 countries.
- Search by surname, given name, town, any field; search types: Phonetically Like, Sounds Like, Starts with, is Exactly (with synonyms for towns and names: Lodz = Litzmannstadt), three levels of Fuzzy; up to four conditions; a comma means OR, a space means AND; region filter.
- According to the project's experience (`catalog/кладбища.md`), results require a free JewishGen login, which a human performs. Details are in the skill `searching-jewishgen`.

### Bessarabia SIG: cemetery project
- About 75 thousand burials in Bessarabia (according to the guide catalogue, `catalog/кладбища.md`).
- Chisinau: 18,751 records and 14,150 photographs in JOWBR, a translation of the register "House of Eternity" (2004) [from search results: JewishGen mailing list].

## 3. Poland

### Foundation for Documentation of Jewish Cemeteries (cemetery.jewish.org.pl) [opened]
- A name database built from inscriptions: Warsaw, Okopowa Street (inventory of 2006-2010), cemeteries of the Mazovia voivodeship, then Suwalki, Augustow, Tarnow and others; the list of cemeteries is under the "Bazy" tab.

## 4. Israel

There is no nationwide name database: each hevra kadisha has its own. Search **in Hebrew**.

| Where | Address | What | Marker |
|---|---|---|---|
| Tel Aviv-Yafo and surroundings (6 cemeteries: Yarkon, Kiryat Shaul, Nahalat Yitzhak, Trumpeldor, Holon and others) | kadisha.biz, search at `/he/search` | search for the deceased without login | [opened] |
| Rehovot | kdr.org.il/deceased | fields: name, surname, date of burial, year of death | [opened] |
| Haifa | kdh.org.il, "Search for deceased" | free search; the search for soldiers is in Hebrew only; **reCAPTCHA is in place** | [opened] |
| Jerusalem (Ashkenazi community) | hkj.org.il/deceased | search by surname, given name | [did not open: Cloudflare] |
| Jerusalem (Sephardi), Ra'anana, Hadera, Petah Tikva | kadishaj.com, kadisha-raanana.co.il, kadisha-hadera.org, kpt.co.il | local searches | [from search results] |
| **BillionGraves / MyHeritage** | billiongraves.com | according to a MyHeritage announcement (02.03.2019) almost all Israeli cemeteries were digitized: photos, GPS, transcription, free; a search in Latin letters finds Hebrew records; burials made after the survey may be missing | [did not open: 403; from search results: blog.myheritage.com, 2019] |

## 5. USA and the rest of the world

- **Find a Grave** (findagrave.com): memorials with photos; a memorial has a photo request for volunteers (needs an account, done by a human) [did not open: 403; from search results].
- **BillionGraves**: photos with GPS; the app supports the Jewish calendar [from search results].
- **JGSNY: burial society plots** (jgsny.org/searchable-databases/burial-society-databases) [opened]: more than 10,600 records from nearly 100 cemeteries in New York, Long Island, Westchester and northern New Jersey; plots of landsmanshaft societies, synagogues, family circles and trade unions. Search by society name, cemetery, keyword or **shtetl** (from 3 characters). There are plot plans and a directory of cemeteries.
- **Geni, cemetery projects**: for example "Jewish Cemeteries Online", "London Jewish Cemeteries", and hometown-society projects with plots in Long Island cemeteries [from search results; Geni pages are closed by Incapsula protection].

## 6. Burial-society records

- **Pinkas of a hevra kadisha** is the society's record book; in emigrant communities it may name the town of origin [from search results].
- According to search results: in 1981 there were 23 known pinkasim (YIVO and the National Library of Israel), and about ten more were found later; examples are the 1895-1925 pinkas of Sighet in Yiddish at the NLI, and the pinkas of Slutsk, about 300 years old.
- Search by shtetl name in the YIVO and NLI catalogues (skill `searching-nli-jewish-press` for the NLI) and in the shtetl's KehilaLinks page on JewishGen.

## 7. Dates: the converter

**Hebcal** (hebcal.com/converter) [opened, tested]. Machine-readable address:
`https://www.hebcal.com/converter?cfg=json&hy=5665&hm=Kislev&hd=12&h2g=1` → 20.11.1904.
Months: Tishrei, Cheshvan, Kislev, Tevet, Sh'vat, Adar (in a leap year **Adar1** / **Adar2**; a plain "Adar" in a leap year is read by Hebcal as Adar II), Nisan, Iyyar, Sivan, Tamuz, Av, Elul. Also: the JewishGen JOS calculator, Steve Morse's "Jewish Calendar Conversions in One Step" and his tombstone converter, where you enter the letters of the date from the stone (stevemorse.org/jcal/tombstone.html) [opened 08.10.2026].
