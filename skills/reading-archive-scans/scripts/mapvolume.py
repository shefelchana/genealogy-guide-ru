#!/usr/bin/env python3
"""Ищет титульные листы в архивном деле, у которого нет оглавления.

Два признака, по очереди:
  printed — печатный титул: много чернил и много длинных вертикальных линеек;
  written — рукописный титул: чернила сгущены в верхней трети, низ пуст.
Промеряет том целиком через DCT-превью (быстро: 2500 страниц ≈ 10 с).

  python3 mapvolume.py FILE.pdf [--mode printed|written|both] [--top N]
"""
import argparse, io
import numpy as np
import pypdf
from PIL import Image

# Делитель DCT-превью. 8 — минимум, на котором ещё различимы линейки.
DRAFT_DIV = 8
# Порог «это чернила»: доля затемнения относительно фона (85-й перцентиль).
# 0.22 отделяет письмо от желтизны бумаги на всех проверенных делах.
INK = 0.22
# Колонка считается линейкой, если затемнена по всей высоте полосы.
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
    ap.add_argument("--top", type=int, default=80, help="сколько кандидатов вывести")
    a = ap.parse_args()

    reader = pypdf.PdfReader(a.pdf)
    n = len(reader.pages)
    feats = {}
    for p in range(1, n + 1):
        arr = page_array(reader, p)
        if arr is not None:
            feats[p] = features(arr)
    if not feats:
        raise SystemExit("изображений не найдено")

    tops = np.array([f["top"] for f in feats.values()])
    mids = np.array([f["mid"] for f in feats.values()])
    hi_top, lo_mid = np.percentile(tops, 80), np.percentile(mids, 35)

    if a.mode in ("printed", "both"):
        # Пороги выведены на делах ДАХмО: печатный бланк заметно чернее
        # рукописной таблицы и несёт больше длинных линеек.
        c = [p for p, f in feats.items() if f["ink"] > 0.18 and f["rules"] > 12]
        print(f"печатные титулы ({len(c)}):", c[:a.top])
    if a.mode in ("written", "both"):
        c = [p for p, f in feats.items() if f["top"] > hi_top and f["mid"] < lo_mid]
        print(f"рукописные титулы ({len(c)}):", c[:a.top])
    print(f"промерено страниц: {len(feats)} из {n}")


if __name__ == "__main__":
    main()
