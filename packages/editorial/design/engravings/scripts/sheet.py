"""Contact sheet of transparent PNGs on white. usage: python -I sheet.py OUT cell IN1 IN2 ..."""
import os, sys
from PIL import Image, ImageDraw

out, cell, files = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
cols = 5
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (cell + 10), rows * (cell + 24)), "white")
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGBA")
    im.thumbnail((cell, cell), Image.LANCZOS)
    x, y = (i % cols) * (cell + 10), (i // cols) * (cell + 24)
    bg = Image.new("RGBA", im.size, "white")
    bg.alpha_composite(im)
    sheet.paste(bg.convert("RGB"), (x + 5, y + 20))
    d.text((x + 5, y + 4), os.path.basename(f), fill="red")
sheet.save(out)
