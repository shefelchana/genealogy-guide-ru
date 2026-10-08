# Access to Websites: Registration, Captchas, Pace, Restrictions

What this section covers: where registration is needed, where websites protect themselves against frequent requests, and how to work so that you are not blocked. The figures come from the experience of one study (September–October 2026); websites change their rules, so a date is given everywhere.

---

## 1. Where registration is needed (free)

| Site | What you get without logging in | What you get after logging in |
|---|---|---|
| **JewishGen** | you can see **how many** records were found in each database | the records themselves, JOWBR, JGFF, ViewMate. Login passes a Cloudflare check; the session lasts about a day |
| **FamilySearch** | almost nothing (as of October 2026 — only the 1950 US census) | search of records, films; some images are available **only at FamilySearch centers** |
| **MyHeritage** | — | a tree (free up to 250 people), the list of hints |
| **JRI-Poland** | the old form `legacy.jri-poland.org` shows everything after you accept the terms (personal research only; when citing, refer to JRI-Poland) | the new search |
| **j-roots.info** (the Jewish Roots forum, Еврейские корни; Russian-language) | threads can be read | forum search, the databases "Archival references" (*Arkhivnye ssylki*) and "Stone archive" (*Kamennyi arkhiv*) |
| **Raduraksti** (Latvia), **GenTeam** (Austria), **Rahvusarhiiv** (Estonia), **pra.in.ua**, **IGRA** | — | search of the databases |

These work without registration: Yad Vashem, USHMM, "Open List" (*Otkrytyi spisok*), OBD Memorial, "Pamyat naroda" ("People's Memory"), Wikimedia Commons, archive.org, Yandex "Archive Search" (*Poisk po arkhivam*), NLI (National Library of Israel), Genealogy Indexer, Mitzvat Emet, Toldot.

## 2. Captchas and protection against frequent requests

| Site | What happens | When (from experience) |
|---|---|---|
| **FamilySearch** | an hCaptcha check; on very fast loading — a freeze and a 429 "overload" error | after roughly **~45 to ~150 images opened (most often about 130 in 40 minutes; earlier over time)**; 1,052 images in 4 minutes — an immediate block (October 2026) |
| **NLI** (Jewish newspapers) | Cloudflare: "Checking your browser", then 403 | after roughly **100–160 requests** per session (October 2026) |
| **Mitzvat Emet** | reCAPTCHA; the form **silently** stops submitting and shows no errors | after roughly **5 searches** |
| **Yandex "Archive Search"** | dropped connections, "Failed to fetch" | after roughly **25 rapid requests** in a row |
| **"Open List"** | Cloudflare, error 429 | after **three** rapid requests |
| **"Pamyat naroda"** | a "security check", error 401 | on automated requests |
| **Geni** | hCaptcha on profile pages | always, for automated reading |
| **HathiTrust**, **Google Books** (programmatic access) | 403 / quota exhausted (429) | on automated requests; by hand in an ordinary browser they work |

## 3. Rules of work

1. **A human passes the captcha, and only a human.** At the first "you are not a robot" check, stop, pass it yourself in an ordinary browser window and continue more slowly. Do not bypass captchas, do not borrow other people's IP addresses, do not use workarounds for blocks.
2. **Pace matters more than speed.** Almost everywhere it was not prohibitions that stopped the work but requests that were too frequent.
   - FamilySearch: no more often than **one image every 5–10 seconds** (even at 10–12 seconds a captcha appeared after about 130 images — take breaks); **one thread — one worker per site**; **do not download a whole film**.
   - Yandex "Archive Search": **one request every 8–9 seconds**.
   - NLI: navigate one page at a time, a pause of at least 5 seconds.
   - Mitzvat Emet: **one search per visit**.
   - "Open List": a pause of at least 6 seconds.
3. **One site — one worker.** Do not run several parallel searches (or helpers) on one site: all of them will get captchas. This is what happened on FamilySearch: three agents in parallel plus one that pulled 1,052 images in 4 minutes — all of them got captchas (October 2026).
4. **Verification in the same tab.** On NLI the checkbox is ticked in an ordinary tab; after that the shared cookie lets you work in the others too. Do not reload the tab with the check. On FamilySearch in October 2026 the check appeared on every load until the account owner logged in right in that same tab.
5. **Passwords, cookies and keys — to no one and nowhere.** Do not paste them into chats, scripts, letters. For a helper (a person or a program) it is enough that you yourself have logged in to the account in your own browser.
6. **Do not enter passwords on dubious sites.**
7. **Do not pay for what is free.** Almost all Ukrainian metrical books, revision lists and inventories are already openly available; many paid services merely name the archive and the file.
8. **Check for "silent" failures.** Some forms silently discard search conditions, and the results look normal:
   - JewishGen: fields 2–4 on the free form are closed, and what is typed in them is **silently ignored** — there is no filter;
   - USHMM: without the correct field name the filter is **silently not applied**;
   - Mitzvat Emet: after the captcha the form simply does not submit.
   Use a control query to check that the filter worked.
9. **If a site does not open**, it is not necessarily an error: try later, from another device, without a VPN, without frequent requests.

## 4. Geographic restrictions

- **From abroad, some Russian government sites do not open** (archives, NEB — the National Electronic Library, RGB — the Russian State Library, RNB — the National Library of Russia, "Pamyat naroda", "Doroga pamyati", Gosuslugi, a number of oblast archives and their EAIS — unified archive information systems). Errors: "connection refused", 401, 403.
- The reverse also happens: some sites (for example the Polish archive portal szukajwarchiwach.gov.pl) have blocked certain foreign addresses entirely.
- **Ukrainian archives**, according to reports in 2026, do not work with researchers from Russia and Belarus, and some archives have introduced IP-address blocking that also affects users from other countries (generaggs.substack.com, April 2026) [checked].
- **A VPN often breaks access.** If you work through a VPN, try turning it off while you work with such sites.
- Do not bypass protection. If a site is unavailable from your country, look for the same material elsewhere (FamilySearch ↔ the archive's site ↔ Commons) or ask acquaintances.
- These also worked from abroad (October 2026): Yandex, GPIB (the State Public Historical Library), archive.org, FamilySearch, JewishGen, Yad Vashem, PHAIDRA.

## 5. What has closed or changed (September–October 2026)

| Site | What happened |
|---|---|
| base.memo.ru (lists.memo.ru) | not working since spring 2026; archived copies remain |
| epoisk.ru | announced closure after 11.08.2026 |
| data.mos.ru | since 03.08.2026 the personal data of the deceased are hidden |
| pmemorial.ru | the search databases are no longer there |
| cgako.ru/base/evac.php (evacuees to Kirov) | reCAPTCHA on the form |
| All Galicia Database (Gesher Galicia) | since September 2026 closed behind membership (from experience; no announcement was found on the site) |
| wiki.alexkrakovsky.com | the domain does not work; the materials moved to Wikisource and Commons |
| Avotaynu CSI | did not open on the date of checking |
| USHMM HSV | closure announced for autumn 2026 |
| Routes to Roots | the online form returned no results (September 2026) — M. Weiner's book is on archive.org |
| forum.j-roots.info | in spring 2025 the forum opened briefly once a day (VGD, 30.04.2025); in October 2026 the site had an expired certificate — the browser warns of danger; the decision whether to open it is the person's |
| the JewishGen mailing list (groups.jewishgen.org) | closed to automated requests by a robot check; can be read in an ordinary browser |

## 6. Peculiarities of specific sites (briefly)

- **JewishGen** shows only the first **50 rows** — narrow your query (town, "any field").
- **FamilySearch**: some films are only at FamilySearch centers — a frequent reason for "not found" even though the record exists.
- **Wikimedia Commons**: download the **whole** PDF of the file, not the preview. A huge file (hundreds of MB) sometimes fails to download because of a server limit — then go page by page.
- **archive.org**: when downloading from the command line you need the redirect flag (`curl -L`), otherwise you will get an empty file.
- **NEB** (National Electronic Library): the status "description only" means there is no scan at all, and registration will not help.
- **Mitzvat Emet**: after roughly five searches in a row the form silently stops submitting — continue later, one search per visit.
- **Facebook groups**: a search within a group shows only the beginnings of posts, the answers are in the comments; inconvenient for systematic searching, forums with open text are better.
- **FamilySearch Community** (forum): can be read without logging in, translation questions with an image get an answer quickly.

Detailed techniques for each site are in [../../catalog/](../../catalog).

> **How to ask AI**
>
> *For a plain chat, add: "If you can't open a source, say so; mark fonds, villages and dates you name from memory as [from memory, verify]. Answer in English, and give names, places and archive titles in the original script in parentheses." ([why](../1-ai-search/02-prompt-library.md)). The note "(browsing agent)" is for an AI that opens websites itself; the other prompts suit any chat.*
>
> - "Site [N] shows [a 403/429 error, a captcha, a blank page]. What does this mean and what should I do without bypassing the protection?" *Check yourself:* you pass the captcha yourself; if blocked by country, the decision is yours.
> - "Draft a plan for an evening of work on [FamilySearch / NLI / another site]: how many images, what pace, when to take a break." *Check yourself:* a result of "0" when the site is returning errors is a technical zero.
>
> *Bad → good:* "Download the whole book from FamilySearch, quickly" (frequent requests lead to a block, and a human passes the captcha) → "Read the book [title] on FamilySearch no faster than one image every 5–10 seconds; if a captcha appears, stop and call me."

---

**See also:** [catalog of sites](../../catalog/README.md) · [AI tools](../1-ai-search/05-ai-tools.md) · [Scenarios: what to do if…](../1-ai-search/07-scenarios.md) (scenario B6)
