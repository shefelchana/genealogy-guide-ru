---
name: writing-family-history
description: >-
  Turns verified genealogical findings into readable prose for relatives — a family history, a chapter about one ancestor, a family book or a short story for a reunion — without inventing facts. Uses a two-layer record (cited fact plus a paragraph for family), adds historical context kept apart from claims about the family, marks hypotheses and legends in words, handles contradictions, footnotes, captions, living people and sensitive topics, and ends with a source table, open questions and a preservation plan. Use whenever the user asks for a family history, a text for relatives, a chapter about an ancestor, a family book or chronicle, or hands over notes for relatives to read. Not for an interactive page of the research (use building-research-showcase). Also triggers on Russian requests: «напиши историю семьи», «сделай текст для родственников», «оформи главу про прадеда», «семейная книга», «перепиши досье понятным языком».
---

# How to write a family history from verified findings

## The main rule

Write **only from the facts in the user's findings log**. An AI easily fills gaps with plausible invention — a wife's name, a profession, "a warm evening in the shtetl". In a family history such invention is worse than a blank: in twenty years it will be retold as fact. If there is no information, the text says "unknown" or "no document yet".

So first ask for the material: the findings log, records of conversations, scans with archival references. If the user asks to "write the family history" from scratch, with no materials, do not compose it; suggest starting from what they know, and ask where the documents are.

## Step 1. The two-layer record

Write up each find twice (template — `assets/two-layer-entry.md`):

1. **A fact for the findings log and the tree** — short: the source with its archival reference, a verbatim quotation, whether it was checked against the scan.
2. **A paragraph for the relatives** — connected: who, where, when, what it means, what was going on around.

Why two layers: relatives read the paragraph and skip the reference code; the next researcher finds the reference code and checks the paragraph. This corresponds to the fifth element of the GPS standard (the written conclusion) and the NGS advice to separate fact from presentation.

Example (invented, reference code a placeholder):

> **Fact:** [Archive], fond N, inventory N, file N, fol. 12 verso, marriages 1895, No. 31 (checked against the scan): «Лейба Мордковъ Гольдманъ, мѣщанинъ м. N, 24 лѣтъ» [Leiba Mordkov Goldman, townsman (*meshchanin*) of shtetl N, 24 years old].
>
> **Paragraph:** In the spring of 1895 the twenty-four-year-old Leiba, son of Mordko Goldman, married in the shtetl of N. In the record he is called a *meshchanin* (townsman) — the way the empire registered townspeople without merchant capital. What he worked at, the document does not say.

Note that the last sentence of the paragraph names the gap outright.

## Step 2. The language of confidence

For each statement choose one rung and hold to it in the text:

| What there is | How to write |
|---|---|
| a document checked against the scan | assertively, a footnote to the source |
| several agreeing pieces of indirect evidence | "most likely", "in all probability", explaining why |
| a single hint (an index, someone else's tree, naming after a deceased grandfather) | "possibly", "there are grounds to suppose", "no document yet" |
| family memory | "according to family legend", "Grandmother told that…" — and who told it |
| nothing | "unknown" |

- **Do not hide contradictions.** If two documents give a different age or name, write about it: relatives find it interesting, the researcher needs it.
- Do not throw away a legend refuted by a document — tell both the legend and what the document showed.

## Step 3. Historical context — separate from the family

A document answers "who and when", context answers "why": why the family moved, why a person disappeared from the lists, why there is no metrical record. Add the events of the era (pogroms, wars, evacuation, changes of borders), the life of the place (trades, fairs, synagogues), daily life and customs, the meaning of professions and estates.

**The boundary:** context describes the era and place, not the actions of ancestors. Not allowed: "in 1905 the family lived through a pogrom" — if there is no document. Allowed: "in October 1905 there was a pogrom in the town; what the family lived through in those days is unknown". Each fact of context also gets a reference.

Where to get context — `references/context-sources.md`.

## Step 4. Structure

Choose with the user one of the working schemes:
1. **By places** — a chapter on each town or shtetl where the family lived, with a map and the history of the place.
2. **By people** — an essay on each key person: what is known, from where, what is unknown.
3. **Chronologically** — from the earliest document to family memory.

Begin with the ancestors about whom there is **the most material** (advice of Lisa Alzo): it is easier to find the tone, and the text gets a foothold.

For a large family book follow the 10 steps (Maegan Kasteler, FamilySearch blog, after Penelope Stratton's RootsTech 2019 talk): remember that it is **a story, not a report** → the reader and the period → format → scope, plan, table of contents → rules of layout → write → narrative and illustrations → reread and correct → name index → publish. The skeleton of a chapter — `assets/chapter-template.md`.

**Mandatory appendices:**
- a table of sources (archival reference, what is in the document, where the scan is);
- **open questions** — what has not been found and where it might be, so that someone else can continue the history;
- a name index (for a book);
- a kinship diagram for the chapter or the whole book.
- for a book with several places — **a geographical and historical appendix**: one nine-point scheme per place: 1) where it is now; 2) whose rule by years (guberniya, uezd, oblast); 3) population in figures (for a shtetl the Jewish community, for a village households and estate); 4) what the place lived through; 5) our family here, with levels of evidence; 6) where the documents are and whether they are online; 7) sources of the note; 8) community or parish and church; 9) way of life and occupations. Keep Step 3's boundary: a fact about the place is not a fact about the family. Take figures from the page image, not from OCR, and mark unchecked ones "[check]".

## Step 5. Footnotes and illustrations

- The source goes in a footnote or at the end of the paragraph. A full reference: the archive or publisher, title, archival reference, folio or frame, and for online copies the address and the date accessed; a brief note on reliability if there is doubt (a calculated date, an index only).
- **Illustrations:** a cutting from a document with a caption and archival reference ("birth record, [archive, reference], fol. 5") convinces better than a retelling. A photo — with a caption: who, when, by what signs it is dated, who holds the original (see the skill `dating-old-photos`). A map of the place.
- The right to a photograph belongs to the photographer, not to the owner of the print. For other people's pictures (for example, gravestones on Find a Grave) permission is needed from whoever took them. For publication in a book for sale — check the law of your country.

## Step 6. Living people and heavy topics

- About **living** people — only with their consent. In a text for a wide circle replace the names of the living with "cousin N.". Before publication show the text to the people it is about.
- **Delicate** matters — DNA surprises, adoption, children born out of wedlock, criminal records, repressions, denunciations, illnesses — write only after discussing with the user who the text is for and who may be hurt. Do not reveal unexpected paternity without consent.
- Write about the dead and about heavy finds calmly, without melodrama and without invented details of the death. Judge ancestors in the context of their era.

## Step 7. Cross-check before handing over the text

Go through the text sentence by sentence: find **every name, date, place and family tie** in the findings log. Give the user, together with the text, a short cross-check sheet:
- what is taken from which document;
- where the wording is a hypothesis or a legend;
- what you added as context, and from where.

A sentence not in the findings log should be deleted or turned into "unknown".

## Step 8. Preservation

The finished text is part of the family archive. Advise (in detail — `references/preservation.md`):
- **three copies, two types of media, one outside the home**; check once a year, move to a new medium about every 5 years;
- keep the text **in several formats** (.docx, .pdf, .txt), scans — a master copy in TIFF and a working one in JPEG;
- beside it, a note "how the archive is arranged"; the relatives should know where it lies and who will continue.

## Format of the reply

1. A short plan (scheme, chapters) — agree it if the text is large.
2. The text of the chapter or history with marks of confidence and footnotes.
3. Appendices: sources, open questions.
4. The cross-check sheet.

## Related skills

`verifying-genealogy-findings` — if there is doubt whether a fact holds; `dating-old-photos` — captions for pictures; `organizing-genealogy-research` — where the materials lie and how to keep the files.
