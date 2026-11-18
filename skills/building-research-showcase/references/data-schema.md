# Showcase data schema

Every key is optional: a section is drawn only if it has data. Text fields are plain text; `**bold**` and `*italic*` are allowed. Do not insert HTML. A full example is `assets/example-shapiro.json` (Russian data, `"lang": "ru"`).

Levels: `🟢` proven by a document, `🟡` likely, with a gap, `⚪` unresolved, `💭` version / family memory, `🔴` disproved, `"zero"` — zero with coverage (source catalogue only).

## Shared (the coordinator's file `00-meta.json`)

```json
{
  "lang": "en",                       // "ru" or "en" — interface language
  "title": "Research showcase: …",
  "description": "one sentence for search engines",
  "kicker": "line above the title",
  "lead": "paragraph under the title",
  "banner": "notice: teaching example / for the family only",
  "footer": "bottom line",
  "lines": [{"id": "a", "name": "Shapiro"}],       // up to 5; colours in order: blue, orange, teal, violet, pink
  "sections": {"sources": {"h": "own heading", "p": "own intro", "aside": [{"h": "Where to make it", "text": "…"}]}}
}
```
`sections` is optional: override a heading or intro and add "aside" boxes under a section. Section names: `methods, sources, people, profile, tree, map, dna, comparisons, story, surnames, library`.

## Catalogues (`building-research-catalogs`)

```json
"sources": [{"ref": "DAZhO 67-3-220", "year": 1899, "type": "vital records", "who": "Naum Itskovich",
             "gave": "born in Berdychiv; mother \"Khaya\"", "level": "🟢", "line": "a"}],
"people":  [{"name": "Naum Itskovich Shapiro", "years": "1899–1966", "role": "Berdychiv → Moscow · great-grandfather",
             "line": "a", "level": "🟢", "initials": "NS"}],      // level — level of the key link
"profile": {"name": "…", "initials": "NS", "kicker": "Great-grandfather · Shapiro line",
            "facts": [["Born", "1899, Berdychiv 🟢"]],
            "timeline": [{"year": "1899", "text": "…", "source": "reference", "level": "🟢"}],
            "family": [{"name": "Itsko Leibovich", "note": "father"}],
            "sources": [{"tag": "DAZhO", "text": "67-3-220 — birth record", "level": "🟢"}],
            "questions": [{"text": "…", "level": "🟡"}]},
"library": {"tree": "multi-line folder scheme", "naming": "file-naming rule",
            "example": "example name", "card": [["reference", "…"], ["status", "…"]]}
```
`type` — short, repeated words (the filter uses them): vital records, revisions, censuses, civil registry, war, evacuation, directories, court and registers.

## Tree and places (`rendering-family-tree`)

```json
"pedigree": {"generations": [
   [{"name": "Maria", "sub": "SHAPIRO · 1991", "line": "none"}],
   [{"name": "father", "sub": "…", "line": "a"}, {"name": "mother", "sub": "…", "line": "c"}],
   [ …4… ], [ …8… ]]},                 // Ahnentafel: in generation g positions 2i and 2i+1 are the father and mother of person i; null = "?"
"ladder": {"title": "Ladder of the … line", "steps": [{"name": "…", "note": "years · document", "level": "🟢"}], "aside": "text on the right"},
"places": {"ber": {"name": "Berdychiv", "lat": 49.9, "lon": 28.6, "info": "who and when", "label": "l", "dy": 10}},
"routes": [{"line": "a", "path": ["ber", "zhi", "ode"], "bend": -0.24}],     // bend: arc curvature, the sign picks the side
"offmap": "↘ Tashkent (evacuation) — off the diagram"
```
The first 4 generations are drawn. `label: "l"` puts the label left of the point; `dy` moves it vertically.

## Evidence (`building-evidence-matrix`)

```json
"cycle":   [{"title": "Question", "text": "…"}],          // the 7 steps of one pass
"methods": [{"title": "Zero with coverage", "note": "what it is", "example": "example from the project"}],
"comparisons": [{"title": "Naum's mother", "columns": ["Name", "Source", "Weight"],
                 "rows": [["Khaya", "birth record 1899", "🟢 recorded at the event"]],
                 "verdict": "Likely 🟡: …", "wide": false}]
```

## DNA (`checking-dna-against-tree`)

```json
"dna": {"caption": "who tested, company, model date",
        "bars": [{"name": "Eastern European", "value": 46.3, "line": "e", "expected": 50, "sd": 4.7, "alt": 75}],
        "verdict": "question, expectation, result, conclusion with a level, caveats", "scale": 80}
```
`expected` and `sd` — expectation from documents and its spread; `alt` — expectation if the legend is true; `scale` — right end of the scale (computed automatically by default).

## Stories and surname

```json
"story": {"kicker": "Story · … line", "title": "…",
          "photos": [{"initials": "PS", "caption": "who, ~year, who identified"}],
          "chapters": [{"when": "Spring 1942 🟢", "text": "what and how it is known"}],
          "quote": {"text": "\"family saying\"", "note": "💭 — how to check"}, "quoteAfter": 1},
"surnames": [{"title": "Certificate of surname origin", "name": "Shapiro", "native": "שפירא",
              "cols": [{"h": "Meaning", "text": "…"}, {"h": "What does not follow", "text": "…"}], "foot": "after the dictionary of …"}]
```
