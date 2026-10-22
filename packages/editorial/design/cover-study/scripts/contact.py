"""Tile images into a contact sheet: contact.py out.png cols width img..."""
import sys
from PIL import Image
out, cols, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ims = [Image.open(p).convert("RGB") for p in sys.argv[4:]]
ims = [im.resize((w, round(im.height * w / im.width)), Image.LANCZOS) for im in ims]
h = max(im.height for im in ims); g = 12
rows = (len(ims) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (w + g) + g, rows * (h + g) + g), (120, 120, 120))
for i, im in enumerate(ims):
    sheet.paste(im, (g + (i % cols) * (w + g), g + (i // cols) * (h + g)))
sheet.save(out)
