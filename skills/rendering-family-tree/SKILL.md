---
name: rendering-family-tree
description: "Draws a family tree from a project's persons file: a pedigree chart in Ahnentafel order (colour = line, unknown ancestors as \"?\", each link with its level of evidence), a \"ladder\" of one direct line with the document behind each step, and places and routes for a migration map with real coordinates and period place names. A bundled script renders a standalone SVG or HTML page; the same data feeds the showcase. Use when the user asks to draw, show or print the tree, a pedigree, a poster for relatives, a map of family moves, or to see which ancestors are still unknown. Not for building the tree on MyHeritage or Geni, not for the full showcase page (use building-research-showcase), not for disputed parentage (use building-evidence-matrix). Also triggers on Russian requests: «нарисуй дерево», «родословная таблица», «дерево для родных распечатать», «лестница одной линии», «карта перемещений семьи», «где у нас дыры в дереве»."
---

# Tree and migration map

In research a tree is a **picture of what is proven**, not a place for guesses. So every link has its own level, unknowns stay "?", and legends are dashed or left out.

## 1. Pedigree chart

- The root is the researcher (or the person whose tree is shown). Then Ahnentafel order: in generation g, positions 2i and 2i+1 are the father and mother of person i of the previous generation. The father is always above the mother.
- A two-line label: the name (as in documents, with a variant: "Naum (Nokhem)") and "SURNAME · years"; for women the maiden name if known, otherwise "maiden name ?".
- **An unknown ancestor is `null` ("?")**, not a name from a story. A name known only from family memory gets 💭 in the name.
- Colour = line (the direct male surname line or as agreed with the researcher). At most five lines; the colours are fixed and checked for distinguishability.
- Living people in a public version — without dates or without names at all ("mother", "father"), unless they agreed.

How many generations: 4 are readable on screen, 5 is already a poster. Deeper — a ladder or a fan chart in a program (Gramps, MyHeritage).

## 2. Ladder of one line

For the deepest proven line: step by step from the earliest ancestor to the researcher. Each step has years, place, **the document that links it to the next one** and a level. It is the best way to show what the pedigree rests on: the reader sees where a link is proven by a birth record and where only by a revision age.

## 3. Places and routes

- The name **as it was in that year** (Ekaterinoslav, not Dnipro, for 1900), coordinates from a reference (Wikipedia, GeoNames, JewishGen Communities). Check same-name villages by uezd and volost — the guide's "Places and maps" section.
- In `info` — who was there and when, with years.
- A route follows the years, one per line. Evacuations and emigrations that go off the edge of the diagram go into the `offmap` line.
- After building, look: if an arc passes through someone else's point, change the sign or size of `bend`; if labels overlap — `label: "l"` (left) and `dy`.

## 4. How to draw it

```bash
python3 scripts/render_tree.py tree.json tree.html   # page, light and dark theme
python3 scripts/render_tree.py tree.json tree.svg    # plain SVG for print or a document
```
The `tree.json` format is at the top of the script (the same keys as the showcase: `lines`, `pedigree`, `ladder`). For the map use the showcase (`building-research-showcase`): places and routes are drawn there together with the other sections.

## 5. Check

- Every person in the picture is in the persons file, and no link has a higher level than there.
- No ancestor is "filled in from a story" without 💭.
- Women are labelled with maiden names or "?".
- If you send it to someone — remove living people.
