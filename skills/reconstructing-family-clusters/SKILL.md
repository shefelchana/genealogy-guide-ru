---
name: reconstructing-family-clusters
description: "Turns a single find, a father with his children, into a whole-family reconstruction, then joins same-surname families into one tree. Establishes estate and registration (listed where versus lived where), the guberniya and uezd for that year, and occupation, then builds a matrix of documents that must exist for such a family (revision lists bridged by ages, 1874–75 family and draft lists, 1897 census, metrical books of every surviving year, notarial, court, press, directories, Soviet, Holocaust, emigration) and a per-family package of have, missing and where to look. Weighs kinship signals between families and grades each link as document, strong version or hypothesis. Use whenever the user found a parent and children, wants to reconstruct the whole family, merge same-surname families into one tree, asks whether this is one family or different ones, asks for a document package, \"family reconstruction\" or \"cluster research\", or has many unconnected families of one surname, even if they ask only about one person. Also triggers on Russian requests: «нашёл отца и детей», «собрать всю семью», «свести однофамильцев в одно дерево», «это одна семья или разные», «пакет документов»."
---

# You found a family: reconstruct it whole, then join the families into one tree

## When to use

- You have found a record that shows a father and children (a revision list, a family list, a census, a run of metrical records).
- The project has accumulated several families of one surname with no proven links.
- The user asks about one person, but the documents about him lie in the files of brothers, sisters and brothers-in-law.

A single find does not connect branches. A family reconstructed as a package gives the ages of all the children, the place of registration, the occupation, the witnesses, and it is by these that kinship with other families becomes visible. So work from the **list of documents that must exist**, not from find to find.

## Order of work

### Step 1. The anchor

Write down what was found verbatim, with the archival reference, frame and standard-of-proof level: head, wife, children, ages, family number, estate, society. This is the anchor; everything else is checked against it.

### Step 2. Who this family is in the imperial system

1. **Estate** (*soslovie*): meshchane (townspeople), merchants (guild), guild artisans (*tsekhovye*), agricultural colonists, honorary citizens, peasants. Estate is a status, not an origin: a family moves from meshchane to merchants and back.
2. **Registration and residence.** Where they were listed (the society under which the revisions and the draft were conducted) and where they lived (where the children are born, where the 1897 census, directories and courts are). These are two different archival addresses. Write down both.
3. **The region for that year**: the guberniya and uezd for the year of the document; borders and jurisdiction changed. Skill `identifying-places`.
4. **Occupation and way of life**: timber and leases, a mill, trade, a craft (guild), medicine, service at the rabbinate, carting. The occupation determines which directories, courts, notaries and press to use.

### Step 3. The matrix of required documents

For this family compile a list of document types by year: which ones **should** have been created, where they are kept and whether they survive. The detailed matrix by period, estate and occupation is in `references/document-matrix.md`. The minimum:

- revision lists bridged by ages (each step separately, by place of registration): `tracing-revision-records`;
- family and draft lists of 1874-1875 (for Jews, the military census of 1875 with the family number according to 1858);
- the 1897 census, by place of residence;
- metrical books for **all surviving years**, not only the "right" one: infants who died, marriages of the children, deaths of the parents;
- notarial deeds, courts, press, directories; recruit lists (before 1874);
- Soviet documents, the Holocaust, evacuation, emigration.

### Step 4. The document package for the family

Start a card from the template `assets/family-card.md`. One line per document type: **have** (reference, frame) / **no, searched** (where, with which forms, coverage) / **not preserved** (how confirmed) / **not searched, where to look**. Before paging through each file, check the indexes and the registry of unread sections (skill `using-community-surname-indexes`).

An absence where a record **must** be is negative evidence (died, fled, transferred, registered elsewhere). Record it as a result, not as an empty search.

### Step 5. Go down the list

One family at a time, line by line of the card, from cheap (indexes, full text) to expensive (reading every page). Check each child found as a separate person: his marriage, his children, his Soviet life. When working with agents: one file per agent, one site per worker (`orchestrating-genealogy-agents`).

If the shtetl of registration holds few traces, look at **the records of the large city** where people moved: the full extracts of the 1906 Lodz metrical records (about 5,500 records) name 884 other places of birth or residence (JRI-Poland, an article by S. Diamond in Avotaynu, 2018) [from search results]. Such records point to the shtetl of origin.

### Step 6. Join the families into one tree

When two or more families of one surname have been assembled, look for links between them using the signals in `references/kinship-signals.md`: a shared place of registration, transfers between societies, names given in memory of the dead, double names and different patronymics among the children, a clerk's unique error, witnesses and guarantors, a shared business, a matching **set** of names across two or three generations.

Enter each link in the table `assets/family-links-table.md` with a status (the guide's single scale: `guide/3-результат/01-доказательность.md`, section 4a; English: `en/guide/3-results/01-standard-of-proof.md` § 4a):

| Status | What is needed |
|---|---|
| 🟢 **Confirmed** | a record that directly names the kinship (son, brother, widow), or an age bridge between revisions, plus a second independent feature (matching family composition and the like) |
| 🟡 **Open / strong version** | two or more independent indirect features, no contradictions; set out with a written rationale |
| ⚪ **Unchecked / weak** | one feature (surname + place, matching name and patronymic, an index line) |
| 🔴 **Withdrawn** | refuted; record the reason |

## Traps

- **Namesakes whose surname is a place name or an occupation** are by default not relatives: such surnames arose independently in different places.
- **The area of a surname** should be judged from the earliest lists with surnames, namely the additional lists of the 5th revision (1805-1808) and the revisions of 1811 and 1816 (Jews usually have no surnames yet in the 1795 lists), not from lists of the early 20th century: by the 1900s families had scattered.
- **Children of one head of household may be by different wives**: a big gap in the children's ages or a different mother's name in a metrical record is a reason to look for a second marriage, not a second family. Divorce among Jews in the first half of the 19th century was frequent (C. Freeze) [from search results].
- **Age "floats"** by 2-5 years between documents; the draft age of sons was altered on purpose, and brides were made "older". Compare intervals and the order of the children, not the exact year.
- **The family number is not carried over between revisions.** A link is given only by an age bridge, matching family composition or the clerk's explicit reference ("by the revision of 1858 No. ...").
- **Namesakes "uncle and nephew"** of similar age, because of the custom of naming after the dead: it is easy to confuse the generations.
- **Different patronymics among siblings** are normal with a father's double name or a change of name during life; they do not disprove kinship.
- **A match in one index reprinted in several places** is one piece of evidence, not several.

## What counts as a find

- For a family: the anchor is confirmed from the scan, and for each required document type there is a status (have / no, with coverage / not preserved).
- For a link between families: status 🟢 or 🟡 with a written rationale. Only 🟢 goes into a publicly available tree; into a personal working tree 🟡 with the note "version"; ⚪ only in the hypotheses file. The decision about kinship and edits to the tree belong to the person.

## If nothing was found

1. Check whether you are searching at the right archival address: registration or residence; the uezd for that year; neighbouring societies and uezds.
2. Widen the years: all surviving years of metrical books, all revisions, not only the "right" one.
3. Search through the circle: brothers, brothers-in-law, witnesses, business partners (the FAN principle: friends, associates, neighbours).
4. Leave the empty and unpreserved lines in the card: they show that the link is not yet proven and stop a hypothesis from being passed off as fact.

## See also

`verifying-genealogy-findings` · `tracing-revision-records` · `using-community-surname-indexes` · `searching-pogrom-records` · `identifying-places` · `soviet-era-records` · `tracing-emigrants-to-origin` · `dna-matches-endogamy` · `search-logic-navigator` · `orchestrating-genealogy-agents` · `writing-family-history`
