# Skills for Claude: what exists and how to install

What this section covers: which ready-made skills are in this guide, when each one triggers, and how to install them in Claude Code or in the Claude app.

> **The skills are written in Russian.** You do not need to translate them or read Russian. Claude reads the skills regardless of your language and answers in the language you write in (English, for example). The installation instructions below are the same for everyone. The skill names and the links in the tables are the same as in the Russian guide; the descriptions in the tables are translated for you.

A **skill** is a folder with an instruction file `SKILL.md` (and sometimes reference files, templates, scripts). Claude loads a skill by itself when a task fits its description: you write "read this scan of a metrical book", and the scan-reading skill is brought in, with all its techniques and traps. The skills repeat the method of this guide in a form convenient for AI.

---

## 1. Which skills exist — by route step

**Starting and organising the work**

| Skill | When it triggers |
|---|---|
| [`genealogy-intake`](../../../skills/genealogy-intake/SKILL.md) | the first conversation, no project files yet: "I want to find my ancestors", what is known, the goal, files, the first question and a plan |
| [`organizing-genealogy-research`](../../../skills/organizing-genealogy-research/SKILL.md) | the course of work in a project where files already exist: one question, a search of your own files, recording finds, "proved?", closing a direction |
| [`search-logic-navigator`](../../../skills/search-logic-navigator/SKILL.md) | forks in the search: "not found", many namesakes, the index disagrees with the scan, a dead end |
| [`orchestrating-genealogy-agents`](../../../skills/orchestrating-genealogy-agents/SKILL.md) | the work is handed to agents: a task from the template, pace and CAPTCHAs, accepting and checking reports |
| [`research-session-handoff`](../../../skills/research-session-handoff/SKILL.md) | end of a session, context compaction, resuming after a break: "save everything", "continue from where we stopped", the "Continue from here" file |

**Place and source**

| Skill | When it triggers |
|---|---|
| [`identifying-places`](../../../skills/identifying-places/SKILL.md) | find a shtetl or village, its uezd and guberniya for the year needed, changes of borders and names |
| [`ukrainian-archives-on-commons`](../../../skills/ukrainian-archives-on-commons/SKILL.md) | files of Ukrainian archives on Wikimedia Commons and inventories on Wikisource (Вікіджерела) |
| [`soviet-era-records`](../../../skills/soviet-era-records/SKILL.md) | war, evacuation, the siege, repression, Soviet ZAGS |
| [`tracing-emigrants-to-origin`](../../../skills/tracing-emigrants-to-origin/SKILL.md) | from US and European documents to the shtetl |
| [`searching-pogrom-records`](../../../skills/searching-pogrom-records/SKILL.md) | pogroms of 1918–1922 (from the end of 1917): victim databases, aid recipients, orphans, refugees |
| [`researching-jewish-cemeteries`](../../../skills/researching-jewish-cemeteries/SKILL.md) | where someone is buried, burial databases, reading a gravestone, converting a Jewish date |

**Index and database search**

| Skill | When it triggers |
|---|---|
| [`using-community-surname-indexes`](../../../skills/using-community-surname-indexes/SKILL.md) | a surname index first (the Jewish Roots forum, JewishGen, JGFF), then page-turning; a register of unread sections |
| [`searching-jewishgen`](../../../skills/searching-jewishgen/SKILL.md) | JewishGen databases: search, row limit, reading fields, going to the scan |
| [`searching-familysearch-films`](../../../skills/searching-familysearch-films/SKILL.md) | FamilySearch films: catalogue → film → frame, boundaries of books, pace and CAPTCHAs |
| [`searching-yandex-archives`](../../../skills/searching-yandex-archives/SKILL.md) | Yandex "Archive Search" (Поиск по архивам): operators, spellings, how to read a result |
| [`searching-nli-jewish-press`](../../../skills/searching-nli-jewish-press/SKILL.md) | Jewish newspapers in the National Library of Israel |

**Scan and reading**

| Skill | When it triggers |
|---|---|
| [`reading-archive-scans`](../../../skills/reading-archive-scans/SKILL.md) | read digitised files, assess scan quality, enhance faded ink, map a volume |
| [`tracing-revision-records`](../../../skills/tracing-revision-records/SKILL.md) | go back in time through the revision lists of 1795–1858 |
| [`reading-hebrew-yiddish-sources`](../../../skills/reading-hebrew-yiddish-sources/SKILL.md) | gravestones, the Hebrew part of metrical records, signatures, Yiddish newspapers |
| [`dating-old-photos`](../../../skills/dating-old-photos/SKILL.md) | date an old photograph by its mount, clothing, studio |
| [`interpreting-jewish-family-photos`](../../../skills/interpreting-jewish-family-photos/SKILL.md) | what a Jewish family photograph says about the way of life and the occasion |

**Checking and result**

| Skill | When it triggers |
|---|---|
| [`verifying-genealogy-findings`](../../../skills/verifying-genealogy-findings/SKILL.md) | check a find, understand whether "not found" means anything, try spellings, full-text search |
| [`reconstructing-family-clusters`](../../../skills/reconstructing-family-clusters/SKILL.md) | you found a father and children — assemble a package of documents on the family and sort out namesakes |
| [`dna-matches-endogamy`](../../../skills/dna-matches-endogamy/SKILL.md) | analysing DNA matches under endogamy |
| [`citizenship-by-descent-dossier`](../../../skills/citizenship-by-descent-dossier/SKILL.md) | assemble a chain of documents for citizenship by descent |
| [`writing-family-history`](../../../skills/writing-family-history/SKILL.md) | turn finds into a readable text for relatives |

The full list with descriptions is in [skills/README.md](../../../skills/README.md) (in Russian).

Besides skills, the [agents/](../../agents/archive-mechanic.md) folder holds two helper agents for Claude Code: `archive-mechanic` (mass mechanical work with scans) and `archive-transcriber` (careful reading of one document).

## 2. How to install

**Claude Code — as a plugin (skills and agents at once).** In Claude Code type:
```
/plugin marketplace add shefelchana/genealogy-guide-ru
/plugin install genealogy-guide-ru@genealogy-guide-ru
```

The second command opens the plugin's card in the `/plugin` menu, where you confirm the installation. Plugin updates do not arrive by themselves: turn on auto-update in `/plugin` → Marketplaces or update with the command `/plugin marketplace update genealogy-guide-ru` (code.claude.com/docs, "Host and maintain a marketplace").

**Claude Code — manually.** Copy the folders from `skills/` into `~/.claude/skills/`, and the files from `agents/` into `~/.claude/agents/`.

**Claude.ai and the Claude app.** On paid plans (Pro, Max, Team, Enterprise) the plugin can be added there too: the menu Customize → Plugins → Add → Add marketplace, then the repository address `shefelchana/genealogy-guide-ru`. A single skill can also be uploaded without the plugin: zip the whole skill folder (a ZIP with a folder containing `SKILL.md` inside) and add it in Customize → Skills; skills need code execution to be enabled (support.claude.com, the articles "Use plugins in Claude" and "Use skills in Claude"). Scripts from the `scripts/` folders may not run in the web version (for example, without network access) [unverified].

**Other assistants (Gemini, ChatGPT and others).** Skills are ordinary text files. You can attach the `SKILL.md` of the skill you need to the conversation, or give a link to it, and ask the assistant to work by that instruction.

## 3. Limitations

- Skills do not pass CAPTCHAs and do not log in to accounts — a human does that.
- Skills do not suggest a letter to an archive instead of searching: online routes first. A letter is addressed to a specific archive and quotes the exact archival reference; the decision and the sending are the human's; AI will help to compose the text if you ask ([Requests and letters](../2-reference/20-requests-letters.md)).
- Sites change: the techniques were checked in September–October 2026.

---

**See also:** [AI tools](05-ai-tools.md) · [Working with agents](03-working-with-agents.md) · [Instructions for an AI agent](../../AGENTS.md)
