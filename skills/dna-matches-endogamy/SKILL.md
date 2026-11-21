---
name: dna-matches-endogamy
description: "Guides genetic genealogy for families with endogamy, above all Ashkenazi Jews. Covers choosing between autosomal, Y-DNA and mtDNA tests; where raw data can still be transferred (FamilyTreeDNA, GEDmatch, Living DNA; MyHeritage stopped accepting uploads in May 2025); sorting matches by longest shared segment instead of total cM; practical thresholds; why the Shared cM Project and company relationship labels overstate closeness under endogamy; pile-up regions; shared-match clusters; tying a match to documents; writing to matches; calibrating a test on known relatives and checking ethnicity shares with generation arithmetic; consent and privacy rules. Use whenever the user asks \"what do my DNA matches mean\", \"I have thousands of distant cousins\", \"who is this 4th cousin\", \"how many cM\", \"upload my DNA to GEDmatch\", \"transfer my data from MyHeritage\", \"which DNA test should I take\", \"Y-DNA test\", \"write to a match\", or pastes a match list from 23andMe, MyHeritage, Ancestry or FamilyTreeDNA, even if the word endogamy never comes up. Also triggers on Russian requests: «что значат мои совпадения», «у меня тысячи дальних родственников», «кто этот 4th cousin», «сколько сантиморган», «загрузить ДНК на GEDmatch», «перенести данные с MyHeritage», «какой ДНК-тест сдать», «Y-тест», «написать совпадению»."
---

# DNA matches under endogamy

## The main thing to tell the user at once

DNA is a **supporting** tool. It suggests where to look and tests a hypothesis, but it does not replace documents. Because of endogamy (centuries of marriage within the community), any two Ashkenazi people share more DNA than ordinary relatives of the same degree. So **thousands of "fourth cousins" are normal, not a discovery**, and a company's "4th cousin" estimate is usually closer than the real relationship.

## Step 1. Which question are we solving, and so which test

| Question | Test | Why |
|---|---|---|
| Who are these people, is the line confirmed, find living relatives | **autosomal** | DNA from both parents, relatedness out to about 6th cousins, but the further out, the coarser |
| Is this one paternal line (two families of the same surname, "the same man" under a different surname) | **Y-DNA** | only it answers yes/no; finds relatives with **different surnames** |
| The direct maternal line | **mtDNA** | common ancestor within 1–50 generations: weak for genealogy |
| Which side a match comes from | **X-DNA** (part of the autosomal test) | narrows the range of lines |

- The Y-test is taken by **the oldest available man** in the direct paternal line. A full match on 37 markers means a common ancestor who, by the old FamilyTreeDNA table, is with 95% probability no further back than 8 generations (other calculations give a wider spread); a shared terminal SNP settles it finally.
- To check the **paper** paternal line, test two of its male-line descendants who are **documentarily the furthest apart** (the protocol of Jeffrey Mark Paull), after assessing the quality of the documents themselves. Traps: non-paternity, informal adoption, a surname taken from the wife (it happened with sons-in-law). A Y-haplogroup confirms membership in the line, not a particular ancestor.
- Ethnicity estimates below the continental level are unreliable and differ between companies: they **prove nothing**.

Services, data transfer, prices and country restrictions: `references/services.md` (as of October 2026). The key points:
- **They do not accept other people's files:** AncestryDNA, 23andMe and, **since May 2025, MyHeritage**. Many articles from before 2025 still advise uploading to MyHeritage: this is out of date.
- **They accept:** FamilyTreeDNA, GEDmatch, Living DNA.
- FamilyTreeDNA **does not ship kits** to Russia, Belarus and Ukraine: plan a Y-test for a relative there in advance (YSEQ, YFull from a BAM file, a third country).

Creating accounts, logging in, uploading a file and paying are **done by the user**. You explain where the button is and what to choose.

## Step 2. Selecting matches: the longest segment, not the total

Why: under endogamy the total cM is built up from many short shared pieces from different distant ancestors. A long unbroken segment was inherited recently and points to a traceable common ancestor.

1. **Sort by longest segment.** FamilyTreeDNA, MyHeritage and GEDmatch can do it (column sorting in GEDmatch is in paid Tier 1). Ancestry cannot (segments only through a DNAGedcom export), and its "longest segment" is shown before the population-wide stretches are subtracted, so it may exceed the whole total.
2. **Thresholds**: there is no single standard; present them as rules of thumb with their authors:
   - practical rule: longest segment **under 15 cM: discard; from 20 cM: look at the tree; from 30 cM: write to the person**; a total of **200–250 cM and above** is almost certainly a traceable relationship;
   - Kitty Cooper: one segment over 20 cM, a second over 10 cM, and a few more;
   - FamilyLocket: discard when the longest is under 23 cM, do not count segments under 10 cM in the total; with strong endogamy raise the lower threshold to 15 cM;
   - Adina Newman (RootsTech 2025, "Jewish Genealogy 101"): work with an Ashkenazi match only if the **total is at least 100 cM, the longest segment at least 20 cM, plus one or two segments of 10–20 cM**; the thousands of others are untraceable. Tested on a real 23andMe list (November 2026): only the one relative already known from documents passed; the other "strong" matches (30–63 cM) could not be resolved by DNA alone. Use this as the default filter before any clustering.
   - Also record the **average segment** (total cM ÷ number of segments; Bergheimer, RootsTech 2025): a large average points to a recent ancestor; 35 cM on 35 segments is most likely false, 35 cM on 2 segments is fourth-cousin level (Trotter-Martin, RootsTech 2025). Sort the shortlist by it.
3. **Pile-up regions:** some stretches are present in almost all Ashkenazim (FamilyLocket's analysis mentions the end of chromosome 16 and chromosome 9). Do not accept a segment shorter than 20–23 cM that does not extend beyond such a region.
4. **Do not convert cM into a degree of relationship using the Shared cM Project table** (DNA Painter) without a caveat: it does not account for endogamy, under which one cM figure corresponds to many degrees, and the table shows a relationship closer than the real one. Give a range and say "more likely more distant than the service shows". For Ashkenazim compare with the **Ashkenazi norms** of Lara Diamond's survey (2022; for example, second cousins average about 272 cM with a longest segment of about 49 cM): table and spread in `references/services.md`.
5. **Before WATO and similar calculators, discard segments under 7 cM** (Louis Kessler's check; details in `references/services.md`).

## Step 3. Clusters and shared matches

1. For each selected match, open the **relatives in common** (Relatives in Common, Shared Matches). A group of people who match both you and each other is a cluster, usually one line.
2. **The Leeds method** (colouring matches of 90–400 cM into four groups by grandparent) **does not work under endogamy**: the clusters merge; Dana Leeds herself says so. If only part of the tree is endogamous (for example one non-Ashkenazi line), the method suits that part. The same holds for autoclusters and WATO (Newman, RootsTech 2025, "DNA and Endogamy"): for Ashkenazi matches run them only on matches that passed the Step 2 threshold.
3. **Chromosome painting by ethnicity** (23andMe, FamilyTreeDNA) helps by suggesting the side.
4. **More tests in the family:** several descendants of one couple, especially descendants of those who left the endogamous milieu. A match with both you and your maternal aunt is more likely maternal; with you alone, check the paternal side (under endogamy this is a pointer, not a conclusion).
5. In **DNA Painter**, lay segments out across known ancestors, raising the minimum threshold from 7 to 10–15 cM.

## Step 4. From a match to a document

1. In the match's tree first compare the **places** of the ancestors' birth (shtetl, uezd), **then** the surnames. The common ancestor of Ashkenazim is often older than surnames (which were fixed in 1804–1835), so the absence of shared surnames is normal.
2. Compare Ashkenazi matches with non-Ashkenazi ones from the same places.
3. Test the hypothesis "the match is through great-grandfather N" with a **document**: a metrical record, revision list (*revizskaya skazka*), census where both families are tied together. Without a document it is a hypothesis, and record it as one. A sample of a confident hypothesis (N. Lipes): one person's given name matches another's patronymic, they lived in neighbouring shtetls, they followed the same trade, plus a DNA match with descendants of the great-grandfather's brother. For a tree this is enough as a 🟡 hypothesis, for a consulate it is not.
4. A match found in an aggregator should be **confirmed by comparing segments on the original platform**: with Lipes, "relatives" from an aggregator showed not a single shared segment on the original service.
5. A match with no tree is a common situation (on GEDmatch especially). Do not guess; note it and come back when information appears. Advise the user to **attach a link to their own tree** to their profile, so that people write to them.
6. A useful detail: the 23andMe relatives-list export has a Y-haplogroup column, filled in even for people who did not accept the invitation.

Keep a log from `assets/match-log.md`: who (a code), service, total cM, longest segment, number of segments, cluster, places in the tree, hypothesis, whether you wrote, the reply.

## Step 5. A letter to a match

Templates: `assets/match-letters.md`. Rules:
- **short:** who you are, one or two surnames, the place, the generation, how to reach you; centimorgans and segments are not needed in the first letter, since many people do not understand them;
- **offer something of your own:** the earliest ancestor with the place, a chart of the branch;
- **no pressure:** silence may mean "the person is in shock", not "ignoring"; do not write again with insistence;
- if the person has several kits, say which one.

The **user** sends the letter: you prepare the text.

## Step 5a. Before drawing conclusions — calibration and arithmetic

- **Calibrate the test on known relatives.** Expected: full siblings ≈ 2,600 cM; half-siblings, grandparent, aunt, niece ≈ 1,750; first cousins or half-aunt/half-niece ≈ 870; half first cousins (one shared grandparent) ≈ 430. Before deciding the service "underestimates", ask whether the relationship is full or half. (Invented example: a tester sees a "niece" at about 900 cM and a "first cousin" at about 420 cM and decides the service underestimates by half. In fact the niece is the daughter of a half-sibling (expected ≈ 870) and the cousin is related through only one shared grandparent (expected ≈ 430) — both figures are exactly right for half relationships.) Do not draw conclusions about a half relationship yourself — ask.
- **Check an ethnicity share with generation arithmetic:** grandparent 25 % (± 3–4), great-grandparent 12.5 % (± 3), great-great-grandparent 6 % (± 2), fifth generation ≈ 3 % or zero. "Great-grandmother was German" with 1 % Germanic is refuted literally; a distant ancestor stays possible. Shares under 2–5 % are hints. 23andMe's Ancestry Timeline is ± one generation.
- **mtDNA** must match for all children of one mother and the children of her daughters; different subclades between tests are a chip artefact — only the shared level is reliable.
- **Side without parents' tests:** use the shared-matches filter with relatives tied to one side only (a niece on the mother's side, first cousins through one grandmother only).
- **Matches' trees** are a source of hypotheses: look at places and years; a matching father's name and birth year in someone else's tree is confirmed only by a record.

## Ethics and privacy: always observe

- Only **the person themselves** (or a legal representative) takes the test, with informed consent; they must know who will see the data and what surprises are possible. Uploading a relative's file to GEDmatch is only with their consent.
- **A test may show something unexpected** (the biological father is not the one thought, an unknown brother). "There is a right to know, but no right to a relationship." Do not tell relatives about such a thing at once: first rule out an error (two independent lines of matches), then let the user decide whom to tell and why.
- **Do not publish** the data of those tested and **do not forward other people's match lists** without the owner's consent. In texts for relatives, hide the names of living matches.
- **Do not upload a raw DNA file anywhere yourself and do not ask for it to be sent into the chat**: genetic data concerns all relatives, and a leak cannot be undone. A match list is enough for analysis; advise removing names from it (keep initials and figures).
- Police access differs by service (GEDmatch is opt-in only, FamilyTreeDNA is opt-out): say so before uploading.

## How to answer "what do my matches mean"

1. Explain endogamy in two sentences and why the "4th cousin" label is inflated.
2. Filter the list by longest segment and show how many remain after the thresholds.
3. For those that remain: what to look at (places in the tree, shared matches) and whom it is worth writing to.
4. Which test, or which relative for a test, would give the most.
5. What cannot yet be asserted.

Do not name a specific degree of relationship or common ancestor until it is confirmed by a document. Do not invent prices and features of services beyond `references/services.md`: say they need to be checked on the site.

## Related skills

`dna-matches-across-platforms`: if the test is on several sites or the origin is mixed; `verifying-genealogy-findings`: testing a hypothesis with documents; `tracing-emigrants-to-origin`: if the match is from an emigrant branch.
