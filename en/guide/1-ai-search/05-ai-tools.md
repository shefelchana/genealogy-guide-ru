# AI tools: Claude, Gemini and others

What this section covers: what kinds of AI assistants there are, what they can really do in searching for ancestors, where they go wrong, how to set them tasks and how to organise the work so that finds can be checked. The experience of one real project (September–October 2026, Claude in the app with access to the project folder and a browser) plus the practices of other genealogists.

The main rule, repeated by everyone: **an AI answer is a hypothesis, not a source.** "Do not trust these things. Verify, verify, verify" (IAJGS AI Virtual Summit, 2026).

---

## 1. What an AI assistant can do

**Claude working with files and a browser** (Claude Code, the Claude app, the Claude in Chrome extension), from the experience of one project:
- **reads old documents from scans**: metrical books, revision lists, pre-reform orthography, handwritten 19th-century Russian, Hebrew and Yiddish (gravestones, newspapers, witnesses' signatures), Romanian and German forms. Enlarges the column needed and reads by fragments;
- **searches databases**: JewishGen, FamilySearch, Yad Vashem, NLI newspapers, Yandex "Archive Search" (Поиск по архивам), Wikimedia Commons, archive.org — and does not tire of trying dozens of spellings of one surname;
- **pages through whole archival files** (hundreds of frames) and keeps a log: which pages were viewed, what was found, what was not;
- **compares documents**: age in a revision ↔ year of birth in a metrical record ↔ a name in a newspaper; notices contradictions;
- **translates** (Yiddish, Hebrew, Romanian, German) and writes a historical note for a find;
- **keeps the project files**: finds log, hypotheses, research log, family history — and records a find at once;
- **launches helper agents** in parallel: for example, three read three different birth books at the same time;
- **writes a coherent text for relatives** on the basis of checked facts.

**Gemini (Google)** was used little in the same project:
- useful as a **second opinion**: difficult handwriting, an inscription on a gravestone, checking a translation;
- the **Deep Research** mode — for an overview of a broad topic (the history of a shtetl, how an archive is organised);
- availability depends on the country and the plan (see below on Gemini in Chrome).

**What AI does not do and should not do** (CAPTCHAs, passwords, payment, letters on your behalf, information from memory instead of a source) — the list is in [Checking results](04-checking-results.md), section 6.

## 2. The main risks — and what to do about them

**1. Plausible errors ("hallucinations").** AI can confidently misread a surname or "see" what it expects. Real cases:
- a database index gave "Ester, daughter of Duvid" — in fact a field-parsing error;
- "Рашковскій мещ." meant "meshchanin of the shtetl Rashkov", not a surname;
- "Михель Кр…торъ" was tempting to read as "Репиторъ", but on enlargement it turned out to be "Кройторъ";
- an agent cited an "already deciphered record" that did not exist (the fact itself turned out to be right).

→ **Every find comes with an address (archive, file, frame) and a verbatim quotation; the key points are checked by eye on an enlarged fragment.** Be especially careful with "expected" names from the task: AI tends to see what it is looking for.

**2. Rediscovery of what has already been found.** A new session or a new agent does not remember the previous conversation. → Keep everything **in files**, not "in the chat's memory"; before a new search the AI first searches the project files.

**3. Use of resources.** Agents can spawn agents themselves and spend many tokens. → In every task: "do not launch other agents; if the work is too large, return a plan".

**4. Requests that are too fast → blocks.** AI works faster than a human, and sites notice: FamilySearch shows a CAPTCHA, NLI closes, and several agents on one site all get CAPTCHAs. → Set a pace (no more than one frame every 5–10 seconds, with breaks), do not download a whole film, **one site — one performer**. Figures by site and cases — [Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md).

**5. The false zero.** A mass pass returned "0 finds" because all the site's answers were access errors. → Check any mass pass against a **positive control example** and by response codes. Other kinds of false zero — a wrongly assembled query address, synonym and literal search, a catalogue that looks for all words in one title — are in the section [The false zero](09-false-zero.md).

**6. Privacy.** Do not give AI passwords, do not ask it to paste cookies or tokens into third-party services; be careful with data about living people. Steve Little's "water-cooler rule": do not enter anything sensitive where the storage policy is unclear. Kathryn Borges: do not upload DNA data — it cannot be taken back (RootsTech 2026). The authors of "Research Like a Pro with AI" warn that since September 2025 Claude by default trains on user data — check the privacy settings of your plan.

## 2a. Technical traps: scripts, files, downloads

When an agent not only visits sites but also writes scripts, whole runs are lost on small things. The list was sent by a reader of the guide whose agents worked on Windows (October 2026, CC BY 4.0); the label **[reader's experience]** means checked by them, not repeated by the compiler ([Glossary](../0-start/06-glossary.md)):

- **Script encoding and Cyrillic.** A script with Cyrillic inside can silently give zeros for all queries — not an error, but empty results, because the environment read the file in the wrong encoding (for the author PowerShell 5.1 read a `.ps1` as ANSI). Pass Cyrillic as command-line arguments or check the file's encoding; a control query with a known result catches this at once. Also there for the author: reading text with an explicitly set encoding still switched to UTF-8 on seeing a BOM mark — for byte-level work, read bytes; and requests in PowerShell 5.1 without `-UseBasicParsing` failed with "NonInteractive mode" — a failure of the environment, not of the site [reader's experience].
- **"Saved" does not yet mean saved.** A script that printed a success message may have written nothing. Check the size and date of the output file [reader's experience]. The same goes for edits on sites — [Hand the routine to agents](08-routine-for-agents.md), section 3.
- **A 200 response is not necessarily a picture.** An image store can return a success code and, instead of an image, the shell of a web application: for the author two different frames gave files of identical length. It is caught by checking the first bytes of the file: a JPEG begins with `FF D8` [reader's experience].
- **Results visible only in a browser.** Some catalogues draw the results in with a script on the page, and they are not in the HTML that a program receives. A programmatic request will return a false zero — look in a browser [reader's experience].
- **Wikimedia Commons thumbnails.** Take the thumbnail address from the `api.php` response (parameters `iiurlwidth` and `iiurlparam`) rather than assembling it yourself: a guessed address gives an instant 404 error that looks like a rate limit [reader's experience]. Permitted widths and other subtleties — the [`reading-archive-scans`](../../../skills/reading-archive-scans/SKILL.md) skill.
- **JPEG 2000 inside a PDF.** In some PDFs the images are stored in JPEG 2000 format (`/JPXDecode`). A byte search for the JPEG markers `FFD8…FFD9` then gives a false zero "no pictures", and the author found no decoder for Windows [reader's experience]. Check the type of images in a PDF before extracting; another non-standard case, a raw raster, is covered in the same skill.
- **The browser blocks multiple downloads.** When an agent pulls a multi-page file through a browser, the browser blocks the automatic download of many files in a row. Join the pages into one file [reader's experience].

**A disputed word** [reader's experience]. Cut it out separately and stretch it to 1500–2000 pixels wide, and decide **by the ending and the number of letters**: "рабичовъ" is 8 letters and "-овъ", "рабиновичъ" is 10 letters and "-овичъ". Do not crop the leftmost columns: they show whether a row is complete. The other techniques — reading by strip, comparing with letters of the same pen, two passes with AI — are in the [`reading-archive-scans`](../../../skills/reading-archive-scans/SKILL.md) skill and in [Handwriting, transliteration, dates](../2-reference/05-handwriting-transliteration-dates.md).

## 3. How to set tasks (tested)

Don't read Russian? See [For English speakers](../0-start/08-for-english-speakers.md).

- **One question at a time** with an answer criterion: "Find in the 1868 birth book of Kishinev the children of Yankel and Leya Rashkovsky".
- **Give what is already known** (extracts from files), and a **control record** — a record from an index that certainly exists, to check that the AI reads correctly. In one project in a single day this technique showed three times at once whether the agent was reading correctly.
- **Demand a checkable report:** "write only what you see"; for every hit — the frame and a quotation; mark an uncertain reading; a **coverage log** ("frame N: records no. X–Y"); an honest "not found" is a normal result.
- **Name the "doubles" in advance** — people already checked and rejected.
- **Each agent gets its own folder** for files (and its own browser tab).
- **Save at once**: a find → the finds log, persons, hypotheses at the same moment.
- **Ask it to tell you before searching**: what we are looking for, what we rely on, what method.
- **Read in two passes.** In the first, give the AI the document type, year and place but not the expected names; in the second, compare what was read with your hypotheses. This combines two observations: context helps AI read (L. Kessler, 2024), while expected names push it to "see" what is needed.

An example of a short task:

> Read the birth book [place, year] on FamilySearch (film …, frames …). We are looking for the children of [father] and [mother] [surname, all spellings, in Cyrillic]. Control record: [name, record number from the JewishGen index] — find it first. Write only what you see; for every find — the frame, record number, verbatim quotation, confidence. Keep a coverage log. Pace — no more than one frame every 10 seconds; on a CAPTCHA stop and report. Do not launch other agents.

## 4. How to organise the work

- A project folder on your computer to which the AI has access; "anchor" files: finds log, persons, hypotheses, research log, source register, family history (see [Keeping files](../0-start/02-keeping-files.md)).
- A "Continue from here" file ([template](../../templates/continue-from-here.md)) — so that a new session immediately understands where you stopped.
- Before compacting a long conversation — ask the AI to "save everything" into files.
- Backups before large edits of text.
- For texts that relatives will read, a separate "History" file written from checked facts ([How to write the family history](../3-results/02-family-history.md)).
- Open every find by an agent yourself and check the quotation letter for letter.

## 5. What AI made possible (examples)

- The father of a man born in Izmail in 1868 was found in a **1889 University of Vienna form** ("Vater: Berco, Kaufmann, Ismail" — the merchant Berko from Izmail): in a German-language archive that one would hardly have looked into by hand.
- A **newspaper correspondence of 1887 in Yiddish** was read and fully translated.
- A **signature "Eliezer Moshkov Weinberg, Izmail, March 1884"** was found in a newspaper — it linked an American emigrant to the family.
- **Whole volumes** of revisions and metrical books (hundreds of pages) were read with a coverage log.

More — [Example finds](../../examples/example-finds.md) and [A case study of a search](../../examples/case-study-newspaper-to-family.md).

## 6. Other people's experience: reading manuscripts

- **Gemini 3** on 50 English manuscripts of the 18th–19th centuries (the experience of Mark Humphries): a character error rate of 1.67%, a word error rate of 4.42%, no invented text was found. **But** proper names and place names are recognised worse, and on illegible passages the result differs from run to run. Conclusion: treat the result as a draft, check names, dates and kinship first (aigenealogyinsights.com, 16.12.2025).
- **A Russian manuscript** (Louis Kessler, 2024): ChatGPT and Copilot read a letter of 1966 correctly on the whole, but **all three models misread the father's name**, Claude 3.5 included; Claude noticed Yiddish influence. The author's conclusion: names must be checked by a human (beholdgenealogy.com).
- **A passport of 1864** (pre-reform Cyrillic, Claude): with a detailed structured prompt the quality is much higher than with a short request. The model honestly marked what was illegible; the rule "never invent text to fill gaps" (jgeppert.com, 2026).
- **Transkribus** — a specialised handwriting recognition program: Russian models (including "Russian Civil Records 1914–1968"), models for Hebrew and Yiddish. Free — 50 credits a month, about 50 pages [checked: transkribus.org/pricing, 2026-10-07].
- **Leo** (tryleo.ai) does not read Cyrillic [from search snippet].

## 7. Other people's experience: agents in the browser

- **Claude in Chrome** (the official help support.claude.com): reads pages, clicks, fills in forms; needs a paid plan and the Google Chrome browser on a computer; for local files — Claude Desktop.
- **Gemini in Chrome ("auto browse")** (Google help): needs Google AI Pro or Ultra, at the time of checking **the USA only**, 18+, device language English; a daily limit of tasks; sensitive actions need confirmation.
- Agentic browsers have described vulnerabilities: malicious text on a page can take control of the agent (prompt injection). Do not let an agent act on unfamiliar sites unsupervised.
- The book by D. Elder and N. Elder Dyer **"Research Like a Pro with AI"** (2nd ed., 2026) walks through such scenarios: an agent opens up branches of the tree and looks for gaps, goes through library catalogues, keeps a log in a table.

## 8. Principles of responsible AI in genealogy

The CRAIGEN coalition (craigen.org; adopted by the National Genealogical Society of the USA): **accuracy, disclosure** (say that AI was used), **privacy, education, compliance with the rules**. James Tanner (RootsTech 2026): when verifiable data runs out, AI "starts to please". Participants of the IAJGS AI Summit: talk to AI as to "a very smart intern on the first day" and ask it to give sources.

More about people, courses and ready prompts — [AI in genealogy](../../reading/ai-in-genealogy.md).

## 9. Which tool for what

| Format | What it can do | What to use it for |
|---|---|---|
| **Ordinary chat** (Claude, ChatGPT, Gemini) | reads an uploaded scan, translates, explains, builds a plan | one document, translation from Yiddish/Hebrew, "what kind of document is this and where to look next" |
| **Deep research mode** (Deep Research) | searches many sites itself and assembles a report with links | an overview of a topic: the history of a shtetl, which archives exist for an uezd, how the documents of the era are organised |
| **An AI plugin in the browser** | visits sites in your browser, fills in search forms, pages through results | searching databases where you are already logged in (JewishGen, FamilySearch, MyHeritage) |
| **An AI agent with access to a folder on your computer** | keeps the project files, reads whole files, launches helpers, records everything | long research, continuous reading of volumes, cross-checking many documents |
| **Specialised recognition programs** (Transkribus and others) | recognise manuscripts with trained models | large volumes of manuscripts of one kind |

The availability of tools depends on the country — check beforehand.

## 10. Example prompts

Ready prompts by route step are in the [Prompt library for AI](02-prompt-library.md); prompts by topic are in the "How to ask AI" boxes in every section of the reference.

## 11. Skills for Claude in this repository

Ready-made skills are instructions that Claude loads by itself when a task fits: checking finds, reading scans, revisions, FamilySearch films, JewishGen, the Jewish press, pogroms, cemeteries and others. The list and installation — [Skills for Claude](06-skills.md).

---

**See also:** [Working with agents](03-working-with-agents.md) · [Checking results](04-checking-results.md) · [The false zero](09-false-zero.md) · [AI in genealogy: people and courses](../../reading/ai-in-genealogy.md) · [Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md) · [Standard of proof](../3-results/01-standard-of-proof.md) · [Scenarios: what to do if…](07-scenarios.md) (scenario C2)
