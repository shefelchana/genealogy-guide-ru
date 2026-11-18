# DNA Tests in Genealogy

What this section covers: the kinds of tests, what they can and cannot do, how to work with matches under endogamy (Ashkenazi families), where you can upload your data, and which ethical rules to follow. Service profiles are in [DNA services](../../catalog/dna-services.md).

Information about companies is current as of October 2026; the rules change, so check the websites.

---

## 1. When you need a DNA test

DNA is a **supporting** tool. It does not replace documents: Nadia Lipes and all the guides we have read agree on this. A test is useful when:
- the documents have run out and you need to check whether it is the same family;
- you are looking for living relatives (including emigrant branches);
- you need to test the hypothesis "these two lines are one paternal line" (only a Y-DNA test can do this).
- the family has a legend about its origin ("great-grandfather was German", "we are a bit Polish"): there may be no documents, and DNA is an independent witness. But the "ethnicity estimate" is an estimate — the percentages change from version to version; the proof is matches with specific relatives. For citizenship DNA does not replace documents.

## 2. Types of tests

According to Wikipedia ("Genealogical DNA test") and the VGD forum (the section "DNA genealogy. Beginners' questions"):

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

Step by step on Y-DNA and mtDNA (which test level to choose, genetic distance, TiP, FamilyTreeDNA projects, mtFull and Mitotree, why "the same haplogroup" is not yet kinship): the skill [`y-and-mtdna-lineage-testing`](../../../skills/y-and-mtdna-lineage-testing/SKILL.md) (written for AI, in English).

## 3. Companies and transferring data (October 2026)

**They do not accept files from others:** AncestryDNA, 23andMe and, since May 2025, **MyHeritage**. MyHeritage help (July 2026): "DNA uploads are no longer supported". According to The DNA Geek's analysis ("The End of an Era: Uploads at MyHeritage"), the restrictions began at the end of May 2025. What happened to older uploads — sources differ. ⚠️ Many articles from before 2025, and even the GEDmatch blog, still list MyHeritage as a site for free upload — this is out of date.

**They accept:**
- **FamilyTreeDNA** — Ancestry, 23andMe and MyHeritage files; matches are free; the $19 unlock was discontinued on 18.08.2026, and advanced features now go through a paid upgrade (per dna-explained.com — $29) [checked: dna-explained.com, 2026-10-07]; uploaded data cannot later be downloaded back.
- **GEDmatch** — free "one-to-many" (the first 50 matches) and "one-to-one" comparisons; Tier 1 is $15 a month for new subscribers (from 01.09.2026; existing subscribers pay $10).
- **Living DNA** — free upload, basic matches.

**Restrictions by country:**
- FamilyTreeDNA, according to its official help pages, **does not ship kits to Russia, Belarus or Ukraine**. A Y-test for a relative in these countries has to be planned in advance: fallback options are YSEQ (Berlin, whole genome about $399) or YFull from a ready BAM file. For Russia, keep in mind law 43-FZ (§ 3a).
- MyHeritage DNA tests are not available at all in some countries (an official restriction). Check before ordering.
- AncestryDNA is not sold in every country (per the help page of September 2026 — in 119).

**23andMe:** the company filed for bankruptcy on 23.03.2025; on 14.07.2025 its assets were bought by the non-profit TTAM Research Institute ($305 million), which promised to keep the previous policy; the service is operating [checked: Wikipedia "23andMe", 2026-10-07; the company website did not open].

**Police access** (per the GEDmatch blog; some of the information is out of date — re-check): GEDmatch — only with the user's explicit consent (opt-in); FamilyTreeDNA — permitted, but you can opt out; 23andMe and Ancestry — only by court order.

How to download the raw file, read its header (company, chip or whole genome, version, date), why not to upload an imputed file (for example Genotek's paid "23andMe V5" file), and which file each site accepts as of November 2026: the skill [`dna-raw-data-backup-and-transfer`](../../../skills/dna-raw-data-backup-and-transfer/SKILL.md) (in English). It also covers backing up your match lists before deleting an account or an upgrade.

## 3a. How to order a test if you live in… (checked 17.10.2026)

From the companies' official shipping lists. "—" means the country is not on the official list, i.e. no shipping.

| Country | 23andMe | AncestryDNA | MyHeritage | FamilyTreeDNA |
|---|---|---|---|---|
| Russia | — | — | no (residents of Russia excluded) | no |
| Belarus, Ukraine | — | — | not stated, check when ordering | no |
| Kazakhstan, Uzbekistan | — | — | not stated | yes |
| Armenia | yes | — | not stated | yes |
| Georgia | — | yes | not stated | yes |
| Moldova | yes | yes | not stated | yes |
| Israel | yes | — | no (residents of Israel excluded) | yes |
| Germany, EU | yes, except France | yes, except France | yes, except France | yes, except France |

Sources: [23andMe](https://support.23andme.org/hc/en-us/articles/42966083069975-What-Countries-Do-You-Ship-To) (updated 16.10.2026); [AncestryDNA](https://ancestry.my.site.com/FrCa/articles/en_GB/Support_Site/Countries-Where-AncestryDNA-is-Available) (119 countries); [MyHeritage](https://www.myheritage.com/help/en/articles/13130458-who-is-eligible-to-take-a-myheritage-dna-test); [FamilyTreeDNA](https://help.familytreedna.com/hc/en-us/articles/11805929449487-International-Outbound-Shipping) (updated 22.09.2026; no shipping to 20 countries, including Russia, Belarus, Ukraine, Turkmenistan, Turkey, France). Living DNA says "We ship to any location", with no list of restrictions.

**Prices of the basic test** (17.10.2026): FamilyTreeDNA Family Finder $79 (on sale until 11.11 — $39; international shipping $9.95) · MyHeritage €89 (frequent sales) · 23andMe about $99 · Living DNA from €85 · AncestryDNA about $99 (secondary sources).

**From Russia:** the large companies do not ship. Local labs — Genotek and Atlas — search for relatives in their own database and let you download raw data (from the companies' sites; check the site yourself). A file in 23andMe format, users report, uploads to FamilyTreeDNA and GEDmatch; Genotek is not on FamilyTreeDNA's official list.

**Rules worth knowing:**
- 23andMe and Ancestry require the kit to be used in the country it was shipped to.
- MyHeritage's restrictions for Russia and Israel apply to residents, not to the delivery address.
- Workarounds (changing the account country, a VPN) break the companies' rules — they are not in this guide.

**Laws on genetic data** [verify against the text of the law]:
- **Russia.** Federal Law No. 43-FZ of 20.02.2026, in force from 01.09.2026: genetic research data may be transferred abroad or to foreigners only by decision of an inter-agency commission (Government decree No. 750). The sources do not say clearly whether this covers a private person and their own sample; moderators of the VGD forum treat sending samples abroad as forbidden. No fines were found in the sources. Sources: Pharmvestnik (06.05.2026), T-invariant (30.07.2026), VGD forum moderator posts (September–October 2026); we did not open the text of the law itself. This guide gives no instructions for sending a sample out of Russia: test with a Russian lab, or where you are legally staying.
- **Israel.** Genetic Information Law 5761-2000: genetic testing by a doctor's referral or a court order, in approved labs. Sources disagree on whether tests you buy yourself (direct-to-consumer) are banned or only strictly regulated (Calcalist, 2020, possibly out of date; family-laws.co.il, undated).

Which test to choose for your country and goal, and whom in the family to test first: the skill [`choosing-dna-test-by-country-and-goal`](../../../skills/choosing-dna-test-by-country-and-goal/SKILL.md) (in English; countries, laws and sources are in its `references/country-availability.md`).

**How to take it:** order a kit → **activate it with the code on the site** (otherwise the sample is not processed) → saliva (23andMe, Ancestry, Genotek) or a cheek swab (FamilyTreeDNA, MyHeritage, Living DNA; no food or drink for an hour before) → send it back. Return from abroad is often at your own cost. Sending a sample out of Russia is restricted by law 43-FZ from 01.09.2026 (see above). Time after the lab receives it: MyHeritage 3–4 weeks, Ancestry about 6, FamilyTreeDNA 6–9, Living DNA 6–8, Genotek up to 12.

**Raw data** is the file with your genotypes. Download it at once: it can be uploaded to FamilyTreeDNA (free, matches) and GEDmatch, and it survives even if the company closes. FamilyTreeDNA accepts 23andMe files (V3–V5), MyHeritage (March 2019 – October 2025) and AncestryDNA up to September 2025 ([help](https://help.familytreedna.com/hc/en-us/articles/4415446123663-Autosomal-DNA-Transfers)).

**Y-DNA and mtDNA:** FamilyTreeDNA (Y-37 $119, Y-111 $249, Big Y-700 $449, full mtDNA $159; same country restrictions) and YSEQ in Berlin (Y-STR from €65, mtDNA from €25, "worldwide" shipping; for Belarus ask YSEQ; for Russia see law 43-FZ above): [yseq.net](https://www.yseq.net/shipping.php).

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
- ~~The 23andMe relatives-list export has a Y-haplogroup column; it is filled in even if the person has not accepted the invitation.~~ **Correction (November 2026):** this was not confirmed. If a match has open data sharing turned off and has not accepted the invitation, 23andMe gives neither their haplogroups nor their location. You see only sex, shared percentage, number of segments and the longest segment.
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

## 6a. Reading your own result: calibration, percentages, haplogroups

**First calibrate the test on relatives whose relationship you know.** Find a sibling, niece or nephew, first cousins among your matches and compare the shared cM with the expected values (for non-Ashkenazi lines, the Shared cM Project):

| Relationship | Expected, cM |
|---|---|
| full sibling | ≈ 2,600 |
| half-sibling, grandparent, aunt, niece | ≈ 1,750 |
| first cousin; half-aunt or half-niece | ≈ 870 |
| half first cousin (one shared grandparent) | ≈ 430 |

A real case: the test seemed to "halve" the relationship both with a niece and with a first cousin. It turned out the sister was a maternal half-sister and the aunt a half-aunt through one grandmother — and the numbers were exact. **Before blaming the test, ask whether the relationship is full or half.**

**"Ethnicity" is a model.** Compare two companies: agreement on the main components is reliable; details depend on reference panels. A family story is checked with arithmetic: a great-grandparent contributes 12.5 % on average (± 3), a great-great-grandparent 6 % (± 2), an ancestor five generations back about 3 % — or nothing. "Great-grandmother was German" with 1 % Germanic DNA is refuted literally, but a distant German ancestor remains possible. Shares below 2–5 % are hints, not conclusions. In old Russian usage, *nemtsy* ("Germans") often meant any foreigners — test that reading too.

**The ancestry timeline (23andMe's Ancestry Timeline)** estimates when the most recent ancestor of a single origin was born. Treat it as ± one generation.

**The maternal haplogroup** must be identical for all children of one mother and for the children of her daughters. If you and a maternal niece get different subclades (H1n and H1b2), it is a chip error; only the shared level (H1) is reliable.

**Which side a match is on, when parents cannot test.** Use the "shared matches" filter with relatives linked to only one side: a maternal half-niece shows only your mother's side; a half first cousin through one grandmother shows only that grandmother's line.

**Matches' trees** are read for places and years, not only surnames. A matching father's name and birth year in someone else's tree is a hypothesis; only a metrical record confirms it.

## 6b. The match list step by step: what genetic genealogists advise

A summary of the rules from this section and from the guidance of the BCG, the Shared cM Project (B. Bettinger), D. Leeds, FamilyLocket and L. Diamond, in the order in which to apply them.

1. **DNA tests a hypothesis; it does not name an ancestor.** Under the Genealogical Proof Standard (BCG), a conclusion about kinship rests on documents and DNA together: first a version from the documents, then a check whether the DNA agrees with it. DNA can refute a version; it cannot "name" a person.
2. **Calibrate the test** on known relatives (§ 6a).
3. **Convert everything to centimorgans.** 23andMe shows a percentage: 1 % ≈ 74 cM (roughly; the exact figure is in the match's profile). For each match, record: total cM, number of segments, **longest segment**, **average segment** (total ÷ number).
4. **Cut the noise:** longest segment < 7 cM — false; < 15 cM under endogamy — discard; 15–20 — weak; 20–30 — look at the tree; ≥ 30 — write to the person (§ 4). Many segments with a small average (< 10–12 cM) is a signature of endogamy.
5. **Choose the table by the match's origin.** For non-endogamous lines, the Shared cM Project (averages and ranges, v4):

   | Relationship | Average, cM | Range |
   |---|---|---|
   | 2C (second cousins) | 229 | 41–592 |
   | 2C1R | 122 | 14–353 |
   | 2C2R | 71 | 0–261 |
   | 3C (third cousins) | 73 | 0–234 |
   | 3C1R | 48 | 0–192 |
   | 4C (fourth cousins) | 35 | 0–139 |

   For Ashkenazi matches use L. Diamond's table (§ 4): there the same degrees give 1.2–1.5 times more cM. The DNA Painter calculator (Shared cM Tool) shows every degree compatible with a cM figure; WATO gives the probabilities of competing versions when the tree is known.
6. **With mixed origin, split the list first.** If only one line is endogamous (for example, one grandfather was Ashkenazi), first separate the "endogamous" cluster: matches with Ashkenazi surnames, ancestors from the Pale of Settlement and the USA, and matches shared with a known Jewish relative. Do not apply the Leeds method to it (§ 4, item 5). Apply it to the rest.
7. **The Leeds method** (D. Leeds, 2018). Take matches in the 90–400 cM range (if there are few, go down to longest segment ≥ 20 cM). Go down the list from the top; the first match without a colour gets a new colour, and all its shared matches get the same colour. Ideally you get up to four groups, one per grandparent. A match in two colours hints at a marriage between lines or an error. Automatic equivalents: "DNA Relatives Clustering" at 23andMe, AutoCluster (Genetic Affairs), MyHeritage clusters.
8. **Tie a cluster to a side.** A parent's test is best; without parents, use relatives connected to only one side (§ 6a). Then the trees: the ancestors' **places and years** matter more than surnames.
9. **Triangulation.** If three or more people share a segment on the same chromosome and all of them match each other on that segment, it supports one common ancestor. GEDmatch, MyHeritage and FamilyTreeDNA have a chromosome browser. The common ancestor is still proved with documents.
10. **Test with a purpose.** The oldest living generation carries more of the ancestors' DNA. For the direct male line, Y-DNA of a male descendant; for the direct female line, mtDNA (rarely decisive).
11. **Widen the reach.** Upload the raw data to the databases that still accept files (GEDmatch, FamilyTreeDNA, Living DNA — § 3; MyHeritage has accepted no uploads since 2025); attach a link to your tree to your profile.
12. **Keep a match log:** who, cM, segments, longest, average, threshold, possible degrees of relationship, endogamy yes/no, cluster, side, ancestors' places, surnames, hypothesis, whether you wrote, the reply. Separately: what the DNA refutes and what it allows.

## 6c. Tests on several sites and mixed origin: a worked approach

This is what the analysis looks like when a person has one endogamous grandparent (for example, Ashkenazi) and three Russian peasant lines, and the test sits in four databases. The step-by-step skill: [`dna-matches-across-platforms`](../../../skills/dna-matches-across-platforms/SKILL.md).

1. **Inventory.** One raw file transferred to GEDmatch and FamilyTreeDNA is the same person, but gives different match lists. Find out whose tests you already have access to: on Russian services relatives often share "view results" access.
2. **Separate the endogamous network first** (§ 4): it will fill the top of any list. Apply the Leeds method only to the remaining matches.
3. **Phasing without parents** (§ 6a): the child of a maternal half-sister shows only the mother's side; a cousin through one grandmother shows only that grandmother. "Not among shared matches" does not mean "on the other side": such a relative carries only about a quarter of the DNA in question.
4. **Look for the home village, not only surnames.** Export the whole list together with the "surname — place" fields (many FamilyTreeDNA matches have them) and the places from trees (Genotek). Search for the village and district names in every spelling. A real case: a match of only 38 cM (longest segment 16) turned out to be the key one, because the person's ancestor list had two of the researcher's surnames from the same village. Neither 23andMe nor Genotek showed this.
5. **One family is one piece of evidence.** A match's mother, sister and children with the same ancestor list are one confirmation, not five.
6. **Cross-check between sites.** The same family with a segment of the same length at two companies is almost certainly a real relationship. Look for matches from other sites in GEDmatch by name and source site: there you see the chromosomes and positions.
7. **Triangulation and background.** Segments overlap, and the people also match each other in the same place — this supports one common ancestor. They are related to each other but match you on different chromosomes — that is regional background.
8. **"Are your parents related?"** (GEDmatch): 0 cM means the parents are not related within roughly 5–6 generations. Earlier marriages will show only in metrical records.
9. **Living relatives close at hand.** A parent's social-network page (the "Family" section, maiden names in brackets, "village …, … district") often points to living relatives on the line you need. Read only; who is who is for the family to say, not for guesses.
10. **Paid features.** The FamilyTreeDNA chromosome browser for a transferred kit is now a paid upgrade (the $19 unlock was retired in August 2026). It is worth buying when you already have a lead to check by segments. The free alternative is to ask the match to upload their DNA to GEDmatch.
11. **The letter.** Short, in simple English (B1 level), human: where you found them, how many cM, one shared village, two surnames, "do you speak Russian?", a request to upload their DNA to GEDmatch. Write to the e-mail on the match card; social networks come second.

## 7. Ethics and consent

- **Only the person themselves takes the test**, or their legal representative, with informed consent. The person tested must know who will see the data and what surprises are possible (BCG, code of ethics).
- **A test may show something unexpected** — for example, that the father who raised you is not the biological one. "Everyone has the right to know about their biological family, but no one has a right to a relationship" (FamilySearch, "Ethics and DNA Testing"). Do not pressure those who do not want contact.
- **Do not publish** the data of those who have been tested, and **do not forward other people's match lists** without the owner's consent (BCG).
- **Genetic data concerns all relatives**, and a leak cannot be undone. Protect your account with a strong password (FamilySearch advises changing it every six months). Do not upload DNA data to services with an unclear storage policy — including AI chatbots: "you can't take it back" (K. Borges, RootsTech 2026).

> **How to ask AI**
>
> *For a plain chat, add: "If you can't open a source, say so; mark fonds, villages and dates you name from memory as [from memory, verify]. Answer in English, and give names, places and archive titles in the original script in parentheses." ([why](../1-ai-search/02-prompt-library.md)). The note "(browsing agent)" is for an AI that opens websites itself; the other prompts suit any chat.*
>
> - "Here is a list of my DNA matches [table: total cM, longest segment, number of segments]. Select the ones worth working with under endogamy and explain the thresholds." *Check yourself:* do not upload raw DNA data to a chat; give only the match numbers.
> - "I share [N] cM with a match, longest segment [M] cM. Which degrees of relationship are possible for Ashkenazi Jews? Compare with Lara Diamond's table, not only the Shared cM Project." *Check yourself:* the spread is huge: a cM figure does not name the degree of relationship.
>
> *Bad → good:* "How am I related to a person with [N] cM?" (no longest segment; it will not account for endogamy) → "We share [N] cM, longest segment [M] cM, and we are both Ashkenazi: which degrees of relationship are possible according to Lara Diamond's table?"

---

**See also:** [DNA services](../../catalog/dna-services.md) · [Requests and letters](20-requests-letters.md) · [Standard of proof](../3-results/01-standard-of-proof.md) · [Tree platforms](16-tree-platforms.md)
