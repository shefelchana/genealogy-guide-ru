---
name: surname-variants-cyrillic-cursive
description: >-
  How Jewish surnames mutate between Russian cursive, Ukrainian, Polish, German and Yiddish/Hebrew records — ф/р/т misreadings, е/а/и vowels, an inserted т (-fel → -ftel), -ель/-еръ/-ъ endings, doubled consonants, Hebrew letters with two values, Galician children under the mother's surname, false friends (a trade word in a list, a look-alike German word). Core rule: never exclude a spelling in an agent brief — list it with ⚪ [variant?]; exclude only on other evidence (father, place, age, household, or the same hand writing both forms distinctly), with a same-hand comparison procedure for scans. scripts/variants.py prints the variant list and search regexes. Use when writing a search brief, reading a scan or index where a surname looks different, or re-checking old exclusions. Also triggers on Russian requests: «варианты фамилии», «как ещё могли записать фамилию», «ф или р в скорописи», «та же фамилия?», «отвод по написанию», «одной рукой», «регулярка для фамилии».
---

# Surname variants: cursive, alphabets, false friends

Write project files and reports in the researcher's language unless asked otherwise.

Related skills: `verifying-genealogy-findings` (negative conclusions, Beider–Morse), `reading-archive-scans` (getting a sharp image for the comparison), `reading-galician-jewish-records` (the mother's surname), `tracing-revision-records` (surnames before the 1804/1835 laws), `tracing-emigrants-to-origin` (names at arrival), `orchestrating-genealogy-agents` (briefs and the targets file).

## Why this skill exists
A real pattern from a long project (details changed): search briefs told agents "exclude dissimilar forms: X-tel, X-er, X-fer". The agents obeyed, and the "zero" for whole registry books turned out to be false — those forms had simply not been written out. In one day three earlier exclusions were overturned, and in all three the only argument had been the spelling. Meanwhile the family's own **proven** line was recorded in a dozen forms. With an invented surname Kofel, the pattern looked like this: Кофель, Коферъ, Коферь, Кофаль, Кофиль, Кофтель, Корель (р for ф), Коффель, Кофъ — plus three or four Latin and Hebrew forms.
**Spelling alone is never evidence for or against identity.** It is a search parameter.

## 🔴 The core rule
1. **Never exclude a variant in a brief.** No "do not write out X", no "ignore dissimilar forms". Write: *"Write out every form on the list and anything close to it, marked ⚪ [variant?]. Do not decide identity by spelling."*
2. **List variants, do not rank them away.** Each hit gets ⚪ [variant?] until something other than spelling settles it.
3. **Exclude only on other evidence**, and name it in the record:
   - father's name (patronymic) incompatible with the known person;
   - place (town, estate, registration — *приписка*) incompatible and no move documented;
   - age that does not fit across two or more independent records;
   - household composition (wife, children) that contradicts a known household;
   - **the same hand writes both forms distinctly** in one document (procedure below) — and even then it means "two recorded surnames", not "no kinship".
4. **An etymological argument ("these are different headwords in Beider") is not an exclusion.** It tells you how surnames arose, not what a clerk wrote in a given line.
5. When re-checking old exclusions, search the project files for "not ours / other surname / ruled out / ❌ / 🔴" next to every variant; any exclusion resting only on spelling → back to ⚪.

## The script
`scripts/variants.py` — run it, do not read it. Input in Latin or Cyrillic.
```bash
python3 scripts/variants.py Feigel                 # variants + regexes
python3 scripts/variants.py Фейгель --depth 1      # only single changes
python3 scripts/variants.py Kremer --max 80 --json # for another tool
python3 scripts/test_variants.py                   # self-test
```
It prints four groups (Russian Cyrillic incl. pre-reform -ъ, Ukrainian, Latin in German/Polish/English forms, Yiddish/Hebrew full and defective), each form with ⚪ [variant?] and the rule that produced it, then regexes: `cyrillic_narrow`, `cyrillic_broad`, `latin`, `latin_broad`, `hebrew_yiddish`, and two **OCR forms without the first letter**. Paste the list into the brief; use the regexes on indexes, OCR text and exported tables (`grep -P`, `rg`, Python `re`). Wrap in `\b…\b` when searching running text. Broad regexes over-match on purpose: read every hit, do not count them.
The list is a net, not a dictionary: a form missing from it is not "impossible". Add local forms you see to the project's targets file.

## How a surname mutates — catalogue

### 1. Russian cursive misreadings (by the indexer, by OCR, by you)
| Pair | Why | Check |
|---|---|---|
| **ф ↔ р** | cursive ф has a stroke above and below the line, р only below; a faded or cramped upper loop turns ф into р | compare the upper part with an unambiguous ф/р on the same frame |
| **т ↔ ш ↔ м** | cursive т is written like a Latin m (three strokes) — close to ш, and to м when the first stroke is weak | count the strokes and look for a bar over т |
| **и ↔ н ↔ п** | the connecting stroke's height decides | compare with known и/н/п in the same hand |
| **л ↔ м** | м = л with an extra hook | |
| **е ↔ с**, **ъ ↔ ь ↔ ѣ** | mostly OCR and indexers of printed text | |
| capital letter lost | OCR of pre-1918 print often drops the first letter | search without it (the script gives the regex) |

### 2. Vowels: е / а / и / ей / ай
Clerks wrote what they heard; Yiddish dialects differ in vowels (Polish/Ukrainian Yiddish vs Lithuanian), and a stressed or reduced vowel is written in any of several ways. **Feigel / Faigel / Feigal / Figel** are one family of forms. Hebrew script often omits the vowel altogether.

**Ukrainian catalogues normalise the unstressed vowel.** Archive catalogues transliterated into Ukrainian often change the first-syllable vowel (о/а, е/и): one real test gave 0 hits for one spelling and 1 for the other within the same index. Always run both vowel variants of the root — it is cheaper than phonetic search and catches what phonetics misses (the forms sound alike but are spelled differently).

### 3. An inserted or dropped т: -fel ↔ -ftel
A clerk may "correct" an unfamiliar ending towards a familiar one (a familiar given name, or common -tel surnames), and an indexer may do the same. Treat **X-fel / X-ftel / X-fter** as variants of each other for search, even though etymologists separate them.

### 4. Endings
- **-ель ↔ -ер / -еръ / -ерь**: л/р alternate in clerks' ears and in cursive; a re-check showed that an earlier "-ель in 1816 / -еръ in 1850" example was itself a misreading (no second tail of р on the crop) — so verify such endings against р in a common word of the same frame. A proven case of copyist error is one entry in two copies: "р" in the register, "ф" in the alphabetical index made from it.
- **-ель → -ль, -ел, -елъ** (no soft sign, pre-reform hard sign, syncope).
- **truncated -ъ** in a cramped column or a later hand: "X-фъ" for "X-феръ / X-фель".
- **-ман, -ов, -ский, -ович** derivatives: separate names, but write them out (⚪) — a son-in-law, an adopted relative or a clerk's patronymic can produce them.

### 5. Doubled consonants
German writes ff/ll between vowels (Koffler-type forms), Polish and Russian usually single; Russian records copied from German documents keep фф. Doubling never decides anything.

### 6. Changing alphabets
- **Latin initial**: Sch- (German), Sz- (Polish), Sh- (English, US), S- (careless), Ch- (French clerks).
- **ä, ö, ae, oe** for е; **w ↔ v**, **j ↔ y ↔ i**, **c ↔ ts ↔ tz ↔ z**.
- **German Kurrent and long s (ſ)**: ſ looks like f — "-ſel" may be read "-fel" and vice versa; e/n and u/n are confused.
- **Hebrew/Yiddish letters with two values**: פ = p/f, ב = b/v, ש = s/sh, כ = k/kh; ע marks e in Yiddish and is dropped in Hebrew spelling. A Hebrew form can therefore stand for several Latin surnames: one spelling may be read with p or f, b or v, s or sh — and may belong to a different name entirely. Read the Hebrew column of a metrical record as a second witness, not a tie-breaker.
- **Ukrainian**: и → і, г = h (so Latin H: Hersh/Gersh), Soviet-era Ukrainian civil registers spell differently from the Russian of the same years.

### 7. Not spelling, but a different surname on the same person
- **Galicia: children under the mother's surname.** A couple married only religiously was not married in Austrian law; children were registered as illegitimate under the mother's surname, often with the father acknowledging paternity, sometimes as "A vel B". Brothers may carry different surnames; the US documents of one may use the father's, of the other the mother's. See `reading-galician-jewish-records`.
- **Russian Empire: surname changes across revisions before and soon after the 1804/1835 laws**; families recorded by patronymic only. See `tracing-revision-records`.
- **Arrival in the US**: the surname may be shortened, translated or re-spelled; the given name almost always changes. See `tracing-emigrants-to-origin`.

### 8. False friends — write them out, then rule them out on evidence
- **Polish trade words in a "surname" column**: *szewc* (shoemaker), *krawiec* (tailor), *piekarz* (baker), *rzeźnik* (butcher), *kuśnierz* (furrier), *kantor*. In late-18th-century Galician lists Jews were often recorded by patronymic or trade; a phonetic index may match an odd spelling of such a trade word to a similar-sounding surname. Look at the neighbouring entries: if they are trades, this one is a trade.
- **German words and look-alike surnames**: a common noun that is also a surname (for example *Spiegel*, "mirror") vs a similar-sounding surname; such a family is excluded only after its own documents (wives' maiden names, fathers, towns) show no link — not because "it is a different word".
- **Same skeleton, different root**: a neighbour in the same town with a similar surname is not proof of a variant (check the Beider–Morse index, see `verifying-genealogy-findings`) — and not proof of a different family either.


## Same-hand comparison — procedure for scans
Use it when a disputed form (e.g. -ферь vs -фель, ф vs р, with or without т) decides whether a line is "ours".
1. **Establish the hand.** Same page or adjacent frames; same ink and pen width; same forms of capitals, numerals and the final ъ. Several hands in one file (a December addendum, a clean copy, a later correction) are common — note which hand wrote the line.
2. **Collect controls from the same hand and frame**: 3–5 words where the disputed letter is certain (a ф in a common word or another surname; р in "мѣщанинъ", "рожденія"; т in "сынъ Мошковъ"-type lines; the ending of other -ель/-еръ surnames). Crop each.
3. **Compare glyph by glyph**: upper loop of ф, bar of т, number of strokes, joining stroke height, the ending's last letter (ь vs ъ vs р). Write what you see, not what you expect.
4. **Read the second copy.** Metrical books often exist in two copies (parish and consistory), revision lists in draft and clean copy, many records have an alphabetical index and a Hebrew column. Read every copy that exists before ruling. (In one case the second copy settled ф where the first looked like р.)
5. **Conclude in one of three ways**:
   - the disputed letter matches the controls of form A → read as A (🟢 if clear, 🟡 if partly);
   - **the same hand writes A and B distinctly in different lines** → the file records two surnames; a slip is unlikely, kinship not excluded (⚪);
   - **the same household in different documents/hands appears as A and B** → variants of one surname for this family.
6. **Record**: crop paths of the disputed word and of each control, "same hand / different hand", the verdict and its level. Keep the crops (below).

## Keeping the evidence
- **Never delete surname-column crops.** Keep them under a per-reference folder (e.g. `crops/<reference>/` in the project) and log the reference in the read-sources journal, so a later re-check needs no re-download.
- Keep a **targets file** with every form of every target surname and the false friends; give it to every agent and read each source once for all targets.
- In the finding format the verbatim quotation keeps the original spelling letter by letter; uncertain letters in `[brackets?]`.

## Brief lines to paste
```
Surname variants: <list from variants.py>. Write out EVERY form on the list and anything close to it,
marked ⚪ [variant?]. Exclude nothing by spelling. Exclusion only by father, place, age,
household or a same-hand comparison (crops of the disputed word and of the controls).
Save crops of the surname column to crops/<reference>/.
```
For a Russian-language project:
```
Варианты фамилии: <список из variants.py>. Выписывать ВСЕ формы из списка и близкие к ним
с пометой ⚪ [вариант?]. Ничего не отводить по написанию. Отвод — только по отцу, месту,
возрасту, составу семьи или сверке «одной рукой» (кропы спорного слова и контролей).
Вырезки колонки фамилий сохранить в crops/<шифр>/.
```

## Checklist before saying "not the same surname"
- [ ] Is there a reason other than spelling? Which one, with reference and frame?
- [ ] Were all copies (second copy, index, Hebrew column) read?
- [ ] Same-hand comparison done, crops saved?
- [ ] Was the exclusion written as ⚪/🟡 with the reason, not as "not ours"?
