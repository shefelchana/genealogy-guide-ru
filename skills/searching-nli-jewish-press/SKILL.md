---
name: searching-nli-jewish-press
description: >-
  Searches the Historical Jewish Press of the National Library of Israel (nli.org.il/newspapers) for people and places in 19th–20th-century Hebrew and Yiddish newspapers (Ha-Tsefira, Ha-Melits, Ha-Magid, Yudishes folksblat and others) — builds spellings in Hebrew script, uses annual indexes of correspondents, reads the issue contents and the article image, translates what it finds, and handles Cloudflare checks by slowing down. Use whenever a family history question could be answered by a newspaper notice, correspondence, donation list or obituary, e.g. "search the Jewish newspapers", "find an announcement about my ancestor", "what did the press write about the shtetl", even if NLI is not named. Not for translating a Hebrew or Yiddish text already in hand (use reading-hebrew-yiddish-sources). Also triggers on Russian requests: «поищи в еврейских газетах», «найди объявление», «что писали про местечко».
---

# The Jewish press at the National Library of Israel (NLI)

## What to look for there
- **Announcements** (searches for missing husbands — *agunah*, searches for relatives, weddings, mourning notices).
- **Correspondence from shtetls** (the "Correspondence" section, often signed with a pen name).
- **Donation lists** (name, sometimes patronymic, town, amount).
- **Articles by local authors** (signature with patronymic and town: «Элиэзер Мошков Розенберг, [город], март 1884» [“Eliezer, son of Moshko, Rosenberg, [town], March 1884”]).
- **Annual indexes** of a volume: a list of correspondents with towns and pages is a find in itself.

## How to build a query
1. Name and town **in Hebrew/Yiddish script**, in several spellings: קישינוב / קעשענעוו (Kishinev); ראָזענבערג / ראזענבערג / רויזענבערג (Rosenberg); allow for the silent "ה" (in a town name it sometimes appears and sometimes not), doubled "וו/יי", endings.
2. Newspapers write a Russian surname in Yiddish fashion: Rosenberg → ראָזענבערג/ראזענבערג; the patronymic — «מאשקאוו» (Moshkov).
3. Restrict by **years** and by **publication**: less noise and fewer requests.
4. Recognition of the old typeface makes mistakes: «ראזענבערג» may become «ראזעגבערג». Try 2–3 variants and a neighbouring word (the town).

## How to read
- Result → issue page → article. The issue's table of contents shows the sections.
- **Decide only from the image**: recognized text (OCR) is for searching, not for quoting.
- The whole article image (block) is read at large size; the signature is usually at the end.
- Translation — close to the text, with "(?)" marks on uncertain words; keep the original spellings of names.

## Pace and Cloudflare (experience of October 2026)
- The "Verify you are human" check appears with frequent requests (roughly after a hundred rapid requests), and afterwards the site may keep the tab under suspicion.
- The check is passed by a **human**, in the same tab in which the assistant works.
- Work by **navigating one page at a time** with pauses of at least 5 s; do not go through newspaper numbers with a script in a row.
- **Test a bulk pass on a known positive example**: if the site answers with an error (403), "zero finds" means nothing.

## Recording a find
Publication, date, issue number, section, page/column, link; verbatim (in the original script) + translation; image crop.

## Pitfalls
- The same surnames in different towns — check the town and the patronymic.
- Correspondents' pen names («А гутер бродер» [“A good brother”]): one pen name in different years can link notes together.
- A page number in an annual index often means a **column** of the whole volume, not a page of the issue.

See also: `reading-hebrew-yiddish-sources`, `verifying-genealogy-findings`.
