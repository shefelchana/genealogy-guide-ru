---
name: researching-jewish-cemeteries
description: Uses Jewish cemeteries as a genealogical source. Finds whether a cemetery exists and survives (JewishGen Cemetery Discovery Project, ESJF surveys, Lo Tishkach), searches burial databases (JOWBR, Mitzvat Emet, Toldot, Moscow and Petersburg registers, Israeli hevra kadisha searches, BillionGraves, Find a Grave, JGSNY landsmanshaft plots), reads the matzevah (פ״נ, בן/בת and the father's name, ר׳, מו״ה, הבתולה, ת.נ.צ.ב.ה., the year in gematria and לפ״ק, Kohen hands, Levite pitcher, name animals), converts the Hebrew date, reads Soviet-era stones, uses neighbouring graves, society plots, burial-society pinkasim and destroyed cemeteries, and states a not-found result honestly. Use whenever the user mentions a grave, gravestone, matzevah, Jewish cemetery, "where is my great-grandfather buried", "read the inscription on this stone", "what do the hands on the stone mean", JOWBR, Mitzvat Emet, "find a Jewish grave", "Hebrew tombstone", even if they only send a photo of a stone. Also triggers on Russian requests: «надгробие», «мацева», «еврейское кладбище», «где похоронен прадед», «прочитай надпись на памятнике», «что значат руки на камне», «Мицват Эмет».
---

# Jewish cemeteries as a source

## Principle

A matzevah (*matseva*, gravestone) often gives what the vital records do not: **the father's name** (בן/בת, "son/daughter of"), the exact date of death in the Jewish calendar, Kohen or Levite descent, sometimes a town and a surname. The father's name moves a line up one generation. But the cemetery databases cover only part of the graves, and many cemeteries are destroyed. So "not found in the database" is not a conclusion.

Related skills: `reading-hebrew-yiddish-sources` (names and handwriting), `searching-jewishgen` (JOWBR and the JewishGen login), `tracing-emigrants-to-origin` (USA), `verifying-genealogy-findings` (negative conclusions).

## Step 1. Establish where the person could have been buried

The place of death, not of birth. For each place check:
1. **Is there a Jewish cemetery there?** The JewishGen Cemetery Discovery Project (formerly the IAJGS project): country → locality.
2. **Does it survive?** ESJF surveys (Ukraine, Moldova, Poland, Lithuania, Hungary and others; Belarus is not on the list) give a status of "demolished and built over" / "demolished, not built over" / "fenced", **the dates of the oldest and newest stone**, and GPS. If the oldest stone is from 1885 and the person died in 1850, their stone is most likely not there.
3. If the cemetery was demolished, were there **relocations**? (For example, part of the graves of the destroyed Lukyanivka Jewish cemetery in Kyiv were moved to Berkovtsy.)

Resources, addresses and tips: `references/cemetery-databases.md`.

## Step 2. Search the databases for the burial

Order by region:
- **Ukraine, Belarus, Russia, Moldova, Kazakhstan, Uzbekistan**: Mitzvat Emet (photos of stones), Toldot (surname substring), JOWBR.
- **Moscow**: the hevra kadisha register (Vostryakovo, Malakhovka, Saltykovka cemeteries), Toldot. **Petersburg**: the database of the Preobrazhenskoe Jewish Cemetery.
- **Poland**: the Foundation for Documentation of Jewish Cemeteries database (Warsaw-Okopowa and others), JOWBR.
- **Israel**: search each local hevra kadisha separately (Tel Aviv, Jerusalem, Haifa, Rehovot...) plus BillionGraves / MyHeritage (according to a MyHeritage announcement, almost all Israeli cemeteries had been photographed by March 2019; later burials may be missing). Search **in Hebrew**.
- **USA**: Find a Grave, BillionGraves, JOWBR, the JGSNY database of landsmanshaft society plots.

Search every spelling of the surname and given name, including Soviet forms (Khaim → Yefim) and Hebrew ones. Mitzvat Emet: type the beginning of the surname → **choose the suggestion** → «Поиск» ("Search", the button label on the site). After about 5 searches in a row the form silently stops submitting. Do not work around it; try again later, one search per visit. A human handles CAPTCHAs, logins and registration.

## Step 3. Read the matzevah

A detailed table of formulas, abbreviations, epithets and symbols is in `references/reading-matzevot.md`. Reading order:
1. At the top **פ״נ** ("here lies buried") or **פ״ט** ("here lies hidden").
2. Epithets and title: **ר׳** is "reb", a polite form of address, **not** a rabbi; **מו״ה** "our teacher, Mr." signals learning; **הבתולה** is an unmarried girl; **האשה החשובה** "the esteemed woman" is a married woman; **הילד/הילדה** is a child.
3. The name, then **בן / בת** + the father's name (often **ב״ר**, "son of reb ..."); **הכהן / הלוי** means Kohen or Levite.
4. Surname and town: not always present.
5. Date: day, month and year in letters (gematria), often with **לפ״ק** ("by the small count", without the thousands).
6. At the end **ת.נ.צ.ב.ה.** ("may his soul be bound up in the bond of life").

**Symbols**: hands in the blessing gesture mean a Kohen; a pitcher means a Levite; candlesticks mean a woman; books mean a scholar; a broken tree or candle means an early death; animals often **encode the name**: deer is Tsvi/Hirsch/Naftali, lion is Aryeh/Leib/Yehuda, bear is Dov/Ber, bird is Tsipora/Faige.

**Soviet-era monuments** (1920s-1980s): Russian text with full name and dates, an enamel photo, sometimes one line in Hebrew with the Jewish name and the father's name. Compare the Russian patronymic with the Hebrew father's name: "Borisovich" and "בן דוב בער" (son of Dov Ber) are the same man. Sometimes the name in the documents and the name on the stone **do not reconcile**, neither through Russification nor through a double name: then record both forms side by side and do not force one to fit the other.

**Example.** פ״נ / הבחור / משה / בן ר׳ יעקב הכהן ז״ל / נפ׳ ט״ו אדר ב׳ תרע״ג [Here lies buried the unmarried young man Moshe, son of reb Yaakov the Kohen, of blessed memory; died 15 Adar II 5673.] The father had died by this time; the date is 15 Adar II 5673. Conclusions: he never married; the father died before March 1913; the family are Kohanim (the hands on the stone should confirm it); the next documents are the death record and the death record of the father.

## Step 4. Convert the date

Year in letters + 5000 (if the thousands are omitted) − 3760 = Gregorian year; for the months Tishrei, Cheshvan, Kislev and part of Tevet the result is **one year less** (+1239 instead of +1240 to the abbreviated year). Example: 12 Kislev תרס״ה → 20 November 1904; 12 Nisan of the same year → 17 April 1905. In a leap year check **Adar I or Adar II**: 7 Adar תרע״ג is 14 February or 16 March 1913. Use the Hebcal converter (`references/reading-matzevot.md`). To compare with Russian documents, convert to the Julian calendar: −12 days in the 19th century, −13 from 1 March 1900 until the switch to the new style in February 1918. The same calculation is done by Steve Morse's tombstone converter (stevemorse.org/jcal/tombstone.html).

## Step 5. Neighbours and plots

- Neighbouring graves are often relatives: spouses side by side, children near their parents, family enclosures. Photograph and read the **neighbouring** stones too.
- In the USA, landsmanshaft societies (*landsmanshaftn*, hometown societies) bought plots; the society's section names the **shtetl of origin**. Use the JGSNY database by society or shtetl name. This is an argument, not proof: people from neighbouring places also joined the society; confirm with naturalization papers and ship manifests.
- In Israel and in Soviet cemeteries the plots were allocated by year of burial: the plot number narrows down the year.

## Step 6. Books and records of burials

- **Burial-society pinkasim** (*pinkas*, record book of the hevra kadisha): only a handful survive; the known ones are held at YIVO and the National Library of Israel. Search the catalogues by shtetl name.
- **Cemetery registers** of the Soviet period are held by the cemetery administration or the city funeral service; the record of death is in the ZAGS (Soviet civil registry office) (`soviet-era-records`).
- A destroyed cemetery: look for lists made before the demolition (local historians, ESJF, JOWBR), photographs in memorial books and photographs of funerals in family albums (`interpreting-jewish-family-photos`). An example of a published register: the Chisinau cemetery has 18,751 records and 14,150 photographs in JOWBR, taken from a 2004 register book (Bessarabia SIG project) [from search results].
- **A pedigree "from a great rabbi"** (*yichus*) is tested against the stones: the fathers' names on the gravestones and the chronology of the generations must agree with the family story. See `reading-hebrew-yiddish-sources`, the section on rabbinic families.

## Step 7. Photographs at the site

The person themselves or a volunteer can photograph the stone. Arranging it, asking and paying is done **only by the person**: you do not write or send requests. Advise how to shoot: the whole stone and the inscription close up, in raking side light, both sides, the neighbouring stones, a wide shot with a landmark, GPS. Do not clean the stone with chemicals or outline the letters with chalk.

## Step 8. What counts as a find and how to write "not found"

- **A find**: a photo of the stone (or a database record with a link), a verbatim transcription, a translation, the date in both calendars, and a match of **at least two** features with a known person (name + father's name, name + date, name + place).
- **Not found**: list the databases, the spellings, the cemeteries and their status (survives / demolished / coverage of the database). Formula: "Not found in databases X, Y under spellings A, B; the cemetery is partly destroyed; no conclusion about the place of burial is drawn."

## Answer format

1. Where the person could have been buried and what is known about the cemeteries (state of preservation, years of the stones).
2. Where you searched and what you found, with links and markers.
3. Reading of the stone: transcription, translation, date → Gregorian, symbols and what they mean.
4. New information (father's name, Kohen/Levite, town) and the next document that will check it.
5. Offer to fill in `assets/gravestone-record.md` for each stone.
