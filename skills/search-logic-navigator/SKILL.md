---
name: search-logic-navigator
description: "Guides a genealogy search through its decision points — the route question → place → source → index → scan → verification → record — and says what to do next: a possible match, nothing found, too many namesakes, an illegible document, an index that contradicts the scan, sources seemingly exhausted, a site that blocks access. Diagnoses the stuck step first and logs empty results with their coverage. Use when the user is stuck or unsure of the next move, e.g. \"I'm stuck\", \"I can't find anything\", \"what next?\", \"the index says one thing, the record another\", \"I think I found him\". Not for project routine — question queue, recording finds, closing a branch (use organizing-genealogy-research) — or for running agents (use orchestrating-genealogy-agents). Also triggers on Russian requests: «я застрял», «ничего не нахожу», «что дальше», «много однофамильцев», «в индексе одно, в документе другое», «сайт не пускает», «кажется, нашла»."
---

# Search Logic Navigator (decision points of a genealogy search)

Most dead ends are not a lack of documents but a skipped step of the route: searching for a surname without a place, trusting an index without the scan, reading the wrong volume. So first work out **which step** the search is stuck at, and only then give advice.

## The route

```
question → place → source → index → scan → verification → record
```

| Step | What you should have at the end | Why the step cannot be skipped |
|---|---|---|
| **Question** | one question with an answer criterion and a stopping condition | without a narrow question you cannot tell whether the answer has been found |
| **Place** | a settlement with its district (*uezd*) and province (*guberniya*) *for the year in question*; not a second place with the same name | the place determines the archive and the set of documents; the surname does not |
| **Source** | which type of document could have recorded the event, whether it survived for those years, and where it is held | "not found" in a volume that did not survive is not a search result |
| **Index** | whether there is an index or full-text search; a result with a record number and an image/frame | an index quickly tells you where to look, but it is not proof in itself |
| **Scan** | the frame, the record number, a word-for-word quotation in the original spelling | indexes make mistakes in surnames, mix up fields, and take a place name for a surname |
| **Verification** | a second independent identifier; contradictions worked through | one matching surname is not yet kinship |
| **Record** | findings log, persons file, hypothesis, search log — including an empty result with its coverage | otherwise the same search will be repeated a month later |

## How to use it

1. **Ask, or find in the project files, what has already been done**: the question, the place, where it was searched, which spellings, index or scan. If this is not in the search log, first reconstruct it and write it down. Without it the advice goes in circles.
2. **Identify the decision point** from the table below.
3. **Open the matching section** of `references/scenarios.md` and go through the steps in order. Do not jump to "write to the archive" or "take a DNA test" until the cheap steps have been done.
4. **Finish with a record**: what was done, the coverage, the result, the next step.
5. **Keep the answer short**: a one-sentence diagnosis of the decision point, then 3–5 steps for today. If the user's account does not make clear which step of the route they are stuck at, ask rather than infer. Point to a section for long reference material instead of pasting it into the answer. Answer in the user's language.

## Decision points

| Situation | First thing to do | Section in `references/scenarios.md` |
|---|---|---|
| "I think I found him" | the scan and a word-for-word quotation; then a second independent identifier | "Found it" |
| "I can't find anything" / the person has vanished | check the "place" and "source" steps; then spellings, given name, estate and registration, borders | "Not found" |
| Many namesakes | a table of candidates and a timeline for each, elimination by incompatibility | "Many candidates" |
| The document is illegible | the original scan instead of a preview, the table header, the clerk's handwriting in neighbouring entries | "Document is illegible" |
| The index says one thing, the scan another | trust the scan, record the discrepancy | "Index versus document" |
| Everything online has been checked | check whether it really has: side lines, associates, other types of source | "Everything online has been checked" |
| The site won't let me in | stop; a human solves the CAPTCHA; slow down; look for a copy of the material elsewhere | "Site blocks access" |
| I know only names / only a surname and a region / I start from emigrants | starting scenarios | "Starting points" |
| An agent or an AI brought a finding | open the frame yourself, check the quotation letter by letter | "Found it" |

If you do not know where to look for a particular question (a doctor, killed at the front, evacuation, a gravestone, emigration), open `references/question-to-source.md`.

## Rules common to all decision points

- **Every finding comes with an address and a word-for-word quotation**: archive, fond-inventory-file-folio (*fond–opis–delo–list*) or site–film–frame, record number. Check the key part against an enlarged crop of the scan.
- **Do not fill in the blanks.** If a letter cannot be seen, write "(?)". If only the given name matched, it is a candidate, not an ancestor.
- **"Not found" counts** only if these are stated: the source and its limits, the list of spellings, the method (index, full text, page by page; exact or phonetic), whether the index or the document itself was searched. Plus a control record found by the same method. And one more question: was the person actually obliged to appear in this source?
- **A zero during site errors is not a zero.** If there was a CAPTCHA, a 403/429 error or dropped connections, the result is invalid.
- **CAPTCHAs, account logins, payments and letters are done by a human.** On protected sites keep a slow pace: one request every few seconds, one worker per site.
- **A letter to an archive** comes only after the online routes have been exhausted and logged; it is targeted, with the exact archival reference; the decision and the sending are the human's. Help draft the text if the person asks, but do not suggest a letter in place of searching.
- **Online trees are only for confirmed facts.** Hypotheses live in the hypotheses file.

See also these skills: `verifying-genealogy-findings` (conditions for "proven" and for a negative conclusion, trying spellings), `reading-archive-scans` (an unreadable scan), `tracing-revision-records` (going deeper through the revision lists), `tracing-emigrants-to-origin` (the emigrant branch), `orchestrating-genealogy-agents` (handing reading to agents).
