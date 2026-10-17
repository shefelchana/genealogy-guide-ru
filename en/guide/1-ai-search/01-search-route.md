# The search route: question → place → source → index → scan → verification → record

What this section covers: the scheme on which any genealogical search is built, with an AI assistant or without one. This is the main text about the route: other sections mention it in one line with a link here. At each step: what should result, what you can give to AI, what to check yourself. Most dead ends are not a lack of documents but a skipped step: searching for a surname without a place, believing an index without the scan, reading the wrong volume.

---

## The scheme

```
 QUESTION ──► PLACE ──► SOURCE ──► INDEX ──► SCAN ──► VERIFICATION ──► RECORD
 (one, with  (uezd and  (which     (is there  (frame,   (second         (finds,
 a criterion guberniya  document   an index   record    independent     hypotheses,
 and a       for the    could have or full    number,   feature,        log — and an
 stop)       right      recorded   text)      quotation) contradictions) empty result)
             year)      it, does
                        it survive)
      ▲                                                                │
      └──────────────── next question ◄─────────────────────────────────┘
```

If the search is stuck, first determine **at which step**, then go back to it. Typical forks are in the [Scenarios](07-scenarios.md).

## Step 1. Question

**Output:** one question with an answer criterion and a stopping condition.

- Bad: "find out everything about my great-grandfather". Good: "find the record of my grandfather's birth around 1880 in the metrical books of the rabbinate of shtetl N; stop if all surviving years 1875–1885 have been viewed".
- Before the question — **what is already known**: search your own files. A new AI session does not remember the previous one and easily "finds" what has already been found.
- Lay the events of the era over the "who — where — when" table: wars, pogroms, evacuation, border changes, conscription. Some family legends immediately stop fitting by date, and you can see which documents are missing (advice from N. Lipes; this is a heuristic, not a verdict on the legend).

**What to give AI:** to break your account into "known from a document" and "hearsay", and to propose two or three questions to choose from. **What to check yourself:** that the question really is one and can be checked.

## Step 2. Place

**Output:** a settlement with uezd and guberniya **for the year of the event**; you have made sure it is not a second place with the same name.

- The place determines the archive and the set of documents. The surname does not.
- Distinguish **place of registration** (*pripiska*; where a person was listed as a meshchanin or merchant; revisions and conscription followed it) from **place of residence** (where the children were born, where the 1897 census took place). These are two different archival addresses.
- If there are no documents about the place, type the name of the shtetl into a search engine with the word "genealogy" (or "генеалогия" for Russian-language pages): often you find forums where this place has already been searched and what survives has been described.

Details — [Places and maps](../2-reference/06-places-maps.md), [Place guide](../0-start/05-plan-timeline-place.md).

## Step 3. Source

**Output:** which type of document could have recorded the event, whether it survives for the right years, and where it is held.

- First, a **map of survival** for the place: what exists, what is lost, what has not been filmed. "Not found" in a volume that did not survive is not a result.
- Look at **all surviving years**, not only the year the family named: that is how siblings who died in infancy, cousins and the year of a move are found (N. Lipes).
- Records of a shtetl are sometimes bound into the books of **a neighbouring rabbinate or the district town**; the metrical books of a shtetl without a crown rabbi could have gone to the *zemsky* court (rural district court), even of another uezd. Check the neighbours before concluding "there are no books".
- If there are no direct documents, look for substitutes: censuses, police files, recruitment and tax lists, notarial records, directories, the press.

Details — [Records of the Russian Empire and the USSR](../2-reference/01-records-empire-ussr.md), [Archives by country](../2-reference/07-archives-by-country.md).

## Step 4. Index

**Output:** whether an index or full-text search exists; a result with a record number and frame.

- **Cheap checks first, then continuous reading.** An index tells you in a minute in which file and which section the surname stands. Page-turning without it takes hours.
- Where to look for indexes: the JewishGen, FamilySearch and JRI-Poland databases; community surname lists (the Jewish Roots forum — Еврейские корни, in Russian); alphabetical indexes inside the files themselves; full-text corpora (Genealogy Indexer, Yandex "Archive Search" — Поиск по архивам, in Russian; NLI newspapers). Details — [Community surname indexes](../2-reference/08-surname-indexes.md). Don't read Russian? See [For English speakers](../0-start/08-for-english-speakers.md).
- Before reading a Ukrainian file, check by its archival reference whether it is online and where: the consolidated index "Duck Inspector" (Качиний Інспектор, inspector.duckarchive.com) searches by archive, fond, inventory and file. An empty answer does not mean there is no scan.
- Indexes grow: in 2026 the JewishGen Ukraine Research Division was adding 100–150 thousand records a month. A negative result is valid only as of the date of the search — record the date and repeat the search after additions.

## Step 5. Scan

**Output:** frame, record number, verbatim quotation in the original spelling.

- An index errs: it mixes up fields (the groom's father becomes the bride's father), takes a note of estate ("…ский мещ.", i.e. "meshchanin of …") for a surname, loses the first letter. Check every index row against the scan.
- Take the original scan, not a preview; first read the printed table header.
- When reading with AI, give it the document type, year and place but **not the expected names**: AI tends to see what it is looking for. Comparison with your hypotheses is the second pass.

Details — [Handwriting, transliteration, dates](../2-reference/05-handwriting-transliteration-dates.md).

## Step 6. Verification

**Output:** a second independent feature (patronymic, age, place, names of relatives, occupation); contradictions named and explained.

- A surname alone is not a match. A surname plus place may also be a coincidence of namesakes.
- The index and the scan of the same record are one piece of evidence, not two.
- Open a find by AI or an agent yourself and check the quotation letter for letter — [Checking results](04-checking-results.md).

Details — [Standard of proof](../3-results/01-standard-of-proof.md).

## Step 7. Record

**Output:** the find — in the finds log with its archival reference and quotation; hypotheses updated; the research log records where you searched and with what result, **including an empty one** (source, limits of the view, spellings, method of search).

Details — [Keeping files](../0-start/02-keeping-files.md).

## What not to do on the route

- Do not jump to "write to the archive" or "take a DNA test" until the cheap steps have been passed: indexes, full text, neighbouring years and places. A letter to an archive comes after the online routes, is addressed to a specific archive, and quotes the exact archival reference; the decision and the sending are the human's ([Requests and letters](../2-reference/20-requests-letters.md)).
- Do not enter guesses into an online tree: the tree is only for what is confirmed.
- Do not leap across generations to a "famous ancestor" with the same surname: without intermediate links that is not kinship but coincidence.

---

**See also:** [Prompts for AI by route step](02-prompt-library.md) · [Working with agents](03-working-with-agents.md) · [Scenarios: what to do if…](07-scenarios.md) · [Cheat sheet "question → where to go"](../../catalog/README.md) · the [`search-logic-navigator`](../../../skills/search-logic-navigator/SKILL.md) skill
