# The false zero: when the tool was wrong, not the source

What this section covers: what to check when a search returns zero, before you write "none". Why a site looks unavailable, how a zero comes from a wrongly assembled query, where the control record ends, how to count the gap between spellings, how to query an archive catalogue, and why a mark in a database may not be about your person.

This section was written from materials sent by a reader of the guide (October 2026), under the CC BY 4.0 licence.

The label **[reader's experience]** means: the author of the contribution did this and checked it on live queries (September–October 2026, their own project), and the compiler of the guide did not repeat those queries. The figures belong to one project, sites may have changed since — check yourself before an important conclusion. The other labels are explained in the [Glossary](../0-start/06-glossary.md).

The main point: **"the record does not exist" and "I did not find it" are different statements**, and the second is far more common. Before closing a direction, separately make sure that **the instrument is in working order**: the site, the query address, the search mode, the route. The general conditions of a negative conclusion (coverage, spellings, method, control record, date of search) are in [Standard of proof](../3-results/01-standard-of-proof.md), section 7. Here is what is added to them.

---

## 1. "The site is unavailable": six diagnoses

The page did not open, but the causes differ. "Come back later" applies only to the first three.

| Diagnosis | Sign | What to do |
|---|---|---|
| The site's name is not found (DNS) | the browser does not know such an address | wait, check from another network |
| Connection refused | "connection refused" | wait; check whether the site works only over `http` (below) |
| Certificate | a TLS error, the browser warns of danger | wait; whether to open it is for the human to decide |
| Bot protection | 403, a Cloudflare stub, a CAPTCHA | the human opens it themselves in an ordinary browser |
| A refusal to the program specifically | 403 to a script or agent, while everything opens in an ordinary browser | the site is alive, a zero from it is not a result; work in a browser |
| The resource has changed | the site works, but the section, database or function is no longer there | re-read the site afresh: the notes about it in your files are out of date |

One more case — a block by country or because of a VPN — is covered in [Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md), section 4. The same page has the list of sites that closed or changed in 2026.

Details [reader's experience]:
- **A refusal to a program.** The site of the Jewish community of Lithuania answered 403 to every automatic request and for three weeks stood in the author's notes as "dead", though it opened in a browser. The diagnosis: **only your program gets 403, while in a browser the page opens** — the site is alive, and a zero from it is not a result. What to do: open the page yourself in an ordinary browser or through an AI plugin in the browser. Do not disguise a program as a browser if the site's rules do not allow automatic access. On a CAPTCHA or a robot check — stop: from there a human acts ([Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md), section 3).
- **A site without HTTPS.** A tool that itself rewrites `http` to `https` gets a connection refusal, and it looks like "the archive is down". A South African catalogue of 8.3 million records opened only strictly over `http`.
- **403 for the whole domain, including `/robots.txt`,** is a server protection, not the absence of a page. In the log write "blocked", not "none".
- **A link from someone else's database leads by an old address scheme.** In one name database the "image" button led by an address scheme the archive had long abandoned. There is no 404 error: the link silently takes you to the archive's home page, and this is easy to take for "no image". If a link from an index brought you to the wrong place, look for the file **by its archival reference** on the archive's current site and do not write "not digitised".

## 2. The instrument too has a shelf life

That a negative result is valid only as of the date of the search is stated in [Standard of proof](../3-results/01-standard-of-proof.md), section 7: databases grow. The second half of the rule: **the instrument itself changes**. In a single day the author removed six false zeros, and two of them were about a resource, not about people. One site had put up a login, and "a zero from it" had since meant a zero from one database among many. On another, the text search had been switched off. The notes about them in the project files stayed the same [reader's experience].

→ When you repeat a search on old resources, check at the same time that the resource is **still the same**: the same access, the same databases, the same kind of search. In the research log keep next to a zero the date and what the instrument was like.

## 3. A zero from an address assembled by hand

AI (and a human too) often builds a query address itself: it puts parameters into a link or an API. **A wrong parameter name gives not an error but "nothing found".**

Examples [reader's experience]:
- in the Yad Vashem API the field for the submitter's surname is named differently from the web form (`submitter_ln_search_en` versus `submitter_ln`). A field name from the form, put into the API, gave a silent zero on a whole series of queries;
- the place parameters in the advanced search of the same resource did not work at all: a query for a shtetl that certainly exists gave zero. The sign is in the header of the results ("Search criteria"), which shows not what you asked for.

The opposite trap: **a made-up filter parameter is silently skipped by the database, which returns everything it has** — for the author 24 million records instead of a refusal [reader's experience]. A full list easily passes for the result of a search. Similar "quiet" failures of the JewishGen and USHMM forms are in [Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md), section 3, item 8.

→ **Compare the number found with the total size of the database**: if they match, the filter was not applied. And read what the database showed in the header of the results as your query.

🔑 **A zero from an address assembled by hand proves only that the address was assembled that way.** Take addresses from the pages of the site itself; how to demand this of an agent — [Working with agents](03-working-with-agents.md), section 4.

## 4. A control record — for each route

A control record ([Standard of proof](../3-results/01-standard-of-proof.md), section 7) tests the search itself. It has two limits [reader's experience]:
- **The same database opened another way is a different instrument.** One collection through the general search and through the collection's own page gave different results; in the second case a zero came out even for a surname known to be common. Run the control record **for each route separately**.
- **A control by place tests the place, not the surname.** In a "smart" search different spellings have different dictionaries of synonyms: `KREEL` pulls in `KRELL`, while `KRIL` pulls in nothing. A zero for one spelling with a confirmed place proves only that **this spelling** is absent. To close off a surname you need to go through the spellings with the same place.

## 5. Phonetic search also depends on the spelling

In [Names, surnames, spellings](../2-reference/03-names-spellings.md) (section 2) it is advised to begin with exact mode and add phonetic. The author's experience shows that phonetics does not cover everything either [reader's experience]:

- **Different sets.** The JewishGen general search, the surname Рабичев (Rabichev): `Rabichev` phonetically — 355 records, `Ryabichev` by the same algorithm — 47. And this is **not a subset** of the first: the second result contains whole databases that are not in the first (Belarusian voter lists, a concentration-camp card file), and other households in the census.
- **The gap can be counted.** The surname Пищик (Pishchik): `Pishchik` with synonyms — 111 records, literally — 107; `Piszczyk` — 1; together 108 of 111. `Pischik`, both with synonyms and literally, gives 10 — the remaining three do not fit in them. So at least seven records lie outside the earlier result, and the earlier note "all 111 viewed" was false. This is not a suspicion but a count.
- **It also happens the other way.** In Yad Vashem the mode with synonyms gathers all the spellings known to the database into one set: nine forms of the surname Беленький (Belenky) give exactly 1,850 records each. But `Belenkij`, `Byelenky`, `Belenkyi` give zero even with synonyms — the database simply does not know them.

🔑 So before you go through spellings, find out **what the search does: widens the query with synonyms or searches literally**. Going through spellings means different things in these two cases:
- in the literal one — so as to miss nothing;
- in the synonym one — to find out which spellings the database knows at all: a spelling it does not know gives a false zero.

And within Cyrillic: in a part-of-word search in one catalogue "Беленк" and "Беленьк" found partly different things — **the soft sign breaks the stem** [reader's experience]. Try the stem both with "ь" and without.

## 6. Pairs of cursive letters that break a search by stem

Don't read Russian? See [For English speakers](../0-start/08-for-english-speakers.md).

To the pairs from [Names, surnames, spellings](../2-reference/03-names-spellings.md), section 5 (Б/В, Ш/Т, Р/К, "-ель/-еръ"), the author adds: **г/ч · н/п · и/н · л/м · я/и** [reader's experience].

An example: the surname Велигура (Veligura) in the Omsk ZAGS books is written "Виличура". The stem "лигур" is not in this word, and a search by a truncated stem passes it by. This is a property not of one scribe but of a whole corpus: in another family and another uezd a record turned up, "Велигуров Величуров Иван Ильич" — two forms of one person in one line, and under one archival reference "Любава" and "Любовь" [reader's experience].

→ Found a form with "ч" — look for the form with "г", and vice versa.

## 7. Search by what the scribe could not distort

The surname is the longest and rarest word in a record, and it is spoiled first. The given name, patronymic, year and place of registration are shorter and more familiar: the scribe had heard them hundreds of times. For the author a family was found by a query **without the surname** — "all children of any Tikhon registered in such-and-such a settlement" — and the distorted surname surfaced in the results by itself [reader's experience].

The same technique for metrical records — write out the whole shtetl over a window of years and sort by the parents' names: [Scenarios](07-scenarios.md), B1, item 12.

## 8. An archive catalogue: ask with one word

On the catalogue of one oblast archive (the design is typical) [reader's experience]:

| Query | Answer |
|---|---|
| `похозяйственные книги Называевск` (household registers Nazyvayevsk) | 0, "Nothing found" |
| `Называевского района похозяйственные` (of Nazyvayevsk district household) | 0 |
| `похозяйственные` (household) | 6,644 files |
| `Называевск` (Nazyvayevsk) | 4,161 files |

The catalogue joins words with "AND" and looks for them **in one file title**. But files are titled "Household registers of the aul Ablay" (Похозяйственные книги аула Аблай): the document type and the district do not occur together in one title. **A two-word query gives a guaranteed zero**, however large the fond. This is the same case as in section 3: a zero proves only how the query was assembled.

→ Ask separately for the document type and separately for the place, and intersect the lists yourself.

In the same catalogue [reader's experience]:
- **a stem finds more than the full form**: "Велигура" — 1 file, "Велигур" — 2; the second turned out to be a personal file with an autobiography;
- **a book can be selected whole by the file's reference**, not by name: a query on the reference field (for the author of the form `fields[9]=д. 1336,`) returned all 492 records of the book. This removes the dependence on the "place of registration" column, which is filled in differently within one book;
- **one archive may have two search systems** with different results: for the name of one village — 52 files in one and 37 in the other. These are different sets, not one with different paging.

## 9. The most reliable zero — when the source itself names the total

Before building an external check, see **whether the source gives its own total**. A metrical book closes a month with a line like "total male five" (итого мужескаго пола пять) with the rabbi's signature, a revision gives the number of souls per household, an inventory gives the number of storage units. If the total agreed with the number of records read, the list could not have been overlooked, and the zero for the surname is firm. Checking the numbering of records and households is in the [`reading-archive-scans`](../../../skills/reading-archive-scans/SKILL.md) skill, the section "Proof of completeness" (Доказательство полноты).

The arithmetic of the document itself can also decipher conventional marks [reader's experience]. In a list of parishioners of a prayer house for 1896 there were marks explained nowhere: a blue "V" and a red "Н". There were exactly 66 blue ones and 32 red ones, one line was struck out with the note "excluded on account of death" (за смертію исключенъ) — 99 living. In the minutes of a failed meeting on the neighbouring frame it says that attendance "makes up less than 2/3" (составляетъ менѣе 2/3), that is, a lawful meeting needs two thirds. Two thirds of 99 is exactly 66. The author's conclusion: V — "appeared" (явился), Н — "did not appear" (не явился). This is a conclusion from a converging count inside the file, not from analogy.

## 10. For every zero — a number and a denominator

A zero without the number viewed does not count as a result (see "coverage" in the [Glossary](../0-start/06-glossary.md)). But a number without a denominator also says little [reader's experience]:
- "106 records for the shtetl" is 19% of the shtetl if it has 551 households;
- "our man is not among the 118 signatories" is 118 of 245 householders, 48%, and the direction is not closed.

→ Write in the research log: "viewed N of M (X%)" — and where M comes from.

## 11. One archive — two naming schemes on Commons

On Wikimedia Commons the files of one archive may be uploaded under two schemes of file names [reader's experience]:
- the Ukrainian — `ЦДІАК 1167-1-500 Метрична книга…`;
- the Russian — `Фонд 1240 Опись 1 Дело 46 Метрическая книга…`.

A query in one scheme does not find the files of the other: `ЦДІАК 1267` gave 0, `Фонд 1267` — 49 files. According to the author, in the same place, after several fonds were merged into one (2020), some files lie on Commons twice — under the old and the new number, as different scans. How to find a file by its reference in all variants of the name — the [`ukrainian-archives-on-commons`](../../../skills/ukrainian-archives-on-commons/SKILL.md) skill, step 3.

## 12. A file's title is a statement, not a fact

A file is titled "Metrical book of the synagogue of the shtetl Chernobyl, births 1864–1879" (Метрическая книга синагоги м. Чернобыль о рождении 1864–1879), and in the inventory itself there is a note: "error in the inventory, correctly the shtetl Khabnoe" (ошибка в описи, правильно м. Хабное) [reader's experience]. Read the annotation and the archive's notes in the inventory. File captions on Commons are also sometimes false — the [`reading-archive-scans`](../../../skills/reading-archive-scans/SKILL.md) skill.

Three more observations alongside [reader's experience]:
- **a fond may be by society, not by shtetl**: the metrical books of shtetl A lie in the fond of society B, to which it is registered. A family "of such-and-such society" lives now in one village, now in another, while its records are in one fond (on *pripiska* — [Records of the Russian Empire and the USSR](../2-reference/01-records-empire-ussr.md), section 4);
- **one shtetl may have two fonds — one per confession**, with neighbouring numbers: it is easy to order the Catholic one instead of the Jewish;
- **a whole kind of record may be absent because of the fond's composition, not because of loss**: for one shtetl after 1862 there are neither death books nor divorce books — only births and marriages. Before looking for a death, check in the inventory **whether death books were kept in this fond at all**. Otherwise a month goes on searching for what does not exist, and "not found" goes into the log. How to record such a gap — [Standard of proof](../3-results/01-standard-of-proof.md), section 7, "Gaps in the sources themselves".

## 13. A mark in a database is a property of the collection, not a fact read

Indexers often put a status ("murdered", "killed") on a whole collection by its type, without reading each record. For the author five cards carried the mark "murdered", and the death was recorded as proved. The collection was called "List of murdered Jews from Yizkor books", while the memorial entry itself said nothing about a death. The people it commemorated died their own death overseas — one five months before the Germans arrived, as the date on the gravestone shows [reader's experience].

→ Before accepting a status, ask: **was it read in a document or assigned to the whole collection?** And check whether the source is able to distinguish: if neighbouring records directly write "died in such-and-such a town" and yours is silent, the silence does not mean what it seems.

## 14. A relative's story: what to believe

In two long interviews, for the author **dates, addresses and family links were confirmed, but names were not** [reader's experience]. The narrator remembers that "uncle lived on such-and-such a street and left before the war", and mixes up whether it was Aron or Aaron. Do not fit a find to the name from the story — check it by date and address.

With other narrators memory mixes up years too ([Talking to relatives](../0-start/04-talking-to-relatives.md), section 5), so the general conclusion is more cautious: a name from a story is the least reliable field, and only a document confirms it.

> **How to ask AI**
>
> *For a plain chat, add: "If you can't open a source, say so; mark fonds, villages and dates you name from memory as [from memory, verify]. Answer in English, and give names, places and archive titles in the original script in parentheses." ([why](02-prompt-library.md)). The label (agent with a browser) is for an AI that opens websites itself; the other prompts suit any chat.*
>
> - *(agent with a browser)* "A query to the database [N] returned zero. Before recording a negative result, answer: did the control record pass by this same route; how many records are in the database in all and how many did the query return; does this search widen the query with synonyms or search literally; was the query address taken from a page of the site or assembled by hand." *Check yourself:* the control record is certainly in the database; the query address, opened in a browser, gives the same.
> - "The site [N] does not open: [what is visible on the screen]. What diagnosis is it — the site's name is not found, connection refused, certificate, bot protection, a refusal to the program specifically, the resource has changed, a block by country? What checks each? Do not circumvent the protection." *Check yourself:* open the site in an ordinary browser; pass the CAPTCHA yourself.
>
> *Bad → good:* "Is [surname] in the database [N]?" (a zero without a control record and spellings proves nothing) → "In the database [N] first find the control record [who is certainly there], then [surname] in all spellings; for each zero, how many records the database has in all."

---

**See also:** [Checking results](04-checking-results.md) · [Standard of proof](../3-results/01-standard-of-proof.md), section 7 · [Names, surnames, spellings](../2-reference/03-names-spellings.md) · [Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md) · [Working with agents](03-working-with-agents.md) · the [verifying-genealogy-findings](../../../skills/verifying-genealogy-findings/SKILL.md) skill
