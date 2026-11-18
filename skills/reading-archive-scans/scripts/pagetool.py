#!/usr/bin/env python3
"""Extracts pages from an archival PDF without re-encoding and assembles contact sheets.

The embedded image is taken as a raw JPEG (o._data), so there is no loss.
Requires: pypdf, Pillow, numpy.

  python3 pagetool.py info   FILE.pdf                       - pages, sizes, MB per page
  python3 pagetool.py sharp  FILE.pdf 55,57,59              - sharpness (defective shots)
  python3 pagetool.py page   FILE.pdf 128 out.jpg [options]   - one page
  python3 pagetool.py sheet  FILE.pdf 241,243,245 out.jpg [options] - several in a row

Options: --crop x0 x1 y0 y1 (fractions 0..1) --w WIDTH --rot DEGREES --k COEFF
"""
import argparse, io, sys
import numpy as np
import pypdf
from PIL import Image, ImageDraw, ImageFilter

# Background blur radius: ~1% of the sheet height. Smaller eats the letter strokes,
# larger does not remove uneven lighting and the shadow at the spine.
BLUR_RADIUS = 11
# Contrast gain. Above 1.8 JPEG artefacts turn into false strokes.
DEFAULT_K = 1.6
# Histogram clipping: 2% at each end removes outliers (hole punch, shadow),
# without touching the ink itself.
CLIP_LO, CLIP_HI = 2, 98


def images(reader, page_no):
    """All images on the page (usually one). page_no starts at 1."""
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
    """The page as is, in greyscale. None if there is no image."""
    for obj in images(reader, page_no):
        try:
            return Image.open(io.BytesIO(obj._data)).convert("L")
        except Exception as exc:                      # broken stream - do not crash
            print(f"p.{page_no}: unreadable ({exc})", file=sys.stderr)
    return None


def enhance(im, k=DEFAULT_K):
    """Background subtraction + stretch. Brings out faded ink."""
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
    """Variance of the Laplacian. A third of the median of the neighbours or lower - out of focus."""
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
    ap.add_argument("--w", type=int, default=1750, help="sheet width in pixels")
    ap.add_argument("--rot", type=int, default=0, help="counter-clockwise rotation")
    ap.add_argument("--k", type=float, default=DEFAULT_K)
    a = ap.parse_args()

    reader = pypdf.PdfReader(a.pdf)

    if a.cmd == "info":
        n = len(reader.pages)
        print(f"pages: {n}")
        probe = sorted({1, 2, 3, n // 2, n}) if n > 4 else range(1, n + 1)
        for p in probe:
            for obj in images(reader, p):
                mb = len(obj._data) / 1e6
                print(f"  p.{p}: {obj['/Width']}x{obj['/Height']} px, {mb:.2f} MB")
                break
        return

    pages = [int(x) for x in a.pages.split(",") if x.strip()]

    if a.cmd == "sharp":
        vals = [(p, sharpness(reader, p)) for p in pages]
        good = [v for _, v in vals if v]
        med = float(np.median(good)) if good else 0.0
        for p, v in vals:
            flag = "  <- OUT OF FOCUS" if v and med and v < med / 3 else ""
            print(f"  p.{p}: sharpness {v:.0f}{flag}" if v else f"  p.{p}: no image")
        return

    tiles = []
    for p in pages:
        im = prepare(reader, p, a.crop, a.rot, a.k)
        if im is None:
            continue
        tiles.append((p, im))
    if not tiles:
        sys.exit("no page could be extracted")

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
    print(f"{a.out}: pages {pages}")


if __name__ == "__main__":
    main()
