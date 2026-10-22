"""Composite a black line-art PNG onto a guide cover (top-right, beside the title).

usage: python -I compose.py COVER ART OUT [--frac 0.27] [--maxh 260] [--title "L1|L2"] [--subtitle "..."] [--blank-tiles 1]
Placement: right edge at the page margin (48px @ 648w), top at the kicker line. If that would overlap the
title/subtitle ink, the art is shrunk to fit the free space beside the title; if that is narrower than 70% of
the target width, the art drops below the subtitle instead (still right-aligned). Writes the chosen mode to stdout.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

a = sys.argv[1:]
cover_p, art_p, out_p = a[0], a[1], a[2]
o = dict(zip(a[3::2], a[4::2]))
frac = float(o.get("--frac", 0.27))
maxh_f = float(o.get("--maxh", 260))

cov = Image.open(cover_p).convert("RGB")
W, H = cov.size
s = W / 648.0
M = round(48 * s)
d = ImageDraw.Draw(cov)


def text_block_bottom(img, y0):
    """first y after y0 where >=40 consecutive rows are blank (white) between margins."""
    g = img.convert("L")
    blank = 0
    for y in range(y0, img.size[1]):
        row = g.crop((M, y, img.size[0] - M, y + 1))
        if row.getextrema()[0] > 235:
            blank += 1
            if blank >= round(40 * s):
                return y - blank + 1
        else:
            blank = 0
    return img.size[1]


if "--title" in o:
    tb = text_block_bottom(cov, round(100 * s))
    d.rectangle((0, round(98 * s), W, tb + 2), fill="white")
    if o.get("--blank-tiles") == "1":
        d.rectangle((0, round(630 * s), W, round(985 * s)), fill="white")
    bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", round(52 * s), index=1)
    reg = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", round(16 * s), index=0)
    y = round(108 * s)
    for line in o["--title"].split("|"):
        d.text((M, y), line, font=bold, fill=(17, 17, 17))
        y += round(57 * s)
    y += round(8 * s)
    words, line = o.get("--subtitle", "").split(), ""
    for w_ in words:
        t = (line + " " + w_).strip()
        if d.textlength(t, font=reg) > 430 * s:
            d.text((M, y), line, font=reg, fill=(17, 17, 17)); y += round(22 * s); line = w_
        else:
            line = t
    if line:
        d.text((M, y), line, font=reg, fill=(17, 17, 17))

art = Image.open(art_p).convert("RGBA")
tw = round(frac * W)
maxh = round(maxh_f * s)


def fit(img, w, h):
    r = min(w / img.size[0], h / img.size[1])
    return img.resize((max(1, round(img.size[0] * r)), max(1, round(img.size[1] * r))), Image.LANCZOS)


top = round(52 * s)
tbot = text_block_bottom(cov, round(100 * s))
g = cov.convert("L")
# rightmost ink x within the text block rows
right_ink = 0
for y in range(round(40 * s), tbot):
    row = g.crop((0, y, W, y + 1))
    px = list(row.tobytes())
    for x in range(W - M - 1, M, -1):
        if px[x] < 200:
            right_ink = max(right_ink, x)
            break
gap = round(24 * s)
free_w = (W - M) - (right_ink + gap)
im = fit(art, tw, maxh)
mode = "beside-title"
if im.size[0] > free_w:
    if free_w >= 0.7 * tw:
        im = fit(art, free_w, maxh)
        mode = "beside-title-shrunk"
    else:
        mode = "below-subtitle"
if "--fixed-top" in o:
    mode = "fixed"
    top = round(float(o["--fixed-top"]) * s)
    im = fit(art, tw, maxh)
    if top < tbot + round(16 * s):
        mode = "fixed-COLLIDES"
elif mode == "below-subtitle":
    top = tbot + round(28 * s)
    tiles_top = round(630 * s)
    im = fit(art, tw, min(maxh, tiles_top - top - round(24 * s)))
x = W - M - im.size[0]
layer = Image.new("RGBA", cov.size, (0, 0, 0, 0))
layer.paste(im, (x, top))
outimg = Image.alpha_composite(cov.convert("RGBA"), layer).convert("RGB")
outimg.save(out_p)
print(out_p, mode, im.size, "free_w", free_w)
