# Briefs for the showcase agents

Fill in the paths. Each brief is self-contained: the agent has not seen the conversation. Put the common header at the top of every brief.

## Common header

> You are collecting data for a family research showcase. Read `showcase/brief.md` (audience, language, lines with `id`) and the schema `references/data-schema.md` of the skill `building-research-showcase`. Your only data source is the excerpt `showcase/excerpts/<yours>.md` and the files it points to. Do not search for new documents, do not open websites, do not write to the project files. Invent nothing: no data — no field. Take each level from the project files and do not raise it. Output: one file `showcase/parts/<name>.json` (valid JSON, no comments) and a 5–10 line report: what you took, what you left out and why, which contradictions you noticed (including levels in the project that look too high). If the audience is public — only anonymised names from the excerpt, references marked [invented] / [усл.], no indirect identifiers (addresses, studios, parishes, exact dates).

## 1. Catalogues → `parts/catalogs.json`

> Skill `building-research-catalogs`. Collect `sources` (every source in the excerpt, including zeros with coverage — `"level": "zero"`), `people` (up to 30, each with the level of the key link), `profile` (the person named in the brief; timeline — only rows with a source), `library` (the project's folder scheme as it is, the file-naming rule, a card for one document).

## 2. Tree and places → `parts/tree.json`

> Skill `rendering-family-tree`. Collect `pedigree` (4 generations from the researcher in Ahnentafel order, unknowns as `null`), `ladder` (the deepest proven line), `places` (coordinates from a reference, the place name of that year), `routes` (one route per line, by years), `offmap` (places beyond the edge). After building, check whether an arc passes through someone else's point and fix `bend`.

## 3. Evidence → `parts/evidence.json`

> Skill `building-evidence-matrix`. Find 2–4 places in the excerpt where documents disagree (name, date, patronymic, place). For each — a matrix and a verdict with a level. Plus `cycle`: one real pass "question → … → record" from the project, and `methods`: 2–6 methods used in the project, each with an example.

## 4. DNA → `parts/dna.json`

> Skill `checking-dna-against-tree`. Take the composition from the excerpt (who tested, company, date). Compute the expectation from the tree (`scripts/expected_share.py`), compare, check the family origin legend if there is one (`alt`). Verdict with a level and caveats.

## 5. Stories and surname → `parts/story.json`

> Skill `writing-family-history`. One story of the person named in the brief: 4–7 chapters, each with a date and how it is known (🟢 / 💭). A family saying goes into `quote` with a plan to check it. Photos — captions only (who, when, who identified). `surnames`: 1–2 surnames following the "Surname" section of `building-research-showcase`.

## 6. Fact-check (after the `--check-only` build)

> Fact-checker role, skill `verifying-genealogy-findings`. Files: `showcase/parts/*.json` and the project files. Check every 🟢 row in `profile` and `comparisons`, and a random 20 % of `sources` and `people`. For each: the right reference and year, is it in the project files, is the level not higher than there. For a public version — no real names and no indirect identifiers from the substitution map. Report: a table "field — what the showcase says — what the project says — verdict". Do not fix anything yourself.
