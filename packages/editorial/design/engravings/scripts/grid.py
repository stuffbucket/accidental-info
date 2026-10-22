"""Overlay a 10x10 fraction grid on an image for picking crop coords. usage: python -I grid.py IN OUT"""
import sys
from PIL import Image, ImageDraw
im = Image.open(sys.argv[1]); im.seek(0); im = im.convert("RGB")
im.thumbnail((900, 900))
d = ImageDraw.Draw(im); W, H = im.size
for i in range(1, 10):
    d.line((W * i / 10, 0, W * i / 10, H), fill=(255, 0, 0)); d.line((0, H * i / 10, W, H * i / 10), fill=(255, 0, 0))
    d.text((W * i / 10 + 2, 2), str(i), fill=(255, 0, 0)); d.text((2, H * i / 10 + 2), str(i), fill=(255, 0, 0))
im.save(sys.argv[2])
