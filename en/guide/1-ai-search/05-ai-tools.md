# AI tools: Claude, Gemini and others

What this section covers: what kinds of AI assistants there are, what they can really do in searching for ancestors, where they err, how to set tasks for them and how to organize the work so that finds can be verified. The experience of one real investigation (September–October 2026, Claude in the app with access to the project folder and a browser) plus the practices of other genealogists.

The main rule, repeated by everyone: **an AI answer is a hypothesis, not a source.** "Do not trust these things. Verify, verify, verify" (IAJGS AI Virtual Summit, 2026).

---

## 1. What an AI assistant can do

**Claude working with files and a browser** (Claude Code, the Claude app, the Claude in Chrome extension), from the experience of one investigation:
- **reads old documents from scans**: metrical books, revision lists, pre-reform orthography, handwritten 19th-century Russian, Hebrew and Yiddish (gravestones, newspapers, witnesses' signatures), Romanian and German questionnaires. Enlarges the needed column and reads by fragments;
- **searches databases**: JewishGen, FamilySearch, Yad Vashem, NLI newspapers, Yandex "Archive Search" (Russian-language), Wikimedia Commons, archive.org — and does not tire of going through dozens of spellings of one surname;
- **pages through whole archival files** (hundreds of frames) and keeps a log: which pages were viewed, what was found, what not;
- **correlates documents**: age in a revision ↔ year of birth in a metrical book ↔ a name in a newspaper; notices contradictions;
- **translates** (Yiddish, Hebrew, Romanian, German) and writes a historical note for a find;
- **maintains the project files**: dossier, hypotheses, research log, family history — and records a find at once;
- **launches helper agents** in parallel: for example, three read three different birth books at the same time;
- **writes a coherent text for relatives** on the basis of verified facts.

**Gemini (Google)** was used little in the same investigation:
- useful as a **second opinion**: difficult handwriting, an inscription on a gravestone, checking a translation;
- **Deep Research** mode — for a survey of a broad topic (the history of a shtetl, how an archive is organized);
- availability depends on country and plan (see below about Gemini in Chrome).

**What AI does not do and should not do:**
- does not pass captchas and "I am not a robot" checks — the human does that;
- does not enter passwords, create accounts or pay;
- does not send letters and requests on your behalf without your direct consent;
- does not replace an archive: if a document is not digitised, AI will not find it.

## 2. The main risks — and what to do about them

**1. Plausible errors ("hallucinations").** AI can confidently read a surname wrongly or "see" what it expects. Real cases:
- a database index gave "Ester, daughter of Duvid" — in fact a field-parsing error;
- «Рашковскій мещ.» (Rashkovsky mesh.) meant "meshchanin of the shtetl Rashkov", not a surname;
- «Михель Кр…торъ» (Mikhel Kr…tor) one wanted to read as «Репиторъ» (Repitor), but on enlargement it turned out to be «Кройторъ» (Kroitor);
- an agent cited an "already deciphered record" that did not exist (the fact itself, as it happened, proved correct).

→ **Every find comes with an address (archive, file, frame) and a verbatim quotation; the key points are checked by eye on an enlarged fragment.** Be especially careful with "expected" names from the task: AI tends to see what it is looking for.

**2. Rediscovery of what has been found.** A new session or a new agent does not remember the previous conversation. → Keep everything **in files**, not "in the chat's memory"; before a new search the AI first searches the project files.

**3. Resource consumption.** Agents can breed agents themselves and spend many tokens. → In every task: "do not launch other agents; if the work is too large — return a plan".

**4. Requests too fast → blocks.** AI works faster than a human, and sites notice. In one investigation FamilySearch gave a captcha after ~45–150 opened frames (more often about 130 in 40 minutes; over time — sooner); three agents in parallel plus one that pulled 1052 frames in 4 minutes all got captchas. NLI shut down after a hundred quick requests. → Set a pace (no more than one frame every 5–10 seconds, with breaks), do not download a whole film, **one site — one performer**. Details — [Access, captchas, pace](../2-reference/19-access-captchas-pace.md).

**5. A false zero.** A mass pass returned "0 finds" because all the site's responses were access errors. → Check any mass pass against a **positive control example** and by response codes.

**6. Privacy.** Do not give AI passwords, do not ask it to paste cookies or tokens into third-party services; data on living people — carefully. Steve Little's rule (the "water cooler rule"): do not enter anything sensitive where the storage policy is unclear. Cathryn Borges: do not upload DNA data — it cannot be taken back (RootsTech 2026). The authors of "Research Like a Pro with AI" warn that since September 2025 Claude trains on user data by default — check the privacy settings of your plan.

## 3. How to set tasks (tested)

- **One question at a time** with an answer criterion: "Find in the 1868 birth book of Kishinev the children of Yankel and Leya Rashkovsky".
- **Give what is already known** (extracts from files) and a **control record** — a record known to exist, taken from an index, to check that the AI reads correctly. In one investigation in a single day this technique three times showed at once whether the agent was reading correctly.
- **Demand a checkable report:** "write only what you see"; for every hit — the frame and quotation; mark uncertain readings; a **coverage log** ("frame N: records no. X–Y"); an honest "not found" is a normal result.
- **Name the "doubles" in advance** — people already checked and discarded.
- **Each agent gets its own folder** for files (and its own browser tab).
- **Save at once**: a find goes into the dossier, persons, hypotheses at the same moment.
- **Ask it to explain before searching**: what we are looking for, what we rely on, by what method.
- **Read in two passes.** In the first, give the AI the document type, year and place but not the expected names; in the second, compare what was read with your hypotheses. This combines two observations: context helps AI to read (L. Kessler, 2024), while expected names nudge it to "see" what is wanted.

An example of a short task:

> Read the birth book of [place, year] on FamilySearch (film …, frames …). We are looking for the children of [father] and [mother] [surname, all spellings]. Control record: [name, record number from the JewishGen index] — find it first. Write only what you see; for each find — frame, record number, verbatim quotation, confidence. Keep a coverage log. Pace — no more than one frame every 10 seconds; on a captcha stop and report. Do not launch other agents.

## 4. How to organize the work

- A project folder on your computer to which the AI has access; "anchor" files: dossier, persons, hypotheses, research log, source register, family history (see [Keeping files](../3-results/01-keeping-files.md)).
- A "Start here" or "Current direction" file — so that a new session understands at once where you stopped.
- Before compressing a long conversation — ask the AI to "save everything" into files.
- Backups before large text edits.
- For texts that relatives will read — a separate "History" file written from verified facts ([Writing the family history](../3-results/03-family-history.md)).
- Open every find by an agent yourself and check the quotation letter for letter.

## 5. What AI made possible (examples)

- The father of a man born in 1868 in Izmail was found in a **1889 University of Vienna questionnaire** ("Vater: Berco, Kaufmann, Ismail" — the merchant Berco from Izmail): in a German-language archive that one would hardly have looked into by hand.
- A **Yiddish newspaper correspondence of 1887** was read and fully translated.
- A **signature "Eliezer Moshkov Weinberg, Izmail, March 1884"** was found in a newspaper — it linked an American emigrant with the family.
- **Whole volumes** of revisions and metrical books (hundreds of pages) were read with a coverage log.

Details — [Examples of finds](../../examples/example-finds.md) and [Case study of a search](../../examples/case-study-newspaper-to-family.md).

## 6. Other people's experience: reading manuscripts

- **Gemini 3** on 50 English manuscripts of the 18th–19th centuries (Mark Humphrys's experience): character error 1.67%, word error 4.42%, no invented text found. **But** proper names and place names are recognized worse, and on illegible spots the result differs from run to run. Conclusion: treat the result as a draft, first of all check names, dates and kinship (aigenealogyinsights.com, 16.12.2025).
- **A Russian manuscript** (Louis Kessler, 2024): ChatGPT and Copilot read a letter of 1966 generally correctly, but **all three models misread the father's name**, including Claude 3.5; Claude noticed the Yiddish influence. The author's conclusion: names must be checked by a human (beholdgenealogy.com).
- **A passport of 1864** (pre-reform Cyrillic, Claude): with a detailed structured prompt the quality is much higher than with a short request. The model honestly marked the illegible; the rule "never invent text to fill gaps" (jgeppert.com, 2026).
- **Transkribus** — a specialized handwriting recognition program: Russian models (including "Russian Civil Records 1914–1968"), models for Hebrew and Yiddish. Free — 50 credits a month, roughly 50 pages [page read: transkribus.org/pricing, 2026-10-07].
- **Leo** (tryleo.ai) does not read Cyrillic [from search snippet].

## 7. Other people's experience: browser agents

- **Claude in Chrome** (official help support.claude.com): reads pages, clicks, fills in forms; needs a paid plan and the Google Chrome browser on a computer; for local files — Claude Desktop.
- **Gemini in Chrome ("auto browse")** (Google help): requires Google AI Pro or Ultra, at the time of checking — **USA only**, 18+, device language English; a limit of tasks per day; sensitive actions require confirmation.
- Vulnerabilities have been described in agentic browsers: malicious text on a page can hijack the agent (prompt injection). Do not let an agent act on unfamiliar sites unattended.
- The book by D. Elder and N. Elder Dyer **"Research Like a Pro with AI"** (2nd ed., 2026) works through such scenarios: an agent expands branches of the tree and looks for gaps, goes through library catalogues, keeps a log in a spreadsheet.

## 8. Principles of responsible AI in genealogy

The CRAIGEN coalition (craigen.org; adopted by the National Genealogical Society, USA): **accuracy, disclosure** (say that AI was used), **privacy, education, compliance with rules**. James Tanner (RootsTech 2026): when verifiable data runs out, AI "starts to please". Participants of the IAJGS AI Summit: talk to AI as to "a very smart intern on the first day" and ask it to cite sources.

More on people, courses and ready-made prompts — [AI in genealogy](../../reading/ai-in-genealogy.md).

## 9. Which tool for what

| Format | What it can do | What to use it for |
|---|---|---|
| **An ordinary chat** (Claude, ChatGPT, Gemini) | reads an uploaded scan, translates, explains, builds a plan | one document, translation from Yiddish/Hebrew, "what document is this and where to look next" |
| **Deep research mode** (Deep Research) | itself searches many sites and compiles a report with links | a survey of a topic: the history of a shtetl, which archives exist for a uezd, how documents of the era are organized |
| **An AI plug-in in the browser** | goes through sites in your browser, fills in search forms, pages through results | searching databases where you are already logged in (JewishGen, FamilySearch, MyHeritage) |
| **An AI agent with access to a folder on the computer** | maintains project files, reads whole files, launches helpers, records everything | long research, continuous reading of volumes, correlating many documents |
| **Special recognition programs** (Transkribus and others) | recognize manuscripts by trained models | large volumes of uniform manuscripts |

The availability of tools depends on the country — check in advance.

## 10. Example prompts

Ready-made prompts by route step are in the [Prompt library](02-prompt-library.md); prompts by topic are in the "How to ask AI" boxes in each section of the reference.

## 11. Skills for Claude in this repository

Ready skills are instructions that Claude loads itself when the task fits: verifying finds, reading scans, revisions, FamilySearch films, JewishGen, the Jewish press, pogroms, cemeteries and others. List and installation — [Skills for Claude](06-skills.md).

---

**See also:** [Working with agents](03-working-with-agents.md) · [Checking results](04-checking-results.md) · [AI in genealogy: people and courses](../../reading/ai-in-genealogy.md) · [Access, captchas, pace](../2-reference/19-access-captchas-pace.md) · [Standard of proof](../3-results/02-standard-of-proof.md) · [Scenarios: what to do if…](07-scenarios.md) (scenario C2)
