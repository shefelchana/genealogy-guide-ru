---
name: building-research-catalogs
description: Builds the structured catalogues of a family research project from its working files — a source catalogue (reference, year, record type, who, what it gave, level of evidence, including "zero with coverage" rows), a people catalogue where the level is given to the key kinship link rather than to the person, a MyHeritage-style person profile with a sourced timeline, family, sources and open questions, and a document-library card (folder scheme, file-naming rule, metadata). Output is either tables for the project files or JSON parts for building-research-showcase. Use when the user asks to list, tabulate or index what has been found, to "make cards" for ancestors, to see everything known about one person, or to tidy up the sources register, even if they do not say "catalogue". Also triggers on Russian requests: «каталог источников», «реестр источников», «список всех находок таблицей», «карточки персон», «карточка как в MyHeritage», «всё, что известно о прадеде, на одной странице», «как хранить сканы и называть файлы». Not for searching new records and not for deciding disputed kinship (use building-evidence-matrix / verifying-genealogy-findings).
---

# Research catalogues: sources, people, profile, library

Catalogues prove nothing by themselves — they **show** what has already been found and how solid it is. So the main rule: take data only from the project files (findings log, persons, hypotheses, source register) and never raise a level.

## 1. Source catalogue

One row — one document or one honest zero.

| Field | How to fill it |
|---|---|
| reference | archive, fond-opis-file (sheet / frame) or website and collection. An index entry and the scan of the same record are **one** row: an index is not a second source |
| year | year of the document, not of the event |
| type | one short word from a fixed set: vital records, revisions, censuses, civil registry, war, evacuation, directories, court and registers, newspapers, cemeteries, DNA — the filter uses it (in Russian projects: метрики, ревизии, переписи, ЗАГС, военные, эвакуация, справочники, суд и учёт, газеты, кладбища, ДНК) |
| who | names as written in the document, plus our identification |
| what it gave | one phrase: what follows from this document |
| level | 🟢 🟡 ⚪ 💭 🔴 — as in the project files; for a negative result — "zero with coverage" |

A **zero with coverage** is a row too: "volume 1 read in full — no Mordko", "all 1891 births of the parish read — the couple is not there". A zero without coverage ("searched, didn't find") does not go into the catalogue: it is not a result but a line of the search log. Details: the guide's "False zero" section.

For the showcase — the `sources` array (schema: `building-research-showcase/references/data-schema.md`). For the project — a table in the source register with extra fields "where the scan is", "where the conclusion is (§)", "date checked".

## 2. People catalogue

One card — one person: name (as in documents), years, role in one line ("Berdychiv → Moscow · great-grandfather"), line, **level of the key link**. The level belongs to the link "son of / wife of", not to the person: a name can be 🟢 from a birth record while the link to our family is 💭. This shows who rests on family memory alone.

Namesakes: if the project has two people with one name, the card carries a distinguishing feature (year, place, patronymic). The "who is who" table is in `organizing-genealogy-research`.

## 3. Profile of one person (as on tree sites)

- **Facts** on the left: names and their variants, birth, death, estate / registration, line. Each with a level.
- **Timeline**: year — event — source — level. A row without a source is not added; if an event is known only from a story, the source is "family memory" and the level 💭.
- **Family**: parents, spouse(s), children, with disputed points marked.
- **Sources**: a short list of references.
- **Open questions**: disputed and unknown points go here, not hidden inside the timeline. This is what makes the card better than a usual tree-site profile.

Pick the person with the richest timeline for the profile: it shows the format best.

## 4. Document library

- **Folder scheme** of the project as it is now (logs, persons, hypotheses, archive by line, photos "originals / working", DNA, backup).
- **File-naming rule**: `Archive_fond-opis-file_year_who_what.ext` — the reference first is easy to search, the year next shows the era.
- **Document card**: reference, year, type, who, where and when found, whether there is a scan, status (found in an index → scan downloaded → read → checked against the frame → recorded → level set), where the conclusion is.
- The 3-2-1 rule for copies.

## Anonymised version

For a public example replace names, places and references entirely (not one letter) and mark references [invented] / [усл.]. Structure and record types stay real — that is the point of the example. Indirect identifiers (addresses, studios, parishes) — see step 1a of `building-research-showcase`.

## Check before handing over

- Every 🟢 row has a reference.
- No two rows for one record (index + scan).
- Types in the catalogue come from one set of words (otherwise the filter falls apart).
- No real names in a public version (build with `--forbid`).
