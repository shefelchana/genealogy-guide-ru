# Indexed databases: they point to where a document is

What this section covers: search databases with abstracts of documents (indexes). They quickly tell you where to look, but they are not proof in themselves: check every entry against the scan. Markers, interface-language notes and general rules are in [README.md](README.md).

---

## Jewish and general databases

### JewishGen (jewishgen.org) (English interface)
- **What is there:** the main Jewish genealogy resource. The "Ukraine" database (revision lists — about 1.3 million records, metrical books, 1906–07 Duma elector lists, censuses, business directories), Romania–Moldova, Belarus, Holocaust, the JOWBR cemeteries, the JGFF researcher database (who is looking for which surname and shtetl), the "Family Tree of the Jewish People" (other people's trees — the lowest level of proof), a name dictionary.
- **Access:** Free, registration: yes. Without logging in you can see **how many** records were found in each database; the records themselves only after login (login passes a Cloudflare check). The session lasts about a day.
- **Paid:** multi-field search (surname + town) — about $100 a year. On the free form fields 2–4 are locked, and **what you type into them is silently discarded**: the results look normal, but there is no filter. Filter with your eyes.
- **Limits:** only the **first 50 rows** are shown — narrow the query (town, "any field") and page through.
- **Techniques:**
  - start with **"is Exactly"** mode, turn on phonetics ("Phonetically Like") as a second pass (one surname has 122 exact records versus 2293 phonetic ones);
  - a surname in the indexes can be written unrecognizably — try phonetic search;
  - the "Surname" field also catches the **mother's maiden name** — that is, children whose mother comes from the family you are looking for;
  - the transliteration of the town decides: "Kamenets-Podolsk" — 0, "Kamenets" — 8;
  - phonetics lies: "Kessel × Letichev" returned Kishel and Kisel;
  - not all databases are complete: "Vsya Rossiya 1895" (All Russia 1895) and "Ves Yugo-Zapadnyi Krai 1913" (The Whole South-Western Region 1913) are only partly indexed — absence from them proves nothing.
- **Experience:** the index of revisions, metrical books and elector lists gave links to frames within minutes. But in one 1907 file the index missed several people — only reading the scan found them. Index fields can be mixed up ("daughter of Duvid" turned out to be the groom's father).
- **For advanced users:** a search is addressed by an ordinary link: `jewishgen.org/databases/jgform.php?srch1v=S&srch1t=Q&srch1=<surname>&allcountry=ALLUKRAINE&submitform=submitform` (S — surname, G — given name, T — town, X — any field; Q — phonetic, E — exact, S — starts with). Region codes: ALLUKRAINE, ALLPOLAND, BELARUS, ALLROMANIA, HOLOCAUST; cemeteries — DEFAULT or CEMETERY.

### JewishGen: reference sections
- **Ukraine Research Division** (jewishgen.org/ukraine): shtetl pages by guberniya, maps of about 1910, the Ukraine Given Names database, document translation projects; "Tips To Begin Your Research" — 10 steps for beginners [checked]. Free.
- **Bessarabia SIG** (jewishgen.org/bessarabia): its own database (Bessarabian revision lists, over 300 thousand records), a cemetery project, the database of the M. Weiner collection, a mailing list [checked]. Free.
- **Tashkent: Jewish evacuees** (jewishgen.org/databases/holocaust/0136_uzbek.html): 151,966 cards of 1941–1942, with patronymic and a scan of the card [checked]. See [War, repression, siege](../guide/2-reference/12-war-repression-siege.md).
- **JCA Passenger Lists** — see [usa-and-emigration.md](usa-and-emigration.md).

### FamilySearch — record search (familysearch.org) (English interface)
- **What is there:** indexes of metrical books, censuses, passenger lists, certificates, other people's trees. Moldova/Bessarabia, Ukraine and the USA are important. The films are in [archive-file-scans.md](archive-file-scans.md).
- **Access:** Free, registration: yes. **Some images open only in Family History Centers** — a frequent reason for "not found" although the record exists.
- **Pace:** hCaptcha appears when loading pages and after many frames in a row (see [Access, CAPTCHAs, pace](../guide/2-reference/19-access-captchas-pace.md)).
- **Techniques:**
  - try **all spellings** (there can be about 20 variants) and "fuzzy" mode;
  - search **by the mother's maiden name and place of birth** if the surname is distorted;
  - emigrants changed their surnames — search by place of birth, age, or the relative they were going to;
  - in manifests the towns are distorted: Pokotilov — "Pocolifoff", Proskurov — "Proskaw".
- **Traps:** age in American documents "floats" by 2–4 years; the index may have read a different surname ("Chaim Shefel" turned out on the frame to be Stiefel, checked 03.10.2026).

### JRI-Poland (jri-poland.org) (English interface)
- **What is there:** 6.4 million records, 2.5 million images, 1902 localities: metrical books, revisions, tax lists for Poland and Austrian Galicia; links to scans [checked]. Almost nothing for Podolia and the Kyiv region (in one research project only the 1811/1816 revision lists of Kremenets uezd, Volhynia guberniya turned up).
- **Access:** Free. The new search shows full results only with an account. The **old form** `legacy.jri-poland.org` shows everything without login after you accept the conditions (personal research only; when citing, name JRI-Poland).
- **Techniques:** the results summary has a breakdown by region; details open in a separate form.

### Yad Vashem, Central Database of Shoah Victims' Names (collections.yadvashem.org) (English interface)
- **What is there:** about 5 million names: pages of testimony (about 2.8 million, all scanned [from search snippet]), lists of evacuees (evacuation cards), lists of victims. The most valuable thing is the **name and address of the person who submitted the page** — a relative through whom the whole branch can be found.
- **Access:** Free, no registration, no CAPTCHA seen.
- **Techniques:**
  - search in all three tabs: victims, **submitters**, others (mother's maiden name, spouse);
  - **a search by submitter** immediately gathers everything one person submitted: this is how it emerged that two spellings of a surname in one town were one family;
  - evacuation cards prove patronymics and kinship where there are no metrical books;
  - export a large result (for example, 310 records for one surname) in full and go through it line by line, not by eye — that is how the overlooked is found.
- **Trap:** absence from Yad Vashem means nothing for lists that are not there (for example, some regional lists of evacuees).
- **Pace:** there are temporary server errors (521) — wait and repeat.
- **For advanced users:** the site has an open JSON interface (search, cards, scans); the first request returns an empty answer — that is normal.

### USHMM, Holocaust Survivors and Victims Database (ushmm.org/online/hsv) (English interface)
- **What is there:** Holocaust lists, including evacuation cards (Tashkent and others). Search modes: exact, Fuzzy, **D-M Soundex** (for Eastern European and Yiddish variants).
- **Access:** Free, no login. ⚠️ The pages announce: "the site will stop working in autumn 2026" — save what you need now. As of 2026-10-07 the search pages (`person_advance_search.php`) still open, while the address ushmm.org/online/hsv already redirects to the new database page in the "Remember" section [checked 2026-10-07].
- **Trap:** the search fields have the prefix `NameSearch__` (for example, `NameSearch__lname`); without it the filter is **silently not applied**, and the results look real.

### Routes to Roots Foundation (rtrfoundation.org, Miriam Weiner) (English interface)
- **What is there:** a free "Archive Database": by the name of a shtetl it shows which documents have survived, for which years and in which archive (Belarus, Lithuania, Moldova, Poland, Ukraine; selectively Russia, Latvia, Romania). The right first stop.
- **Caveat:** on 20.09.2026 the online form returned no results. M. Weiner's book *Jewish Roots in Ukraine and Moldova* is on archive.org (archive.org/details/jewishrootsinukr0000wein).

### Lipes Genealogy Database (lipesdatabase.com)
- **What is there:** **an index, not scans** — it shows in which archive a document lies. The database page mentions the 1897 census and the 1875 military census (Kyiv guberniya, Odesa) [checked]. The author is the genealogist Nadia Lipes (see [genealogists-and-authors.md](../reading/genealogists-and-authors.md)).
- **Access:** there is no self-service search on the site — the database works as a paid service: a search of the internal database (over 2 million records) costs €250, and then you choose copies of which documents to order; a search for a specific document in an archive costs €350, an assessment of whether an archive search is possible €450, a check of a document package for repatriation €250. The database does not contain the documents themselves [checked: lipesdatabase.com, 2026-10-07]. The earlier description "limited access free, full access €10–20 a day" (from the FamilySearch Wiki) is out of date.

### pra.in.ua (the "Ridni" society)
- **What is there:** a database of "residents of Ukraine born 1650–1920": about 3.9 million people, 445 thousand pedigrees, from revision lists and metrical books; mostly the Christian population [checked].
- **Access:** registration is needed for searching; access is free.

### IGRA — All Israel Database (genealogy.org.il)
- Over 4 million records, mostly for Israel and Mandatory Palestine; free registration opens the main part of the database [checked]. Name changes from the Palestine Gazette 1917–1948 — see [usa-and-emigration.md](usa-and-emigration.md).

### Arolsen Archives (collections.arolsen-archives.org) (English interface)
- Documents on Nazi persecution, concentration camps, forced labor, displaced persons (the digital archive has over 40 million documents [checked: arolsen-archives.org, Online Search page, 2026-10-07]; an old press release said about 30 million documents and 17.5 million people — out of date). Search is open; the e-Guide helps read the abbreviations; an enquiry about a person is free and can be made in Russian [checked].

### EHRI — European Holocaust Research Infrastructure (English interface)
- A portal of archival inventories on the Holocaust across Europe. Free [from search snippet: FamilySearch]. It is a guide to archives, not a database of names.

---

## War, evacuation, repression

The full list of databases by region (Russia, Leningrad, Ukraine, Belarus, Moldova, the Baltics) with the fields of the records is in [War, repression, siege](../guide/2-reference/12-war-repression-siege.md). Here are working techniques for the main databases. The Russian-language sites below need Cyrillic search terms. Don't read Russian? See [For English speakers](../guide/0-start/08-for-english-speakers.md).

### "People's Memory" (Память народа) (pamyat-naroda.ru) (in Russian)
- **What is there:** awards, the 1985 jubilee card file (**only here**), loss reports, hospital registers, documents of prisoners of war. **Hospital registers** are more informative than loss reports: they have a column "relatives' address".
- **Access:** Free, no registration. Automated requests get a "security check" (error 401); a human passes it, and then the session works.
- **Techniques:** the main filter is **place of birth**, combined with given name and patronymic; in "grouping" mode exact matches come first, then fuzzy ones. The lists are drawn by a script — "save page" does not work. Scans open only from the card page.
- **Network:** may not open from abroad.

### OBD "Memorial" (obd-memorial.ru) (in Russian)
- **What is there:** documents of TsAMO (Central Archive of the Russian Ministry of Defence, Podolsk): losses, prisoners, awards, burials.
- **Access:** Free, no CAPTCHA (as of 26.09.2026).
- **Techniques:** the search is **exact by surname** — each spelling as a separate query. The earlier query from the general field is mixed into the new one and gives "nothing found" — start a new search from a clean form. Truncated words are not searched.
- **For advanced users:** the parameter `ps` — up to 100 records per page, `p` — the page number, only together.

### "Open List" (Открытый список) (ru.openlist.wiki) (in Russian)
- **What is there:** victims of political repression 1917–1991 (3,380,827 records as of 2026-10-07), built as a wiki [checked].
- **Techniques:** search **under all spellings** (in one research project a relative written with "ff" was missed on the first search); **a search by place of birth without a surname** gives all the repressed of a village at once — the best way to see the family's surroundings. Full-text search is switched off; prefix and extended search are available.
- **Pace:** Cloudflare and a hard limit: after three quick requests — error 429; pause at least 6 seconds.

### "Book of Memory of Besieged Leningrad" (Книга памяти блокадного Ленинграда) (blockade.spb.ru) and visz.nlr.ru/blockade (in Russian)
- **What is there:** it brings together TsAMO, the siege books, evacuation, regional archives. No CAPTCHA.
- **Limits:** only the Leningrad circle — it is **not** a replacement for "People's Memory". Search by address gives only a map.
- **Technique:** scans of the files lie as separate files with numbered images; the neighboring images of the same file open by changing the number — that is how a file is read in full.

### "Immortal Regiment" (moypolk.ru) and "Feat of the People" (podvignaroda.ru) (in Russian)
- "Immortal Regiment" — an ordinary search form by surname, no CAPTCHA. "Feat of the People" works; it is now part of "People's Memory".
- From abroad these did not open: gwar.mil.ru (the 1914–1918 card file of losses — the only source of the guberniya, uezd and volost of a soldier's birth), "Road of Memory" (Дорога памяти).

---

## Trees and platforms

### MyHeritage (myheritage.com)
- **What is there:** family trees, "Record Matches" hints, DNA (see [dna-services.md](dna-services.md)).
- **Access:** registration: yes; a tree is free up to **250 people**. The details of hints need a paid subscription, but **the list of people with matches is visible for free**.
- **Rule:** only confirmed facts go into the tree. "Smart Matches" from Geni, if the tree on Geni is your own, are your own data, not an independent source.
- **Technique (profile biographies):** text pasted by a program is silently **not saved** — type at least one character from the keyboard; enter a long text in paragraphs; the limit of one note is about 2,300 characters.

### Geni (geni.com)
- A shared worldwide tree. Profile pages are behind an hCaptcha check. Other people's data are hypotheses, not a source.

An overview and choice of platforms is in [Tree platforms](../guide/2-reference/16-tree-platforms.md).

---

**See also:** [archive-file-scans.md](archive-file-scans.md) · [Standard of proof](../guide/3-results/01-standard-of-proof.md) · [War, repression, siege](../guide/2-reference/12-war-repression-siege.md) · [europe-by-country.md](europe-by-country.md)
