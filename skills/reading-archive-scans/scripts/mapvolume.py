#!/usr/bin/env python3
"""Finds title pages in an archival file that has no table of contents.

Two criteria, in turn:
  printed - printed title: a lot of ink and many long vertical rules;
  written - handwritten title: ink concentrated in the top third, empty bottom.
Measures the whole volume via DCT previews (fast: 2500 pages ~ 10 s).

  python3 mapvolume.py FILE.pdf [--mode printed|written|both] [--top N]
"""
import argparse, io
import numpy as np
import pypdf
from PIL import Image

# DCT preview divisor. 8 is the minimum at which ruled lines are still distinguishable.
DRAFT_DIV = 8
# 'This is ink' threshold: share of darkening relative to the background (85th percentile).
# 0.22 separates writing from the yellowing of the paper on all files checked.
INK = 0.22
# A column counts as a ruled line if it is darkened over the whole height of the strip.
RULE_FRAC = 0.65


def page_array(reader, p, div=DRAFT_DIV):
    res = reader.pages[p - 1].get("/Resources")
    xo = res.get("/XObject") if res else None
    if xo is None:
        return None
    for key in xo.get_object():
        o = xo.get_object()[key].get_object()
        if o.get("/Subtype") != "/Image":
            continue
        try:
            im = Image.open(io.BytesIO(o._data))
            im.draft("L", (o["/Width"] // div, o["/Height"] // div))
            return np.asarray(im.convert("L"), np.float32)
        except Exception:
            return None
    return None


def features(a):
    h, w = a.shape
    bg = np.percentile(a, 85)
    ink = (bg - a) / max(bg, 1) > INK
    bands = [float(ink[i * h // 10:(i + 1) * h // 10].mean()) for i in range(10)]
    return dict(
        ink=float(ink.mean()),
        rules=int((ink.mean(axis=0) > RULE_FRAC).sum()),
        top=bands[1] + bands[2],
        mid=sum(bands[4:8]) / 4,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--mode", choices=["printed", "written", "both"], default="both")
    ap.add_argument("--top", type=int, default=80, help="how many candidates to print")
    a = ap.parse_args()

    reader = pypdf.PdfReader(a.pdf)
    n = len(reader.pages)
    feats = {}
    for p in range(1, n + 1):
        arr = page_array(reader, p)
        if arr is not None:
            feats[p] = features(arr)
    if not feats:
        raise SystemExit("no images found")

    tops = np.array([f["top"] for f in feats.values()])
    mids = np.array([f["mid"] for f in feats.values()])
    hi_top, lo_mid = np.percentile(tops, 80), np.percentile(mids, 35)

    if a.mode in ("printed", "both"):
        # Thresholds derived on DAKhmO files: a printed form is noticeably blacker
        # than a handwritten table and carries more long ruled lines.
        c = [p for p, f in feats.items() if f["ink"] > 0.18 and f["rules"] > 12]
        print(f"printed titles ({len(c)}):", c[:a.top])
    if a.mode in ("written", "both"):
        c = [p for p, f in feats.items() if f["top"] > hi_top and f["mid"] < lo_mid]
        print(f"handwritten titles ({len(c)}):", c[:a.top])
    print(f"pages measured: {len(feats)} of {n}")


if __name__ == "__main__":
    main()
