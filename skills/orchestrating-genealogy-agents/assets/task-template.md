# Task template for an agent

Copy it, fill in all the fields in square brackets, delete what is not needed. If a field cannot be filled (for example, there is no control record), say so explicitly in the task and allow for it when accepting the result.

```
Task: [one source] — [what we are looking for] — [why it is needed].

Already known (do not rediscover):
- [fact verbatim, with archival reference: archive, fond-inventory-file, folio/frame]
- [fact …]
Ruled-out lookalikes (not ours, do not report as a find): [name, year, place — why ruled out]

Source: [site, collection, film/file, frames X–Y]
How the book is arranged: [if known — sections, where the male/female entries are, whether there are duplicate shots]
Control record (certainly exists, find it first): [frame/entry number/date/names]

What to look for: [surname in all spellings, including distortions and without the first letter; given names; in which column]
What is NOT needed: [for example, conclusions about kinship, search in other sources]

How to report:
- write only what you see; do not complete what you expect;
- for each hit: frame, entry number, verbatim quotation in the original's spelling, crop saved to [agent's folder];
- mark anything uncertain with "(?)" and say what prevents reading it;
- a coverage log "frame → entries No. …" to the file [path] after each batch;
- note technical failures: captcha, error codes 403/429, dropped connections, skipped frames;
- "not found" is a normal result, but with coverage.

Pace and restrictions:
- no more than [1 frame / 1 request] per [N] seconds; batches of [4]; a break every [30] frames;
- on a captcha or block — stop, click nothing, report which frame to continue from;
- work only in your own tab and your own folder;
- do not enter passwords, send no letters, pay for nothing;
- no suitable tools — stop and write "a human decision is needed"; do not touch system scripts (OS-level automation of other apps), screenshots, the clipboard, browser settings or other people's tabs;
- in network requests — a neutral User-Agent, no personal data;
- append to your own file as you go and do not overwrite; working files go in a temporary folder; already downloaded: [paths];
- two technical zeros in a row (captcha, login, block) — stop and report;
- do not launch other agents; if the volume is too large, return a plan and stop.

Final report: finds (in the form above) → control record (found? how read?) → coverage → failures → what remains unread.
```

---

## Short variants

**Mechanic (downloading, volume map):**
```
Download [file/frames X–Y] from [address] to [folder]. Pace — [N] s between requests.
Check each file: size not zero, opens, resolution [≥ …].
Build a volume map: page number → section heading/year/type of entries.
Do not interpret the content, do not read handwriting. On an access error — retry once after a minute, then stop and report the error code.
Do not launch other agents.
```

**Researcher (internet search):**
```
Find [what] for [place/topic, years]. Check no more than [2–3] sources, with an entry in [report file] after each.
For every statement — the page address and a verbatim quotation; mark whether you opened the page or only saw the search results.
Do not edit project files other than your own report. Do not pass captchas. Do not launch other agents.
```

---

## Example of filling in (generalised)

```
Task: birth register of the Jewish community of town N for 1869 — find the children of Chaim and Rivka [surname] — test hypothesis H-07 that Mordko, born 1869, is their son.

Already known (do not rediscover):
- Mordko Chaimovich [surname], 27 years old, in the family list of 1896 (archive A, fond 1-2-345, fol. 12, family No. 84).
Ruled-out lookalikes: Mordko Chaimovich, born 1867, from shtetl M (different mother, see H-05).

Source: FamilySearch, film DGS 00XXXXXXX, frames 210–290 (book of 1869).
How the book is arranged: male entries on the left half of the spread; spreads were shot twice in a row.
Control record: No. 41 male, frame 224 (per the JewishGen index — son of Moshko and Ita).

What to look for: surname [variant 1, variant 2, without the first letter]; the "father and mother" column.
…
Pace: no more than one frame per 10 s; a break every 30 frames.
```
