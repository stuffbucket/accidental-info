"""Convert an engraving scan to one-colour black line art on transparency.

usage: python -I clean.py IN OUT [--crop l,t,r,b] [--thr N|otsu] [--minside PX] [--despeck N]
  --crop  fractions of width/height to keep (left,top,right,bottom), e.g. 0,0,1,0.9
  --thr   luminance threshold (0-255); pixels darker become ink. default: otsu
  --minside upscale so the shorter side is at least PX before thresholding (default 1600)
  --despeck remove connected specks smaller than N pixels (default 0 = off)
"""
import sys
from PIL import Image, ImageOps, ImageFilter

Image.MAX_IMAGE_PIXELS = 300_000_000


def otsu(hist):
    total = sum(hist)
    sum_all = sum(i * h for i, h in enumerate(hist))
    wb = sb = 0
    best, thr = 0, 128
    for t in range(256):
        wb += hist[t]
        if wb == 0:
            continue
        wf = total - wb
        if wf == 0:
            break
        sb += t * hist[t]
        mb, mf = sb / wb, (sum_all - sb) / wf
        between = wb * wf * (mb - mf) ** 2
        if between > best:
            best, thr = between, t
    return thr


def main():
    a = sys.argv[1:]
    src, out = a[0], a[1]
    opts = dict(zip(a[2::2], a[3::2]))
    im = Image.open(src)
    im.seek(0)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, "white")
        bg.alpha_composite(im)
        im = bg
    g = im.convert("L")
    if "--crop" in opts:
        l, t, r, b = [float(x) for x in opts["--crop"].split(",")]
        W, H = g.size
        g = g.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
    if "--erase" in opts:  # semicolon-separated rects in fractions of the (cropped) image
        from PIL import ImageDraw
        dr = ImageDraw.Draw(g)
        W, H = g.size
        for rect in opts["--erase"].split(";"):
            l, t, r, b = [float(x) for x in rect.split(",")]
            dr.rectangle((l * W, t * H, r * W, b * H), fill=255)
    minside = int(opts.get("--minside", 1600))
    s = min(g.size)
    if s < minside:
        f = minside / s
        g = g.resize((round(g.size[0] * f), round(g.size[1] * f)), Image.LANCZOS)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = g.filter(ImageFilter.GaussianBlur(0.6))
    thr = opts.get("--thr", "otsu")
    t = otsu(g.histogram()) if thr == "otsu" else int(thr)
    ink = g.point(lambda v: 255 if v < t else 0, "L")  # 255 = ink
    n = int(opts.get("--despeck", 0))
    if n:
        # crude despeckle: open with a small min/max filter pair
        ink = ink.filter(ImageFilter.MinFilter(n)).filter(ImageFilter.MaxFilter(n))
    bbox = ink.getbbox()
    if bbox:
        pad = 8
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(ink.size[0], bbox[2] + pad), min(ink.size[1], bbox[3] + pad))
        ink = ink.crop(bbox)
    rgba = Image.new("RGBA", ink.size, (0, 0, 0, 0))
    rgba.putalpha(ink)
    rgba.save(out, optimize=True)
    print(out, "thr", t, "size", rgba.size)


main()
