#!/usr/bin/env python3
"""Достаёт страницы из архивного PDF без перекодирования и собирает контактные листы.

Встроенное изображение берётся как сырой JPEG (o._data), поэтому потерь нет.
Требуется: pypdf, Pillow, numpy.

  python3 pagetool.py info   FILE.pdf                       — страниц, размеры, МБ/стр
  python3 pagetool.py sharp  FILE.pdf 55,57,59              — резкость (брак съёмки)
  python3 pagetool.py page   FILE.pdf 128 out.jpg [опции]   — одна страница
  python3 pagetool.py sheet  FILE.pdf 241,243,245 out.jpg [опции] — несколько в ряд

Опции: --crop x0 x1 y0 y1 (доли 0..1) --w ШИРИНА --rot ГРАДУСЫ --k КОЭФФ
"""
import argparse, io, sys
import numpy as np
import pypdf
from PIL import Image, ImageDraw, ImageFilter

# Радиус размытия фона: ~1 % высоты листа. Меньше — съедает штрихи буквы,
# больше — не снимает неравномерность освещения и тень у корешка.
BLUR_RADIUS = 11
# Усиление контраста. Выше 1.8 JPEG-артефакты превращаются в ложные штрихи.
DEFAULT_K = 1.6
# Обрезка гистограммы: 2 % с каждого края убирают выбросы (дырокол, тень),
# не трогая сами чернила.
CLIP_LO, CLIP_HI = 2, 98


def images(reader, page_no):
    """Все изображения страницы (обычно одно). page_no с 1."""
    res = reader.pages[page_no - 1].get("/Resources")
    if res is None:
        return []
    xo = res.get("/XObject")
    if xo is None:
        return []
    out = []
    for key in xo.get_object():
        obj = xo.get_object()[key].get_object()
        if obj.get("/Subtype") == "/Image":
            out.append(obj)
    return out


def native(reader, page_no):
    """Страница как есть, в градациях серого. None, если изображения нет."""
    for obj in images(reader, page_no):
        try:
            return Image.open(io.BytesIO(obj._data)).convert("L")
        except Exception as exc:                      # битый поток — не валимся
            print(f"стр.{page_no}: не читается ({exc})", file=sys.stderr)
    return None


def enhance(im, k=DEFAULT_K):
    """Вычитание фона + растяжка. Вытягивает выцветшие чернила."""
    a = np.asarray(im, np.float32)
    bg = np.asarray(im.filter(ImageFilter.GaussianBlur(BLUR_RADIUS)), np.float32)
    d = (a - bg) * k + 128
    lo, hi = np.percentile(d, [CLIP_LO, CLIP_HI])
    return Image.fromarray(np.clip((d - lo) * 255 / max(hi - lo, 1), 0, 255).astype(np.uint8))


def prepare(reader, page_no, crop, rot, k):
    im = native(reader, page_no)
    if im is None:
        return None
    if rot:
        im = im.rotate(rot, expand=True)
    w, h = im.size
    x0, x1, y0, y1 = crop
    im = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    return enhance(im, k)


def sharpness(reader, page_no):
    """Дисперсия лапласиана. Вчетверо ниже соседних — снято не в фокусе."""
    im = native(reader, page_no)
    if im is None:
        return None
    x = np.asarray(im, np.float32)
    lap = x[1:-1, 1:-1] * 4 - x[:-2, 1:-1] - x[2:, 1:-1] - x[1:-1, :-2] - x[1:-1, 2:]
    return float(lap.var())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["info", "sharp", "page", "sheet"])
    ap.add_argument("pdf")
    ap.add_argument("pages", nargs="?", default="")
    ap.add_argument("out", nargs="?", default="out.jpg")
    ap.add_argument("--crop", nargs=4, type=float, default=[0, 1, 0, 1])
    ap.add_argument("--w", type=int, default=1750, help="ширина листа в пикселях")
    ap.add_argument("--rot", type=int, default=0, help="поворот против часовой")
    ap.add_argument("--k", type=float, default=DEFAULT_K)
    a = ap.parse_args()

    reader = pypdf.PdfReader(a.pdf)

    if a.cmd == "info":
        n = len(reader.pages)
        print(f"страниц: {n}")
        probe = sorted({1, 2, 3, n // 2, n}) if n > 4 else range(1, n + 1)
        for p in probe:
            for obj in images(reader, p):
                mb = len(obj._data) / 1e6
                print(f"  стр.{p}: {obj['/Width']}x{obj['/Height']} px, {mb:.2f} МБ")
                break
        return

    pages = [int(x) for x in a.pages.split(",") if x.strip()]

    if a.cmd == "sharp":
        vals = [(p, sharpness(reader, p)) for p in pages]
        good = [v for _, v in vals if v]
        med = float(np.median(good)) if good else 0.0
        for p, v in vals:
            flag = "  ← НЕ В ФОКУСЕ" if v and med and v < med / 3 else ""
            print(f"  стр.{p}: резкость {v:.0f}{flag}" if v else f"  стр.{p}: нет изображения")
        return

    tiles = []
    for p in pages:
        im = prepare(reader, p, a.crop, a.rot, a.k)
        if im is None:
            continue
        tiles.append((p, im))
    if not tiles:
        sys.exit("ни одна страница не извлеклась")

    if a.cmd == "page" or len(tiles) == 1:
        p, im = tiles[0]
        r = a.w / im.size[0]
        im.resize((a.w, int(im.size[1] * r))).save(a.out, quality=92)
    else:
        cw = a.w // len(tiles)
        ch = int(cw * tiles[0][1].size[1] / tiles[0][1].size[0])
        sheet = Image.new("L", (cw * len(tiles), ch + 18), 255)
        draw = ImageDraw.Draw(sheet)
        for i, (p, im) in enumerate(tiles):
            sheet.paste(im.resize((cw, ch)), (i * cw, 18))
            draw.text((i * cw + 3, 4), str(p), fill=0)
        sheet.save(a.out, quality=92)
    print(f"{a.out}: страницы {pages}")


if __name__ == "__main__":
    main()
