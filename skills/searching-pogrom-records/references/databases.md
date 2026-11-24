# Pogrom databases: query recipes and field explanations

Checked with queries on 07.10.2026. Sites change: repeat the control query before any mass work.

## 1. jewishpogroms.info — Nadia Lipes's database

**What it is.** "Jewish Pogroms Memorial", about 77,777 records (the counter on the home page). The sources are only archival documents and memorial sheets. The database holds the killed, the wounded, the robbed, refugees, **recipients of relief** (for example "people who get financial help from America (… zemlyachestvo)", with the sum in the note, "100 $"), **orphanage pupils** ("Pupil of the 3rd orphanage"), staff of children's institutions.

**The form on the site.** The surname field accepts only Latin letters; a "Sounds like" checkbox; drop-down lists Region, City, Record type, Incident, Notes, Found, Register, Case, Archive, Is Alive. A city can be chosen without a surname.

**A query without a browser** (the same one the page sends):

```
curl -s -A "GenealogyGuideTool/1.0 (personal family research)" \
  -X POST https://jewishpogroms.info/wp-admin/admin-ajax.php \
  --data-urlencode "action=pogroms_search" \
  --data-urlencode "family_name=Rabin*" \
  [--data-urlencode "soundslike=yes"] [--data-urlencode "city=Pavoloch"]
```

The answer is an HTML fragment: a line `NN persons found`, then a table. The script `scripts/pogrom_search.py lipes …` does the same and prints TSV.

**How the search behaves** (checked on the control surname):

| Query | Result | Conclusion |
|---|---|---|
| `Lipes`, no checkbox | 24 records (incl. "Lipes/Libes ?") | the exact search also catches compound records |
| `Lipes`, soundslike=yes | 23 | "Sounds like" is not a superset of the exact search |
| `Libes`, soundslike=yes | 8, only Libes | "Sounds like" does not merge B/P |
| `Lip*s` | 49: Lipes, Lipets, Lipshits, Lips, Lipis… | the asterisk is the main tool |
| `city=Pavoloch`, surname empty | 131 | a search by place without a surname works |

Order: exact query → with an asterisk in the middle and at the start → soundslike → by city. Every query is a line in the log.

**Record fields → archival reference**

| Field | Meaning |
|---|---|
| Region / City | guberniya or oblast / shtetl (in Latin letters, as the volunteer entered it) |
| Record type | `list` — a name-by-name list, `text` — a mention in a text |
| Family name / Name / Patronymic / Age | as in the document, in Latin transliteration |
| Incident | what happened: murdered, wounded, robbed, refugee, relief, orphanage |
| Is Alive | yes / no / empty |
| Notes | details: killed by whom, when, where from, sum of relief, "child" |
| **Found / Register / Case / Page** | **fond / inventory / file / folio** |
| Archive | Dako (DAKO), State archive of Vinnytsia region (DAViO), DAOO (Odesa), TsDAVO, etc. |

A link to an individual record (`/pogroms_people/pogroms-post/?id=…`) shows no content without a browser [checked: the page is empty for curl] — take the data from the answer table.

⚠️ The data was entered by volunteers: shifted columns are visible in the drop-down lists (a city name in the "Region" field, a given name in the "Is Alive" field). Check the file and folio number against the inventory and the scan. An example of a discrepancy: a 1922 relief record for a shtetl refers to a file that the inventory names as correspondence with the committee of another city — so either the list is filed into someone else's file or the database has a typo; only the folio decides.

## 2. pogrom.amhazikaron.org — Am HaZikaron

**What it is.** A memorial project: about 7,929 victims (the `X-WP-Total` header without filters), 136 shtetl categories (`categories`, checked 08.10.2026) and 118 pages about shtetls (`/wp-json/wp/v2/mestechki`). Sources in each record: E. D. Rosenthal's "Свиток резни" ("Svitok rezni", the Scroll of Slaughter; Russian translation), DAKO R-3050 (State Archive of Kyiv Oblast; with folios **and PDF pages**), TsDAVO fond 2497 (Central State Archive of Supreme Bodies of Power of Ukraine), YIVO RG 80 (the Tcherikower archive), TsDIAK fond 1164 inventory 1 file 171 (Central State Historical Archive of Ukraine, Kyiv; a metrical book of Kyiv — deaths of 1918), S. Weigman's "Кадиш сироты" ("Kadish sirot", Orphan's Kaddish; Kyiv), the Proskurov lists with addresses. About a third of the project's documents are in Yiddish.

**Query** (open WordPress REST, honest tool User-Agent):

```
https://pogrom.amhazikaron.org/wp-json/wp/v2/victims?search=Фастов&per_page=100&page=1
```

- The number found is in the response headers `X-WP-Total`, `X-WP-TotalPages`.
- The search is by substring in the title and text of the record, in Cyrillic.
- Shtetl categories: `/wp-json/wp/v2/categories?per_page=100` (the `count` field), records of a category: `victims?categories=ID`.
- The text of the record is `content.rendered`: circumstances, occupation, place of origin, sources.

Script: `scripts/pogrom_search.py amh Фастов [--all]`.

⚠️ One record is often a whole family in one title ("Yohanan …, his wife …, their daughter …, her husband …"): search by the surname of each family member, by given names and by shtetl. Age "by different lists" is given with "or" — this is an honest note of a discrepancy; carry it into the dossier as it is.

⚠️ An empty answer does not mean "Rosenthal does not have him": the database does not cover the "Svitok rezni" in full.

## 3. What is not openly available

- lipesdatabase.com: there is no public search at present; the internal database is a paid service (as of October 2026).
- "Книга погромов" ("Kniga pogromov", The Book of Pogroms; a collection of documents) and "Khurbn Proskurov" (1924) are books; you can search them for a surname only in full-text copies, if they exist (see `verifying-genealogy-findings`, full-text corpora) [unverified].
