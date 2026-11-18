# Files of a new project

Create the listed files in the project folder, each with its own template. The names can be changed, but keep them the same throughout the project: they are what you search before every new search. Subfolders: `scans/` (original frames), `crops/` (cut-outs of the needed lines), `branches/` (when there are several lines of enquiry).

---

## FINDINGS-LOG.md

```
# Findings log
One entry, one find. Record at once, at the moment of the find.

## YYYY-MM-DD — [briefly: who, what]
**Question:** …
**Source:** archive · fond-inventory-file · folio · record no.
**Where the scan is:** site · film/file · frame · link
**Crop:** crops/year_archive-code_frame_who-what.png
**Verbatim:** "…"
**Explanation / translation:** …
**Confidence of reading:** confident / unsure (what gets in the way)
**What it changes:** …
**Checked against the scan:** yes / no (index only)
```

## PERSONS.md — reference on people

```
# Persons

## [Surname Given-name Patronymic] (years of life, as known now)
- Variants of name and surname in documents: …
- Born: date, place — source
- Marriage: … — source
- Died: … — source
- Occupations, addresses: … — source
- Parents / spouse / children: …
- Associates (witnesses, business partners, neighbours, fellow travellers): …
- According to relatives (not verified): "…" — who, when
- Open questions: …
```

## HYPOTHESES.md

```
# Hypotheses
Status: ⚪ not verified / 🟡 open, strong version / 🟢 confirmed (date, by what: document + a second marker) / 🔴 withdrawn (date, why)

## H-01. [Short statement]
**Status:** ⚪
**Grounds:** (each match on its own line)
**Weak points:** …
**How to check:** (which document will settle it, where it may be)
**Into the tree:** into a public one only 🟢; into a private one 🟡 with the note "version".
```

## SEARCH-LOG.md

```
# Search log
| Date | Where (site/archive, collection) | What was searched (all spellings; name; place; years) | How (index / page by page / full text; exact / phonetic) | Coverage | Result |
|---|---|---|---|---|---|
```
An empty result is recorded too, with its coverage and an explanation of what the zero means: the surname is not there at all, the needed given name is not there, or there is no person of the needed age.

## SOURCES.md — source registry

```
# Source registry
| Code | Archive and reference code | What it is (type, years, place) | Where the scan is / how to obtain it | Reading status | What was found |
|---|---|---|---|---|---|
| S-001 | home archive | birth certificate, 1938 | scans/1938_birth-cert_name.jpg | read | … |
```

## TIMELINE-[surname or family].md

```
# Timeline: [who]
**The question it was drawn up for:** …
| Date (as in the document) | Calculated year | Event | Who (age per document) | Place (name at the time, uezd, guberniya) | Source | Reliability (scan / index / account) |
|---|---|---|---|---|---|---|

Check for the impossible: mother's age; gaps between children; a child after the father's death; two places at once; discrepancies in age.
```

## PLACE-[name].md — guide to the place (created once the place is known)

```
# Place: [name now; names in documents]
Years needed: …   Updated: YYYY-MM-DD
1. Where it is and what it was called
2. Jurisdiction by year (state, guberniya, uezd, volost)
3. Maps (each with a link to its source)
4. Brief history, destruction of documents
5. Which documents exist (type, years, where held, online?, index?)
6. Archives and reference codes
7. What has already been looked through (link to the search log)
```

## FAMILY-HISTORY.md — text for relatives

A continuous text based only on verified facts. Created empty and added to as questions are closed.

## CONTINUE-FROM-HERE.md

The template is in the `research-session-handoff` skill. If it is not available, the minimum is this:
```
# Continue from here (updated YYYY-MM-DD)
Current question: …
What was done in the last session: …
Waiting for the person: (find documents, interview relatives, log in to an account, a decision)
Next step: …
```
