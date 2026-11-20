---
name: identifying-places
description: Identifies a shtetl, town or village of the former Russian Empire, Poland, Galicia, Bukovina or Bessarabia from a distorted or partial name, determines which country, guberniya, uezd, volost, parish or rabbinate it belonged to in the year that matters, and names the archive that should hold its records. Uses JewishGen Communities and Gazetteer (Daitch-Mokotoff), Where Once We Walked, the Lists of Populated Places of the Russian Empire (Spiski naselyonnykh mest), Vasmer's Namenbuch, old maps (three-verst map, Mende, Strelbitsky, WIG, Mapster) and a timeline of border and name changes (Bessarabia 1812, 1856–1878, 1918–1940; Galicia; interwar Poland; Soviet renamings). Finds villages that no longer exist and separates same-named places by uezd and volost. Produces a place card from assets/place-card.md. Use whenever the user asks where a shtetl is, what it is called now, which uezd it belonged to, which archive to search, says a US document gives an unreadable town name, or gives a town name from a manifest, a family story or a tombstone. Also triggers on Russian requests: «где это местечко», «как сейчас называется», «к какому уезду относилось», «в каком архиве искать», «в американском документе написано непонятное название».
---

# Identify the place and find its archive

## Why the place matters more than the surname

Records of the Russian Empire are kept **by place**: metrical books by rabbinate or parish, revision lists (*revizskie skazki*) by uezd and the society of registration, a Soviet ZAGS (civil registry office) by district. Until the place is identified down to uezd and volost **for the relevant year**, searching for documents is pointless: you do not know which archive or which inventory to use. A mistake about the place produces the most expensive false conclusions: a week spent reading the records of a different village with the same name.

## Input: what you may have in hand

- a distorted name from an American, Canadian or Argentine document ("Pocolifoff", "Proskaw", "Kaminetz, Russia");
- a name from a family story ("near Vinnitsa, a shtetl on a river");
- an entry "meshchanin of m. N" in a metrical record: this is the **place of registration** (*pripiska*), not the place of residence;
- an inscription on a gravestone in Hebrew or Yiddish;
- a Soviet name that replaced the old one (or vice versa).

For emigration documents where the name appears, see the skill `tracing-emigrants-to-origin`; for reading Hebrew and Yiddish on gravestones, `reading-hebrew-yiddish-sources`.

## Order of work

```
- [ ] 1. Write down the name VERBATIM and all known features of the place
- [ ] 2. Build spelling variants
- [ ] 3. Find candidates in gazetteers
- [ ] 4. Screen the candidates against the features
- [ ] 5. Jurisdiction by year: state → guberniya → uezd → volost → rabbinate/parish
- [ ] 6. Archive and fonds for the relevant years
- [ ] 7. Fill in the place card (assets/place-card.md)
```

### 1. Verbatim, and the features

Write the name **exactly as in the source**, with the source and year. Then collect everything except the name: the nearest large town, a river, a border, the language, the occupations of the inhabitants, how far it was to the railway station, which country the narrator considered the place to belong to at the time of the telling. Why: there are dozens of similar names, and you will screen them precisely by these features.

⚠️ In emigrant documents the country and guberniya are written **as at the time of the telling**: "Roumania" for Bessarabia in the 1920s, "Poland" for Volhynia in the 1930s, "Austria" for Galicia. This is not an error but a hint about the years.

### 2. Spelling variants

The name passed through a clerk, a foreign alphabet and the ear. Build variants like this:
- **endings**: -ов / -off / -ow / -ew / -iv / -uv (Проскуров (Proskurov) = Proskurow = Proskuriv); -ец / -etz / -ets / -ec / -iec; -ка / -ka; -ичи / -icze / -ichi;
- **German and Polish spelling**: sch / sz / ш (sh), tsch / cz / ч (ch), w / в (v), j / й (y), ż / ж (zh);
- **Yiddish**: vowels shift (Каменец (Kamenets) → Kaminetz, Kamenitz), final -ов is often dropped;
- **Ukrainian and Russian** spelling: и/і/ы (i/i/y), е/є (e/ye), г/х (g/h/kh) (Галич / Halych), case endings and language forms in catalogues ("Білилівка / Белиловка" (Bilylivka / Belilovka), Ukrainian / Russian);
- **prefixes**: Старый / Новый (Old / New), Великий / Малый (Great / Little), Польный / Русский (Polish / Russian) are often lost in stories;
- **transliteration decides**: a query for "Kamenets-Podolsk" may give zero, while "Kamenets" gives eight matches. Start with a short stem.

### 3. Candidates

Start with the tools that search **by sound**, then move to the exact gazetteers. A list with purposes and limitations is in `references/gazetteers-and-maps.md`; read it at this step.
1. **JewishGen Communities Database**: communities with name variants (including Yiddish ones) and **jurisdiction by era**; **JewishGen Gazetteer**: millions of localities, search by Daitch-Mokotoff Soundex and by radius from a known town.
2. **Where Once We Walked**: about 23,500 places with a Jewish population and name variants (a book).
3. **"Lists of Populated Places of the Russian Empire"** (*Spiski naselyonnykh mest Rossiiskoi imperii*): by guberniya, uezd and volost; **they cannot be used without knowing the guberniya**, and the Kingdom of Poland is not in them.
4. **Vasmer, Russisches Geographisches Namenbuch**: the fullest list of names; paper only.
5. For Poland and Galicia: Słownik geograficzny Królestwa Polskiego, the JRI-Poland town index, Gesher Galicia; for Bessarabia: the Bessarabia Geographical Dictionary; for Belarus: Radzima.org.

Record **all** the candidates, not just the first one that fits.

### 4. Screening

- Compare each candidate with the features from step 1: distance to the named town, the river, the guberniya from other family documents.
- ⚠️ **A matching name proves nothing until the uezd and volost are checked.** Villages with the same name in one guberniya are normal (in Podolia alone there may be several villages with one and the same name, in different uezds).
- A hint from estate documents: a **prefix with the owner's surname** in the name of a works or estate (of the type "Familiyevo-Selsky zavod", the Familiyev village works) indicates which of the same-named villages is meant.
- A distance of up to 20-60 versts between the place of registration and the place of residence is the usual marriage and trading circle, not evidence of kinship.
- If two candidates remain, record it that way, with arguments for and against. Do not choose silently.

### 5. Jurisdiction by year

The same village in 1850, 1910, 1930 and 1950 could belong to different guberniyas, uezds, districts and even states. Documents are sought in the archive of the jurisdiction **in force in the year of the event**.

A chronology of border changes and administrative reforms by region is in `references/border-changes.md`. Read it for every place where the event fell in years of reforms or wars. Key cases:
- **Bessarabia**: Russian from 1812; **the south (Izmail, Kiliya, Bolgrad, Cahul) in 1856-1878 belonged to the Principality of Moldavia / Romania**; all of Bessarabia in 1918-1940 and 1941-1944 was Romania. Someone born there in the 1860s does not and cannot have a Russian metrical record.
- **Galicia** was Austria until 1918, Poland in 1919-1939; **western Volhynia and Belarus** were Poland in 1921-1939.
- **Soviet reforms**: guberniyas and uezds → okrugs (1923-1930) → districts and oblasts (from the 1930s); mass renamings in the 1920s-1950s and after 2016 in Ukraine.

JewishGen Communities shows the jurisdiction by era; use it as a first check, but for the year of the event verify against the Lists of Populated Places or a directory of uezds.

### 6. Archive

- Pre-revolutionary documents are in the archive of the **present-day oblast** to which the guberniya or uezd archive passed (for Ukraine: the "Consolidated Catalogue of Metrical Books" (*Zvedenyi katalog metrychnykh knyh*), skill `ukrainian-archives-on-commons`; for Moldova: ANRM, the National Archives of the Republic of Moldova, and FamilySearch films, skill `searching-familysearch-films`).
- Documents of the central institutions of a guberniya may lie not in the oblast where the village now is: the guberniya capital is sometimes in a neighbouring oblast.
- Romanian, Polish and Austrian periods are in the archives of the corresponding systems (Polish civil registration, Austrian metrical districts: the record of a small shtetl may lie in the book of a neighbouring, larger one).
- What should have survived for a shtetl: Routes to Roots / Miriam Weiner's book *Jewish Roots in Ukraine and Moldova* (on archive.org only for temporary lending, with a login).
- The metrical books of a shtetl without a crown rabbi (*kazyonny ravvin*) could be passed to the **zemsky court, sometimes of a neighbouring uezd**; then they lie in the court's fond, not the rabbinate's (details: `ukrainian-archives-on-commons`).
- Before concluding "nothing has survived for this place", search the internet for the place name together with the word "genealogy" (in Russian «генеалогия»): forums have often already described what survived and where.

### 7. The place card

Fill in `assets/place-card.md`: all variants of the name with sources, the candidates and why one was chosen, the jurisdiction by year with a source on each line, coordinates and map, archives and fonds, what has already been checked. One place, one card; put in links to the gazetteers rather than copying them.

## If the village no longer exists

1. Determine the **locality** from documents: neighbouring villages, a river, the volost, the parish or rabbinate.
2. Find the surviving neighbours on a modern map.
3. Overlay old maps (Schubert's three-verst map, Mende, Strelbitsky, survey maps; for Poland and Galicia: WIG, Mapster, Arcanum) and find the vanished name next to its neighbours.
4. Check the Lists of Populated Places for the relevant year: uezd, volost, number of households.
5. Record in the card on which map and of what year it was found; coordinates with their source.

Khutors (hamlets), folwarks (manorial farms), suburbs ("predm.") and works often do not appear in volost lists as separate points: look for them in estate descriptions and on large-scale maps.

## Rules

- Every conclusion about a place comes with a source and a year. "Now it is village X of district Y" without a link to a gazetteer is not a conclusion.
- Read the place name that goes into a conclusion on the scan at full resolution: in a preview «Проскуровъ» (Proskurov) and «Проскуровкъ» (Proskurovk-) are indistinguishable, yet they are a town and a village in different uezds.
- Gazetteer sites may require a login (JewishGen) or be unreachable from abroad (the Presidential Library, some Russian sites): a human logs in and makes the decisions about the network; do not bypass geoblocks.
- If the place could not be identified, the card is still filled in: variants, gazetteers checked, candidates and why they were rejected.
