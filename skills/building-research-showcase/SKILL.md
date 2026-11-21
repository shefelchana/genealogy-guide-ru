---
name: building-research-showcase
description: "Turns a family research project (findings log, persons, hypotheses, DNA results, family stories) into one interactive HTML \"showcase\" page — source catalogue with filters, person cards and a MyHeritage-style profile, pedigree chart and line ladder, migration map, DNA-against-the-tree check, evidence matrices, chapters of a life, surname certificate, document library — by running several agents in a fixed order, each producing one JSON part, then validating and assembling them with a bundled script (including a check that no real names are left in a public version). Use when the user wants to show, present, visualise or \"make a page / dashboard / overview / card index\" of their research, prepare something for relatives, turn a dossier into something readable, or make an anonymised teaching example, even if they never say \"showcase\". Also triggers on Russian requests: «сделай витрину», «покажи исследование наглядно», «собери страницу для родных», «карточки как в MyHeritage», «нарисуй дерево и карту по нашим данным», «оформи результаты», «обезличенный пример для методички». Not for writing a narrative text (use writing-family-history) and not for searching for new documents."
---

# Research showcase: one page from the project's data

The result is **one HTML file** that opens in a browser without internet (fonts aside): source catalogue, people, profile, tree, map, DNA, comparisons, stories, surname, library. A finished example is `examples/витрина-форматов-шапиро.html` in the "Tracing Your Ancestors" guide (English: `en/examples/formats-showcase-shapiro.html`).

Do not write the page by hand. Agents collect **data** following the schema (`references/data-schema.md`), and `scripts/build_showcase.py` checks it and injects it into `assets/showcase-template.html`. That way every family's page is built the same way, and mistakes (a link to a line that does not exist, a place without coordinates, percentages over 100) are caught by the script, not by the reader. The page interface can be Russian or English (`"lang": "ru" | "en"`); the data can be in any language.

## Step 0. Agree with the researcher (before any agent starts)

Ask, or decide from context:
1. **Audience.** Only for the researcher / for relatives / public (a guide, social media). A public version needs **anonymisation**: other names, places and references marked [invented] / [усл.], plus a list of forbidden strings for the check (step 1a, step 3).
2. **Language** of the interface: `ru` or `en`.
3. **Lines**: at most five (colours are fixed and checked for colour-blind readers). Fold the rest into "other lines".
4. **Sections**: which data exists. No DNA test — no DNA section; no photos — chapters without photos. An empty section is not drawn.
5. **Whose profile** goes into the card (one person with the richest timeline) and **whose story** goes into the chapters.

Write this to `showcase/brief.md` in the project folder: audience, language, lines with `id`, list of sections, paths to source files.

## Step 1. Excerpts for the agents

Do not give an agent the whole findings log of thousands of lines. The coordinator prepares **excerpts** in `showcase/excerpts/`: by people, by sources, by disputed points, by DNA — only what that agent needs. The project rule on excerpts is in `orchestrating-genealogy-agents`.

**Small project** (project files together under ~300 lines): no excerpts needed; the parts can be done in one pass without subagents. The data schema and the script check stay — that is where the skill's value is.

## Step 1a. Public version: substitution map and indirect identifiers

Real surnames are only the start. A family is also given away by **indirect identifiers** that let anyone find it in five minutes:
- addresses (a street and house from a directory, where the real surname can be read by the address);
- photo studio names and stamps, church and parish names, neighbouring villages, school or unit numbers;
- exact day-level dates, village coordinates, a rare combination "occupation + town + year";
- archival references and record numbers, names of witnesses and godparents; a patronymic that makes a directory entry searchable;
- living people: names, years, towns — in a public version only as a role ("the researcher", "mother").

Make a **substitution map** `showcase/excerpts/00-anon-map.md` (real → invented, one replacement for every occurrence, including old spelling with "ъ" and Latin transliteration) and mark it "do not publish". Put into `forbid.txt` not only the surnames but every indirect identifier from the map: address, studio, parish, neighbouring village. First names of the deceased that a lesson depends on (Стефан / Степан, Сура / Сарра) may stay.

## Step 2. Five agents in parallel

Each agent gets `brief.md`, its excerpt, its skill and a path for the result. It writes **only its own file** `showcase/parts/<name>.json` and a short report: what it took, what it left out and why. Ready-made briefs are in `references/agent-briefs.md`.

| Agent | Skill | Keys in its JSON |
|---|---|---|
| catalogues | `building-research-catalogs` | `sources`, `people`, `profile`, `library` |
| tree and places | `rendering-family-tree` | `pedigree`, `ladder`, `places`, `routes`, `offmap` |
| evidence | `building-evidence-matrix` | `comparisons`, `cycle`, `methods` |
| DNA | `checking-dna-against-tree` | `dna` (only if test results exist) |
| stories and surname | `writing-family-history` + "Surname" below | `story`, `surnames` |

The shared keys (`lang`, `title`, `kicker`, `lead`, `banner`, `footer`, `lines`, `sections`) are written by the coordinator to `showcase/parts/00-meta.json`.

Agents do not start other agents, do not search for new documents and do not write to the project files (findings log, persons, hypotheses): the showcase **shows** what is already established. If an agent notices a contradiction or a gap, it puts it in its report, and the coordinator decides what to do.

Without subagents (a plain chat) — the same five steps one after another, each into its own file.

## Step 3. Build with checks

```bash
python3 scripts/build_showcase.py showcase/check.html showcase/parts/*.json --check-only
```

The script merges the parts (lists are concatenated, objects merged, two different values for one field are an error) and checks: lines exist, levels are from the scale 🟢 🟡 ⚪ 💭 🔴 or `zero`, places have coordinates, routes go through existing places, DNA percentages do not exceed 100, timeline rows have a source, comparisons have a verdict. The agent who owns the file fixes the errors.

For a public version add `--forbid showcase/forbid.txt`: one line per real name, surname, village, reference, address. The build fails if anything from the list is left in the data.

## Step 4. Fact-check

A separate agent (fact-checker role, skill `verifying-genealogy-findings`) takes a **sample**: every 🟢 line in the profile and in the comparisons, and a random 20 % of the catalogue, and checks them against the project files: the right reference, the right year, the level not raised. A level in the showcase may not be higher than in the project's findings log or hypotheses. Fix differences in the part and rebuild.

**Weak spots in the project itself.** Building a showcase is a good moment to see where the research is weak: a hypothesis is 🟢 while the log gives the same link 🟡; a person is 🟢 with no document named; a year of death comes from nowhere; an identity rests only on name and year. The showcase **does not change** such levels (it shows them as in the project, with the doubt under "Open questions"), but the coordinator lists them for the researcher as "what to check in the project". This is often the most useful part of the report.

For a public version the fact-checker also goes through the substitution map once more: are any indirect identifiers from step 1a left in the page (search the finished HTML, case-insensitive, with "ъ" and Latin).

## Step 5. Final build and visual check

```bash
python3 scripts/build_showcase.py showcase/showcase.html showcase/parts/*.json
```

Open the page and look: do labels on the map overlap (fix with `label: "l"` and `dy` on the place, `bend` on the route), does an arc pass through someone else's point, are the tree labels readable. The "Theme" button switches dark mode.

Report to the researcher: path to the file, which sections exist, which do not and why, what the fact-check found, the "what to check in the project" list (step 4), what is worth looking at by eye. For a public version — remind that the substitution map and `forbid.txt` must never be published.

## Section "Surname"

An honest version of a "surname certificate": the dictionary meaning (Beider for Jewish surnames; Unbegaun, Nikonov, Fedosyuk for Russian ones), **what does not follow from the meaning** (kinship with famous namesakes, a great-grandfather's trade), spellings to search, the earliest record in the family with its level. Do not use "meaning of your surname" generator sites. Coats of arms belonged to noble families; a "family coat of arms" for townspeople and peasants is invented — offer a family emblem built from what is proven instead.

## What not to do

- Do not invent missing data to make a section "look complete". An empty field is better than an invented one.
- Do not raise a level for appearance: 💭 stays 💭.
- Do not put living people with birth dates into a public version without consent.
- Do not write the page by hand instead of using the template: the check is lost.
