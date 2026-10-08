# Press: newspapers in Hebrew, Yiddish and Russian

What this section covers: where to look for old newspapers with advertisements, correspondence from shtetls, donation lists and obituaries — and how to search them when the recognized text is full of errors. Why this is valuable — in [Jewish genealogy](../guide/2-reference/02-jewish-genealogy.md), the section on the Jewish press. Markers are in [README.md](README.md).

---

### NLI — National Library of Israel, Historical Jewish Press (nli.org.il/en/newspapers)
- **What is there:** a multitude of Jewish newspapers, mostly in Hebrew and Yiddish ("Ha-Tsfira", "Ha-Melitz", "Ha-Magid", "Yidishes folksblat", "Forverts" and others). Full-text search of the recognized text. Advertisements, correspondence from shtetls (**donation lists with full names and place of residence**), weddings, obituaries, articles by local authors, annual indexes of correspondents.
- **Access:** Free, no registration.
- **CAPTCHA / limit:** **Cloudflare** ("Checking your browser", then 403) turns on after roughly 100–160 rapid requests per session (October 2026). A human passes the check: ticks the box in an **ordinary tab**; after that the shared cookie lets you work in other tabs too. Do not reload the tab with the check. Work by navigating one page at a time with pauses of 5 seconds or more.
- **Techniques:**
  - Boolean search: parentheses, AND, OR work; the asterisk `*` is too broad and noisy;
  - variants of the surname spelling in Hebrew and Yiddish — all of them (6–7 variants), plus a **group of spellings of the town** joined with AND (Izmail: איזמאיל, איזמאהיל);
  - recognition confuses letters, including final ones (ב is read as כ) — add variants;
  - limit the search by years and by publication;
  - an article can be obtained whole as an image and as text. Make the decision **from the image**; use the recognized text only for searching.
- **Noise:** "sheffel" (шеффель) is a grain measure in price lists of the 1860s–70s; "shefele" (шефеле) — "little sheep"; ataman Shepel in newspapers of 1919–1927; an annual cut by a single surname without a place gives hundreds of irrelevant articles.
- **Experience:** a 1895 correspondence from Letichev about a wedding in Derazhnya — with a donation list naming the father, the matchmaker, the groom's brothers and partners in the timber business; an advertisement and a correspondence from Izmail of 1887, the signature of the author of an 1884 article (analysis — [../examples/case-study-newspaper-to-family.md](../examples/case-study-newspaper-to-family.md)).
- **For advanced users:** the issue and the article are served in XML format with full text (add `&f=XML` to the address); a whole article — through the image of the block (`type=blockimage`). Request XML selectively, not by brute force. Detailed method — the skill `searching-nli-jewish-press` in [../../skills/](../../skills/).

### Russian Empire newspapers — CRL and East View (gpa.eastview.com/crl/irn/)
- 33 titles, 61,887 issues, 824,916 pages, up to 1918; full-text search; open access [checked].

### Yandex "Archive Search" (Poisk po arkhivam) — periodicals (Russian-language)
- "Kommersant" 1909–1917, "Senatskie ob"yavleniya" (Senate announcements), guberniya gazettes, "Vechernyaya Moskva", "Pravda"; about 6 million pages of periodicals. "Kommersant" — provincial chronicle, obituaries, trade news; "Senatskie ob"yavleniya" — auctions, pledges, summonses of heirs with full names and patronymics. In detail — [archive-file-scans.md](archive-file-scans.md).

### Scientific Library of Odesa University, DSpace (rarebook.onu.edu.ua:8081)
- "Odesskie novosti" 1909, 1911–1917 (6,536 issues), "Odesskii listok" 1908–1913, "Izvestiya Odesskogo uchebnogo okruga" 1917. PDF without registration (checked 23.09.2026).
- **Trap:** there is **no text layer** — text search is impossible, read page by page. These newspapers are not in libraria.ua at all.

### RNB: "Gazety v Seti" (Newspapers on the Web) (Russian-language)
- An index of over 5,600 digitized newspapers [from search snippet].

### Genealogy Indexer
- Also searches some newspaper and book collections, including memorial books — see [directories-and-books.md](directories-and-books.md).

### US newspapers
- Chronicling America (Library of Congress) and newspapers.com (paid) — content not verified on the page. Obituaries in American newspapers sometimes name the shtetl; so do announcements of landsmanshaftn societies. See [usa-and-emigration.md](usa-and-emigration.md).

### What was not confirmed
- "Starye gazety" (oldgazette.ru) — the domain does not open (October 2026). A verified replacement — CRL/East View.

---

**See also:** [directories-and-books.md](directories-and-books.md) · [Jewish genealogy](../guide/2-reference/02-jewish-genealogy.md) · [../examples/case-study-newspaper-to-family.md](../examples/case-study-newspaper-to-family.md)
