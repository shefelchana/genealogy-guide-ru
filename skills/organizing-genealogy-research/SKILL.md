---
name: organizing-genealogy-research
description: "Runs the working cycle inside an ongoing family-history project with an AI assistant — one active question at a time with a stop condition, checking the project's own files before any new search, pacing work so sites do not block, writing every finding into the project files at once, the short checklist before saying \"proven\", and closing a line of inquiry in two layers (cited fact + readable paragraph for relatives). Use during a research session in a project that already has its files — choosing the next question, before a new search, right after a find, when closing a direction — even if the user only says \"let's keep searching\", \"what do we look for now\", \"record this find\", \"is this proven yet?\", \"let's close this branch\". NOT for the first conversation with a newcomer — use genealogy-intake; NOT for briefing background agents or accepting their reports — use orchestrating-genealogy-agents; NOT for saving state before the session ends or is compacted, or resuming after a break — use research-session-handoff. Also triggers on Russian requests: «давай искать дальше», «что ищем теперь», «запиши находку», «это уже доказано?», «закрываем эту ветку»."
---

# How to run a genealogy investigation with AI

## Project files (create at the start)
- `FINDINGS-LOG.md` — the findings log: date, source with archival reference, verbatim quotation, crop, assessment.
- `PERSONS.md` — a reference of people (including an "associates" line: witnesses, business partners, neighbours, fellow travellers).
- `HYPOTHESES.md` — grounds / weak points / how to test / status on a single scale: 🟢 confirmed · 🟡 open / strong version · ⚪ not tested · 🔴 withdrawn.
- `SEARCH-LOG.md` — every search, including empty ones, with coverage.
- `SOURCES.md` — the register: archive, fond-inventory-file (*fond-opis-delo*), where the scan is, what has been read.
- `FAMILY-HISTORY.md` — a connected text for the relatives.
- `CONTINUE-FROM-HERE.md` — the current line of inquiry, running tasks, next steps. At the end of every session it is **rewritten in full**, not appended to: anything outdated is moved to the bottom or into an archive.
- `WHO-IS-WHO.md` (in a Russian-language project `КТО-ЕСТЬ-КТО.md`) — a table of namesakes and lookalikes: people with the same or similar names (grandfather and grandson, first cousins, people with the same surname from a neighbouring shtetl), their years, father, place and **the feature that tells them apart**, with a status 🟢/🟡/⚪/🔴. Start it as soon as a second person with the same name appears; add to it at every new mix-up. A technique from Polina Krivosheeva's practice.

## Start of a round
1. Read `CONTINUE-FROM-HERE.md`.
2. Formulate **one question** with an answer criterion and a time limit.
3. **Search your own files** (surname, place, given name) — so as not to rediscover what is found.
3a. **Before any identification** ("is this the same X?") — check against `WHO-IS-WHO.md`. This catches the mistake "we ruled out the right person by comparing him with the wrong namesake".
4. Tell the user briefly: what we are looking for, what we rely on, by what method.

## The task for the agent (verifiable)
- Put the **already known** into the task verbatim, with a list of **ruled-out lookalikes**; attach `WHO-IS-WHO.md`.
- **Do not let the agent read large logs whole** — only excerpts relevant to the question. A long log eats the agent's budget, and what is needed in it is a few lines.
- Give a **control record** — one that certainly exists, to check the reading.
- Require: "write only what you see"; for each hit — frame/folio + quotation + crop; mark what is uncertain; a **coverage log**; an honest "not found".
- A separate folder for each agent's files.
- "**Do not launch other agents.** If the volume is too large, return a plan and stop".
- **One site — one executor**; set the pace explicitly; on a captcha — stop, click nothing.
- Captchas, passwords, sending messages and payments are done only by the human.

## Receiving the report
1. **Check each find against the frame yourself** (agents see what they expect).
2. Check that a mass pass is not "empty because of errors" (were there 403 responses or a captcha).
3. Record at once: FINDINGS-LOG + PERSONS + status in HYPOTHESES + a line in SEARCH-LOG.

## Before the word "proven"
- The search was reasonably complete (coverage and spellings are named).
- The source is quoted with its archival reference.
- There is a **second independent** match (an index entry and the scan of the same record count as one piece of evidence).
- Contradictions are resolved explicitly.
- For indirect conclusions — a written justification.
Into the online tree — only what is confirmed.

## Closing a line of inquiry / end of session
- The outcome in two layers: a fact with its archival reference + a paragraph for the family history.
- Update `CONTINUE-FROM-HERE.md` (what works, what waits for the human — captchas, VPN, decisions).
- Record lessons (what worked, what slowed things down) — in a separate methodology file.

See also: `genealogy-intake` (the first conversation, no files yet), `orchestrating-genealogy-agents` (tasks for agents and accepting reports), `research-session-handoff` (saving a session and resuming after a break), `verifying-genealogy-findings`, `reading-archive-scans`.
