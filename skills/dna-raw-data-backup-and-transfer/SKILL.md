---
name: dna-raw-data-backup-and-transfer
description: >-
  Step-by-step work with raw DNA files from consumer tests: where the download button is at AncestryDNA, 23andMe, MyHeritage, FamilyTreeDNA and Genotek; how to read the file header (company, chip or whole-genome sequencing, version, date, no-calls); which file each site still accepts in late 2026 (a dated "from → to" matrix — MyHeritage closed uploads in 2025, the new Ancestry file of January 2026, FamilyTreeDNA NGS of March 2026 and MyHeritage WGS files are often refused); why to upload the original file and not an imputed "improved" one; privacy and law-enforcement settings at upload; and a backup and audit routine before any bankruptcy, upgrade, recalculation or account deletion. Use when the user asks "how do I download my DNA file", "why won't my file upload", "where else can I upload my test", "GEDmatch says too many matches", "should I back up before 23andMe / before the FTDNA upgrade", "VCF or 23andMe V5", "my match list changed after the upgrade", or plans to delete a DNA account. Not for interpreting matches (use dna-matches-endogamy or dna-matches-across-platforms). Also triggers on Russian requests: «как скачать сырые данные», «файл не загружается», «куда ещё загрузить тест», «перенос на GEDmatch», «резервная копия ДНК», «VCF или V5», «после апгрейда пропали совпадения».
---

# Raw DNA files: download, check, back up, transfer

The raw file is the only part of a DNA test the user really owns. Companies go bankrupt, change chips, close uploads and recalculate matches, and the old list does not come back. This skill keeps the file and the match lists safe and moves them only where they are still accepted.

**Facts below are as of November 2026.** Formats and rules changed several times in 2025–2026. Before giving advice, say the date of these facts and suggest the user checks the site's current help page. The full matrix with sources is in `references/transfer-matrix.md`.

The user does every login, download, upload and payment. You explain where the button is and what to choose. **Never ask the user to send a raw DNA file into the chat**, and never upload it anywhere yourself: genetic data concerns all relatives, and a leak cannot be undone.

## Step 1. Download the original file

| Company | Where | Notes |
|---|---|---|
| AncestryDNA | DNA → Settings → Download Raw DNA Data | ZIP with a TXT inside; confirmation by e-mail |
| 23andMe | Settings → 23andMe Data → Download Raw Data | may ask for the date of birth given at registration |
| MyHeritage | Manage DNA kits → ⋮ → Download kit → DNA data file | only the kit manager, from a computer; the link lives 24 hours. WGS kits also offer a CRAM file (~2 GB) |
| FamilyTreeDNA | Account Settings → Download Raw Data | needs two-factor authentication; autosomal CSV/GZ; Y and mtDNA (FASTA) are separate files |
| Genotek | in the personal account | VCF is free; the "23andMe V5" file is paid and **imputed** (computed, not measured) |

Ask the user to download **every** test of every relative they manage, not only "the main one".

## Step 2. Read the header before uploading anywhere

Open the file in a text editor (not Excel: it damages long files) and note:
- **company and format line** — for MyHeritage, `##chip=GSA` means a chip test, `##method=Low-pass Whole Genome Sequencing` means the new WGS kit;
- **build and version** (e.g. "build 37", "v5", "v2e");
- **date** of the file;
- **number of lines** (roughly: classic chips 600–700 thousand; the new Ancestry file about 435 thousand);
- **share of no-calls** (`--` or `00`): many no-calls mean a weak sample, and GEDmatch may then allow only one-to-one comparison.

Write these five facts into the project log next to the file name. Most "the site can't read my file" problems are explained by the header.

## Step 3. Keep originals, not imputed files

- An **imputed** file (Genotek "V5", a MyHeritage WGS CSV, any "converted" or "improved" file) contains guessed positions. For **matching** this produces false matches: on GEDmatch such kits get "too many matches" (forum reports of over a million instead of the usual 25–65 thousand).
- Use an imputed file only where nothing else is accepted, and only for ethnicity calculators. Label it clearly as imputed.
- Keep files exactly as downloaded. Some sites refuse a ZIP but accept the same TXT unpacked; others want the archive. Try the other form before deciding the file is broken.

## Step 4. Choose where to transfer (dated matrix)

Short version for November 2026:

| File ↓ / site → | GEDmatch | FamilyTreeDNA | MyHeritage | Genotek |
|---|---|---|---|---|
| Ancestry, before Dec 2025 | yes | yes (matches free) | no | partly |
| Ancestry, from Jan 2026 | not confirmed | no | no | no (forum) |
| 23andMe v3–v5 | yes | yes | no | yes |
| MyHeritage chip (before late 2025) | yes | yes | no | yes (forum) |
| MyHeritage WGS CSV | with gaps | no | no | no (forum) |
| FamilyTreeDNA, before Mar 2026 | yes | — | no | yes |
| FamilyTreeDNA NGS, from Mar 2026 | complaints | — | no | no (forum) |
| Genotek V5 (imputed) | "too matchy" | yes, unarchived TXT | no | — |
| Whole genome 30x (BAM/CRAM) | via conversion tools | via conversion | no | yes, free (forum) |

Rules that follow from it:
1. **MyHeritage accepts no uploads at all** since mid-2025. Pre-2025 articles that say "upload to MyHeritage for free" are out of date.
2. **When a company changes its own format, other sites may refuse the new file for months.** If the user has an older file of the same test, transfer the older one.
3. **FamilyTreeDNA:** uploaded files get free matches and the Matrix only; the chromosome browser and ethnicity need a $29 upgrade (the $19 unlock ended on 18 August 2026).
4. **GEDmatch:** one file — one kit; the file cannot be downloaded back. Upload autosomal files only.
5. The 2026 expert advice is: **test where you want matches.** Transfers are now a bonus, not a plan.

## Step 5. Privacy settings at upload

- **GEDmatch:** at upload the user chooses law-enforcement access (opt-in, opt-out, private, research). Explain the options neutrally and let the user decide.
- **FamilyTreeDNA:** has a law-enforcement matching setting (opt-out); EU accounts are excluded automatically.
- MyHeritage, Ancestry and 23andMe forbid police matching in their terms.
- **Record the choice** (site, kit, setting, date) in the project log. A downloaded file is no longer protected by the company's settings: store it encrypted or in a private folder.

## Step 6. Backup and audit before any change

Do this **before**: deleting an account, a company sale or bankruptcy (as with 23andMe in 2025), an upgrade (FamilyTreeDNA chip → NGS), a "recalculation", or switching a kit to a new manager.

1. Raw file of every kit (Step 1), named `company_kit-owner-initials_test-type_YYYY-MM-DD.ext`.
2. **Match list as CSV** where it exists (FamilyTreeDNA, 23andMe, GEDmatch, MyHeritage for chip kits). Where there is no export, save the top of the list (all matches with the longest segment ≥ 15 cM) by hand or by screenshots.
3. **Segment data** (chromosome, start, end, cM) where available.
4. **Ethnicity screenshots** with the date and model version.
5. Messages with matches that matter.

After the change, compare old and new lists: how many matches left, how many came, did key matches stay. In one published comparison, a FamilyTreeDNA upgrade from chip to NGS dropped about 1,700 old matches and added about 400 new ones. Write the result in the log; do not delete the old kit — results from different tests of the same person differ, and all of them are useful.

Deleting a 23andMe account is **irreversible** and deletes profiles managed from it. Download everything first.

## Common upload errors

| Symptom | Likely cause | What to do |
|---|---|---|
| "Cannot read file" | new format of the source company | check the header; use an older file of the same test or wait |
| GEDmatch "too many matches" / kit limited to one-to-one | imputed file or many no-calls | upload the original file; retest if the sample was weak |
| Upload refused as duplicate | the same file is already in another kit | use the existing kit |
| ZIP refused | site wants plain text (or the reverse) | unpack or pack and retry |
| File opens badly in Excel | Excel converts values | use a text editor |

## Output

A short table for the user: kit, company, file version (from the header), where it is uploaded, privacy setting chosen, date of the last backup. Plus one line: what to do next and why.
