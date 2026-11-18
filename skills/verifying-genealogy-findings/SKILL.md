---
name: verifying-genealogy-findings
description: >-
  Establishes whether a genealogical finding actually holds — ranks sources by evidential weight, states the four conditions a negative conclusion must meet, searches surnames across period spellings and alphabets, queries free full-text corpora, keeps a register of family legends broken into separate claims, and briefs a research agent so its report is verifiable rather than merely plausible. Use when the user asks "is this finding reliable?", "can I trust this record or family tree?", "does 'not found' mean anything?", "how do I search a surname spelled many ways?", or when confirming or rejecting a family-history claim, or coordinating agents on archival research. Also triggers on Russian requests: «проверь находку», «доказано или нет», «что значит „не найдено“».
---

# Standard of proof in genealogy

## The script

**`scripts/fulltext.py`** — full-text search on `genealogyindexer.org` (2.24 million pages of directories, address calendars, memorial books, name lists of First World War casualties; no login). Run it, do not read it.
```bash
python3 scripts/fulltext.py Фейгель --scope podolia
python3 scripts/fulltext.py Розенберг --scope any --match ocr --collection military
```
Regions: `podolia kiev volhynia ukraine galicia russia empire any`. Modes: `regular`, `dm` (Daitch-Mokotoff), `ocr`.
The query string goes to the site as is, so the site's own syntax works (per the site's manual): `'"surname name"~4'` — both words within four words of each other in any order; `'surname {1890-1917}'` — year filter; `{d82,y17}` — collection codes; `*` — only in `regular` mode. The site keeps growing: repeat a negative search after new additions. (Search in Cyrillic: Russian directories are recognized in Cyrillic, so the Russian spelling is what is searched.)

## Hierarchy of sources

Primary document (scan of an archival file, or an original of the time held by relatives, including a photo of it) → printed directory of the period → later family notes and oral account → pointer, index, database → someone else's tree.
**An archive and a document are always above an entry in a tree and above family memory.** Someone else's tree is not a source but someone else's hypothesis.
⚠️ The hierarchy ranks carriers, but what decides is the specific document and the specific field. An original held by relatives (ZAGS certificate — Soviet civil registry —, passport, certificate) is not lower than a scan and is higher than a directory. Fields within a document are not equal: an age stated by the person himself is weaker than a date from a metrical record, though both stand in a primary document.
⚠️ **Encyclopedias, Wikipedia and published biographies rank below a metrical record and a census**, especially in the "place of birth" field: they often give the place of registration (*pripiska*) as the place of birth, and understate the number of children (the authors did not know of infants who died). An entry in a pre-revolutionary dictionary may have been paid for by the subject himself. Nadya Lipes, who compared such biographies with metrical records and censuses, considers errors in places of birth very common — this is a practitioner's opinion, not a statistic.
⚠️ **An AI chat's answer without a reference to a specific record is not a source**, even if it sounds like "recorded in the documents". First find the record, then believe it.

## Age arithmetic

Ages in documents shifted not only at random — there were reasons, and they can be tested by calculation.
· **Conscription.** Under the 1874 statute, those who had turned 20 by 1 January of the draft year were called to the lottery; not all served by lot, and the term of active service was 6 years (later shortened). If it is known that a man married after service, the marriage is not earlier than about age 26 — this tests the birth year when there are no metrical records for the year you need. Sons were both aged and made younger because of the draft.
· **Marriage.** A bride younger than the permitted age was not married, so her age was **inflated**.
· **NKVD questionnaires and other Soviet questionnaires:** the ages of children given by relatives are sometimes wrong.
· **Census against legend.** A family date "eldest son born 1895" is refuted by the 1897 census, in which the mother is 18 and unmarried. Check the legend against the parents' ages in the nearest census.

## Negative conclusion

⚠️ **An index is not proof.** A verified case: a person is on the list at frame 502 and is absent from the alphabetical index of his own section. By JRI-Poland's experience, the annual indexes to metrical records are correct about 90% of the time: some records did not make it into them, some surnames were misread.

**"Not found" has force only if four things are stated:**
1. the source and its exact limits — the file, the pages, what exactly was viewed;
2. the list of spellings searched;
3. the search mode — exact, phonetic, page by page;
4. whether the index or the file itself was viewed.

An empty result is a full result if the coverage is named: it saves the next attempt weeks. But "searched and did not find" is a report on work done, not evidence: it proves only absence inside a document where the record was bound to be.

⚠️ A negative result is often **meaningful** if you understand how the source is built. Example: a surname is not in the list of rural settlers — because the family was urban and could not have got there. That is not a gap but a confirmation.

Three more checks before saying "there is no book" or "there is no record":
· **A shtetl's books are sometimes bound into the books of neighbours.** JRI-Poland found the "missing" metrical records of Gowarczów inside the books of Ostrołęka (article by S. Diamond, Avotaynu, 2018) [from the search results], and the 1885 births of Nowy Targ inside the books of Krościenko [not verified]. Before writing "there are no metrical records of shtetl X for years Y", look through the books of neighbouring rabbinates and of the district town.
· **A database that keeps growing answers only for the date of the search.** The JewishGen Ukraine Research Division posts new records every month, and Genealogy Indexer adds collections. Record a negative result from such a database with the date (month) of the search and repeat it after uploads for the place you need.
· **The 1897 census survives by name almost nowhere**: the local copies were supposed to be destroyed, and only isolated uezds (districts) survived; for Bessarabia there are no name sheets in the National Archives of Moldova (paper by A. Chastina, IAJGS 2012). Absence from the 1897 census means almost nothing.

## Spellings of surnames

· **Yiddish → Russian**: the Latin `s` serves samekh, sin and sov (Ashkenazi pronunciation of tav) and is part of `sh` and `ts`. Фейгель / Фейгаль / Файгель / Фейгелль / Фейгейль [Feigel / Feigal / Faigel / Feigell / Feigeil] — a regular family of forms, not variants.
· **Phonetics**: Beider-Morse for original European spellings; Daitch-Mokotoff for anglicized ones (it truncates after six consonants and treats all vowels as the same, so it produces junk).
· **Pre-revolutionary OCR often swallows the first letter** — search without it too: «ейгель», «озенберг», «евин», «аплан» [i.e. (F)eigel, (R)ozenberg, (L)evin, (K)aplan].
· Check the ending: «-ель» versus «-еръ», «-манъ», «-бергъ», «-штейнъ» — different surnames, confused on a poor scan. **Write out explicitly** the candidates you have ruled out, so the next attempt does not waste time on them.
· Search in all the languages of the place: Russian, Ukrainian, Polish, German, Hebrew, English.
· **Run through the vowel of the root**: Плет → Плит → Плат → Плот [Plet → Plit → Plat → Plot]. If a family "disappeared" from a uezd, check the **electors' lists for the crown rabbi** (*kazyonny ravvin*) and the resolutions on his election: Lipes found there a dozen bearers of the surname in a different vocalization, who were not in the uezd's database.
· **A one-letter difference within one town is sometimes deliberate**: relatives changed a letter to separate themselves from another family (of the type «-ский» / «-цкий» [-sky / -tsky]). And conversely: a family could merge with the local form of a surname and become a "namesake" of strangers.

### When a namesake is a relative (after N. Lipes)
· A **toponymic** surname or an **occupational** surname — by default **not** kinship. A toponymic surname was usually given on leaving **from** a place, so the bearer lived elsewhere (exceptions occur).
· One locality, a surname that is neither a toponym nor an occupation, and especially a rare one — probably relatives; this is a hypothesis, to be confirmed by a document.
· 🔑 **A unique scribe's error is evidence of common origin**: two independent enumerators could not have made the same error. Lipes's example: Ясногородский → Зиногород → Зиниград [Yasnogorodsky → Zinogorod → Zinigrad] (the letter «Я» read as «З», the ending moved to another line).
· **The range of a surname** ("home of the surname") should be determined from the **earliest revisions (1805–1816)**, not from the geography of Beider's dictionary: it rests on sources of the early 20th century, when families had already dispersed.
· The rule "one surname + one region = one family" (as the Am HaZikaron institute puts it) is stronger for Galicia and the Kingdom of Poland, where under the 1821 rules and the Galician rules different families of one locality were assigned different surnames; within the Pale of Settlement it is weaker, and for toponyms and occupations it does not work.
🔑 When working with the trees of DNA matches, **a match by shtetl is worth more than a match by surname**: Jewish surnames are new (law of 1804), whereas the shtetl is held for generations. An example from one search: the emigrant Moische Feigel in Philadelphia became Max Fairman — his descendants cannot be found by surname.

## Resources

Wikimedia Commons (whole archival files of DAKhmO — State Archive of Khmelnytskyi Oblast —, DAKO — State Archive of Kyiv Oblast —, DAViO — State Archive of Vinnytsia Oblast), the list of digitized holdings on `uk.wikisource.org` in the `Архів:` namespace (structure `Архів:<ARCHIVE>/<fond>/<inventory>`, can be pulled via `?action=raw`), archive.org, NEB (National Electronic Library, Russia), Vivaldi of the Russian National Library, HathiTrust, JewishGen, Gesher Galicia, JRI-Poland, Yad Vashem.
⚠️ Archive sites are sometimes available only over **http** (for example `rgada.info`) — if https is silent, try http.
⚠️ **A zero from full-text search proves nothing**: verified — a known line in an address calendar is not indexed by genealogyindexer, and the filters by guberniya are stuffed with Soviet telephone directories.

## Family legends: a register and breaking them into parts
- Keep a legends file: one line per claim, a status (🟢 document · 🟡 partly · ⚪ unchecked · 🔴 refuted · ❓ contradiction) and what it was checked against. A new legend starts at ⚪.
- Break a legend into parts: "born in village N, came from the Germans, her mother was a healer" is three claims with different statuses.
- In older Russian usage *nemtsy* ("Germans") meant foreigners in general; test that reading too (local non-Slavic groups, people from the Baltic provinces).
- Information from other people's trees, service hints and DNA percentages are hypotheses; into the tree only after a document.

## How to brief an agent

The report must be **verifiable, not plausible**:

1. **"Write only what you see."** Do not fill in, **do not carry names from the task itself into the report** if the agent did not see them. This is the main cause of invented finds: the agent reproduces what is expected.
2. **For every hit, an address and a quotation:** file, page, household number, exactly how the name is written, all ages and notes verbatim.
3. **Mark an uncertain reading "uncertain"** and explain what is in the way.
4. **A log of pages viewed** with ranges of numbers.
5. **Declare an honest "not found" a normal result** and explicitly forbid inventing.
6. **Rule out known lookalikes in advance** — list the surnames already checked and rejected.
7. **Separate the files**: each agent gets its own subdirectory. Otherwise they overwrite each other's scripts in the middle of the work.
8. **Ask the agent to correct the brief.** A description of how the file is built, given in the brief, may be wrong; an agent who checked this and reported saves the work. A verified case: the brief claimed "odd pages are the male sex", but each page turned out to be a whole spread, and viewing "every other page" would have lost half the households.

⚠️ **Check not only the result but the source.** There was a case where an agent cited an "already deciphered record" that did not exist — and the content turned out to be correct. The footnote was invented, the fact genuine. Mark such places "unverified" rather than deleting them, and re-check against the original.

## 🔑 Checking a surname reading against the Morse–Beider index

`https://stevemorse.org/phonetics/beider.php` — the official index to Alexander Beider's dictionaries, five books: **djsre** (Russian Empire, 2008) · **djsg** (Galicia, 2004) · **djskp** (Kingdom of Poland, 1996) · **djsp** (Prague) · **dgjs** (German, Menk 2005).

✅ Look **only at the "BMPM exact" column** — these are the headwords of the dictionary. "approx" and "Daitch-Mokotoff soundex" are noise.
⚠️ The index gives **the existence of an entry, but not its text**: no etymology and no list of uezds.

**How to apply it to a disputed reading:**
· the surname **is in** the index → the reading is plausible;
· the surname **is absent from all five books** → 🔴 **the reading is almost certainly wrong**;
· then run **closely spelled variants** through the index and return to the reader a list of those that really exist — let him check on the scan.
Verified: «Штейнтманъ» and «Кравнецъ» [Steintman, Kravnets] gave zero matches and turned out to be misreadings; «Фейгель», «Гроссъ», «Кройзманъ» [Feigel, Gross, Kroizman] were found at once.

⚠️ **Neighbouring surnames in one shtetl prove nothing.** «Фейгманъ» [Feigman] next to «Фейгелемъ» [Feigel] is not a variant of one surname but **a separate surname formed differently**, with its own headword in the dictionary. Check by the index, not by resemblance to the eye.
⭐ For exact etymology tied to uezds — the topic `forum.j-roots.info/viewtopic.php?t=92`, where **Beider answers personally** (a user account is needed).
