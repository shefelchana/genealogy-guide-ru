---
name: checking-dna-against-tree
description: "Checks an autosomal ethnicity estimate against what the documented tree predicts: computes the expected share of each component from the ancestors' documented origins with the usual spread (grandparent ≈ 25 % ± 3–4), tests an origin legend with a second \"if the legend is true\" expectation, and writes a cautious verdict with a level of evidence (panels overlap, shares under 2–5 % are noise, components are panels, not peoples). A bundled script does the arithmetic. Use when the user shares ethnicity percentages and asks whether they fit the family, wants to test \"great-grandmother was Polish / German / Jewish\". Not for matches, cM or endogamy (use dna-matches-endogamy, dna-matches-across-platforms). Also triggers on Russian requests: «сходится ли этнический состав с деревом», «проверь легенду по ДНК», «откуда у меня 5 % финнов», «сколько должно быть еврейского, если дед еврей», «раздел ДНК для витрины»."
---

# Ethnicity estimate against the tree

Test percentages are a company's model, not a measurement. They are useful only next to an **expectation** worked out from documents. Without it, "26 % Ashkenazi" says nothing; with "25 % ± 3, because one grandfather was Jewish by his birth record" it confirms the tree.

## 1. What you need

- Who took the test (the researcher, a mother, an uncle), the company and the date of the model (companies recalculate).
- The whole composition, every line with its percentage.
- The ancestors of one generation (usually the tester's grandparents), each with an origin **by documents**: birth record, estate, place. If an origin is known only from a story, that is the legend — check it separately.

## 2. Compute the expectation

```bash
python3 scripts/expected_share.py tree.json --test test.json
```

File formats are at the top of the script. Arithmetic: a parent gives exactly 50 %, a grandparent ≈ 25 % ± 3–4, a great-grandparent ≈ 12.5 % ± 3, a 2× great-grandparent ≈ 6 % ± 2; the spreads of independent ancestors add as squares (two grandparents ≈ 50 % ± 4.7). Use the same component names as the company.

## 3. Test the legend

State the legend as a different origin of one ancestor ("Anna Mikhailovna was Polish"). With the `legend` key the script gives a second expectation (`alt`). Compare the observed value with both:
- observed near the main expectation and far from `alt` (more than 2–3 spreads) → the legend **taken literally** is probably not confirmed, 🟡;
- near `alt` → the legend is compatible, 🟡 (not 🟢: DNA does not name a person);
- in between, or the difference smaller than the spread → DNA does not decide, ⚪.

An ethnicity estimate almost never gives 🟢 or 🔴 on its own. A document decides: birthplace, religion in the birth record, estate.

## 4. Caveats that always go into the verdict

- Neighbouring peoples (Poles, Ukrainians, Belarusians, Russians) overlap a lot in company panels; a "Polish" ancestor may show up as "Eastern European" or even "Russian".
- Shares under 2–5 % are at the noise level: a direction, not a conclusion.
- A component's name is a reference panel, not the ancestor's people: "Estonian" or "Finnish" in Russians from the North is common.
- A legend often means something else: "Polish" — from Poland, Catholic, from the western provinces; "German" — foreigners in general.
- Component dating (23andMe Ancestry Timeline) is a rough hint of the generation, ± one generation.

More: the "Tracing Your Ancestors" guide, section "DNA", 6a.

## 5. Output

For the showcase — the `dna` key (schema: `building-research-showcase/references/data-schema.md`): `caption` (who tested, company, date), `bars` with `value`, `expected`, `sd`, `alt`, and a `verdict`: question → expectation → observation → conclusion with a level → caveat → which document would decide.

For the project — a line in the legends register: legend, how it was checked, result, new status. Do not delete a legend; change its status with a note.
