# AI in genealogy: other people's experience and links

What this section covers: which genealogists work with AI systematically, which rules and ready-made tools (prompts, skills, GPTs) already exist, and what experiments in reading manuscripts have shown. The practical guide is in [AI tools](../guide/1-ai-search/05-ai-tools.md).

The markers in square brackets ([checked], [from search snippet], [unverified] and others) are explained in the [Glossary](../guide/0-start/06-glossary.md). This area changes fast — the dates matter.

---

## People and venues

- **Steve Little** — head of the AI program at the National Genealogical Society (NGS) of the USA. His blog "AI Genealogy Insights" (aigenealogyinsights.com) moved in January 2026 to **VibeGenealogy.ai**: a library of open prompts (including for transcribing manuscripts) and a glossary [checked]. The podcast **The Family History AI Show** (with Mark Thompson). Webinars on Legacy Family Tree Webinars (familytreewebinars.com/speaker/stevelittle; whether paid is not stated) [checked]. At the IAJGS 2024 conference — the talk "AI Genealogy: The Basics and a Bit Beyond" and a set of custom GPTs: Item Identifier, Facts Extractor/Narrator, Photograph Analysis, Lingua Maven [checked].
- **Blaine Bettinger** — the Facebook group "Genealogy and Artificial Intelligence" (about 7,000 members by 2024); articles in APGQ (2023) and New York Researcher (2024); the GRIP course "Practical AI for Genealogists" together with Little (thegeneticgenealogist.com/artificial-intelligence/) [checked].
- **IAJGS AI Virtual Summit** (26.04.2026): more than 500 participants from 25 countries; speakers included Little, Thompson, Marlis Humphrey, Gil Bardige, Alec Ferretti, hosted by Jarrett Ross. Conclusions: AI is good for summaries and translation; talk to it as to "a very smart intern on the first day"; ask it to name its sources; "Do not trust these things. Verify, verify, verify" (iajgs.org/ai-virtual-summit-lessons-in-using-artificial-intelligence-in-jewish-genealogy/) [checked].
- **JewishGen** — a paid course "Advanced AI: Beyond the Prompt" (2026) [checked].
- **Diana Elder, Nicole Elder Dyer** (FamilyLocket) — the book "Research Like a Pro with AI", 2nd ed., 2026: agentic browsers (Claude in Chrome, Perplexity Comet, Chrome Auto Browse, ChatGPT Atlas); the agent opens up branches of a tree and looks for gaps, goes through library catalogs, keeps a log in Google Sheets or Airtable. A privacy warning: "Claude trains on user data by default since September 2025" (familylocket.com/agentic-browsers-and-native-integrations-inside-the-new-edition-of-research-like-a-pro-with-ai/) [checked].

## Principles of responsible AI

- **CRAIGEN — Coalition for Responsible AI in Genealogy** (craigen.org), principles adopted by NGS: Accuracy, Disclosure (of the use of AI), Privacy, Education, Compliance (with rules) [checked].
- **RootsTech 2026** (from a Church News article, 06.03.2026) [checked]: James Tanner — when verifiable data run out, AI "starts to please"; Steve Little — the "water-cooler rule": do not enter sensitive material where the storage policy is unclear; Katherine Borges — do not upload DNA data, you cannot get it back.

## Reading manuscripts: experiments

- **Gemini 3** (the experience of Mark Humphrey, 50 English manuscripts of the 18th–19th centuries): an error of 1.67% by character and 4.42% by word, no invented text was found; but names and place names are worse, and in illegible places the result "floats". Treat it as a draft (aigenealogyinsights.com/2025/12/16/when-the-machine-finally-learned-to-read-gemini-3-and-the-question-of-good-enough/) [checked].
- **A Russian manuscript of 1966** (Louis Kessler, 15.11.2024): ChatGPT ("Genealogy Eyes") and Copilot read the letter correctly on the whole, but **all three models, including Claude 3.5, misread the father's name**; Claude noticed Yiddish influence (beholdgenealogy.com/blog/?p=3917) [checked].
- **A passport of 1864** (pre-reform Cyrillic, Claude): a detailed structured prompt gives much better quality than a short request; the model marked what was unreadable; the rule "never invent text to fill gaps" (jgeppert.com/2026/05/17/ai-transcribing-1864-russian-passport/) [checked].
- **Transkribus** (transkribus.org): 50 free credits a month (about 50 pages); Scholar — €99 a year [checked: transkribus.org/pricing, 2026-10-07]. Russian models [checked: Transkribus blog]: Russian Generic Handwriting 2 (late 19th – early 20th century, 5.8% character error), **Russian Civil Records 1914–1968** (7.3%), Rychkov Archive 1911–1913 (4.4%), Russian Print of the 18th century. Hebrew and Yiddish: the models "The Dybbuk" (handwritten Yiddish), "Pinkas Brody" (a 19th-century community record book), DiJeSt (printed texts in Hebrew type) [from search snippet].
- **Leo** (tryleo.ai) — Latin script only, **does not read Cyrillic** [from search snippet].

## Agents in the browser

- **Claude in Chrome** (support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) [checked]: reads pages, clicks, follows links, fills in forms; a paid plan is needed; Google Chrome on a computer only; for local files — Claude Desktop. According to third-party reviews, the agent makes no purchases, creates no accounts, does not pass CAPTCHAs and uses up limits faster [from search snippet].
- **Gemini in Chrome, "auto browse"** (support.google.com/chrome/answer/16821166) [checked]: Google AI Pro or Ultra, USA only, 18+, device language English; 20 tasks a day on Pro, 200 on Ultra; sensitive actions need confirmation.
- **Perplexity Comet** — free; **ChatGPT Atlas** was closed on 09.08.2026, its functions moved to the ChatGPT desktop app [checked: Wikipedia "ChatGPT Atlas", 2026-10-07]. Agentic browsers are described as vulnerable to hijacking through malicious page text (prompt injection) (nohacks.co/blog/agentic-browser-landscape-2026 — a third-party review, recheck the dates) [checked].

## Ready-made skills, prompts and GPTs

| What | Where | What is inside | Licence, access |
|---|---|---|---|
| **Open-Genealogy** (Steve Little) | github.com/DigitalArchivst/Open-Genealogy [checked] | Genealogical Research Assistant (a skill for Claude), Transcription Helper, Image Analysis, **Hebrew Headstone Helper** (gravestones in Hebrew), Narrative Assistant, GEDCOM Builder, custom GPT configs, scripts for batch transcription | CC-BY-NC-SA 4.0, free |
| **Genealogical Research Assistant** on all platforms | vibegenealogy.ai (the article "The Genealogical Research Assistant — Claude Code / Cowork skill & prompt") [checked] | Custom GPT, Gemini Gem, a ZIP skill for Claude, a prompt to copy; the GPS method: evaluation of source, information, evidence | free |
| **claude-family-history-research-skill** | github.com/emaynard/claude-family-history-research-skill [checked] | research planning, citation of 14+ types of sources after Evidence Explained, analysis of contradictions, templates | MIT |
| **genealogy-research** (sliday) | github.com/sliday/genealogy-research [checked] | a skill for Claude Code, Codex, Gemini CLI: GPS, Obsidian, 80+ databases, separate storage of transcription, transliteration and translation; includes Poland and the Russian Empire | MIT |
| **gedcom-skills** | github.com/vaelen/gedcom-skills [from search snippet] | reading, searching and editing GEDCOM | — |
| Genealogy Research Agent | gist.github.com/peas/ee5b0bcdb54a809b6ddee83caff51ca6 [from search snippet] | a full cycle: OCR, databases, tasks for a human | — |
| **Genealogy Eyes** (custom GPT, Steve Little) | chatgpt.com/g/g-gmIAn5mh6-genealogy-eyes [from search snippet] | analysis of photos and documents | a ChatGPT subscription is needed |

No specialized skill or GPT **for the Jewish genealogy of the Russian Empire** was found as of October 2026; the closest is the Hebrew Headstone Helper. The skills of this repository (checking finds, reading archival scans, the revision "ladder" and others) are in the [list of skills](../../skills/README.md) (in Russian).

---

**See also:** [AI tools](../guide/1-ai-search/05-ai-tools.md) · [genealogists-and-authors.md](genealogists-and-authors.md) · [groups-and-communities.md](groups-and-communities.md)
