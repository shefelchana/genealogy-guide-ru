# Checking results: what to do with an AI answer

What this section covers: how to check a find brought by an AI assistant or agent before you write it into your files, and above all into a tree. A short working order; the theory of proof is in Part 3, [Standard of proof](../3-results/01-standard-of-proof.md).

The main rule, repeated by everyone who works with AI in genealogy (including participants of the IAJGS AI Virtual Summit, 2026): **an AI answer is a hypothesis, not a source**; it must be checked, checked and checked again.

> **Where AI really goes wrong** [reader's experience]. It is rarely caught on an invented ancestor's name — the scan is there for that. It is caught on an **invented address** (a link, a query parameter, a section of a site), on **retelling a source it did not open**, and on **a zero that it brought as a result**. All three are cured by one thing: every statement must have an address, every zero must have a number of what was viewed and a way of checking. More — [The false zero](09-false-zero.md).

---

## 1. An answer without an address is not a find

Every find must have an **address** (archive, fond-inventory-file-folio, or site, collection, film, frame, record number) and a **verbatim quotation** in the spelling of the original. If they are missing, ask for them. If the AI cannot give them, it is not a find but a retelling.

An example from a Jewish genealogy group (2026): a person asked a chatbot about an ancestor, it answered that "a burial is recorded", and the person came to the group for confirmation. There was no record that could be cited.

## 2. The order of checking

1. **Open the frame named yourself.** Not from a retelling — the scan itself.
2. **Check the quotation letter for letter**, enlarging the fragment. Especially names, dates, ages, numbers: this is where AI errs most often. On manuscripts, models read the printed form well and handwritten names and places worse.
3. **Check the fields.** Are the groom's father and the bride's father mixed up, a note of estate and a surname, the age "by the last revision" and the current one.
4. **Check the control record**: if you gave a record that certainly exists, did the AI find it and read it correctly.
5. **Look for a second independent feature**: patronymic, age, place, names of relatives, occupation. The index and the scan of the same record are one piece of evidence.
6. **Record at once** — in the finds log, marked "checked against the scan" and dated.

## 2a. Is this the right document, and has all of it been read

Before reading a file through, and all the more before writing "no record" on its basis, make sure that the file under the catalogue card really is this file and that you know how many folios it has. The points below were sent by a reader of the guide (October 2026, CC BY 4.0) [reader's experience]. Related material — in [False zero](09-false-zero.md), section 12 ("a file's title is a statement, not a fact"), and in the [`reading-archive-scans`](../../../skills/reading-archive-scans/SKILL.md) skill (read the cover before starting work).

1. **The cover and the certification sheet first.** The first and the last frames are read first, always. They are what certifies which file this is — not the number on the website, not the title on the card, and not a field "this image belongs to file N" in the site's response: that field says which card the image is attached to, not what was photographed. For the author, under the card "book of surname changes, 1922–1928, 333 folios" lay the scan of the neighbouring file: on the cover a stamp with another file number, in the certification note (*zaveritelnaya nadpis*) 325 folios, the same number of images for both files (652), and the first images identical byte for byte. Such a file is in fact not digitised; its status is "blocked", not "no record". Had an agent read those folios silently, the log would have gained negative evidence for a whole window of years, built on someone else's book. The case is rare: the author checked the whole fond of 1,015 files, found four suspicious pairs (neighbouring numbers, the same number of images, different folio counts), and the scan matched only in this one. That is exactly why nobody looks for it on purpose.
2. **There may be two certification notes.** One file carried notes from 2002 ("200 + 1 folio, lettered folio 40a") and from 2020 ("203 folios, lettered 40a, 186a, 198a"). The file was re-described. Take the later note, and record the discrepancy: the make-up of the file changed.
3. **The number of people — from the cover, not from the folios.** The cover named civil records No. 1–88 for one year and No. 1–104 for another: 192 records on 203 folios, because second copies are bound in with some of the records. A denominator by folios would have been wrong.
4. **The denominator — from the full list of files, not a filtered one.** A pattern for image names "three digits and maybe a letter" did not catch the file `40a.jpg`, and the lettered folio dropped out of the count. And in the run `185 → 186a → 187` folio 186 was missing altogether. The headings of the neighbouring folios (185 — "record No. 91" (запис № 91), 186a — "extract No. 82" (випис № 82), 187 — "record No. 93") show that 186a is not it: folio 186 exists and is not digitised. Check a gap in the numbering by the headings of the neighbouring folios, not by arithmetic, and write honestly: "202 of 203 folios read". How to record missing folios — [Standard of proof](../3-results/01-standard-of-proof.md), section 7, "Gaps in the sources themselves".
5. **The size field on the card is not the size.** The "number of files" field on the cards of one fond differed from reality in both directions: 208 against 456 images, 2,090 against 2,059. The author recounted all 1,015 files: 508,279 images, while the field added up to 377,458, a quarter less; 78 files without images, not 13 as the field implied; and five files showed zero in the field but had 3,295 images. A zero in a service field is checked against the images themselves — just like a zero in search results. Nor can you judge from this field how long reading will take. And a spot check of the field checks the sample, not the field: having first checked only the zero fields, the author corrected "13" to "8" — and was wrong again.

## 3. How to read with AI so that there are fewer errors

- **Two passes.** In the first, give the document type, year and place but **not the expected names**: AI tends to see what it is looking for. In the second — comparison with your hypotheses.
- **High resolution and a fragment.** Luis Kessler (2024) got nothing usable at low resolution; a fragment at high resolution plus context (who, to whom, when) helped. The father's name was nevertheless misread by all three models (beholdgenealogy.com).
- **Mark the unreadable.** Ask it to write "(?)" or "illegible" in place of what cannot be read and to keep the original spelling rather than guess.

## 4. A "not found" from AI

An empty AI answer means nothing until these are named:
- the source and the limits of the view (which frames, years, sections);
- the list of spellings;
- the method of search (index, full text, page by page; exact or phonetic);
- whether a **control record** was found by the same method;
- whether the site had errors (CAPTCHA, 403/429, cut-offs). A zero while the site refuses is a technical zero, not a result;
- how much was viewed and out of how many: "106 records for the shtetl" without a denominator says nothing.

And the question: was the person obliged to appear in this source?

A zero can be false even when the site answered without errors: the query address was assembled by hand with a wrong parameter, the search widens the query with synonyms and does not know your spelling, the catalogue looks for all words in one title. How to check the instrument — [The false zero](09-false-zero.md).

## 5. The status of a find

Give every find and hypothesis a status on the guide's single scale:

- 🟢 **confirmed** — a document read from the scan, plus a second independent feature;
- 🟡 **open / strong version** — several independent indirect features, no proof yet;
- ⚪ **unverified / weak** — one feature: a match of surname and place, an index row without a scan, a legend;
- 🔴 **rejected** — with the reason.

In detail, with the rules for the tree, see [Standard of proof](../3-results/01-standard-of-proof.md), section 4a. Only 🟢 goes into an online tree. The decision about kinship and about the status is made by the human, not by AI.

## 6. What AI does not do and should not do

- It does not pass CAPTCHAs and "I am not a robot" checks.
- It does not enter passwords, create accounts or pay.
- It does not send letters and requests on your behalf without your direct consent.
- It does not pass off information from memory as fact: a fond number, a village name or a date without an open source it marks "[from memory, verify]".
- It does not replace the archive: if a document is not digitised, AI will not find it.

---

**See also:** [Standard of proof](../3-results/01-standard-of-proof.md) · [The false zero](09-false-zero.md) · [Working with agents](03-working-with-agents.md), section 5 · [Scenarios](07-scenarios.md), scenario C2 · the [verifying-genealogy-findings](../../../skills/verifying-genealogy-findings/SKILL.md) skill
