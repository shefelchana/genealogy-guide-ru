---
name: dna-matches-across-platforms
description: >-
  Analyses one person's autosomal DNA matches across several sites (23andMe, Genotek, GEDmatch, FTDNA, MyHeritage) when the family is of mixed origin (one endogamous line, e.g. Ashkenazi, next to rural lines with scattered matches). Covers kit inventory, calibration, splitting off the endogamous network, phasing without parents through one-side relatives (a half-sibling's child, a cousin via one grandparent), searching place lists for the home village, cross-site confirmation, triangulation and population background in GEDmatch, "Are your parents related?", one tested family as one piece of evidence, a B1 letter to the match and the journal. Use when the user asks which side a match is from, can see a relative's test, or brings match lists from more than one company, even without saying "phasing". Also triggers on Russian requests: «разбери мои совпадения на всех сайтах», «с какой стороны этот родственник», «у меня есть доступ к тесту родственника», «родители не родня ли», «как написать совпаденке».
---

# DNA matches on several sites: a full analysis for mixed origin

Write files and reports in the user's language unless asked otherwise.

**The main thing:** DNA suggests where to look and tests a hypothesis; only a document names the ancestor. Record every conclusion with its level: 🟢 proven by a document, 🟡 strong hypothesis, 💭 guess, ⚪ background or noise.

Work on the sites (logging in, paying, letters) — **by the user's hands only**: you prepare, explain, and read what they have opened. Paid upgrades and sending letters are their decision.

## Step 0. Inventory: whose tests are where

Make a table: person → site → kit number → access (own / "view only" / none) → where the data came from (tested here or transferred).
- The same raw file often sits in 2–4 databases (for example, a 23andMe test transferred to GEDmatch and FamilyTreeDNA). These are **not new people**: the matches in each database are different, but the person is the same.
- Check which tests the user already has access to: in Russian services relatives often grant "view results". The test of **a relative connected to one side only** — a half-sibling or a half-sibling's child, a cousin through one grandparent — is the main phasing tool (step 3).
- What each site can do and where its limits are — `references/platforms.md`.

## Step 1. Calibration on known relatives

Find known relatives in the lists and compare the cM with the expectation (half-siblings ≈ 1,750, first cousins ≈ 870, half first cousins ≈ 430). Before deciding that the test "underestimates", ask whether **the relationship is full**. Do not draw conclusions about half relationships yourself. Details — the guide's DNA section, § 6a (`guide/2-справочник/15-днк.md`; English: `en/guide/2-reference/15-dna.md`).

## Step 2. Separate the endogamous network first

If one line is Ashkenazi (or otherwise endogamous), its matches will take the top of any list: thousands of people at 15–20 cM in one segment, and Leeds-method clusters merge. So:
1. Mark as "endogamous network" those who have the service's Ashkenazi label (Genotek, 23andMe), Ashkenazi surnames and places in the Pale of Settlement, or who are among the shared matches with a known Jewish relative.
2. **Do not apply the Leeds method to this part** (skill `dna-matches-endogamy`). Apply it to the rest.
3. Even a strong segment from this network (30+ cM) can almost never be assigned to a line (which of two Jewish great-grandparents). Record this honestly.

## Step 3. Phasing without parents

No parents — use relatives connected **to one side only**:
- a half-sibling or a half-sibling's child → only the side of the shared parent;
- a cousin through one grandparent → only that grandparent (example: a first cousin who is a child of the mother's brother shares only the mother's parents; a half-cousin through the maternal grandfather's second marriage shares only that grandfather).

The match is among the shared matches with them → the side is determined. **Not among the shared ones → means nothing**: such a relative carries only about ¼ of the DNA of the line in question. A person shared with both the "maternal" and the "paternal" relatives, with a total under 12 cM, is usually regional background, not a marriage between the lines.

## Step 4. ⭐ Searching for the home village in all ancestor lists

The strongest technique for non-endogamous lines (peasants, odnodvortsy, Cossacks — where matches have many surnames and few trees):
1. Export the **whole** match list with the fields "ancestral surnames with places", "birthplaces in the tree", "ancestral countries". In FamilyTreeDNA many people have a "surname — place" list; in Genotek, places and surnames from the trees.
2. Search for the **name of the village, volost, uezd** (in Cyrillic and in all Latin spellings: with and without the apostrophe for the soft sign, -oye/-oe, old and new name), not only surnames. Add neighbouring villages and the uezd town.
3. A match whose list has **two or more of the user's surnames from the same village**, even at a modest total (say 25–45 cM) and a longest segment under 20 cM, is a strong lead 🟡: the common ancestor was probably in that village in the 19th century. Which of the surnames is the shared one, DNA will not say — the metrical books will.
4. Someone else's surname in a Polish or Latin spelling next to a Russian one from the same village (hypothetically: Kowalewski ↔ Kovalev) is more likely one family in two records. Do not attribute it to the user.

## Step 5. One family — one piece of evidence

If a match's shared list contains several people **with the same ancestor list** (mother, sister, children), it is one family tested several times. That is **one** confirmation, not five. Their own surnames outside the shared list are their other line; do not look for your ancestors in it without a reason.

## Step 6. Cross-checking between sites

- The same family (one surname, similar names) with a segment **of the same length** at two companies → the match is almost certainly real 🟡.
- Transfer to GEDmatch: many users of Genotek, MyHeritage and FamilyTreeDNA are uploaded there. Look for a match from another site there by name or surname and by source site. If found, compare **segment positions** (One-to-One).
- The same name is not yet the same person: a different segment layout for "the same" person → not confirmed.

## Step 7. Triangulation and background (GEDmatch or a chromosome browser)

1. For 3–6 key people get the segments (chromosome, start–end, cM).
2. **Triangulation:** their segments with the user **overlap**, and they match **each other on the same stretch** → an argument for one common ancestor.
3. They match each other, but **in a different place**, and match the user on different chromosomes → shared population background, not a common ancestor.
4. A segment that runs through the centromere may be two glued together. Count it with caution.
5. Free comparisons in GEDmatch are limited: on a refusal ("access closed") stop, do not repeat.

## Step 8. "Are the parents related?"

GEDmatch "Are your parents related?" looks for long identical stretches from both parents (ROH ≥ 7 cM).
- **0 cM** → within roughly 5–6 generations the parents are not related.
- Earlier marriages between the lines (18th century) DNA does not see and does not rule out. The check is only through the metrical books of both villages. If the parents' home villages lie close to each other (the same or a neighbouring uezd), that is a reason to look, but not proof.
- Run all of one person's kits: the results should agree.

## Step 9. Living relatives nearby: the parents' social networks

A parent's page on a social network (the "Family" section, friends with a maiden name in brackets, a place "с. …, … район" [village …, … district]) often shows living relatives on the line being searched for. Rules:
- **read only**, at the user's direct request, on the page they named; do not compile a dossier on outsiders;
- record the name, place, year of birth if shown, and the "relative/family" mark;
- who is related to whom and how — **ask the user**, do not guess. Coinciding dates (a birthday that matches the grandfather's birthday) are only a reason to ask;
- writing to people is the user's decision.

## Step 10. A letter to the match

Template — `assets/first-letter.md`. Short, simple, human:
- English — **level B1**: short sentences, ordinary words, no officialese and no "smooth" AI style;
- how you know the person (site, cM), **one shared place and two surnames**, the question "do you speak Russian?", a request to upload the DNA to GEDmatch;
- write to the email from the match card on the site, rather than looking for the person on social networks. A social network — only if the letter got no reply;
- the **user** sends it.

## Step 11. The journal and recording finds

Template — `assets/journal.md`. For each site: what was exported (how many, which fields), thresholds, what is closed (paid features), sides, main leads, "what DNA refutes / allows", what next. Record a find **at once**, as soon as you find it: a long session may break off.

## What not to do

- Do not declare a common ancestor without a document.
- Do not treat "not among the shared matches" as proof of the other side.
- Do not count several tested members of one family as independent confirmations.
- Do not buy upgrades, accept terms, log in to accounts or send letters for the user.
- Do not publish the names of living matches and their lists; in texts for relatives and in public examples — placeholder names.

## Related skills

`checking-dna-against-tree` (ethnicity shares against the tree), the guide's DNA section, § 6a (calibration, haplogroups); `y-and-mtdna-lineage-testing` (Y-DNA and mtDNA); `dna-matches-endogamy` (thresholds and clusters under endogamy); `verifying-genealogy-findings` (checking with documents); `soviet-era-records` and `searching-familysearch-films` (the village's metrical books for checking).
