# Prompt library for AI

What this section covers: ready-made prompts for an AI assistant — Claude, Gemini, ChatGPT and others — following the steps of the [route](01-search-route.md) "question → place → source → index → scan → verification → record". Copy them and put your own data in the square brackets. After each prompt it says what to check yourself.

The general rule: **an AI answer is a hypothesis, not a source.** Ask for an address (archive, file, frame or link) and a verbatim quotation for every find. Every section of the reference has its own "How to ask AI" box with prompts on the section's topic.

Don't read Russian? See [For English speakers](../0-start/08-for-english-speakers.md). Where a search needs Cyrillic, the prompts below say so.

## Add to any prompt: "not from memory"

An ordinary chat (ChatGPT, Gemini, Claude without access to websites) cannot open an archive inventory or a database. Asked "in which fond is … held", it will answer anyway — plausibly and often wrongly: it invents a fond number, mixes up villages with the same name, "remembers" a date. So add this to prompts that deal with facts:

> If you can't open a source, say so. Don't name fond or file numbers, village names, uezds, dates or website addresses from memory; if you do name them, mark each one "[from memory, verify]" and tell me where I can check it. Answer in English, and give names, places and archive titles in the original script in parentheses.

And ask for **a search plan and checkable sources**, not ready-made facts: not "in which fond are the records of shtetl N", but "where can I check whether the records of shtetl N survive and in which fond they are held".

**For a chat or for an agent.** Prompts without a label suit any chat: you give the AI a text, a scan or a table, and it works with what it is given. Prompts labelled *(agent with a browser)* require the AI to open websites itself (Claude Code, Claude in Chrome, the agent mode of other assistants). In an ordinary chat, use the "draw up a search plan" version instead, and open the websites yourself.

---

## Rules for a good prompt

- **One question at a time**, with an answer criterion.
- **Give what is already known**: extracts from your own files. Otherwise the AI will "discover" what has already been found.
- **Name the "doubles" that have been ruled out**: people you have already checked and rejected.
- **Ask it to tell you the plan first**: what we are looking for, what we rely on, what method.
- **Demand a checkable answer**: "write only what you see", mark anything uncertain with "(?)", an honest "not found" is a normal result.
- **Do not give AI passwords** or data about living people without need. Do not upload raw DNA data to a chat.

## Start: what is known and where to begin

**Break down a family story**
> Here is what I know about the family: [text]. Split it into three lists: (1) confirmed by a document — which one; (2) hearsay — whose; (3) contradictions and unclear points. Make a table "person — dates — place — source". Add nothing of your own.

*Check yourself:* the AI did not turn "hearsay" into "known" and did not add dates you never gave.

**Lay the events of the era over the table**
> Here is a table "who — where — when": [table]. Lay the events of the era over it for these places and years: wars, pogroms, evacuation, border changes, conscription. Mark which family stories do not fit by date and which document could check this. Every historical event comes with a link to a source.

*Check yourself:* the dates of events at the links given; a mismatch is a reason to check the legend, not to discard it.

**Choose the first question**
> Propose three options for a first research question based on this table. For each: which source can answer it, how accessible it is online, the stopping condition.

## Place

> I need to identify the place [name] [guberniya/oblast, if I know it] in [year]: what it was called then, which uezd and guberniya it belonged to, which state it belonged to, whether there are other places with the same name. Name the reference works to check this (JewishGen Communities, the "Lists of Populated Places" (Списки населённых мест), etc.) and say what to compare in them. Mark your guesses "[from memory, verify]".

*Check yourself:* in the reference work named; the uezd and volost match, not only the name.

## Source

**What survives**
> I am looking for [event: birth, marriage, death, revision] of [whom] in [place, uezd, guberniya] around [year]. Which types of document could have recorded it? Draw up a plan for checking: in which archive such documents are usually held and **where I can check** what survives and is digitised (consolidated catalogue, inventory, archive website, FamilySearch catalogue). Separately — substitutes, if there are no direct documents. Give fond numbers only with a link to a source; otherwise mark them "[from memory, verify]".

*Check yourself:* fond references — against the archive's inventory or its website; "survives" — against the consolidated catalogue, not the AI's memory.

**Plan**
> Here is what is known about the person: [extract]. The question: who were his parents? Draw up a plan: which documents could have mentioned him, where to look for them, in what order — from cheap (indexes, full text) to expensive (continuous reading); separately — what to do if the first step yields nothing.

## Index and spellings

**All spellings of a surname**
> Make a list of all possible spellings of the surname [N]: Cyrillic (including pre-reform orthography), Latin, Polish, Romanian and German transcriptions, Yiddish and Hebrew. Add variants with a different vowel in the root, with -ский/-цкий, -ман/-манн, and without the first letter (text recognition often loses it).

*Check yourself:* doubtful forms — against the Beider dictionaries index (stevemorse.org); if a form is not in the dictionaries, it is most likely a reading error (but the dictionaries do not cover every surname).

**Read an index row**
> Here is a row from the database: [text of the row, all fields]. Explain each field. What is the surname here, what is the patronymic, what is the place of registration? How do I get from this row to the record itself (archive, fond, inventory, file, frame)?

*Check yourself:* open the scan — the index mixes up fields.

## Scan: reading a document

**Read a document (first pass — no expectations)**
> This is a scan of [document type: metrical book / revision list / ZAGS record], [place], [year]. First read the printed table header — what is in which column. Then, line by line, write out [the columns needed] as written, in the spelling of the original. Mark anything illegible "(?)" and explain what gets in the way. Do not guess.

**Second pass — comparison with the hypothesis**
> Now compare what you read with what I am looking for: [names, age]. Which lines fit, which do not, and why? Where might your reading have adjusted itself to the expectation?

*Check yourself:* enlarge the fragment and read the name with your own eyes. AI reads proper names worse than everything else in the text.

**Hebrew and Yiddish**
> Read the inscription on the gravestone: the name, the father's name, the date by the Jewish calendar; convert the date to Gregorian (allowing ±1 day). Give the original spelling of the names.

> Translate the Yiddish article close to the text; leave names and towns in the original next to the translation; mark doubtful words "(?)".

## Verification

**Two candidates**
> Here are two people with the same name: [data]. Make a table of features (age, patronymic, place, relatives, occupation), mark matches and contradictions and which document would settle the question. The conclusion "same person" only with two independent matches.

**Check a conclusion**
> Here is my hypothesis and its grounds: [text]. Find the weak points: which grounds depend on each other, which contradictions are unexplained, which document could refute it.

**Check a "not found"**
> I did not find [whom] in [source]. Here is how I searched: [limits of the view, spellings, method]. Does that mean anything? Was the person obliged to appear in this source? What else should I check before recording a negative result?

## Dead ends

> The person is not in the revision of [year], although by age he should be. List the possible reasons (spelling, double name, estate, another society, omission, border, loss of the document) and how to check each.

> Many namesakes have turned up in [place]. How do I tell which of them are relatives? Which features (a surname from a place name or occupation, the set of given names across two generations, a clerk's unique mistake, witnesses) will work here and which will not?

## The emigrant branch

> Here is a death certificate from the USA: [text]. Which other documents should I look for (census, naturalisation, ship manifest, draft card), what each may say about place of birth and parents, and how to recognise a distorted shtetl name.

## Record and family history

**Record of a find**
> Write up the find using the template: date, source with the full archival reference and frame, verbatim quotation, translation, what it gives, what contradicts it, level of confidence. Add nothing beyond the document.

**Historical note for relatives**
> Write a paragraph about life in the shtetl [N] in [years]: the authorities, restrictions on Jews, occupations of the inhabitants. Every fact comes with a link to a source. Invent nothing about our family — only the general background.

## A task for an agent: continuous reading (agent with a browser, for advanced users)

> Read [the birth book, year], frames [X–Y]. In the father's column look for the surname [N] in any spelling. First find a control record (one that certainly exists): [record]. For every hit — the frame, record number, verbatim quotation, a crop. Keep a log "frame → record numbers". Pace — no more than one frame every 5–10 seconds. If a CAPTCHA appears, stop and click nothing. Do not launch other agents.

The full task template is in [Working with agents](03-working-with-agents.md), section 4.

## Continue work in a new session

> Read the "Continue from here" file and the research log. Retell in five lines: what the current question is, what has been done, what is waiting for me (CAPTCHAs, decisions), what the next step is. Do not start searching for anything until I confirm.

---

**See also:** [The search route](01-search-route.md) · [Checking results](04-checking-results.md) · [AI tools](05-ai-tools.md) · [Prompts from other authors](../../reading/ai-in-genealogy.md)
