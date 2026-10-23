"""Search Wikimedia Commons files, fetch thumbnails + license metadata, build a contact sheet.

usage: python -I commons_search.py OUTDIR "query" [limit]
"""
import json, os, re, sys, urllib.parse, urllib.request, io
from PIL import Image, ImageDraw

UA = "AccidentalGuideResearch/0.1 (illustration shortlist; contact friend@accidental.info)"
API = "https://commons.wikimedia.org/w/api.php"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def strip(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def main():
    outdir, query = sys.argv[1], sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    os.makedirs(outdir, exist_ok=True)
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrnamespace": "6", "gsrsearch": query + " filetype:bitmap", "gsrlimit": str(limit),
        "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": "260",
    }
    if query.startswith("titles="):
        titles = query[7:]
        params = {"action": "query", "format": "json", "titles": titles,
                  "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": "260"}
    data = json.loads(get(API + "?" + urllib.parse.urlencode(params)))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: (p.get("index", 0), p.get("title")))
    meta = []
    cells = []
    pages = [p for p in pages if "imageinfo" in p]
    for i, p in enumerate(pages):
        ii = p["imageinfo"][0]
        em = ii.get("extmetadata", {})
        m = {
            "i": i, "title": p["title"], "w": ii["width"], "h": ii["height"],
            "url": ii["url"], "page": ii["descriptionurl"],
            "license": strip(em.get("LicenseShortName", {}).get("value")),
            "license_url": strip(em.get("LicenseUrl", {}).get("value")),
            "artist": strip(em.get("Artist", {}).get("value"))[:120],
            "date": strip(em.get("DateTimeOriginal", {}).get("value"))[:60],
            "desc": strip(em.get("ImageDescription", {}).get("value"))[:200],
            "credit": strip(em.get("Credit", {}).get("value"))[:200],
        }
        meta.append(m)
        try:
            im = Image.open(io.BytesIO(get(ii["thumburl"]))).convert("RGB")
            im.thumbnail((240, 240))
        except Exception as e:  # noqa
            im = Image.new("RGB", (240, 240), "gray")
        cells.append(im)
        print(f"[{i}] {m['w']}x{m['h']} {m['license']} | {m['date']} | {m['title'][5:90]}")
    with open(os.path.join(outdir, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)
    cols = 5
    rows = max(1, (len(cells) + cols - 1) // cols)
    sheet = Image.new("RGB", (cols * 250, rows * 260), "white")
    d = ImageDraw.Draw(sheet)
    for i, im in enumerate(cells):
        x, y = (i % cols) * 250, (i // cols) * 260
        sheet.paste(im, (x + 5, y + 18))
        d.text((x + 5, y + 2), f"[{i}]", fill="red")
    sheet.save(os.path.join(outdir, "sheet.png"))


main()
