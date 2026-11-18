---
name: soviet-era-records
description: >-
  Finds a person in Soviet-era sources 1918–1991 — WWII soldiers and the missing (Pamyat Naroda, OBD Memorial, Podvig Naroda, Doroga Pamyati, district conscription books, martyrology.org.ua), evacuees 1941–1942 (Yad Vashem evacuation cards, the Tashkent cards on JewishGen, Leningrad evacuation), siege of Leningrad victims (Blockade Book of Memory, siege house pages, Returned Names), the repressed (Open List, Immortal Barracks, regional books of memory, SBU/KGB archives), Holocaust victims in occupied Soviet territory, and ZAGS registers of the 1920s–1940s. Use whenever a 20th-century relative died in the war, went missing, was a POW, was repressed, shot or dekulakised, died in the siege, was evacuated or killed in a ghetto — even if no database is named. Also triggers on Russian requests: «погиб на войне», «пропал без вести», «был в плену», «был репрессирован», «расстрелян», «раскулачен», «умер в блокаду», «погибли в гетто», «ОБД», «эвакокарточка», «Открытый список».
---

# Soviet-era sources: war, evacuation, siege, repressions, Holocaust, ZAGS

## When to use

The person lived in the USSR between 1918 and 1991, and the question concerns the war, evacuation, the siege, an arrest, death under occupation, or a Soviet record of birth, marriage or death. Pre-revolutionary metrical books and revision lists are in the skills `tracing-revision-records` and `reading-archive-scans`; Soviet ZAGS (civil registry office) books of Ukraine on Wikimedia Commons are in the skill `ukrainian-archives-on-commons`.

A reference of databases by country and region is `references/by-region.md`. Read it as soon as you know where the person lived, served or died: there are few all-Union databases and dozens of regional ones.

## Step 0. Assemble an identifying set before the first query

Soviet databases almost never search "by meaning". A search is either exact or by the start of a word, and scribes distorted everything. A person is identified not by surname but by a combination of features. So first write down:

- all known forms of the **surname** (including the maiden name), the **given name** (home, synagogue, passport) and the **patronymic** (see the section "Changes of names" below);
- the **year of birth** — you will search in a ±2-year window, as ages in wartime documents "float";
- the **place of birth** down to the district or village — this is the main filter in all military databases;
- the last known place of residence, place of conscription, place of arrest;
- the names of closest relatives: in hospital registers, loss reports and evacuation cards they stand alongside.

Without a place of birth or a year of birth, a common surname gives hundreds of namesakes and you cannot choose "the one". If this data is missing, find it first (family documents, ZAGS, census) and only then go to the databases.

## Step 1. Choose the source by the question

| Question | Start with | Then |
|---|---|---|
| Fought, died, went missing | OBD Memorial (no captcha) | Pamyat Naroda (loss reports, hospital registers, the 1985 card file), regional books of memory |
| Awards, combat path | Pamyat Naroda / Podvig Naroda | Doroga Pamyati (photos), Immortal Regiment |
| Was a German prisoner of war, deported to labour | Pamyat Naroda (prisoner documents), the prisoner-of-war database in Dresden | Arolsen Archives, regional databases of prisoners, filtration files (FamilySearch, DAKO — State Archive of Kyiv Oblast) |
| Evacuated 1941–1942 | Yad Vashem (evacuation lists), JewishGen Tashkent database | regional databases of evacuees, registers of oblast archives |
| Died in the siege of Leningrad | "Blockade. Book of Memory" (all volumes), the consolidated memorial book of the siege | evacuation from Leningrad, OBD for military personnel |
| Arrested, shot, exiled | Open List ("Otkrytyi spisok") | "Immortal Barrack", regional books of memory, archives of the SBU / HDA UINP (Ukraine) |
| Killed under occupation, in a ghetto | Yad Vashem (Pages of Testimony) | USHMM, ChGK acts (name lists 1944–1945), "Book of Sorrow", local martyrologies, the Babi Yar database |
| Birth, marriage, death in the 1920s–1940s | ZAGS books (Ukraine — Commons) | household books (*pokhozyaistvennye knigi*), evacuation cards as a substitute for a lost metrical record |

Before the first query in a region, open `references/by-region.md`: it notes which databases are unavailable from abroad, which have closed and which need a human.

## Step 2. How to search in any database

1. **Write in Cyrillic.** Soviet documents are recognized and indexed in Russian; transliteration yields less and worse. Latin letters are needed only for Yad Vashem, USHMM, Arolsen, JewishGen — and there try both alphabets.
2. **Each spelling is a separate query** if the database searches exactly (OBD, Pamyat Naroda without grouping). Compile the list of variants in advance: doubled and single consonants (Рабинович/Раббинович), е/э/и, soft sign at the end, -ман/-манн, masculine and feminine forms, devoicing (Гольдберг/Гольдберк), transposed letters.
3. **Where the database searches by the start of a word, enter the beginning of the surname**: this catches distortions in the tail (martyrology.org.ua, Open List through prefix search).
4. **Search by place without a surname** when the database allows. Pamyat Naroda with a filter by place of birth and the Open List by place of birth give all natives of a village at once — this also finds surnames distorted beyond recognition, and the circle of relatives.
5. **Year ±2, patronymic in several forms.** If the patronymic filter narrows the results to zero, remove it and look with your eyes.
6. **Cross-check in at least two databases.** What is not in Pamyat Naroda may be in OBD, and vice versa; a siege record may be in another volume under a distorted surname. For the Holocaust the holdings of Yad Vashem, Arolsen, USHMM and the Holocaust collections of Ancestry do not coincide — go through all of them.
   ⚠️ **Printed books of memory reprint the distortions** of the primary records (example: "Book of Memory of Jewish Soldiers"). "No such surname" in a book is a reason to look in the primary OBD record, not a conclusion.
7. **Check that the filter worked.** Some forms silently drop a field (USHMM without the correct field name, the free JewishGen form). Control: a query with a record known to exist.

## Step 3. Features of the main databases

**OBD Memorial** (obd-memorial.ru). Works without captcha and without login. The surname search is **exact**: a truncated word will not be found, enter each spelling separately. The card has full name, year of birth, place and date of conscription, last place of service, reason for leaving the ranks. Open the **scan** of the document: in the "relatives" column of a loss report the name and address of the family often appear — a bridge to civil documents.

**Pamyat Naroda** (pamyat-naroda.ru). Responds to automated requests with a "security check": **a human passes the captcha**, after which the session lives. The main filter is **place of birth**; it combines with name and patronymic. In grouping mode exact matches come first, then fuzzy ones — view the fuzzy ones too. Only here is the **1985 anniversary card file** (surviving veterans). **Hospital registers** are more informative than loss reports: they have a "relatives' address" column. Scans open only from the card page.

**Conscription books of district military enlistment offices** (*voenkomaty*; scans in Pamyat Naroda, reached from the card "Conscription and demobilisation"). They are alphabetical, usually with initials instead of given names; they have the address and the date of conscription. "Команда № …" ["Detachment No. …"] stands in the column "Receipt of the mobilisation order" — it is the number of the dispatch on that day, **not a unit number**. One person is sometimes entered twice. There is no filter by date or detachment: comrades from the same detachment are found only by paging through all the images of the book, and the images load only inside an open session on the site. The portals do not search by address, so find a serviceman by the family's address like this: surname + years of birth + district of conscription, then the "address" column in the conscription book or the "family address" in the loss report. The field "Фамилия (Другая)" ["Surname (Other)"] in an enlistment-office card holds the current (maiden) surname. A negative conclusion only with coverage: how many images and rows were read.

**Podvig Naroda** is now inside Pamyat Naroda, but the separate site works; form fields sometimes do not accept keyboard input — fill them in one at a time, by entering the value into the field. **Doroga Pamyati** is photographs; there are photos from personal files that exist nowhere else.

**Evacuation cards (Yad Vashem).** Read the card **in full**, not only name and year: it has the patronymic (or father's name), occupation, place of work, composition of the family, from where and to where evacuated, address of accommodation. This is often the only document proving a patronymic when there are no metrical records. If several people have **the same path to the scan image**, they stand on the same page of a list: one family or one train. First compare the image paths, then read the names. Those evacuated together are a ready-made **list of collateral relatives**: use it to search the ZAGS books for births of children of **all** men of the family. The place of birth given by an evacuee may lead to a shtetl rather than a city. Only **Jews** are entered in the Yad Vashem name database — by the museum's figures, more than half of the roughly 1.5 million refugees and evacuees; non-Jews from the same Soviet lists are not there. The site is a single-page application: the bare page is empty, the data arrive in separate requests, so read it in a browser or through its own data sources.

**Tashkent database (JewishGen).** 151,966 cards of Jews who arrived in Tashkent before February 1942. They were selected from the card file of the Central State Archive of Uzbekistan (more than 250,000 cards, about 339,000 people), which includes non-Jews; the database includes only Jews and only those who arrived directly in Tashkent. Fields: surname, given name, patronymic, year of birth, from, to; the number opens the scan of the card. Those who came later or to another city are absent — this is a property of the database, not a trace.

**Open List** (ru.openlist.wiki). A wiki database of victims of repressions. Full-text search is switched off, but a search of pages **by the start of the title** works — go through all spellings of the surname. Harsh throttling: after three rapid queries — a block; keep a pause of at least 6 seconds. A search by place of birth without a surname shows all the repressed of a village.

**The Siege.** "Blockade. 1941–1944. Leningrad. Book of Memory" — 35 volumes; distorted surnames in it are the norm, a person may stand in another volume. The consolidated siege memorial book gathers TsAMO (Central Archive of the Russian Ministry of Defence), the siege books and evacuation, but only the Leningrad circle. The scans in it are files with sequential numbering — neighbouring images of the same file open by changing the number. The house page `blockade.spb.ru/address/<id>/` lists all the residents of the house who died, with flat numbers (`?page=N`); the id is found by trying neighbouring numbers, which are grouped by street. The script `scripts/blockade_address_probe.sh` prints the address for an id or a range of ids, and with `-r` all the residents of a house; it pauses between requests — do not run it in parallel. Name search on this site works only in a browser (the results are loaded by a script).

**Holocaust (Yad Vashem).** The basis of the database is the **Pages of Testimony**. The most valuable is the **name and address of the person who submitted the page**: that is a relative through whom a whole branch is found. Search in three roles: victim, submitter, mentioned.

**If there is no page — ChGK acts and dates by place.** The Extraordinary State Commission (ChGK) in 1944–1945 compiled name lists of the dead by district and village (GARF fond 7021; GARF = State Archive of the Russian Federation). A copy is USHMM microfilm RG-22.002M with an index of about 1,456 places; the lists are handwritten, in Russian. The date and circumstances of an action in a shtetl are given by the encyclopedias of A. Kruglov and I. Altman ("The Holocaust on the Territory of the USSR", 2009: articles on places where at least 100 Jews were killed or where there were ghettos and labour camps). A match "last address of the family — date of the action" is a hypothesis and a precise question for the lists, not proof of death.

**ZAGS of the 1920s–1940s.** There is almost nowhere a search by surname — only page-by-page reading of the book by place and year. Read **all surviving years**, not only the one the family named: dead infants, cousins and the year of moving come up; the column "has lived here N years" dates a move, but it was filled in by the declarant. Early forms often lack parents and place of birth; the form changes even within one book. Early records (before the new form of 1926 in the RSFSR; in the Ukrainian SSR the forms changed in their own way) **often have no** nationality column: a Jew is recognized by the name and by the place of burial (Jewish cemetery); for 1918–1920 look at both rabbinate books and ZAGS. From 1926 the birth-record form has a "nationality" column [from the search results: article "Civil status registration books of the 1920s–1930s", CyberLeninka]. Documents with personal and family secrets are closed for 75 years from creation (Russia — art. 25 of law 125-FZ; Ukraine — art. 16 of the law on the National Archival Fond). In Russia the registry books are kept for 100 years in ZAGS bodies, not in an archive.

## Changes of names and patronymics in the Soviet period

Without this section a third of searches end in a false "not found".

- One person sometimes had **three names**: in documents, at home, in the synagogue. The transition often went through a diminutive: Moishe → Misha → Mikhail.
- Stable pairs: Khaim → Efim, Borukh/Berko → Boris, Abram → Arkady, Srul → Alexander/Sasha, Movsha/Moishe → Mikhail or Moisei, Gersh → Grigory, Shloma → Solomon, Rakhil → Raisa, Khana → Anna, Khaya → Klara.
- Non-obvious pairs (after N. Lipes; these are tendencies, not rules, and a noticeable share of renamings have no logic at all): Leib (Arye-Leib) → Lev **or Alexei**; Akiva → Kiva → Nikolai; Nisan → Andrei; Avigdor → Viktor; Motl → Matvei, Dima; Efraim, Faivish → Fyodor, Filipp; Usher → Yuri, Georgy; Kopel → Yakov; Ber, Bendit, Bentsion, Benyamin → Boris; Issakhar (Sukher) → Alexander. Female: Shneidl → Evgenia; Zeidl, Zisl → Zoya, Zina; Golda → Olga; Ester → Fira → Ira; Keila → Ekaterina; Mirra → Maria. The full list is `citizenship-by-descent-dossier/references/name-identity.md`.
- **Children's patronymics were changed even if the father did not change his name.** The father in documents is Berko, the daughter is «Борисовна» [Borisovna]. Father Khaim — the son is «Ефимович» [Efimovich]. Run through the patronymic using the pairs above.
- **A father's double name gives full brothers and sisters different patronymics**: some after one half of the name, others after the other, and in Russification besides — «Абрамович», «Александрович», «Гершевна», «Григорьевна» [Abramovich, Aleksandrovich, Gershevna, Grigorievna] among children of one father. Run through both halves.
- **ZAGS around 1928–1933 did not ask the parents for documents** when registering a child (after N. Lipes): the mother is recorded under a new, "Russian" name. Later the discrepancy was legalized by "same person" certificates (*spravki «он же»*) or in court, often for the sake of an inheritance — these documents are the bridge.
- An official change of surname or name after 1924 was published as a notice in the local official newspaper of the city where the person lived.
- **Administrative borders changed**: look for the place within the borders of that year. Example: Zhytomyr oblast was formed on 22.09.1937 — an arrest in the summer of 1937 is listed under Kyiv oblast; districts moved between oblasts. Check both the previous and the next division.
- In military documents the patronymic of Jewish soldiers is written now in the original form, now in the Russified form, now abbreviated — check both variants.

A match "by the table of pairs" is a hypothesis, not identity. Confirm with a second feature: year and place of birth, names of relatives, address.

## Pace, access and limits

- **A captcha, logging into an account, payment, letters and requests to archives are done only by a human.** At the first "I am not a robot" check, stop and ask the person to pass it in a regular browser window.
- **One site — one worker.** Do not run parallel searches on one site.
- Pauses: Open List — at least 6 seconds; Pamyat Naroda — by navigation, without series of automatic requests; OBD is more tolerant, but also no bursts.
- Many Russian state sites (Pamyat Naroda, Doroga Pamyati, oblast archives, "Vozvrashchennye imena" [Returned Names]) **do not open from foreign addresses**. Do not work around this. Tell the person that the site is unavailable from their network and that the decision (turn off the VPN, ask acquaintances in Russia) is theirs. Look for the same material in another database.
- If a database has closed or moved (base.memo.ru — closed since spring 2026; the old USHMM HSV site stops working in autumn 2026, the database has moved to a new address; the database of the Piskaryovskoye cemetery has disappeared), note the date and go to the replacements in `references/by-region.md`.
- In Russia, the files of the repressed and ZAGS records younger than 75 years are issued to the person himself, and after his death to relatives or heirs. In Ukraine, under law No. 316-VIII of 09.04.2015 the archives of the repressive organs are open: only the victim himself may restrict access to information about himself, and relatives to certain sensitive information, for no longer than 25 years. If the trail runs into a closed file, record the exact archival reference and this restriction; how to proceed is for the person to decide.

## Repressions: how to read what was found
- Mass arrests of 1937–1938 went in "operations" under NKVD orders: No. 00447 of 30.07.1937 (the "kulak" one), No. 00485 of 11.08.1937 (the "Polish" one) and others. The operation suggests which body decided the case (a *troika*, a "dvoika") and where to look for the protocol.
- A sentence of "10 years without the right of correspondence" often meant execution. In death certificates issued to relatives in the 1950s the date and cause of death are often **false** — check against the databases of the shot and against the file.
- This is context for the search, not a conclusion about a specific person: assert a fate only from a document.
- In an investigation file look at the **enclosures**: the passport and personal letters confiscated at the arrest are sometimes the only surviving documents of the person and give addresses and relatives.

## What counts as a find

A find = **address** (database, record number or link to the card, archival reference of the document: fond–inventory–file–folio) + **verbatim quotation** of the fields + **check against the scan** if a scan is available. An index card without a scan is a hint, not proof: the "year of birth" field in it was typed from a document where the age was stated by a neighbour in a train.

Record a negative result like this: "Not found in OBD under spellings A, B, C (exact search), in Pamyat Naroda by place of birth X without surname, year ±2; date." Without the list of spellings and sources "did not find" means nothing (see `verifying-genealogy-findings`).

## If nothing was found

1. Check all spellings and the search by place without a surname.
2. Check neighbouring databases of the same type and regional books of memory (`references/by-region.md`).
3. Check the surroundings: neighbours at the same address, fellow servicemen, travelling companions in the train.
4. Check whether the person changed name or patronymic, and run the search again with the Soviet form.
5. Record which source is **unavailable** (closed, geo-blocked, not digitized) — that is not the same as "the person is not there".
