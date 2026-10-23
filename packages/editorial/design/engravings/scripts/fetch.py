"""Download candidate originals + Commons file-page metadata (license templates, source, author).

usage: python -I fetch.py CANDIDATES_JSON RAW_ROOT META_ROOT
CANDIDATES_JSON: list of {group, n, commons} or {group, n, url, ...}
"""
import json, os, re, sys, urllib.error, urllib.parse, urllib.request

UA = "AccidentalGuideResearch/0.1 (illustration shortlist; contact friend@accidental.info)"
API = "https://commons.wikimedia.org/w/api.php"


def get(url):
    import time
    for attempt in range(6):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            time.sleep(2)
            return data
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(15 * (attempt + 1))
    raise RuntimeError("rate limited: " + url)


def strip(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


cands = json.load(open(sys.argv[1]))
raw_root, meta_root = sys.argv[2], sys.argv[3]
os.makedirs(meta_root, exist_ok=True)
for c in cands:
    cid = f"{c['group']}-{c['n']}"
    d = os.path.join(raw_root, c["group"], str(c["n"]))
    if os.path.exists(os.path.join(meta_root, cid + ".json")):
        print("skip", cid)
        continue
    os.makedirs(d, exist_ok=True)
    meta = dict(c)
    if "commons" in c:
        q = {"action": "query", "format": "json", "titles": c["commons"],
             "prop": "imageinfo|revisions", "iiprop": "url|size|extmetadata",
             "rvprop": "content", "rvslots": "main"}
        data = json.loads(get(API + "?" + urllib.parse.urlencode(q)))
        p = list(data["query"]["pages"].values())[0]
        ii = p["imageinfo"][0]
        em = ii.get("extmetadata", {})
        text = p["revisions"][0]["slots"]["main"]["*"]
        meta.update({
            "source_url": ii["descriptionurl"], "image_url": ii["url"],
            "w": ii["width"], "h": ii["height"],
            "license": strip(em.get("LicenseShortName", {}).get("value")),
            "license_url": strip(em.get("LicenseUrl", {}).get("value")),
            "artist_meta": strip(em.get("Artist", {}).get("value"))[:300],
            "date_meta": strip(em.get("DateTimeOriginal", {}).get("value"))[:100],
            "credit_meta": strip(em.get("Credit", {}).get("value"))[:400],
            "desc_meta": strip(em.get("ImageDescription", {}).get("value"))[:400],
            "license_templates": re.findall(r"\{\{\s*((?:PD|Cc|CC|PD-|Public|No known|Flickr-no)[^}|]*)", text),
            "wikitext_head": text[:1500],
        })
        url = ii["url"]
    else:
        url = c["image_url"]
    ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower() or ".img"
    out = os.path.join(d, "original" + ext)
    with open(out, "wb") as f:
        f.write(get(url))
    meta["raw_path"] = out
    json.dump(meta, open(os.path.join(meta_root, cid + ".json"), "w"), indent=1, ensure_ascii=False)
    print("ok", cid, meta.get("license"), meta.get("license_templates"), out)
