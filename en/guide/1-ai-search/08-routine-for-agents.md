# Hand the routine to agents: trees, sites, files

What this section covers: what an AI agent can do for you besides searching. It draws trees and diagrams, fills in profiles on sites, downloads and sorts materials, uploads them, and cross-checks different places where data is stored. All of this comes from the experience of one project (2026); your details may differ.

The main rule: **the agent works with its hands, you decide.** You log in to accounts and pass CAPTCHAs yourself. The agent makes every edit in a tree that others can see only after your "yes".

---

## 1. Trees and diagrams as illustrations

The agent draws a tree straight from your files (persons, dossier) — no need to carry people over by hand.

| What | How | Where it is useful |
|---|---|---|
| A diagram of a branch | Mermaid in Markdown (GitHub and many editors draw it themselves), Graphviz, SVG | in the dossier file, in a story for relatives |
| A web page with a tree | HTML with expandable branches | share a link without giving access to the tree site |
| A timeline and a map of moves | a table by year, a map with points and arrows | see gaps and "jumps" |
| A diagram of a "disputed" person | the person in the centre, branches are sources and what each says | sort out contradictions |

🔑 **Show the degree of proof on the diagram.** For example, a solid line — 🟢 confirmed, a dashed line — 🟡 version, grey — ⚪ unverified. Otherwise a beautiful picture looks more proven than it is and will be copied as fact.

A diagram is an illustration, not a database. Keep the data in your files and in GEDCOM, and rebuild the diagram from them.

## 2. GEDCOM — moving a tree

- The agent assembles a GEDCOM from your files for import to a platform or a program.
- It checks someone else's or your own GEDCOM: duplicates, impossible dates (a mother younger than 12, a child after the father's death), different spellings of one person.
- It compares two exports: who is in one and not in the other.
More on formats and platforms — [Tree platforms](../2-reference/16-tree-platforms.md).

## 3. Filling in profiles on sites

The agent in your browser (for example, Claude in Chrome) opens your tree site and enters: dates and places, biographies with references to archival references, source citations with a level of reliability; adds people and re-attaches parents.

From experience (MyHeritage, September 2026):
- The text editor often does not notice text inserted by a program: without a "live" key press the save silently fails. **Check every save by re-reading the profile.**
- Long text typed "from the keyboard" sometimes loses spaces — type it in parts.
- The plan limits the number of people in the tree, and the biography field its length (about 2,300 characters in our case). Check the limits before mass work.
- Changing a parent can by mistake make them "adoptive" — check the type of relationship after the edit.
- If you yourself work in the same tab, it is better for the agent to open its own.

## 4. Download, assemble, sort

- Download the whole file, not a preview; cut out the lines needed (crops), label them with the archival reference and frame.
- Sort into folders and rename by a single rule ([Keeping files](../0-start/02-keeping-files.md)).
- Assemble a report for a relative: a PDF or a page with crops of documents, archival references and links.
- Keep a log: what was downloaded, from where, when.

## 5. Upload and keep copies

- Upload documents and photographs to profiles (MyHeritage, FamilySearch Memories, WikiTree), to the cloud or to a repository.
- 🔴 **The site is the second copy, not the only one.** Services change their plans, close down, get blocked in particular countries. The main copy is with you: files and GEDCOM, plus a backup somewhere else.

## 6. Cross-check different places of storage

When a tree lives in several places (your files, MyHeritage, FamilySearch, Geni), they drift apart. The agent:
1. exports or reads each place;
2. makes a table of discrepancies: who is in only one place, where dates, names, parents differ;
3. for each discrepancy finds which document is right, from your files;
4. proposes a list of edits, and makes them after your "yes".

The source of truth is your files with documents. The site is brought into line with them, not the other way round.

## 7. Regular checks

- New digitisations for your shtetls (Wikimedia Commons, archive catalogues, FamilySearch).
- Going through the spellings of a surname in all databases once every few months: databases grow.
- DNA matches: new relatives with your shtetls in their trees.

## Limits and safety

- **Passwords, login, CAPTCHAs, payment — only you.** The agent does not create accounts and does not enter passwords.
- **Site rules.** Many sites forbid robots and mass download. Read the terms; work at a human pace; do not download whole databases.
- **Shared trees** (Geni, WikiTree, FamilySearch Family Tree) are edited by other people, and everyone sees your edits. Only 🟢 goes there, and only after your review.
- **Living people.** Do not post documents and data of living people without their consent.
- **Messages and publications** — letters to researchers, posts, joining groups — you send.
- The agent can miss a click or "see" a save that did not happen: ask it to check the result by re-reading and to write in the report what was checked.

> **How to ask AI**
>
> *For a plain chat, add: "If you can't open a source, say so; mark fonds, villages and dates you name from memory as [from memory, verify]. Answer in English, and give names, places and archive titles in the original script in parentheses." ([why](02-prompt-library.md)). The label (agent with a browser) is for an AI that opens websites itself; the other prompts suit any chat.*
>
> - "Here are my persons and dossier files. Draw the tree of the branch [name] in Mermaid: a solid line — 🟢, dashed — 🟡, ⚪ in grey. Do not add people who are not in the files."
> - *(agent with a browser)* "Cross-check the tree on [site] with my files: a table of discrepancies (person, field, on the site, in the files, which document is right). Change nothing until I reply."
>
> *Bad → good:* "Draw my family tree" (it will draw from memory and will not tell a guess from the proven) → "Draw the tree of the branch [name] only from my files [files]; 🟡 versions dashed."

---

**See also:** [Working with agents](03-working-with-agents.md) · [AI tools](05-ai-tools.md) · [Tree platforms](../2-reference/16-tree-platforms.md) · [Ethics and preservation](../3-results/03-ethics-preservation.md)
