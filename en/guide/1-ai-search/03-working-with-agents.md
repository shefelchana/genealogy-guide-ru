# Working with AI agents

What this section covers: how to organize a long genealogical investigation in which not one chat but several AI agents work: who is responsible for what, how to set tasks, how to accept results, how not to run into captchas and not lose what has been done. Based on a real investigation (September–October 2026, Claude Code with access to the project folder and a browser). If you work with a single chat, sections 2, 4 and 5 are enough.

---

## 1. Roles

| Role | Who | What it does | What it does not do |
|---|---|---|---|
| **Human (owner of the research)** | you | sets the goal, makes decisions about kinship and the tree, passes captchas, logs in to accounts, pays, writes letters, decides disputed points | does not reread hundreds of pages alone |
| **Coordinator** | the main AI assistant in your session | holds the overall picture and the project files, formulates questions, sets tasks for agents, **checks every find against the scan itself**, records the outcome, reports to you | does not read whole volumes — delegates |
| **Reader agent** | a background agent (mid-level model) | reads one volume, film or file as tasked, keeps a log, sends finds with quotations and crops | draws no conclusions about kinship; does not launch other agents |
| **Mechanic agent** | a background agent (cheap model) | downloads files, builds a map of a volume, counts pages, searches recognized text | does not read handwriting, does not judge content |
| **Researcher agent** | a background agent | searches the internet (guides, databases, reference works, laws), compiles a report with links | does not edit project files other than its own report |

The rule: **judgement belongs to the coordinator and the human, bulk work to the agents.**

The [agents/](../../agents/archive-mechanic.md) folder holds ready descriptions of two helpers for Claude Code: a mechanic (`archive-mechanic`) and a reader of a single document (`archive-transcriber`).

## 2. The work cycle (one iteration)

```
1. Question     → one, with an answer criterion and a time limit
2. Check        → what is already known? (search your own files)
3. Source       → where can the answer be? (place → archive/database → volume/film)
4. Index        → is there an index? it comes first
5. Task         → to an agent: volume, frames, goal, control record, pace
6. Reading      → the agent reads, keeps a coverage log, sends finds
7. Verification → the coordinator opens every frame itself, checks the quotation
8. Record       → finds log + persons + hypotheses + research log — at once
9. Decision     → the human: confirmed / weakened / withdrawn; what next
```

This is the same [search route](01-search-route.md), laid out by performers.

## 3. How to divide the work

- **One agent — one source** (a volume, a film, a newspaper for a year). A large volume can be split by frames among 2–3 agents, **only if they are on different sites**.
- **One site — one performer at a time.** Three agents on FamilySearch at once — a captcha for all of them within half an hour.
- Sites without protection (Wikimedia Commons, archive.org, local PDFs) — can be run in parallel.
- First **cheap checks** (indexes, full-text search, community surname indexes), then **continuous reading**.
- Broad tasks like "go through eight libraries" are beyond agents. Give 1–2 sources and a log entry after each.

## 4. Task template for an agent

```
Task: [one source] — [what we are looking for] — [why].

Already known (do not rediscover):
- [facts verbatim, with archival references]
Ruled-out doubles (not ours): [list]

Source: [site, collection, film/file, frames X–Y; how the book is organized, if known]
Control record (it definitely exists, find it first): [frame/date/names]
What to look for: [surname in all spellings / column / features]

How to report:
- write only what you see; do not complete what you expect;
- for each hit: frame, record number, verbatim quotation, a crop saved to the folder [folder];
- mark anything uncertain "(?)" and explain what hinders;
- a coverage log "frame → records no. …" after each batch;
- "not found" is a normal result, but with coverage.

Pace and limits:
- no more than 1 frame every 5–10 s; batches of 4; a break every 30 frames;
- on a captcha/block — stop, press nothing, report;
- work only in your own tab/folder;
- do not launch other agents; if the volume is too large — return a plan.
```

A ready template for Claude is in the `orchestrating-genealogy-agents` skill ([../../../skills/](../../../skills/)). The agents and the skills are written in Russian; the template above works in English as is.

## 5. How to accept results

1. **Open every find yourself** at the frame. Agents tend to see what they expect: in one investigation the note "…ский мещ." (meshchanin of the shtetl) was taken for a surname, and an illegible surname was read as the one named in the task.
2. **Check the control record** — whether the agent found it and read it correctly.
3. **Check the coverage**: what was read, what not, where the filming duplicates.
4. **Check that an "empty" result is genuine**: whether there was a captcha, 403/429 errors, drop-outs. "0 finds" when the site was refusing means nothing.
5. **Record at once** and update the status of the hypotheses.
6. **Do not accept footnotes unchecked**: an agent may cite a non-existent "already found record".

**Bulk extraction.** If an agent extracts hundreds of records (for example, a whole shtetl over ten years), accept only what passed automatic checks and has a link to the frame. This is how the open dataset on name changes in the "Palestine Gazette" 1921–1947 (mandatenamechanges.org) is built: the text was recognized by AI, and only records that passed the checks went into the table — about 19 thousand, each with a link to the scan page. The rest goes to manual checking.

More on checking — [Checking results](04-checking-results.md).

## 6. Typical failures and what to do

| Failure | Sign | Solution |
|---|---|---|
| Captcha / anti-bot | "Verify you are human", hCaptcha | the agent stops → the human passes the captcha in its tab → continue from the same frame |
| Block for speed | 403/429, "hangs" in all tabs | a pause of no less than an hour; one performer; lower the pace |
| Block by country | the site does not open or returns a block page; Ukrainian archives, according to 2026 reports, do not work with researchers from Russia and Belarus, and some archives introduced IP-address blocking; Russian government sites do not open from some foreign addresses and VPNs | do not bypass; tell the human — they decide (for example, switch off the VPN) |
| An agent is "silent" for long | no log entry for longer than usual | check whether it is alive; a log after each batch helps to continue |
| Agent connection drops | connection error | launch a **new** agent for the remainder by the log, rather than "waking" the old one |
| An agent itself breeds agents | rising costs | in every task: "do not launch other agents" |
| Rediscovery of what was found | a "new find" is already in the files | before the task — search your own files and paste what is known into the task |
| Browser tabs interfere with each other | screenshots "hang", tabs disappear | each agent has its own tab; check the list of tabs before work |

## 7. Memory and handover between sessions

- Everything goes **into project files**, not into the conversation.
- The "Continue from here" file: the current question, which agents are working and where their logs are, what awaits the human (captchas, decisions), next steps.
- Before the end of a session or the compression of a conversation: "save everything" — the coordinator updates the files and "Continue from here".
- Lessons (what worked, what slowed things) go into a separate methodology file; once a week a short review.
- A register of **partly read files**: a file read for one surname later passes itself off as "viewed" for another. Record which sections were read and for which surname.

Skills: `research-session-handoff`, `organizing-genealogy-research`.

## 8. Costs and pace

- Continuous reading — with a mid-level model; mechanics — with a cheap one; judgement and synthesis — with a strong one.
- Limit parallelism by sites, not by desire: 3 agents on different sources is good, 3 on one is bad.
- Break long tasks up: a result in 15–45 minutes is better than "everything overnight".
- A time limit per line of inquiry and a stopping condition written in advance.

## 9. How to give this guide to an agent

Give your AI agent the link to the guide and say: "Read the agent instructions ([AGENTS.md](../../AGENTS.md)) and [llms.txt](../../llms.txt), then ask me what is known about the family and propose a plan". The agent will take from here the order of work, the rules and the prompt library. For Claude Code — install the skills as a plugin (see [Skills for Claude](06-skills.md)).

---

**See also:** [AI tools](05-ai-tools.md) · [Scenarios: what to do if…](07-scenarios.md) · [Standard of proof](../3-results/02-standard-of-proof.md) · [Access, captchas, pace](../2-reference/19-access-captchas-pace.md)
