# Prompt library for AI

What this section covers: ready-made prompts for an AI assistant — Claude, Gemini, ChatGPT and others — by step of the route "question → place → source → index → scan → verification". Copy them and substitute your data in the square brackets. After each prompt it says what to check yourself.

*Note for English-speaking users:* the prompts below work in an English-language chat. Many of the documents and sites you will be pointing the AI to are in Russian, Ukrainian, Polish or Yiddish; tell the AI it may need to read sources in those languages and to give you the original text with a translation.

General rule: **an AI answer is a hypothesis, not a source.** Ask for an address (archive, file, frame or link) and a verbatim quotation for every find. Each section of the reference has its own "How to ask AI" box with prompts on the section's topic.

---

## Rules of a good prompt

- **One question at a time**, with an answer criterion.
- **Give what is already known**: extracts from your own files. Otherwise the AI will "discover" what has been found.
- **Name the ruled-out "doubles"**: people you have already checked and discarded.
- **Ask it first to describe the plan**: what we are looking for, what we rely on, by what method.
- **Demand a checkable answer**: "write only what you see", anything uncertain with a "(?)" note, and an honest "not found" is a normal result.
- **Do not give the AI passwords** or data on living people without need. Do not upload raw DNA data into a chat.

## Start: what is known and where to begin

**Break down a family story**
> Here is what I know about the family: [text]. Divide it into three lists: (1) confirmed by a document — which one; (2) hearsay — whose; (3) contradictions and unclear points. Make a "person — dates — place — source" table. Add nothing of your own.

*Check yourself:* the AI did not turn "hearsay" into "known" and did not add dates you did not give.

**Lay the events of the era over it**
> Here is the "who — where — when" table: [table]. Lay over it the events of the era for these places and years: wars, pogroms, evacuation, border changes, conscription. Mark which family stories do not fit by date and which document could check it. Give every historical event with a link to a source.

*Check yourself:* the dates of events through the links given; a mismatch is a reason to check the legend, not to discard it.

**Choose a first question**
> Propose three variants of a first research question based on this table. For each: which source can answer it, how accessible it is online, the stopping condition.

## Place

> Where is [name] [guberniya/oblast, if I know it]? What was it called in [year], which uezd and guberniya did it belong to, which state? Are there other places with the same name? Name the reference work to check against (JewishGen Communities, the "Lists of Populated Places", etc.).

*Check yourself:* against the named reference work; the uezd and volost must match, not just the name.

## Source

**What survives**
> I am looking for [event: birth, marriage, death, revision] of [whom] in [place, uezd, guberniya] around [year]. What types of documents could have recorded it? Where should they be held (archive, fond), and which of them survive and are digitised? Separately — substitutes, if there are no direct documents. Mark what you know for certain and what you are assuming.

*Check yourself:* fond references — against the archive's inventory or its website; "survives" — against a consolidated catalogue, not the AI's memory.

**Plan**
> Here is what is known about the person: [extract]. Question: who were his parents? Make a plan: which documents could have mentioned him, where to look for them, in what order — from cheap (indexes, full text) to expensive (continuous reading); separately — what to do if the first step yields nothing.

## Index and spellings

**All spellings of a surname**
> Make up all possible spellings of the surname [N]: Cyrillic (including pre-reform orthography), Latin, Polish, Romanian and German transcriptions, Yiddish and Hebrew. Add variants with a different vowel in the root, with -sky/-tsky, -man/-mann, and without the first letter (text recognition often loses it).

*Check yourself:* doubtful forms against the index of Beider's dictionaries (stevemorse.org); if a form is not in the dictionaries it is most likely a reading error (but the dictionaries do not cover all surnames).

**Read a row of an index**
> Here is a row from a database: [text of the row, all fields]. Explain each field. What here is the surname, what the patronymic, what the place of registration? How do I get from this row to the record itself (archive, fond, inventory, file, frame)?

*Check yourself:* open the scan — indexes mix up fields.

## Scan: reading a document

**Read a document (first pass — without expectations)**
> This is a scan of [document type: metrical book / revision list / ZAGS record], [place], [year]. First read the printed table header — what is in which column. Then line by line write out [the columns needed] as written, in the original spelling. Mark anything illegible "(?)" and explain what hinders. Do not guess anything. The document is in Russian (or Ukrainian/Polish/Hebrew/Yiddish) — give me the original text and an English translation side by side.

**Second pass — comparison with the hypothesis**
> Now compare what you read with what I am looking for: [names, age]. Which lines fit, which do not, and why? Where might your reading have adjusted itself to the expectation?

*Check yourself:* enlarge the fragment and read the name with your own eyes. AI reads proper names worse than all the rest of the text.

**Hebrew and Yiddish**
> Read the inscription on the gravestone: the name, the father's name, the date by the Jewish calendar; convert the date to Gregorian (allowing ±1 day). Give the original spelling of the names.

> Translate the Yiddish note close to the text; leave names and towns in the original beside the translation; mark doubtful words "(?)".

## Verification

**Two candidates**
> Here are two people with the same name: [data]. Make a table of features (age, patronymic, place, relatives, occupation), mark matches and contradictions and which document would settle the question. The conclusion "the same person" only with two independent matches.

**Check a conclusion**
> Here is my hypothesis and its grounds: [text]. Find the weak points: which grounds depend on each other, which contradictions are unexplained, which document could refute it.

**Check "not found"**
> I did not find [whom] in [source]. Here is how I searched: [limits of viewing, spellings, method]. Does this mean anything? Was the person obliged to appear in this source? What else should be checked before recording a negative result?

## Dead ends

> The person is not in the revision of [year], although by age he should be. List the possible reasons (spelling, double name, estate, another society, transfer, border, loss of the document) and how to check each.

> Many namesakes turned up in [place]. How do I tell which of them are relatives? Which features (a toponymic or occupational surname, the set of given names in two generations, a unique clerk's error, witnesses) will work here and which will not?

## Emigrant branch

> Here is a death certificate from the USA: [text]. Which other documents should I look for (census, naturalization, ship manifest, draft card), what may each contain about birthplace and parents, and how to recognize a distorted name of a shtetl.

## Recording and family history

**Recording a find**
> Format the find by the template: date, source with full archival reference and frame, verbatim quotation, translation, what it gives, what contradicts, confidence level. Add nothing beyond the document.

**A historical note for relatives**
> Write a paragraph about life in the shtetl [N] in [years]: authorities, restrictions on Jews, residents' occupations. Every fact with a link to a source. Invent nothing about our family — only the general background.

## A task for an agent on continuous reading (for advanced users)

> Read [the birth book, year], frames [X–Y]. In the father's column look for the surname [N] in any spelling. First find a control record (one known to exist): [record]. For each hit — the frame, record number, verbatim quotation, a crop. Keep a log "frame → record numbers". Pace — no more than one frame every 5–10 seconds. On a captcha — stop and press nothing. Do not launch other agents.

The full task template — [Working with agents](03-working-with-agents.md), section 4.

## Continue work in a new session

> Read the "Continue from here" file and the research log. Retell in five lines: what the current question is, what has already been done, what awaits me (captchas, decisions), what the next step is. Do not start searching for anything until I confirm.

---

**See also:** [Search route](01-search-route.md) · [Checking results](04-checking-results.md) · [AI tools](05-ai-tools.md) · [Ready-made prompts by other authors](../../reading/ai-in-genealogy.md)
