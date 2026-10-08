# Three levels: from a single check in a browser to a project with agents

What this section covers: how to start with AI if you have never done it, and how to grow into a large project if you want to. Pick your level — the rest of the guide can be read later.

---

This guide grew out of work in **Claude Code**: AI agents, a project folder, log files, instructions for the agent (AGENTS.md), skills. But you don't have to start there.

If big, monotonous work puts you off, or if it is hard or unclear where to begin — **make one check on one relative right in your browser**. No programs to install, no files, and no need to read the whole guide.

## Level 1. Just try it: one check in a browser

**What you need:** the Google Chrome browser and an AI plugin for it — for example, **Claude in Chrome** (it needs a paid Claude plan). The plugin sees the open page, types the query into the search form by itself, opens the cards and scrolls through the results. If you have no plugin, an ordinary chat will do: copy into it what you find on the site yourself.

**Time:** 15–30 minutes.

**How:**
1. Pick one person about whom you know the name, an approximate birth year and the place.
2. Open a suitable site:
   - served in the war, was killed, went missing, was decorated — ["Pamyat naroda" (People's Memory, in Russian)](https://pamyat-naroda.ru/), [OBD "Memorial" (in Russian)](https://obd-memorial.ru/);
   - was repressed — ["Otkrytyi spisok" (Open List, in Russian)](https://ru.openlist.wiki/), the "Victims of political terror" databases (see [War, repression, the siege](../2-reference/12-war-repression-siege.md));
   - was killed in the Holocaust or was evacuated — [the Yad Vashem names database](https://collections.yadvashem.org/ru/names) (English interface available).
3. Ask the plugin to search and bring it together:

> "Find on this site everything about the person: [surname, given name, patronymic], born about [year], [place]. Go through the spelling variants: the surname with е/а/и, with one and two letters, without the first letter; the given name in full and in its everyday form; the patronymic in old and new spelling. Search in Cyrillic as well as in transliteration. Open every suitable card. Make a table: record — what it says word for word — link. Then say which records most likely concern the same person, where the surname, given name, date and place differ, which version is more likely and why. Don't make anything up; if you are not sure, say so."

*Don't read Russian? See [For English speakers](08-for-english-speakers.md).*

**Why this works.** On one site there are often many scattered records about one person: a casualty report, an award sheet, a hospital list, a card index, a repeat entry by another clerk. They contain mistakes — in the surname, in the patronymic, in the birth year by a year or two, in the name of the village. Going through all the variants, opening every card and putting them together into one picture by hand is long and dull. **Agents are very good at exactly this**: they sort through a lot of scattered material and show what matches and what does not.

**What to do with the result:**
- save the table and the links — even in a notes app;
- open at least one record yourself and compare it with the scan of the document;
- pass captchas yourself, and don't give the plugin your password.

A hit is already a result. No hit is also a result: write down where you searched and under which spellings.

What this looks like from start to finish — [A worked example for beginners](../../examples/worked-example-for-beginners.md).

## Level 2. A chat and a few files: one branch over a few weeks

**What you need:** an ordinary AI chat (Claude, ChatGPT, Gemini) and three files — a finds log, hypotheses, a research log. Word or Notes will do.

**How:** give the assistant the instructions in [AGENTS.md](../../AGENTS.md) — how to do that is in the [Quick start](01-quick-start.md). You keep the records: copy the "Write to files" block from the answers, and at the start of a new conversation paste the "Continue from here" file ([template](../../templates/continue-from-here.md)).

**It suits** the case when you want to follow one branch: from a great-grandfather to the metrical record of his birth, from an emigrant to his shtetl.

## Level 3. A project with agents

**What you need:** Claude Code or the Claude app with access to a folder on your computer; the skills from this guide ([how to install](../1-ai-search/06-skills.md)); a project folder.

**How:** the AI keeps the project files itself, launches background helpers, reads archive files a hundred pages at a time, brings dozens of namesakes together into one tree, and fills in profiles on sites with your permission. You pose the questions, pass the captchas and decide what counts as proven. Details — [Working with agents](../1-ai-search/03-working-with-agents.md) and [Routine work for agents](../1-ai-search/08-routine-for-agents.md).

**It suits** large work: several lines, continuous reading of volumes, hundreds of documents. You don't need to know programming. But it helps to understand what files and folders are, and not to be afraid of text files in Markdown format.

## Comparison

| | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| What you need | Chrome + an AI plugin, or a chat | a chat + 3 files | Claude Code or the Claude app with a folder, skills |
| Time to start | 15 minutes | an evening | a few evenings |
| Who keeps the records | you, if you want | you | the AI; you check |
| Suits | a first check of one person | one branch | the whole research |
| Where to start | this section, steps 1–3 | [Quick start](01-quick-start.md) | [Skills](../1-ai-search/06-skills.md), [AGENTS.md](../../AGENTS.md) |

You can move between levels in either direction. Many people begin with a single check in a browser and, when it draws them in, set up files.

The rules are the same at all levels: **an index or a card is a hint — check it against the scan; "found" means at least two features match; write down empty results too.**

---

**See also:** [Quick start](01-quick-start.md) · [What to read for beginners](../../reading/what-to-read.md) · [AI tools](../1-ai-search/05-ai-tools.md) · [Access, captchas, pace](../2-reference/19-access-captchas-pace.md) · [What this guide does not cover](07-not-covered.md)
