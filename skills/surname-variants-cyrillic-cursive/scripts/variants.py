#!/usr/bin/env python3
"""Spelling variants of an Eastern European Jewish surname.

Give a surname in Latin or Cyrillic; get the variants a clerk, an indexer
or an OCR engine may have produced, each marked "⚪ [variant?]", plus
search regexes (Cyrillic, Latin, Hebrew/Yiddish, OCR without first letter).

    python3 variants.py Feigel
    python3 variants.py Фейгель --depth 1 --max 30
    python3 variants.py Kremer --json

The list is a search net, not a verdict: a variant is excluded only on
other evidence (father, place, age, household, same-hand comparison).
"""
import argparse
import json
import sys

VOWELS = {"A", "E", "I", "O", "U", "EI", "AI", "OI"}

# ---------------------------------------------------------------- parsing
LAT_TOKENS = [
    ("szcz", "SHCH"), ("shch", "SHCH"), ("tsch", "CH"), ("sch", "SH"),
    ("sh", "SH"), ("sz", "SH"), ("cz", "CH"), ("ch", "KH"), ("kh", "KH"),
    ("zh", "ZH"), ("tz", "TS"), ("ph", "F"), ("ck", "K"),
    ("ei", "EI"), ("ey", "EI"), ("ai", "AI"), ("ay", "AI"), ("ej", "EI"),
    ("aj", "AI"), ("oi", "OI"), ("oy", "OI"), ("oj", "OI"),
    ("ie", "I"), ("ee", "I"), ("oo", "U"), ("ae", "E"), ("oe", "E"),
    ("ä", "E"), ("ö", "E"), ("ü", "I"), ("é", "E"), ("ł", "L"), ("ś", "S"),
    ("ć", "TS"), ("ń", "N"), ("ó", "U"), ("ą", "O"), ("ę", "E"), ("ź", "Z"),
    ("ż", "ZH"), ("ſ", "S"),
    ("a", "A"), ("e", "E"), ("i", "I"), ("o", "O"), ("u", "U"), ("y", "I"),
    ("b", "B"), ("c", "TS"), ("d", "D"), ("f", "F"), ("g", "G"), ("h", "H"),
    ("j", "Y"), ("k", "K"), ("l", "L"), ("m", "M"), ("n", "N"), ("p", "P"),
    ("q", "K"), ("r", "R"), ("s", "S"), ("t", "T"), ("v", "V"), ("w", "V"),
    ("x", "KS"), ("z", "Z"),
]
CYR_TOKENS = [
    ("ей", "EI"), ("ай", "AI"), ("ой", "OI"), ("щ", "SHCH"), ("ш", "SH"),
    ("ж", "ZH"), ("ч", "CH"), ("ц", "TS"), ("х", "KH"), ("г", "G"), ("ґ", "G"),
    ("й", "Y"), ("а", "A"), ("я", "A"), ("е", "E"), ("э", "E"), ("є", "E"),
    ("ѣ", "E"), ("ё", "O"), ("и", "I"), ("і", "I"), ("ї", "I"), ("ы", "I"),
    ("о", "O"), ("у", "U"), ("ю", "U"), ("б", "B"), ("в", "V"), ("д", "D"),
    ("з", "Z"), ("к", "K"), ("л", "L"), ("м", "M"), ("н", "N"), ("п", "P"),
    ("р", "R"), ("с", "S"), ("т", "T"), ("ф", "F"), ("ѳ", "F"),
]


def is_cyrillic(s):
    return any("Ѐ" <= ch <= "ӿ" for ch in s)


def parse(name):
    s = name.lower().strip()
    tokens = CYR_TOKENS if is_cyrillic(s) else LAT_TOKENS
    out, i = [], 0
    while i < len(s):
        if s[i] in "ьъ'’-" or not s[i].isalpha():
            i += 1
            continue
        if i == 0 and s[i] in "яю":                      # initial ya / yu
            out += [["Y", False], ["A" if s[i] == "я" else "U", False]]
            i += 1
            continue
        if i == 0 and s[i] == "y" and len(s) > 1 and s[1] in "aeiou":
            out.append(["Y", False])
            i += 1
            continue
        if s.startswith("rz", i) and i + 2 < len(s) and s[i + 2] in "aeiouy":
            out.append(["ZH", False])                    # Polish rz before a vowel
            i += 2
            continue
        for tok, code in tokens:
            if s.startswith(tok, i):
                i += len(tok)
                for c in (["K", "S"] if code == "KS" else [code]):
                    if out and c not in VOWELS and out[-1][0] == c and out[-1][1] is False:
                        out[-1][1] = True                # ff, фф, ll -> doubled
                    else:
                        out.append([c, False])
                break
        else:
            i += 1
    return [tuple(p) for p in out]


# ------------------------------------------------------------- rendering
CYR = {"A": "а", "E": "е", "I": "и", "O": "о", "U": "у", "EI": "ей", "AI": "ай", "OI": "ой",
       "B": "б", "V": "в", "G": "г", "H": "г", "D": "д", "ZH": "ж", "Z": "з",
       "Y": "й", "K": "к", "L": "л", "M": "м", "N": "н", "P": "п", "R": "р",
       "S": "с", "T": "т", "F": "ф", "KH": "х", "TS": "ц", "CH": "ч", "SH": "ш",
       "SHCH": "щ"}
LAT = {
    "German":  {"A": "a", "E": "e", "I": "i", "O": "o", "U": "u", "EI": "ei", "AI": "ai", "OI": "oi",
                "B": "b", "V": "w", "G": "g", "H": "h", "D": "d", "ZH": "sch", "Z": "s",
                "Y": "j", "K": "k", "L": "l", "M": "m", "N": "n", "P": "p", "R": "r",
                "S": "s", "T": "t", "F": "f", "KH": "ch", "TS": "z", "CH": "tsch",
                "SH": "sch", "SHCH": "schtsch"},
    "Polish":  {"A": "a", "E": "e", "I": "i", "O": "o", "U": "u", "EI": "ej", "AI": "aj", "OI": "oj",
                "B": "b", "V": "w", "G": "g", "H": "h", "D": "d", "ZH": "ż", "Z": "z",
                "Y": "j", "K": "k", "L": "l", "M": "m", "N": "n", "P": "p", "R": "r",
                "S": "s", "T": "t", "F": "f", "KH": "ch", "TS": "c", "CH": "cz",
                "SH": "sz", "SHCH": "szcz"},
    "English": {"A": "a", "E": "e", "I": "i", "O": "o", "U": "u", "EI": "ei", "AI": "ai", "OI": "oi",
                "B": "b", "V": "v", "G": "g", "H": "h", "D": "d", "ZH": "zh", "Z": "z",
                "Y": "y", "K": "k", "L": "l", "M": "m", "N": "n", "P": "p", "R": "r",
                "S": "s", "T": "t", "F": "f", "KH": "kh", "TS": "tz", "CH": "ch",
                "SH": "sh", "SHCH": "shch"},
}
HEB = {"A": "א", "E": "ע", "I": "י", "O": "א", "U": "ו", "EI": "יי", "AI": "יי", "OI": "וי",
       "B": "ב", "V": "וו", "G": "ג", "H": "ה", "D": "ד", "ZH": "זש", "Z": "ז",
       "Y": "י", "K": "ק", "L": "ל", "M": "מ", "N": "נ", "P": "פ", "R": "ר",
       "S": "ס", "T": "ט", "F": "פ", "KH": "כ", "TS": "צ", "CH": "טש", "SH": "ש",
       "SHCH": "שטש"}
HEB_INITIAL = {"E": "ע", "A": "א", "O": "א", "I": "אי", "U": "או", "EI": "איי", "AI": "איי", "OI": "אוי"}
HEB_FINAL = {"כ": "ך", "מ": "ם", "נ": "ן", "פ": "ף", "צ": "ץ"}


def render_cyr(ph):
    s, i = "", 0
    while i < len(ph):
        c, d = ph[i]
        nxt = ph[i + 1][0] if i + 1 < len(ph) else None
        if c == "Y" and nxt in ("A", "U"):
            s += "я" if nxt == "A" else "ю"
            i += 2
            continue
        if i == 0 and c == "E":
            s += "э"
        elif i == 0 and c in ("EI", "AI"):
            s += "эй" if c == "EI" else "ай"
        else:
            s += CYR[c] * (2 if d else 1)
        if c == "L" and (nxt is None or nxt not in VOWELS):
            s += "ь"                                     # Гольд-, -ель
        i += 1
    return s.capitalize()


def render_lat(ph, table):
    s = "".join(table[c] * (2 if d and len(table[c]) == 1 else 1) for c, d in ph)
    return s[:1].upper() + s[1:]


def render_heb(ph, defective=False):
    s = ""
    for i, (c, _) in enumerate(ph):
        if i == 0 and c in HEB_INITIAL:
            s += HEB_INITIAL[c]
        elif defective and c in ("E", "A", "O"):
            continue
        else:
            s += HEB[c]
    if s and s[-1] in HEB_FINAL:
        s = s[:-1] + HEB_FINAL[s[-1]]
    return s


# ------------------------------------------------- phoneme-level mutations
VOWEL_SHIFT = {"E": ["A", "I", "EI"], "A": ["E", "O"], "I": ["E"], "EI": ["AI", "E", "A"],
               "AI": ["EI", "A", "E"],
               "O": ["U", "A"], "U": ["O"], "OI": ["EI", "O"]}
CONS_SWAP = [("G", "H", "г/х/h (Hersh/Gersh)"), ("G", "KH", "г/х"), ("H", "KH", "h/ch"),
             ("P", "F", "Hebrew פ = п/ф"), ("B", "V", "Hebrew ב = б/в"),
             ("S", "SH", "Hebrew ש = с/ш"), ("S", "Z", "с/з"), ("TS", "S", "ц/с")]


def mutations(ph):
    """Yield (new_phonemes, label). Ordered from most to least frequent."""
    n = len(ph)
    last = ph[-1][0] if ph else None
    # endings -el <-> -er, syncope -el -> -l, truncation
    if last in ("L", "R"):
        other = "R" if last == "L" else "L"
        yield ph[:-1] + ((other, False),), f"ending -{last.lower()} -> -{other.lower()}"
        if n >= 3 and ph[-2][0] in VOWELS:
            yield ph[:-2] + (ph[-1],), "syncope (-el -> -l, -er -> -r)"
            if n >= 5:
                yield ph[:-2], "truncated ending (cramped column)"
    # inserted / dropped t after F or S
    for i in range(n - 1):
        if (ph[i][0] in ("F", "S", "SH") and i + 2 == n - 1
                and ph[i + 1][0] in VOWELS and ph[-1][0] in ("L", "R")):
            yield ph[:i + 1] + (("T", False),) + ph[i + 1:], "inserted t (-ftel)"
        if ph[i][0] in ("F", "S") and ph[i + 1][0] == "T":
            yield ph[:i + 1] + ph[i + 2:], "dropped t"
    # vowels
    for i, (c, d) in enumerate(ph):
        for v in VOWEL_SHIFT.get(c, []):
            yield ph[:i] + ((v, d),) + ph[i + 1:], f"vowel {c.lower()} -> {v.lower()}"
    # doubled / single consonant
    for i, (c, d) in enumerate(ph):
        if 0 < i < n - 1 and c not in VOWELS and c not in ("Y", "SHCH", "CH", "ZH"):
            yield ph[:i] + ((c, not d),) + ph[i + 1:], ("single " if d else "doubled ") + c.lower()
    # consonant swaps
    for i, (c, d) in enumerate(ph):
        for a, b, label in CONS_SWAP:
            if c in (a, b):
                yield ph[:i] + ((b if c == a else a, d),) + ph[i + 1:], label


def expand(ph, depth):
    seen = {ph: "base"}
    frontier = [ph]
    for _ in range(depth):
        new = []
        for p in frontier:
            for q, label in mutations(p):
                if q and q not in seen:
                    seen[q] = label if seen[p] == "base" else seen[p] + " + " + label
                    new.append(q)
        frontier = new
    return seen


# ------------------------------------------------- string-level mutations
CURSIVE = [("ф", "р"), ("р", "ф"), ("т", "ш"), ("ш", "т"), ("т", "м"), ("и", "н"),
           ("н", "и"), ("п", "н"), ("и", "п"), ("л", "м"), ("м", "л"), ("е", "с")]
KURRENT = [("f", "s"), ("s", "f"), ("e", "n"), ("n", "u"), ("u", "n"), ("rn", "m")]


def single_subs(word, pairs, label):
    low = word.lower()
    for a, b in pairs:
        start = 0
        while True:
            j = low.find(a, start)
            if j < 0:
                break
            if j > 0:                                    # keep the capital letter
                v = word[:j] + b + word[j + len(a):]
                yield v, f"misreading {a}/{b} ({label})"
            start = j + 1


def prereform(word):
    if word.endswith("ь") and word[-2:-1] == "л":
        yield word[:-1] + "ъ", "pre-reform -лъ"
        yield word[:-1], "no soft sign"
    elif word[-1:] in "бвгджзклмнпрстфхцчшщ":
        yield word + "ъ", "pre-reform -ъ"
        if word[-1] == "р":
            yield word + "ь", "-рь"


def ukrainian(word):
    t = word.replace("и", "і").replace("ы", "и").replace("Э", "Е").replace("э", "е")
    return t.replace("ъ", "")


# ------------------------------------------------------------- regexes
CYR_RX = {"SH": "[шщс]", "SHCH": "щ", "S": "[сшз]", "Z": "[зс]", "F": "[фрп]", "T": "[тшм]",
          "L": "[лмр]", "R": "[рлф]", "G": "[гхк]", "KH": "[хгк]", "H": "[гх]", "K": "[кх]",
          "V": "[вб]", "B": "[бв]", "P": "[пф]", "N": "[нип]", "M": "[мл]", "D": "[дт]",
          "ZH": "[жз]", "TS": "[цс]", "CH": "[чц]", "Y": "й?"}
LAT_RX = {"SH": "(?:sch|sh|sz|s|ch)", "SHCH": "(?:szcz|shch|schtsch)", "S": "(?:s|sz|z)",
          "Z": "(?:z|s)", "F": "(?:f|ph|p|v|s)", "T": "(?:t|th)", "L": "(?:l|r)",
          "R": "(?:r|l)", "G": "(?:g|h|ch|k)", "KH": "(?:ch|kh|h|k|g)", "H": "(?:h|g|ch)",
          "K": "(?:k|c|ck|q|ch)", "V": "(?:w|v|b|f)", "B": "(?:b|w|v)", "P": "(?:p|ph|f)",
          "N": "(?:n|u)", "M": "m", "D": "(?:d|t)", "ZH": "(?:zh|ż|rz|sch|sh|j)",
          "TS": "(?:tz|ts|z|c|s)", "CH": "(?:tsch|cz|ch|tch)", "Y": "(?:j|y|i)?"}
HEB_RX = {"SH": "[שס]", "SHCH": "שטש", "S": "[סש]", "Z": "ז", "F": "[פף]", "T": "[טת]",
          "L": "[לר]", "R": "[רל]", "G": "ג", "KH": "[כךח]", "H": "[הח]", "K": "[קכך]",
          "V": "(?:וו|ב)", "B": "ב", "P": "[פף]", "N": "[נן]", "M": "[מם]", "D": "ד",
          "ZH": "זש", "TS": "[צץ]", "CH": "טש", "Y": "י?"}


def regex(ph, script, broad=False, drop_first=False):
    parts = []
    seq = ph[1:] if drop_first else ph
    for i, (c, _) in enumerate(seq):
        if c in VOWELS:
            if script == "cyr":
                parts.append("[аеёиіїйоуыэюяєѣ]{0,3}" if broad else
                             ("[аеиіэєйяѣ]{1,2}" if c in ("E", "A", "I", "EI", "AI") else "[оуюёай]{1,2}"))
            elif script == "lat":
                parts.append("[aeiouyäöü]{0,3}" if broad else "[aeiouyäöü]{1,3}")
            else:
                parts.append("[אעיו]{0,2}")
            continue
        table = {"cyr": CYR_RX, "lat": LAT_RX, "heb": HEB_RX}[script]
        cls = table[c]
        parts.append(cls if c == "Y" or script == "heb" else cls + "{1,2}")
        if c in ("F", "S"):
            parts.append({"cyr": "т?", "lat": "t?", "heb": "ט?"}[script])
    if broad and len(seq) >= 4 and seq[-1][0] in ("L", "R") and seq[-2][0] in VOWELS:
        parts[-2:] = ["(?:" + parts[-2] + parts[-1] + ")?"]     # truncated "-ъ" forms
    body = "".join(parts)
    if script == "cyr":
        body += "[ьъ]?"
    return "(?i)" + body if script != "heb" else body


# ----------------------------------------------------------------- main
def build(name, depth=2, cap=40):
    ph = tuple(parse(name))
    if not ph:
        raise SystemExit("could not parse the surname")
    forms = expand(ph, depth)
    groups = {"Russian Cyrillic": {}, "Ukrainian": {}, "Latin": {}, "Yiddish/Hebrew": {}}

    def add(group, form, label, rank=None):
        if rank is None:
            rank = 0 if label in ("base", "German", "Polish", "English") else label.count("+") + 1
        if form and form not in groups[group]:
            groups[group][form] = (label, rank)

    base_cyr = render_cyr(ph)
    for p, label in forms.items():
        cyr = render_cyr(p)
        add("Russian Cyrillic", cyr, label)
        for v, l2 in prereform(cyr):
            if label == "base":
                add("Russian Cyrillic", v, l2, 0.5)
            else:
                add("Russian Cyrillic", v, label + " + " + l2)
        add("Ukrainian", ukrainian(cyr), label)
        for orth, table in LAT.items():
            add("Latin", render_lat(p, table), (label + " + " if label != "base" else "") + orth)
        if label.count("+") == 0:
            add("Yiddish/Hebrew", render_heb(p), label + " (Yiddish)")
            add("Yiddish/Hebrew", render_heb(p, True), label + " (defective)")
    for v, l2 in single_subs(base_cyr, CURSIVE, "cursive"):
        add("Russian Cyrillic", v, l2, 1.5)
    for v, l2 in single_subs(render_lat(ph, LAT["German"]), KURRENT, "Kurrent/OCR"):
        add("Latin", v, l2, 1.5)

    out = {"input": name, "phonemes": " ".join(c + ("2" if d else "") for c, d in ph),
           "groups": {}, "regex": {}}
    for g, d in groups.items():
        keys = list(d)
        items = sorted(d.items(), key=lambda kv: (kv[1][1], keys.index(kv[0])))
        out["groups"][g] = [{"form": f, "rule": r[0]} for f, r in items[:cap]]
        out["groups"][g + " (total)"] = len(d)
    out["regex"] = {
        "cyrillic_narrow": regex(ph, "cyr"),
        "cyrillic_broad": regex(ph, "cyr", broad=True),
        "latin": regex(ph, "lat"),
        "latin_broad": regex(ph, "lat", broad=True),
        "hebrew_yiddish": regex(ph, "heb"),
        "ocr_first_letter_dropped_cyr": regex(ph, "cyr", drop_first=True),
        "ocr_first_letter_dropped_lat": regex(ph, "lat", drop_first=True),
    }
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("surname")
    ap.add_argument("--depth", type=int, default=2, help="how many mutations to combine (default 2)")
    ap.add_argument("--max", type=int, default=40, help="forms shown per group (default 40)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = build(a.surname, a.depth, a.max)
    if a.json:
        json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
        print()
        return
    print(f"Surname: {res['input']}   phonemes: {res['phonemes']}")
    print("Mark every form ⚪ [variant?] in a brief. Exclude only on other evidence.\n")
    for g, items in res["groups"].items():
        if g.endswith("(total)"):
            continue
        total = res["groups"][g + " (total)"]
        print(f"== {g} ({len(items)} of {total})")
        for it in items:
            print(f"  {it['form']:<22} ⚪ [variant?]  {it['rule']}")
        print()
    print("== Regexes (case-insensitive; broad ones over-match on purpose — read every hit)")
    for k, v in res["regex"].items():
        print(f"  {k:<30} {v}")


if __name__ == "__main__":
    main()
