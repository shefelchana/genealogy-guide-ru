# DNA Tests in Genealogy

What this section covers: the kinds of tests, what they can and cannot do, how to work with matches under endogamy (Ashkenazi families), where you can upload your data, and which ethical rules to follow. Service profiles are in [DNA services](../../catalog/dna-services.md).

Information about companies is current as of October 2026; the rules change, so check the websites.

---

## 1. When you need a DNA test

DNA is a **supporting** tool. It does not replace documents: Nadia Lipes and all the guides we have read agree on this. A test is useful when:
- the documents have run out and you need to check whether it is the same family;
- you are looking for living relatives (including emigrant branches);
- you need to test the hypothesis "these two lines are one paternal line" (only a Y-DNA test can do this).

## 2. Types of tests

According to Wikipedia ("Genealogical DNA test") and the VGD forum (the section "DNA genealogy. Beginners' questions", Russian-language forum):

| Test | What it examines | Questions it answers |
|---|---|---|
| **Autosomal** (chromosomes 1–22 and X) | DNA from both parents | "Who are these relatives?", "Is the line confirmed?" Finds relatives out to roughly 6th cousins, but the more distant the relationship, the less accurate the estimate. Ethnicity estimates below the continental level are unreliable and differ between companies |
| **Y-DNA** | men only, the direct paternal line | "Is this the same paternal line?" With a full match on 37 markers, the common ancestor is, with 95 % probability, no more than 8 generations back. Finds relatives with **different surnames** |
| **mtDNA** | the direct maternal line, in both sexes | A full match means a common ancestor somewhere within 1–50 generations; of limited use for genealogy |
| **X-DNA** | part of the autosomal test | helps narrow down the possible lines |

The **Y-test** is the only way to answer "yes / no" to "is this the same paternal line" where the documents break off (a common terminal SNP). An autosomal test will not show this. Test **the oldest available man** in the direct male line.

The order for checking a paternal line (J. M. Paull, Y-DNA studies of rabbinic dynasties) [checked]:
1. First assess the paper pedigree: the quality of the documents, the clarity of the generations.
2. Test **two descendants who are documentarily the furthest apart** in the male line; the steps are Y-37 → Y-111 → Big Y.
3. Remember the pitfalls: non-paternity events, informal adoption, **a surname taken from the wife or the maternal line**, a frequent case when sons-in-law were recorded.

A Y-haplogroup confirms **membership in a line**, not a specific ancestor (the principle of Adam Brown's Avotaynu DNA project) [checked].

**mtDNA among Ashkenazim.** About 40 % of Ashkenazi maternal lines go back to four "founding mothers": haplogroups K1a1b1a, K1a9, K2a2a, N1b (D. Behar et al., 2006) [from search snippet]. A match on such haplogroups says almost nothing about genealogical kinship. Check your haplogroup against K. Brook's catalogue "The Maternal Genetic Lineages of Ashkenazic Jews" (2022): a rare haplogroup is more informative [checked].

## 3. Companies and transferring data (October 2026)

**They do not accept files from others:** AncestryDNA, 23andMe and, since May 2025, **MyHeritage**. MyHeritage help (July 2026): "DNA uploads are no longer supported". According to The DNA Geek's analysis ("The End of an Era: Uploads at MyHeritage"), the restrictions began at the end of May 2025. What happened to older uploads — sources differ. ⚠️ Many articles from before 2025, and even the GEDmatch blog, still list MyHeritage as a site for free upload — this is out of date.

**They accept:**
- **FamilyTreeDNA** — Ancestry, 23andMe and MyHeritage files; matches are free; the $19 unlock was discontinued on 18.08.2026, and advanced features now go through a paid upgrade (per dna-explained.com — $29) [page: dna-explained.com, 2026-10-07]; uploaded data cannot later be downloaded back.
- **GEDmatch** — free "one-to-many" (the first 50 matches) and "one-to-one" comparisons; Tier 1 is $15 a month for new subscribers (from 01.09.2026; existing subscribers pay $10).
- **Living DNA** — free upload, basic matches.

**Restrictions by country:**
- FamilyTreeDNA, according to its official help pages, **does not ship kits to Russia, Belarus or Ukraine**. A Y-test for a relative in these countries has to be planned in advance: fallback options are YSEQ (Berlin, whole genome about $399), YFull from a ready BAM file, or forwarding through a third country.
- MyHeritage DNA tests are not available at all in some countries (an official restriction). Check before ordering.
- AncestryDNA is not sold in every country (per the help page of September 2026 — in 119).

**23andMe:** the company filed for bankruptcy on 23.03.2025; on 14.07.2025 its assets were bought by the non-profit TTAM Research Institute ($305 million), which promised to keep the previous policy; the service is operating [page: Wikipedia "23andMe", 2026-10-07; the company website did not open].

**Police access** (per the GEDmatch blog; some of the information is out of date — re-check): GEDmatch — only with the user's explicit consent (opt-in); FamilyTreeDNA — permitted, but you can opt out; 23andMe and Ancestry — only by court order.

## 4. Endogamy: why everything is harder for Ashkenazim

**Endogamy** is marriage within one community over many centuries. Because of it, any two Ashkenazim share noticeably more DNA than random people at the same degree of relationship: matches are connected to you by several paths at once. The relationship looks closer than it is. Ashkenazim have thousands of apparent "fourth cousins".

What to do:

1. **Sort by the longest segment, not by the sum of centimorgans (cM).** FamilyTreeDNA, MyHeritage and GEDmatch can do this; Ancestry cannot (segments are visible only in an export via DNAGedcom). On Ancestry the "longest segment" is shown before population-wide regions are subtracted and may be larger than the total (Kitty Cooper).
2. **Thresholds** differ between authors; there is no single standard:
   - a rule of thumb from one study: longest segment **below 15 cM — discard; from 20 cM — look at the tree; from 30 cM — write to the person**. A total of 200–250 cM and above is almost certainly a traceable relationship;
   - Kitty Cooper: one segment above 20 cM, a second above 10 cM and a few more;
   - FamilyLocket: discard matches whose longest segment is below 23 cM, and do not count segments below 10 cM in the total; under strong endogamy raise the lower threshold to 15 cM.
3. **Pile-up regions:** some stretches of chromosomes are present in almost all Ashkenazim. Do not accept matches in such regions if the segment is shorter than 20–23 cM and does not extend beyond the region (FamilyLocket).
4. **The Shared cM Project table** (DNA Painter) does not take endogamy and pedigree collapse into account: it understates the distance, and one cM value corresponds to many possible degrees of relationship. For Ashkenazim, compare with Lara Diamond's survey (Ashkenazic Shared DNA Survey, 6,455 pairs of known relationship, 2022 update) [checked]: average values — total cM / longest segment:

   | Relationship | Total, cM | Longest, cM |
   |---|---|---|
   | first cousins (1C) | 922 | 84 |
   | first cousins once removed (1C1R) | 485 | 61 |
   | second cousins (2C) | 272 | 49 |
   | 2C1R | 164 | 37 |
   | third cousins (3C) | 113 | 28 |
   | 3C1R | 77 | 21 |
   | fourth cousins (4C) | 53 | 13 |

   The spread is huge: for second cousins, from 7 to 698 cM. The table is a guide, not a calculator.

   ⚠️ Naming of degrees: in the English system 2C (second cousins) are what Russian-language sources call *troyurodnye* (literally "third cousins"), and 3C are *chetveroyurodnye* (literally "fourth cousins"). The labels in the table above are the English ones.

   **Short segments are population background.** Because of the bottleneck in Ashkenazi history, any two people share very many short segments (S. Carmi et al., Nature Communications, 2014) [from search snippet]. Before any relationship-probability calculator (for example WATO in DNA Painter), **discard segments below 7 cM**: on FamilyTreeDNA data without this filter, L. Kessler's total was overstated by about 50 cM, and with the filter WATO gave the correct answer (beholdgenealogy.com) [checked]. Triangulating a segment weeds out chance matches, but the common ancestor still has to be proved with documents.
5. **The Leeds method** (colouring matches of 90–400 cM into four groups by grandparent) **does not work under endogamy** — the clusters merge. Dana Leeds herself says so. If only part of the tree is endogamous, it can be used for the other lines.
6. **More tests in the family.** Test several descendants of one couple. Descendants whose ancestors left the endogamous environment are especially valuable.
7. **Match trees:** first compare the ancestors' **birthplaces**, then surnames (FamilyLocket). Compare Ashkenazi matches with non-Ashkenazi ones from the same places.
8. **DNA Painter:** map segments to known ancestors, raising the minimum threshold from 7 to 10–15 cM.
9. **Chromosome ethnicity paintings** (23andMe, FamilyTreeDNA) suggest which side a match may come from.

Sources: familylocket.com ("Strategies for Overcoming Endogamy", "Endogamy: Ashkenazi Jewish Case"); blog.kittycooper.com ("Ancestry and the Longest Segment"); danaleeds.com; dnapainter.com.

## 5. What it looks like in practice

From one real study (September 2026):
- The ancestry estimate at 23andMe matched what was expected from the documents — but by itself proves nothing.
- The first close match turned out to be a relative on the same paternal line, which agreed with the documents. He did not accept the invitation — it had to be handled through mutual relatives.
- The 23andMe relatives-list export has a Y-haplogroup column; it is filled in even if the person has not accepted the invitation.
- Not one of the family surnames appeared in the cluster of matches. This is normal: the common ancestor may be centuries back, before surnames were adopted (1804–1835).
- On GEDmatch, by the "long segment from 20 cM" rule, several people qualified, but without attached trees there was nothing to compare against. Hence the advice: attach a link to your tree to your profile.
- MyHeritage removed the built-in export of matches to a spreadsheet; you have to work with screenshots and filters.

## 6. Working with matches

1. Select matches by the long segment (see above). A match found on an aggregator service should be checked by comparing segments on the original platform: for N. Lipes, "relatives" from an aggregator showed not a single shared segment on the original platform (nadialipes.info, 2019).
2. Look at their trees: the ancestors' **places** of birth, then surnames.
3. Find **shared** relatives (Relatives in Common, Shared Matches).
4. Write briefly and in a friendly way — templates and advice are in [Requests and letters](20-requests-letters.md).
5. Record in the log: who, how many cM, longest segment, which hypothesis, whether they replied.
6. **Choose in advance whom to test**, for a specific hypothesis — descendants of different children of one couple — and write down the reasoning: the DNA of known relatives is needed both to confirm and to **refute** hypotheses (I. Pikholtz, "Endogamy: One Family, One People", 2015) [from search snippet].

**An example of combining documents and DNA** (N. Lipes on her own line, isrageo.com, 2020): one man's name matches another man's patronymic, they lived in neighbouring shtetls 12 km apart and traded in the same goods — this is a "father – son" hypothesis. Confirmation came from a DNA match with descendants of a great-grandfather's brother. Lipes notes that such evidence is not enough for a consulate.

## 7. Ethics and consent

- **Only the person themselves takes the test**, or their legal representative, with informed consent. The person tested must know who will see the data and what surprises are possible (BCG, code of ethics).
- **A test may show something unexpected** — for example, that the father who raised you is not the biological one. "Everyone has the right to know about their biological family, but no one has a right to a relationship" (FamilySearch, "Ethics and DNA Testing"). Do not pressure those who do not want contact.
- **Do not publish** the data of those who have been tested, and **do not forward other people's match lists** without the owner's consent (BCG).
- **Genetic data concerns all relatives**, and a leak cannot be undone. Protect your account with a strong password (FamilySearch advises changing it every six months). Do not upload DNA data to services with an unclear storage policy — including AI chatbots: "you can't take it back" (K. Borges, RootsTech 2026).

> **How to ask AI**
>
> - "Here is a list of my DNA matches [table: total cM, longest segment, number of segments]. Select the ones worth working with under Ashkenazi endogamy and explain the thresholds you use." *Check yourself:* do not upload raw DNA data to a chat; give only the match numbers.
> - "I share [N] cM with a match, longest segment [M] cM. Which degrees of relationship are possible for Ashkenazi Jews? Compare with Lara Diamond's Ashkenazic Shared DNA Survey, not only the Shared cM Project." *Check yourself:* the spread is huge: a cM figure does not name the degree of relationship.
> - "Help me write a short, polite first message to a DNA match: who I am, which surnames and places I am researching, and what we appear to have in common." *Check yourself:* you send the message yourself.

---

**See also:** [DNA services](../../catalog/dna-services.md) · [Requests and letters](20-requests-letters.md) · [Standard of proof](../3-results/02-standard-of-proof.md) · [Tree platforms](16-tree-platforms.md)
