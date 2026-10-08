# Skills for Claude: what exists and how to install

What this section covers: which ready-made skills are in this guide, when each one triggers, and how to install them in Claude Code or in the Claude app. (The skills themselves are written in Russian; they work with an English-language conversation, and the AI will translate what it reads.)

**A skill** is a folder with an instruction `SKILL.md` (and sometimes reference works, templates, scripts). Claude loads a skill itself when the task fits its description: you write "read this scan of a metrical book" — and the scan-reading skill is connected, with all its techniques and traps. The skills repeat the method of this guide in a form convenient for AI.

---

## 1. Which skills exist — by route step

**Start and organization of work**

| Skill | When it triggers |
|---|---|
| `genealogy-intake` | the first conversation: "I want to find my ancestors", what is known, the goal, project files, the first question and plan |
| `organizing-genealogy-research` | start of a session, tasks for agents, accepting reports, "save everything" |
| `research-session-handoff` | "save everything", "continue from where we left off": the "Continue from here" file |
| `orchestrating-genealogy-agents` | how to split a search into tasks for agents, the task template, pace, accepting reports |
| `search-logic-navigator` | forks in a search: "not found", many namesakes, the index disagrees with the scan, a dead end |

**Place and source**

| Skill | When it triggers |
|---|---|
| `identifying-places` | find a shtetl or village, the uezd and guberniya for the right year, changes of borders and names |
| `ukrainian-archives-on-commons` | files of Ukrainian archives on Wikimedia Commons and inventories on Wikisource (Vikidzherela) |
| `soviet-era-records` | war, evacuation, the siege, repression, Soviet ZAGS |
| `tracing-emigrants-to-origin` | from documents of the USA and Europe to the shtetl |
| `searching-pogrom-records` | pogroms 1917–1922: victim databases, aid recipients, orphans, refugees |
| `researching-jewish-cemeteries` | where someone is buried, burial databases, reading a gravestone, converting a Jewish date |

**Index and database search**

| Skill | When it triggers |
|---|---|
| `using-community-surname-indexes` | the surname index first (the "Jewish Roots" forum, JewishGen, JGFF), then page-turning; a register of unread sections |
| `searching-jewishgen` | JewishGen databases: search, the row limit, reading fields, moving to the scan |
| `searching-familysearch-films` | FamilySearch films: catalogue → film → frame, boundaries of books, pace and captchas |
| `searching-yandex-archives` | Yandex "Archive Search": operators, spellings, how to read a result |
| `searching-nli-jewish-press` | Jewish newspapers in the National Library of Israel |

**Scan and reading**

| Skill | When it triggers |
|---|---|
| `reading-archive-scans` | read digitised files, assess scan quality, enhance faded ink, map a volume |
| `tracing-revision-records` | go deeper through the revision lists of 1795–1858 |
| `reading-hebrew-yiddish-sources` | gravestones, the Hebrew part of metrical books, signatures, Yiddish newspapers |
| `dating-old-photos` | date an old photograph by the mount, clothing, studio |
| `interpreting-jewish-family-photos` | what a Jewish family photograph says about way of life and occasion |

**Verification and result**

| Skill | When it triggers |
|---|---|
| `verifying-genealogy-findings` | verify a find, understand whether "not found" means anything, going through spellings, full-text search |
| `reconstructing-family-clusters` | you found a father and children — assemble a document package for the family and sort out namesakes |
| `dna-matches-endogamy` | analysis of DNA matches under endogamy |
| `citizenship-by-descent-dossier` | assemble a chain of documents for citizenship by descent |
| `writing-family-history` | turn finds into a readable text for relatives |

The full list with descriptions — [skills/README.md](../../../skills/README.md).

Besides the skills, the [agents/](../../agents/archive-mechanic.md) folder holds two helper agents for Claude Code: `archive-mechanic` (bulk mechanical work with scans) and `archive-transcriber` (careful reading of a single document).

## 2. How to install

**Claude Code — as a plugin (skills and agents at once).** In Claude Code type:
```
/plugin marketplace add shefelchana/genealogy-guide-ru
/plugin install genealogy-guide-ru@genealogy-guide-ru
```

The second command opens the plugin's card in the `/plugin` menu, where you confirm the installation. While the repository is private, the commands will work only for those who have access to it (Claude Code clones the repository through git with GitHub credentials already saved). Plugin updates do not arrive by themselves: turn on auto-update in `/plugin` → Marketplaces or update with the command `/plugin marketplace update genealogy-guide-ru` (code.claude.com/docs, "Host and maintain a marketplace").

**Claude Code — manually.** Copy the folders from `skills/` into `~/.claude/skills/`, and the files from `agents/` into `~/.claude/agents/`.

**Claude.ai and the Claude app.** On paid plans (Pro, Max, Team, Enterprise) the plugin can be added there too: Customize → Plugins → Add → Add marketplace, then the repository address (for a private repository you need access to it through GitHub). A single skill can also be uploaded without the plugin: zip the whole skill folder (a ZIP containing a folder with `SKILL.md`) and add it under Customize → Skills; skills require code execution to be enabled (support.claude.com, the articles "Use plugins in Claude" and "Use skills in Claude"). Scripts from the `scripts/` folders may not run in the web version (for example, without network access) [unverified].

**Other assistants (Gemini, ChatGPT and others).** Skills are ordinary text files. You can attach the `SKILL.md` of the skill you need to the conversation, or give a link to it, and ask the assistant to work by this instruction.

## 3. Limitations

- Skills do not pass captchas and do not log in to accounts — the human does that.
- Skills do not suggest writing to archives as a step of the search: online routes first. The decision about a letter is the human's ([Requests and letters](../2-reference/20-requests-letters.md)).
- Sites change: the techniques were checked in September–October 2026.

---

**See also:** [AI tools](05-ai-tools.md) · [Working with agents](03-working-with-agents.md) · [Instructions for the AI agent](../../AGENTS.md)
