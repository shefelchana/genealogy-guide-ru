#!/usr/bin/env python3
"""Tests for variants.py (neutral example surnames only). Run: python3 test_variants.py"""
import os
import re
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import variants as v  # noqa: E402


def forms(name, depth=2):
    res = v.build(name, depth, cap=10_000)
    return res, {x["form"].lower() for g, items in res["groups"].items()
                 if isinstance(items, list) for x in items}


class ParseTest(unittest.TestCase):
    def test_same_phonemes_from_both_scripts(self):
        self.assertEqual(v.parse("Feigel"), v.parse("Фейгель"))
        self.assertEqual(v.parse("Kremer"), v.parse("Кремер"))

    def test_doubled_consonant(self):
        self.assertIn(("G", True), v.parse("Feiggel"))
        self.assertIn(("F", True), v.parse("Loffel"))

    def test_polish_and_german_digraphs(self):
        self.assertEqual(v.parse("Szmid")[0], ("SH", False))
        self.assertEqual(v.parse("Schmid")[0], ("SH", False))
        self.assertEqual(v.parse("Rzepka")[0], ("ZH", False))
        self.assertEqual(v.parse("Schwarz")[-1], ("Z", False))   # final rz is r + z


class VariantTest(unittest.TestCase):
    def test_conventional_family_of_forms(self):
        _, f = forms("Feigel")
        for w in ["фейгель", "фейгаль", "файгель", "фейггель", "фейгль", "фейгеръ",
                  "feigel", "fejgel", "faigel", "feigl", "פייגעל", "פייגל"]:
            self.assertIn(w, f, w)

    def test_inserted_t_and_ending(self):
        _, f = forms("Lofel")
        for w in ["лофтель", "лофер", "лоферъ", "лафель", "лоффель", "loftel", "loffel", "lofer"]:
            self.assertIn(w, f, w)

    def test_cursive_misreading_f_r(self):
        _, f = forms("Lofel", depth=1)
        self.assertIn("лорель", f)          # ф read as р

    def test_every_form_marked(self):
        out = subprocess.run([sys.executable, v.__file__, "Feigel", "--max", "5"],
                             capture_output=True, text=True, check=True).stdout
        forms_part = out.split("== Regexes")[0]
        lines = [ln for ln in forms_part.splitlines() if ln.startswith("  ")]
        self.assertTrue(lines)
        self.assertTrue(all("⚪ [variant?]" in ln for ln in lines))


class RegexTest(unittest.TestCase):
    def test_cyrillic_narrow_and_broad(self):
        res, _ = forms("Lofel")
        narrow = re.compile(res["regex"]["cyrillic_narrow"])
        broad = re.compile(res["regex"]["cyrillic_broad"])
        for w in ["Лофель", "Лофтель", "Лоферъ", "Лафель", "Лорель", "Лоффель"]:
            self.assertTrue(narrow.fullmatch(w), w)
        for w in ["Лофль", "Лофъ"]:
            self.assertTrue(broad.fullmatch(w), w)
        self.assertFalse(narrow.fullmatch("Розенберг"))

    def test_latin_and_hebrew(self):
        res, _ = forms("Lofel")
        lat = re.compile(res["regex"]["latin"])
        for w in ["Lofel", "Loffel", "Loftel", "Lofer", "Lafel", "Lufel"]:
            self.assertTrue(lat.fullmatch(w), w)
        heb = re.compile(res["regex"]["hebrew_yiddish"])
        for w in ["לאפעל", "לפל", "לפטל"]:
            self.assertTrue(heb.fullmatch(w), w)

    def test_ocr_first_letter_dropped(self):
        res, _ = forms("Feigel")
        self.assertTrue(re.fullmatch(res["regex"]["ocr_first_letter_dropped_cyr"], "ейгель"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
