import json, sys
from pathlib import Path
from PIL import Image
src = Path(sys.argv[1]); out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
(out / "img").mkdir(exist_ok=True)
recs = json.loads((src / "shortlist.json").read_text())
keep = []
for r in recs:
    clean, cover = Path(r.get("clean_png") or ""), Path(r.get("cover_png") or "")
    if not clean.is_file() or "rejected" in str(clean):
        continue
    key = f"{r['group']}-{r['n']}"
    im = Image.open(clean).convert("RGBA")
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
    bg = bg.convert("L"); bg.thumbnail((720, 720)); bg.save(out / "img" / f"{key}.png", optimize=True)
    if cover.is_file():
        c = Image.open(cover).convert("RGB"); c.thumbnail((420, 700)); c.save(out / "img" / f"{key}-cover.jpg", quality=82)
    keep.append({k: r.get(k) for k in ("group", "n", "title", "source_url", "book", "artist", "year", "license", "license_templates", "notes")} | {"key": key, "cover": cover.is_file()})
(out / "data.json").write_text(json.dumps(keep, indent=1, ensure_ascii=False))
print(len(keep))
