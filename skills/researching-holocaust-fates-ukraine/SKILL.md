---
name: researching-holocaust-fates-ukraine
description: >-
  Establishes the fate of Jews who stayed under German occupation in Soviet Ukraine in 1941–1944, and of those who escaped: Yad Vashem names read as documents (the Page of Testimony, who submitted it, when, from what address), the Yahad-In Unum map, ChGK acts (GARF R-7021, USHMM microfilm), post-war victim lists, yizkor books, the Babyn Yar database, evacuation cards, the "Book of Sorrow of Ukraine", Transnistria as a different fate, and each source's false zeros. Use when the user asks "what happened to the family in 1941", "were they killed or evacuated", "when were the Jews of this town shot", "who submitted this Page of Testimony", or a branch disappears after 1941. Not for soldiers, POWs, the repressed, the Leningrad siege or ZAGS (use soviet-era-records). Also triggers on Russian requests: «судьба семьи в войну», «погибли в Холокост», «погибли в гетто», «расстрел евреев местечка», «листы свидетельских показаний», «Книга скорботи».
---

# Holocaust fates in Soviet-occupied Ukraine

For Jews of Podolia, Volhynia, Kyiv and Zhytomyr regions there are rarely personal documents of death. The fate is assembled from **lists made by others** (relatives, Soviet commissions, survivors of the town, landsmanshaft societies) and from **what is known about the place** (dates of shootings, ghetto, Romanian or German zone). Each source misses different people. Keep two questions apart: **what happened in the place** and **what happened to this person**.

Related skills: `soviet-era-records` (evacuation, soldiers, ZAGS, repression), `researching-jewish-cemeteries` (landsmanshaft plots, gravestones with memorial inscriptions), `reading-hebrew-yiddish-sources` (yizkor books, Hebrew pages), `identifying-places` (which zone, current name), `verifying-genealogy-findings`.

## 1. Order of work

1. **The place first.** Current name in Latin and Ukrainian, the 1941 district, and the **zone**: German civil administration (Reichskommissariat Ukraine), military zone, or **Romanian Transnistria** (south of Podolia between the Dniester and the Southern Bug). In Transnistria the typical fate was ghettos and camps with deportations and deaths from hunger and typhus, not mass shootings in the first months; many survived. Write the zone before interpreting any list.
2. **The dates of actions in the place** (Yahad-In Unum, encyclopedias, ChGK acts) — §2.
3. **The names** — §3, every source, with all spellings ("sounds like" searches; Russian, Ukrainian, Yiddish, Hebrew, Polish forms).
4. **The escape routes** — evacuation cards, Red Army, later Soviet records — §4. A person on an evacuation card in 1941–1942 was alive then.
5. **Put both together** in a fate table (§6), with levels.

## 2. Sources about the place

- **Yahad-In Unum map** (yahadmap.org): a profile per execution site — number of victims, sites and dates of actions, extracts from local witnesses' testimonies and from ChGK acts. Works without sign-in; the list of all profiles is on the map's home page; search by the current Latin name. No profiles for many small villages and for Romanian-zone places. Names of victims are almost never there: it is about the place, not the people. Tested November 2026 (source: K. Prince Hollenberg, RootsTech 2025, "Navigating Holocaust Resources Online", [handout](https://cms-z-assets.familysearch.org/30/20/fc651668d8f7cf796caa339cc5c4/rt-navigating-holocaust-resources-online-handout-kaye-prince-hollenberg.pdf)).
- **Encyclopedias**: "Холокост на территории СССР" (ed. I. Altman, 2009; places with at least 100 Jews killed or a ghetto), A. Kruglov's works, USHMM "Encyclopedia of Camps and Ghettos" vol. II (ghettos in the occupied East; free download). Use them for dates and for the source list of each article.
- **Yad Vashem "The Untold Stories"**: killing sites in the occupied USSR.
- **ChGK acts** (Extraordinary State Commission, 1944–1945): reports by district and village, often with name lists of victims. Originals in **GARF fond R-7021**; USHMM microfilm **RG-22.002M** with an index to about 1,456 places. Hard handwriting, Russian, names distorted by the clerks; lists are incomplete and sometimes list families as "X with family".

The date of an action in the family's last known town is a **question**, not a proof of death: did they flee, were they deported, had they moved before 1941?

## 3. Sources about the people

| Source | What to read | False zero |
|---|---|---|
| **Yad Vashem central names database** (collections.yadvashem.org) | **Open the record and the scan, not just the line.** For a Page of Testimony read the **submitter's name, relation, address and the date of submission**: the submitter was a living relative then, and the way to the surviving branch. Search the tabs victim, **submitter**, other (mother's maiden name, spouse). Searching by submitter gathers all pages one person filed (two spellings in one town can turn out to be one family). Note the source type of every record: Page of Testimony, a list (evacuation, local list, ChGK-based), a memorial book | absence proves nothing: many families had no one left to file a page; check every spelling; the first API call returns an empty body by design |
| **Post-war local victim lists** (e.g. lists linked from town pages on jewua.org, compiled by survivors from memory) | name, often "with family", sometimes age or street | incomplete, from memory; spelling Russian or Ukrainian |
| **Memorial (yizkor) books** (JewishGen Yizkor Book Project translations; NYPL and YIVO scans) | chapters on the town, **memorial pages / "plaques"** listing the dead with "from <town>", sometimes the donor's name (a surviving relative) | a book of a regional centre may include the town only as a chapter; the plaque lists only families with someone to commemorate them |
| **Landsmanshaft memorial monuments** in US cemeteries (e.g. "to the martyrs of <town> killed by the Nazis 1941–1945") | names engraved in English and Hebrew; the memorial committee by name | names often only on photographs (Museum of Family History pages), not typed; find the plot through the JGS NY Burial Society database (`researching-jewish-cemeteries`) |
| **Babyn Yar names database** (babynyar.org) | about 29,700 names, with age, address, relatives, occupation | Kyiv only |
| **JDC Names Index** (names.jdc.org) | names in JDC records (relief, emigration, post-war) | behind a Cloudflare check: open it in the person's browser (tested November 2026) |
| **USHMM Holocaust Survivors and Victims Database** (old address ushmm.org/online/hsv) | the same evacuation cards, lists of victims and survivors; Exact, Fuzzy and D-M Soundex modes | **alive on 20 November 2026**: the old address leads to the new page and the search form opens, but results are behind a "Browser Verification" — use the person's browser, not a script |
| **"Книга скорботи України"** (Book of Sorrow) | civilian victims of the occupation by oblast and district | only some parts are online (KehilaLinks, archive.org): for one oblast with four volumes, only two districts were found online (November 2026) |
| Arolsen Archives, EHRI portal | deportations, camps, archival descriptions | mostly outside the occupied USSR |
| **Gidonim Mass Grave Database** (gidonim.com/mgt) | — | **Poland only**: none of 779 places in its list is in Ukraine, Belarus or Moldova (tested November 2026). Do not search it for Ukrainian towns |

## 4. Those who escaped

- **Evacuation cards** (Yad Vashem: data on more than half of roughly 1.5 million evacuated Jews [from search results]; USHMM): read the whole card — patronymic, occupation, family members, from where and to where, address. They prove patronymics and kinship where metrical books are missing.
- **Tashkent database** (JewishGen, 151,966 cards of 1941–1942 from the Central State Archive of Uzbekistan) with a scan of each card.
- Red Army soldiers and the missing — `soviet-era-records`. A man at the front and his family killed at home is a common pattern: search both.
- "Not on an evacuation card" does not mean "stayed": many evacuation lists are not in any database.

## 5. Traps

1. **One source, one fate.** A Page of Testimony can be wrong about the date and place (filed decades later, from memory). Two independent sources (a page and a local list or ChGK list) are stronger than one.
2. **The same person in two "fates".** A name on a victim list and on an evacuation card may be two people with one name: compare age, parents, address (`verifying-genealogy-findings`, namesake table).
3. **Romanian zone vs German zone** — different fates, different archives; check the zone before reasoning from dates.
4. **A list that says "with family"** does not name the family members: do not assign children to it without another source.
5. **Living people.** Submitters and descendants may be alive: record what is needed for research, do not publish living people's data, and leave contact to the person.

## 6. Worked example (invented family)

The Brener family (invented, in an invented town "N."), last known there in 1940: father Leib, mother Rivka, children Sonia 1928 and Mendel 1932.
1. Place: N. was in the German zone (the map of zones, not the family story, decides this). The Yahad profile gives two actions in 1942 at two sites, with testimony extracts. → The date range of the danger.
2. Yad Vashem: Leib Brener, Page of Testimony filed 1957 by "Chaim Brener, brother, Haifa, <street>"; the scan says "killed 1942 in N. with wife and two children". → Leib 🟡 (page read on the scan, one source filed 16 years later); wife and children ⚪ (not named on the page).
3. Post-war local list of N.: "Бренер Лейб с семьёй". → A second, independent source for Leib's fate in N. → Leib 🟢.
4. Tashkent database: "Бренер Соня Лейбовна, 1928", evacuated from the oblast centre. → Sonia was alive in 1942; the page's "two children" was wrong or the family was split: "Sonia killed" 🔴.
5. Next: Mendel — search evacuation cards and the "Book of Sorrow" volume for the district; Chaim Brener in Haifa — the living branch (contact is the person's decision).

## Answer format

1. The place: names, zone, dates of actions with sources.
2. A fate table per person: source (with record id, scan and submitter) · what it says verbatim · date and place of death or of the last sign of life · level.
3. Zeros with spellings tried and the date of the search; sources not yet searched and why (browser needed, not online).
4. Living people found (submitters, descendants) — reported to the person, not contacted.
