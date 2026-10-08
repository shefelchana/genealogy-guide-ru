# Working with AI agents

What this section covers: how to organise a long genealogical research project in which not one chat but several AI agents work: who is responsible for what, how to set tasks, how to accept results, how to avoid running into CAPTCHAs and losing what has been done. It is based on a real project (September–October 2026, Claude Code with access to the project folder and a browser). If you work with a single chat, sections 2, 4 and 5 are enough.

Some of the advice below was sent by a reader of the guide who runs their own research with agents (October 2026, CC BY 4.0). It is marked **[reader's experience]**: the author tested it on their own project, the compiler did not repeat it ([Glossary](../0-start/06-glossary.md)).

---

## 1. Roles

| Role | Who | What it does | What it does not do |
|---|---|---|---|
| **Human (owner of the research)** | you | sets the goal, decides about kinship and the tree, passes CAPTCHAs, logs in to accounts, pays, writes letters, decides disputed points | does not re-read hundreds of pages |
| **Coordinator** | the main AI assistant in your session | holds the overall picture and the project files, formulates questions, sets tasks for agents, **checks every find against the scan itself**, records the outcome, reports to you | does not read whole volumes — delegates |
| **Reader agent** | a background agent (mid-level model) | reads one volume, film or file as tasked, keeps a log, sends finds with quotations and crops | draws no conclusions about kinship; does not launch other agents |
| **Mechanic agent** | a background agent (cheap model) | downloads files, builds a volume map, counts pages, searches recognised text | does not read handwriting, does not judge content |
| **Researcher agent** | a background agent | searches the internet (guides, databases, reference works, laws), assembles a report with links | does not edit project files other than its own report |

The rule: **judgement to the coordinator and the human, volume to the agents.**

The [agents/](../../agents/archive-mechanic.md) folder holds ready-made descriptions of two helpers for Claude Code: the mechanic (`archive-mechanic`) and the single-document reader (`archive-transcriber`).

**Handoff "up to the threshold"** [reader's experience]. The AI brings a task to the step that only a human can take and hands it over in one line:

| AI does | Human does |
|---|---|
| finds the file, the archival reference, the film number, the range of frames | logs in to the account, registers |
| says what to look for in these frames | passes the CAPTCHA |
| at the human's request prepares a draft request | pays, if needed |
| | writes to living people and to institutions |

Keep in the project files a separate list of **"what only a human can do"** and from time to time check whether it contains a move shorter than everything the agents are doing. For the author such a move turned out to be a ZAGS record of two twins born in 1933: it gives the father's patronymic and the mother's maiden name, while the archive fonds where the agents were searching end in 1925, and for weeks the father was sought by indirect signs. This is no reason to replace searching with letters: when and how to write to an archive or ZAGS and who decides — the guide's rule is in [Requests and letters](../2-reference/20-requests-letters.md).

## 2. The work cycle (one iteration)

```
1. Question    → one, with an answer criterion and a time limit
2. Check       → what is already known? (search your own files)
3. Source      → where may the answer be? (place → archive/database → volume/film)
4. Index       → is there an index? it comes first
5. Task        → to the agent: volume, frames, goal, control record, pace
6. Reading     → the agent reads, keeps a coverage log, sends finds
7. Check       → the coordinator opens every frame itself, checks the quotation
8. Record      → finds log + persons + hypotheses + research log — at once
9. Decision    → the human: confirmed / weakened / withdrawn; what next
```

This is the same [search route](01-search-route.md), laid out by performer.

## 3. How to divide the work

- **One agent — one source** (a volume, a film, a newspaper for a year). A large volume can be split by frames between 2–3 agents, **only if they are on different sites**.
- **One site — one performer at a time.** Three agents on FamilySearch at once — a CAPTCHA for all of them within half an hour.
- Sites without protection (Wikimedia Commons, archive.org, local PDFs) — may run in parallel.
- First **cheap checks** (indexes, full-text search, community surname indexes), then **continuous reading**.
- Broad tasks like "go through eight libraries" are beyond agents. Give 1–2 sources and a log entry after each.

### Continuous reading of volumes or checking names: a measurement from one project

A reader compared two ways of working on one project, with the same agents [reader's experience]:
- **continuous reading of volumes** — "read such-and-such file through and write out all the namesakes". The answer is about the volume, not about the family;
- **checking names against productive resources** — you take the whole set of names, dates and places already found, and run each name through the resources that have already yielded results for this line. The list of "where we have already searched" is deliberately ignored.

| | Continuous reading of volumes | Checking names |
|---|---|---|
| Time | three days | one day |
| Cost | ≈ 3.8 million tokens | ≈ 1.4 million tokens |
| Covered | five volumes read through, about 2,500 records | four lines across all resources that had already produced results |
| Into the direct line | 2 people | 6 confirmations and the first photograph of an ancestor |
| False zeros removed | 1 | 6 |
| New sources | 2 | 9 |

⚠️ These are figures from one project and rough: an observation, not an experiment with a control group, and the tasks differed from day to day. But the gap is large.

Why: a negative result has a shelf life. Databases grow, people acquire patronymics and dates. In three days the author accumulated about forty names that had been searched for nowhere, and about two dozen old ones acquired patronymics for the first time — for them re-checking was the first real attempt. A side result: the method also exposes your own mistakes — six false zeros in a day ([The false zero](09-false-zero.md)).

Continuous reading is not abolished: it is needed where a name is already tied to a specific book. But as the main method it lost for the author.

## 4. Task template for an agent

```
Task: [one source] — [what we are looking for] — [why].

Already known (do not rediscover):
- [facts verbatim, with archival references]
Ruled-out doubles (not ours): [list]

Source: [site, collection, film/file, frames X–Y; how the book is organised, if known]
Control record (certainly exists, find it first): [frame/date/names]
What to look for: [surname in all spellings / column / features]

How to report:
- write only what you see; do not finish what you expect;
- for every hit: frame, record number, verbatim quotation, a crop into the folder [folder];
- mark anything uncertain "(?)" and explain what gets in the way;
- a coverage log "frame → records no. …" after each batch;
- "not found" is a normal result, but with coverage.

Pace and limits:
- no more than 1 frame every 5–10 s; batches of 4; a break every 30 frames;
- on a CAPTCHA/block — stop, click nothing, report;
- work only in your own tab/folder;
- do not launch other agents; if the volume is too large, return a plan.
```

A ready template for Claude is in the [`orchestrating-genealogy-agents`](../../../skills/orchestrating-genealogy-agents/SKILL.md) skill.

### A task for checking names: four parts

A reader's form for the "checking names" method (section 3); all four parts are mandatory [reader's experience]:
1. **A worksheet** — the path to the set of names and which of its sections go to this agent.
2. **Productive resources for this line** — with a note of what exactly each has already yielded. The agent must understand why it is going there.
3. **What counts as a find** — a list of fields: occupation, address, spouse, children, patronymic, neighbours in the list. "The person exists" does not count as a find.
4. **What not to do** — which resources are blocked, which need action by a human (login, payment, CAPTCHA), which volumes other agents are reading.

The report begins with the line `NEW PERSONS: N` and contains a table "name × resource × how much was viewed".

### What to add to any task

Lines that saved the reader's work [reader's experience]:
- **"Write into the report as you go, not at the end."** By default an agent accumulates its result and hands it over in one piece — and loses everything if cut off. For the author reports survived a cut-off four times (the battery died, the request limit ran out, the laptop lid closed) because they were written as the work went on.
- **"Stop at about 70% of your context** (the working memory of the conversation): finish writing how far you got and report." That is better than working until cut off.
- **"Do not assemble a single address from your head: take addresses from the pages of the site; if an address was nevertheless assembled by hand, say so in the report."** A model confidently builds plausible addresses: in three weeks the author got an invented path to a DNA-match list, a section of a cemetery catalogue, a record-card address in a name database, all three with a 404 error. It is worse when an invented address does not fail but answers with zero or with the whole database: [The false zero](09-false-zero.md), section 3.
- **"If you find an argument against my premise or against your own find, it matters more than the find."** Without such permission a model builds out the world to fit what it was told. So write your own statements in the task as checkable facts with an address, not as background. The author described an article to an agent, going by its headline, as "an eyewitness's memoirs", and it turned out to be another author's survey from another decade; wrote that Raduraksti works without registration — the agent checked it as its first action and returned the site's own sentence: images only for registered users. Both times the lead was wrong and the agent caught it.

## 5. How to accept the result

1. **Open every find yourself** at the frame. Agents tend to see what is expected: in one project a note "…ский мещ." (meshchanin of a shtetl) was taken for a surname, and an illegible surname was read as the one named in the task.
2. **Check the control record** — did the agent find it and read it correctly.
3. **Check coverage**: what was read, what was not, where there are duplicate shots.
4. **Check that an "empty" result is genuine**: were there CAPTCHAs, 403/429 errors, cut-offs. "0 finds" while the site refuses means nothing.
5. **Record at once** and update the status of hypotheses.
6. **Do not accept footnotes without checking**: an agent may refer to a non-existent "already found record".
7. **Judge by the file, not by the last message** [reader's experience]. Twice for the author an agent's last line looked as if it had broken at the first step, while a finished 148 KB report already lay on disk. A cheerful stream of messages guarantees nothing either. The sign of work is a growing report file.
8. **Read the report, not the agent's raw work log** [reader's experience]: the log is dozens of times larger than the report and will clog the coordinator's conversation memory.
9. **Check the AI's own conclusions for the impossible**, not only the testimony of sources ([Plan, timeline, place guide](../0-start/05-plan-timeline-place.md), section 3). A cheap reader's trick: after every entry into the tree, ask about the new cards how old each parent was at the birth of each child; anything outside 15–50 for a mother and 15–70 for a father goes for review. In the author's register a "great-great-grandmother" of a person born in 1905 appeared, herself born in 1894; an agent caught it [reader's experience].
10. **Value an agent that refutes its own find** [reader's experience]. In one day the reader's agents themselves withdrew their hypothesis "Solomon = Shmerko", took back the mark "the file contains the village needed" after reading the list through, and struck "not digitised" from a report after finding a mistake in their own query. Ask for exactly this in the task (section 4).

**Mass extraction.** If an agent extracts hundreds of records (for example, a whole shtetl over ten years), accept only what has passed automatic checks and carries a link to the frame. This is how the open dataset of name changes in the *Palestine Gazette* 1921–1947 (mandatenamechanges.org) is built: the text was recognised by AI, and only records that passed the checks went into the table — about 19,000, each with a link to a scan page. The rest went for manual checking.

More on checking — [Checking results](04-checking-results.md).

## 6. Typical failures and what to do

| Failure | Sign | Solution |
|---|---|---|
| CAPTCHA / anti-bot | "Verify you are human", hCaptcha | the agent stops → the human passes the CAPTCHA in its tab → continue from the same frame |
| Block for speed | 403/429, "hangs" in all tabs | a pause of at least an hour; one performer; lower pace |
| Block by country | the site does not open or shows a block page; Ukrainian archives, by 2026 reports, do not work with researchers from Russia and Belarus, and some archives have introduced IP blocking; Russian state sites do not open from some foreign addresses and VPNs | do not circumvent; tell the human — they decide (for example, switch off the VPN) |
| An agent "is silent" for long | no log entry for longer than usual | check whether it is alive by whether the report file is growing, not by the last message; a log after each batch helps to continue |
| An agent's connection breaks | connection error | launch a **new** agent for the remainder using the log, rather than "waking" the old one |
| An agent spawns agents itself | rising costs | in every task: "do not launch other agents" |
| Rediscovery of what was found | a "new find" is already in the files | before the task — search your own files and paste the known into the task |
| Browser tabs interfere with each other | screenshots "hang", tabs disappear | each agent has its own tab; check the list of tabs before work |
| An agent entered the browser where the coordinator works [reader's experience] | login to a site broken; only the owner can restore it | in every task: "do not touch this browser, do not enter site [N] — the coordinator runs it"; a browser logged in to accounts is run by one performer |
| An agent edits a shared file [reader's experience] | a section appended straight into the shared register under someone else's number; for the reader this twice surfaced much later | shared files (register, dossier, set of names, tree) are edited only by the coordinator; agents write into their own reports |
| Two agents write one temporary file [reader's experience] | an agent read another's script or another's extract | name temporary files after the agent |
| A false zero | "0 finds", while the source is alive | check the instrument: [The false zero](09-false-zero.md) |

## 7. Memory and handoff between sessions

- Everything — **in the project files**, not in the conversation.
- The "Continue from here" file: the current question, which agents are working and where their logs are, what awaits the human (CAPTCHAs, decisions), next steps.
- Before the end of a session or compaction of the conversation: "save everything" — the coordinator updates the files and "Continue from here".
- Lessons (what worked, what slowed things down) — in a separate methodology file; once a week, a short review.
- A register of **partly read files**: a file read for one surname later passes itself off as "viewed" for another. Record which sections were read and for which surname.

Skills: [`research-session-handoff`](../../../skills/research-session-handoff/SKILL.md), [`organizing-genealogy-research`](../../../skills/organizing-genealogy-research/SKILL.md).

## 8. Costs and pace

- Continuous reading — with a mid-level model; the mechanic — with a cheap one; judgement and synthesis — with a strong one.
- Limit parallelism by sites, not by desire: 3 agents on different sources is good, 3 on one is bad.
- Break long tasks up: a result in 15–45 minutes is better than "everything overnight".
- A time limit per direction and a stopping condition written down in advance.
- **The real price** [reader's experience]: one task for one agent on one line, with reading of scans and catalogues, costs 265 to 430 thousand tokens and takes 20 minutes to an hour and a half; four lines at once — about 1.4 million tokens in a day; continuous reading of five volumes — 3.8 million in three days (comparison in section 3).

## 9. How to give an agent this guide

Give your AI agent the link to the guide and say: "Read the instructions for the agent ([AGENTS.md](../../AGENTS.md)) and [llms.txt](../../llms.txt), then ask me what is known about the family and propose a plan." The direct links that almost any assistant opens, and the ready message in full, are in the [Quick start](../0-start/01-quick-start.md). If the assistant has no access to your folder, you keep the records yourself from its "Write into files" block (AGENTS.md, section 3a). The agent will take from here the order of work, the rules and the prompt library. For Claude Code — install the skills as a plugin (see [Skills for Claude](06-skills.md)).

---

**See also:** [AI tools](05-ai-tools.md) · [The false zero](09-false-zero.md) · [Scenarios: what to do if…](07-scenarios.md) · [Standard of proof](../3-results/01-standard-of-proof.md) · [Access, CAPTCHAs, pace](../2-reference/19-access-captchas-pace.md)
