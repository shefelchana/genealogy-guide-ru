---
name: genealogy-intake
description: Runs the first conversation with a person who is starting a family-history search or has just handed the assistant this guide — asks, in small batches, about names, dates, places, documents and photos at home, legends, relatives abroad, the goal (family story, citizenship, DNA, living relatives, fate of a war victim), languages, site access and accounts; sets up the project files from templates; turns what is known into a person–dates–place–source table; formulates the first research question with a stop condition; and proposes a concrete plan for the first one to two weeks. Use when someone begins genealogy research and the project has no files yet — even if the user only says "I want to find my ancestors", "where do I start", "here is everything I know about my grandmother", "read the guide and help me", "I am looking for my grandfather who was killed in the war". NOT for a project that already has its files — to resume after a break use research-session-handoff, to run the next research round use organizing-genealogy-research. Also triggers on Russian requests: «хочу найти предков», «с чего начать», «вот всё, что я знаю о бабушке», «прочитай руководство и помоги», «ищу деда, погибшего на войне».
---

# The first conversation: from "I want to find my ancestors" to a first question and a plan

A person at the start of a search usually brings a mixture: exact dates, scraps of legend, unlabelled photographs and a strong wish to "find out everything". The job of the first conversation is to sort this into verifiable and unverified, set up the files, and pick **one** question to start the work with. Start searching websites only after that. Without a foundation, searching turns into dashing between databases.

## If the person gave a link to the guide

First read the agent instructions AGENTS.md and the llms.txt map: they set the rules and the order of work. Then, as needed, the sections "Where to start", "How to keep files", "Standard of proof" and "Scenarios: what to do if…". Open the rest when it is needed. Tell the person in one sentence that you have read it and how you will work. If the guide is unavailable, work from this skill: it has everything needed for the first conversation.

## How to run the conversation

- **Ask in batches of 3–5 questions**, not a forty-item questionnaire. After each batch, briefly repeat what you understood. The person will correct you, and the error will not reach the files.
- **Start with the goal and with what the person already knows.** Ask the technical questions about access and accounts later.
- **Record verbatim and with a note of the source**: "so says Mum, conversation of 12.03.2026". Write place names as the narrator pronounces them: the home name of a shtetl (*mestechko*) may differ from the official one, and that is a lead.
- **Legends are hypotheses, not facts.** Do not argue and do not discard. Record them as a hypothesis with status ⚪ (not verified). Legends often confuse generations and dates, but a true detail does turn up: a place, a trade, relatives abroad.
- **Do not promise a result.** Say honestly that much depends on how well the documents for the place have survived.
- **Heavy subjects** (war, the Holocaust, repression) are touched gently and without insistence.
- **If people of the older generation are alive, interviewing them is the first item of the plan**: it cannot be postponed (*Am a-Zikaron*). It helps to split the talk into a genealogical one (dates, marriages, moves, documents, photos) and a biographical one (character, events). Ask about **very distant** relatives too: they often keep what close ones do not. Discrepancies between accounts are leads; they are recorded, not smoothed over.

The full list of questions by block is in `references/intake-questions.md`. Open it before the conversation and choose what fits the situation. There is no need to ask all the questions.

## What must be found out

1. **The goal.** It determines which documents are needed:
   - a family history for relatives: scans and quotations are enough;
   - citizenship or repatriation: documents for **every generation** and official copies are needed, and different spellings of names will have to be reconciled;
   - DNA: what has already been tested and where (without uploading raw data anywhere on your own initiative);
   - the fate of someone killed or missing: start with military and memorial databases;
   - living relatives: DNA, emigrant branches, communities.
2. **People**: the oldest person for whom there is at least one document, and his or her parents according to family accounts.
3. **Places**: where they were born and lived, with uezd (district) and guberniya (province) if known. The place matters more than the surname: it determines the archive and the set of surviving documents.
4. **What lies at home**: documents, photographs with captions, letters with addresses, work record books, military IDs, evacuation certificates. Ask the person to photograph and send them, and not to touch the originals.
5. **Emigrant branches**: who left, where and when. Documents of another country often name the shtetl and the parents directly.
6. **Languages**: which the person reads. Documents come in pre-reform Russian, Ukrainian, Polish, Romanian, Yiddish, Hebrew, German.
7. **Access**: country of residence and VPN (some sites are closed from abroad or through a VPN); which services already have accounts (JewishGen, FamilySearch, MyHeritage and others); whether you have access to a folder on the computer and to the browser.
8. **Time and budget**: how many evenings a week, whether the person is ready to pay for subscriptions or copies. Much is free, and there is no need to pay for what lies open.

**About accounts, ask only "do you have one".** Do not ask for or accept passwords. If the person sends a password into the chat, say it is not needed and advise changing it. Logging in, CAPTCHAs, payment and sending letters are done by the person, in their own browser.

## Setting up the project files

Create the project folder (with the person's consent and where they say) and the files from `assets/project-files.md`: findings log, persons, hypotheses, search log, source registry, timeline, "Continue from here". Why this matters from day one: a new AI session does not remember the previous one, and a month later the person will not remember where they already searched. If you have no access to a folder (an ordinary chat), do not pretend the files exist: at the end of every answer give a "Write to the files" block for the person (AGENTS.md, section 3a). Divide everything that came up in the conversation like this:
- names, dates and places **with a document** → into persons and timeline, noting which document;
- stories and legends → into hypotheses (⚪) and into persons with the note "according to …";
- what was sent (scans, photos) → into the source registry; name the files clearly: `year_type_who.jpg`.

## The first summary table

Build a "person — dates — place — source" table for everyone about whom anything is known. In the "source" column honestly write "Mum's account" if there is no document. This table at once shows where there is a foundation and where there is only memory.

Then **lay the events of the era over the table** by years and places (advice from N. Lipes): wars, pogroms, evacuation, border changes, conscription. Some legends immediately stop adding up by date, and you can see which documents are missing. This is a heuristic, not a verdict on the legend: a mismatch is a reason to check, not to discard.

## The first question

Choose **one** question with an answer criterion and a stop condition. A good first question:
- concerns a person whose **place** is known (better with the uezd);
- can be solved with an available source: the Soviet and military layer is closer and more accessible than the pre-revolutionary one; emigrant documents often name the place outright;
- takes one generation back, rather than a leap over three.

Bad: "find out more about my great-grandfather". Good: "where was grandfather, born 1912, born: look for him in the databases of war participants and in evacuation cards; stop after three databases". Show the person two or three variants of the first question and let them choose.

## A plan for 1–2 weeks

Fill in `assets/first-plan.md` and show it to the person. In the plan separate what the person does (find documents at home, interview relatives, log in to accounts, decide about DNA) from what you do (search the databases, a place guide, a timeline). The goal of the plan is modest: by the end of two weeks there is a table for all known people, a guide to the main place, and an answer to the first question, positive or "not found" with coverage. The guide includes a **survival map**: which documents exist for the place and years and which are lost; this is checked before searching for a specific person.

## How to end the conversation

Briefly retell: what has been recorded, what the first question is, what the person should do before the next meeting, what you will do. Update "Continue from here" (CONTINUE-FROM-HERE.md) so that the next session starts from this point.

See also the skills: `organizing-genealogy-research` (how to carry the research on), `research-session-handoff` (resume a project after a break), `search-logic-navigator` (where to go from a question), `tracing-emigrants-to-origin` (if there is an emigrant branch).
