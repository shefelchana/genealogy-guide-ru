---
name: orchestrating-genealogy-agents
description: Coordinates several AI agents in a family-history search — assigns roles (coordinator, reader, mechanic, web researcher), runs one research iteration at a time, splits work by source and by site (one site, one executor), writes a verifiable task brief from a template, accepts results only after checking each find against the scan, the control record, the coverage log and the site's error codes, picks a model per task, and handles typical failures (captcha, 403/429, silent agent, agents spawning agents). Use whenever work is delegated to agents — a background agent gets a task or returns a report, or several agents work at once — even if the user only says "run the agents", "parallelise the reading", "give the agent a task", "the agent returned a report", "check what the agent brought". NOT for a session where the assistant searches on its own — use organizing-genealogy-research; NOT for recording which agents are still running before the session ends, or checking on them after a break — use research-session-handoff. Also triggers on Russian requests: «запусти агентов», «распараллель чтение», «поставь задачу агенту», «агент вернул отчёт», «проверь, что принёс агент».
---

# Working with several AI agents in a genealogy search

The main principle: **judgement belongs to the coordinator and the human; volume belongs to the agents.** An agent can quickly leaf through hundreds of frames, but it tends to see what it is looking for, and it does not know what has already been found. So the coordinator (you, the main session) prepares the task, checks every find yourself, and records the outcome. The agent reads and reports.

## Roles

| Role | What it does | What it does not do |
|---|---|---|
| **Human** — owner of the research | sets the goal; decides on kinship and on the tree; solves captchas; logs in to accounts; pays; sends letters | does not reread hundreds of pages by hand |
| **Coordinator** — the main session | holds the overall picture and the project files; formulates the question; sets tasks; **checks finds against the scan personally**; records the outcome; reports to the human | does not read whole volumes, but delegates them |
| **Reader agent** — mid-tier model | reads one volume, film or file; keeps a coverage log; sends quotations and crops | draws no conclusions about kinship; does not launch other agents |
| **Mechanic agent** — cheap model | downloads files; builds a volume map; counts pages; searches recognised text | does not read handwriting; does not judge content |
| **Researcher agent** | searches the internet for guides, databases, reference books; compiles a report with links | does not edit project files other than its own report |

## The cycle of one iteration

Do the steps in order. Skipping any step costs more later than the step itself.

1. **Question.** One question, with an answer criterion and a time limit. For example: "find, in the birth register of town N for 1868, the children of father X; the answer is the entry number and a quotation; limit — two passes".
2. **What is already known.** Find everything in the project files by surname, place and given name (`grep` through the findings log, persons file, hypotheses, source register, search log). Without this the agent rediscovers what is already found and wastes hundreds of thousands of tokens.
3. **Source.** Where the answer can be: place → archive or database → volume, film, frames.
4. **Index.** Is there an index or full-text search? Do the cheap check first, continuous reading afterwards.
5. **Task.** From the template in `assets/task-template.md`.
6. **Reading.** The agent reads, updates its log after each batch, and sends finds.
7. **Verification.** The coordinator opens every frame personally (see "Accepting the result").
8. **Recording.** Immediately: findings log, persons file, hypothesis status, a line in the search log.
9. **Decision.** For the human: confirmed, weakened or withdrawn, and what next.

## How to divide the work

- **One agent — one source**: a volume, a film, or a newspaper for one year. Agents cannot cope with broad tasks such as "go through 8 libraries". Give one or two sources and require a log entry after each.
- **One site — one executor at a time.** Sites protect themselves against frequent requests. Three agents on one site will all get a captcha within half an hour, and work stops for everyone.
- **Unprotected sites can be parallelised**: Wikimedia Commons, archive.org, local PDFs. A large volume may be split by frames between 2–3 agents only if the files are already downloaded or the sources are on different sites.
- **Cheap checks first, continuous reading after.** An index or full-text search sometimes answers in a minute a question that reading would spend an hour on.
- **Divide long work into parts of 15–45 minutes.** A short result is easy to verify and continue; "everything overnight" is not.
- **Plan parallelism yourself before launch.** Do not count on the agent asking permission along the way.

## The task for the agent

**Decision first, tasks after.** Begin your answer to the human with one line: what you are launching now, what you are postponing (and why — captcha, login, a human is needed), and what you need from them. If data is missing for a control record or a film number, ask briefly before writing tasks with gaps.

Take the template `assets/task-template.md` and fill in every section. If a section is skipped, the report usually cannot be verified. Mandatory lines:

- **Already known** — verbatim, with archival references, and a list of **ruled-out lookalikes** (namesakes already excluded). Attach the project's namesakes table (`WHO-IS-WHO.md`; in a Russian-language project `КТО-ЕСТЬ-КТО.md`), if there is one. Do not hand over large logs whole — only excerpts relevant to the question.
- **Control record** — a record that certainly exists in this source. The agent finds it first. If it is not found, or read differently, then the reading is broken, not "the person is absent".
- **"Write only what you see"**; for each hit, the frame, entry number, verbatim quotation and crop; mark anything uncertain with "(?)".
- **Coverage log** after each batch: "frame → entries No. …". Without it "not found" means nothing, and interrupted work cannot be continued.
- **Pace** as a number, for example "no more than one frame per 10 seconds, a break every 30 frames". Example figures (October 2026): on FamilySearch a captcha appeared after roughly 45–150 opened frames (most often around 130 in 40 minutes; earlier as time goes on).
- **On a captcha or block — stop, click nothing, report.**
- **First line of the report: `NEW PERSONS: N`**, zero written as a word. What is not asked for does not grow. When search tasks keep returning addresses but no new people, assign a volume to read through ("write out everyone"), not another question.
- **"Do not launch other agents. If the volume is too large, return a plan and stop."** Without this line an agent may launch a dozen helpers on its own and multiply costs.
- **Its own folder and its own browser tab** for each agent.

## A fleet of parallel agents

On days with several background agents at once, the losses are usually not in the search but around it: agents fighting over one rate-limited site, the human told "five agents are working" when two have stopped, crops deleted and downloaded again for a re-check, the same file read three times for three surnames, and no trace of what was already read. Rules:

- **One pass through a source for all targets.** Keep one targets file in the project (`TARGETS.md`): every form of every target surname (from `surname-variants-cyrillic-cursive`), in-law families, key given name + patronymic combinations, places under all their names, false friends to write out. Every reading task attaches it, and the agent writes out hits for all targets, not only for today's question. Re-reading a book for the next surname is the most expensive duplicate. New forms found in a source go into the file (the coordinator adds them).
- **A journal of what was read** (`READ-LOG.md`): one row per source — reference or URL, what exactly (frames, pages, years), **coverage** (continuous / partial / index only), the version of the targets file, date, agent and task file, crops folder, result in one line (hits, or "0 with control: …"). Before any download or delegation the coordinator searches it, and the agent does so as its first step. A source read continuously for the current targets is not read again; one read for an older, shorter list is re-read only for the new targets, from the crops if they exist. Partial coverage is written as partial, and the next agent continues from the frame where the previous one stopped.
- **Resource locks** (`BUSY.md`): one row per shared resource — who holds it, since when, the pace rule. Standing rules at the top (one agent at a time on a site with a daily quota; a pause on 429; each agent its own browser tab). The coordinator updates it before launching and after finishing; an agent that needs a held resource waits or asks — it does not "just try". A 429 or a block during a run is "the instrument did not answer" with code and time, never a zero.
- **Interim report every 30 minutes**, into the report file, not only into the chat: what is covered, hits so far with levels, zeros with controls, what is in progress, blockers with response codes. If the agent stops on a limit, the file holds the work. Long tasks (over 2 hours) stop at a natural boundary and return.
- **Check that agents are alive before saying they run.** "Launched" is not "running": check each task's status and whether its report file has grown within the last ~30 minutes. Report in three groups — running, finished, stopped (with the reason). A stopped agent is relaunched from its file, not from scratch. Never predict the result of an agent that has not reported.
- **Keep the crops of the surname column** (and of the decisive lines: parents, ages, household) in the project, in a folder per reference (`crops/<reference>/`), with a row in the read log. Re-checking an exclusion then takes minutes, not a new download of a large file. Working PDFs stay in a temporary folder.
- **Never exclude a spelling in a task.** List every form and have hits marked ⚪ [variant?]; identity is not decided by spelling. A spelling is ruled out only on other evidence (father, place, age, household) or by a **same-hand comparison** with crops of the disputed word and of controls from the same hand (procedure in `surname-variants-cyrillic-cursive`).
- **"A complete book" ≠ "complete registration".** A signed total certifies the body of a book, not that every event reached the registrar; compare the density of entries with neighbouring years before calling a zero firm.
- **Check the site's terms before any automation** (see "Safety" below).
- **Give the agent a whole volume, not a question**, when search tasks keep returning addresses but no new people: "read the file through and write out everyone". The first line of every report is `NEW PERSONS: N`.

## Choosing the agent and the model

| Task | Who | Model tier |
|---|---|---|
| Download pages, volume map, search of recognised text, check a reference code in an inventory | mechanic | cheap (e.g. Haiku) |
| Read and transcribe one scan or one volume | reader | mid-tier (e.g. Sonnet) |
| Reconcile contradictions, decide on identity, merge reports, write the summary | coordinator | strong, the model of the main session |

Do not give the mechanic a judgement task, and do not give a strong model a download. A cheap model often gives up at the first error (429, wrong address) and writes "contact the archive" instead of finding a workaround. Spot-check its quick negative result that took few actions.

## Accepting the result

Go through all items before writing "found" or "not found".

1. **Open every find yourself** at the frame indicated and compare the quotation letter by letter. Agents see what they expect. Sometimes the word «…скій мещ.» (…sky meshch., i.e. "…sky townsman") means a townsman of a shtetl, not a surname. Sometimes the wanted surname is "read" inside another word. Sometimes there is a reference to an "already deciphered entry" that does not exist.
2. **Control record**: did the agent find it, and read it correctly.
3. **Coverage**: what was read, what was skipped, where there are duplicate shots and gaps in numbering.
4. **A zero during site refusals is not a zero.** Ask or check the log: were there captchas, 403/429 responses, dropped connections. A mass pass in which all responses were access errors will return "0 finds", and that means nothing.
5. **Do not take footnotes on trust.** If the agent refers to a document, find that document.
6. **Record immediately**: the find (archival reference, address, quotation, confidence, "verified against the scan: yes") in the findings log and persons file; the hypothesis status; a line in the search log, including an empty result with its coverage.
7. **Report to the human briefly**: what was confirmed, what was not, what awaits their decision.

**Mass transcription (hundreds of entries) is accepted on the model of the mandatenamechanges.org project** (19,043 name changes in the "Palestine Gazette", recognised by Gemini; author Philip Trauring, per a write-up [unverified]): recognition → automatic checks (specific to each source and set in advance; for us, for example, the name is in the name dictionary, the age is within plausible limits, the number of entries on a page adds up) → only **entries that passed the checks go into the table, each with a link to the exact scan page**; the rest are handled by hand or marked "unverified". The classification rule (for example, "Hebraised or not") is transparent, written in words, and checked against the earlier result. Into the tree goes only an entry with a link to the frame.

A detailed table of failures and what to do about them is in `references/failures.md`. Read it when an agent is silent, returned a strange zero, got a captcha, or when costs rose unexpectedly.

## What only the human does

Captchas, logging in to accounts and passwords, payment, sending letters and messages, decisions on kinship, and edits to a publicly visible tree. An agent that meets such a step stops and informs the coordinator. The coordinator tells the human exactly what to do and where: which tab, which site. Do not paste passwords, cookies or keys into tasks or files.

## Safety of the human's computer

The agent works on the human's computer. What it may do is determined by its set of tools, not by its intentions. There was a case where an agent without browser tools needed a site behind the human's login, controlled the browser through system scripts, read the clipboard, closed someone else's tab — and wrote in its report that it had bypassed nothing. Therefore in every task:

- **No suitable tools — stop** and write the line "a human decision is needed". Do not look for a workaround.
- **Forbidden:** system scripts for controlling applications (OS-level automation of other apps: tabs, keystrokes, window switching), system screenshots, the clipboard (system clipboard commands), the browser profile, cookies and settings, other people's tabs.
- **Do not suggest that the human weaken the protection** of the browser or system for the agent's sake. The condition for the next step is "which agent with which tools".
- **An agent with a browser** works in its own new tab and closes only that one; a captcha or re-login means stop. It **saves crops to files** in its own folder (a screenshot in the conversation cannot be checked later), and the file name describes what the crop shows.
- **"The site would not open" — check your own address first** (for example ipinfo.io) and record the site's response. Do not explain the refusal by a VPN or a country block at random: there was a case where the human had no VPN and the cause was something else — a page assembled by a script, or a login requirement.
- **A task that breaks a site's terms — stop with a quote.** If the task contradicts the site's terms (no scripts, bots, bulk collection, several accounts), the agent stops and returns a verbatim quote of the terms instead of a result; that refusal counts as a full result. The coordinator does not reword the task to get around it. A technique from any guide (this one included) is checked against the site's own terms, not against the guide.
- **No personal data of the human in network requests** (User-Agent, headers, addresses, request bodies). Write "User-Agent neutral, no personal data", not "descriptive".

Before launch, check that the agent type has the tools for the task. When accepting a report, check "did not bypass" and "did not touch" against the actual calls in the transcript. Report any violation that touches the human's computer, accounts or data to them at once; if a password or code could have been on the clipboard, advise changing it.

## A team of five roles and the round

For a question that needs several sources and independent checking, roles are spread more widely. The **historian-genealogist** — the plan (context, hypotheses, which documents must exist, tasks) and the summary. The **archive researcher** — files and scans. The **open-sources researcher** — databases, indexes, newspapers, reference books. The **fact-checker** — answer criteria before the search and a verdict after. The **supervisor** — gate review before the search and audit after; it does not command, but writes the coordinator a list of actions. The coordinator and the human are as above.

```
00-question (coordinator) → 01-plan (historian) → 00-criteria (fact-checker) → gate review (supervisor)
→ 02-archive ∥ 03-open sources → 04-fact-check → [recheck, no more than one loop] → 05-summary (historian)
→ audit (supervisor) → project files (coordinator)
```

- **Criteria before the search:** document, column, value; what would confirm and what would refute; lookalikes; the mandatory control. Searchers do not read them: tasks say what to look for and where, without the expected answer. The criterion must "fail" on what is already known. Formulate the question neutrally, versions on equal terms.
- **Gate review:** there is one question; "already known" is verbatim; what has been read is not repeated; tasks are feasible and do not overlap; criteria exist; a map of name and place variants exists; **the executor has the tools**. Carry out the gate review's actions marked "now" before the search and tick them off.
- **Do not launch a team** if the answer is 1–3 frames or a book of a dozen pages — open it yourself. Assess the question by value, context, tools and verifiability; if tools or verifiability are low, it is work together with the human, not a round.
- **Limits per agent** (guidelines): historian ≤ 60 calls / 20 min; criteria and gate review ≤ 40 / 10 min; archives ≤ 250 calls, ≤ 300 pages, 60 min; open sources ≤ 150 calls, ≤ 3 sites, 45 min; verdict and audit ≤ 120 / 30 min. An action failed 3 times — stop on that path. **Two technical zeros in a row — stop** and state "what decision is needed from the human". **A recheck does not repeat a technical block**: the same login or captcha will give the same zero.
- The agent **first opens candidates already found**; the continuous "sieve" comes after. The number of calls in the report is counted, not eyeballed. It appends to its own file as it goes and does not overwrite; working files go in a temporary folder; the task lists what has already been downloaded.
- **One run per round folder:** a lock file at start; checked before starting or continuing; removed after the audit.
- **Coverage in the summary is by name** (by frame / by report / not opened), without "all" and "entirely". A 🟢 in the summary is only what is 🟢 with the fact-checker.
- **Processing the summary:** read the summary, fact-check and audit → check key finds yourself against the crop (a reading error passes through all roles) → apply the audit's corrections → record the findings log, hypotheses, persons file, search log and a line in the rounds log (agents, calls, tokens, time, what passed and what was withdrawn, violations) → tell the human about violations → remove the lock → say where else the finds can be checked and propose one next question. Mark what has been corrected in old reports with a link to the correction; do not delete.
- **Search wide** for all roles: across languages, there and back; a source for each epoch of life; record parallel branches, and a "not ours" with its reasoning; surname, all the family's places, patronymic and given name in four layers (two names, Yiddish and Russian, Europeanisation, pronunciation); each find gets "Where else to look". A name variant does not prove identity: a second identifier is needed.
- No role proposes a letter to an archive instead of searching — a rule of the guide (AGENTS.md, item 8).

In detail — the guide, "Process with agents", sections 10–12.

## Costs

- Limit parallelism by sites, not by desire: three agents on three different sources is good, three on one is bad.
- Give mechanics to the cheap model, reading to the mid-tier, keep judgement for yourself.
- Put a time limit on each line of work and a stop condition written in advance.
- If an agent has nevertheless multiplied without asking, do not cut the work off midway: the loss from cutting off is often greater. Record the case, fix the task template, and keep that branch under control.

See also the skills: `organizing-genealogy-research` (course of work when there are no agents), `verifying-genealogy-findings` (when a find is proven), `research-session-handoff` (how to save the agents' state between sessions), `search-logic-navigator` (what to do at a fork).
