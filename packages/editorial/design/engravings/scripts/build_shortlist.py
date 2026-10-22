"""Assemble shortlist.json from meta/*.json plus hand-written notes. usage: python -I build_shortlist.py ROOT"""
import json, os, sys, glob
root = sys.argv[1]
FIG = "Louis Figuier, Les Merveilles de la science (Paris: Furne, Jouvet et Cie, 1867-1891)"
SCAM = "Henry B. Scammell, Cyclopedia of Valuable Receipts (St Louis: Planet Publishing, 1897)"
PSM39 = "Popular Science Monthly, vol. 39 (1891)"
info = {
 "collection-ai-1": ("Harper's New Monthly Magazine, vol. 30, Dec 1864 ('Portion of Babbage's difference engine')", "Benjamin Herschel Babbage (per Commons)", "1864", "TOP PICK (Accidental Intelligence). The literal ancestor of the calculating machine; reads as 'machinery' even when dense. Busy at 175px, so give it the larger collection size."),
 "collection-ai-2": ("James Ferguson, Astronomy Explained upon Sir Isaac Newton's Principles, 9th edn (1794)", "James Ferguson", "1794", "Ferguson's orrery. Elegant but wide and low; a faint vertical fold/tonal band survives thresholding. Title banner and caption cropped off."),
 "collection-house-1": (SCAM + ", p.326", "Unknown (signed 'Tuttle' engraver)", "1897", "TOP PICK (Around the house). The 'Universal' clothes wringer: a bold, faintly absurd household contraption; strong silhouette at small size."),
 "collection-house-2": (FIG + ", tome 2, fig. 77", "Unknown engraver for Figuier (Breguet apparatus)", "1868", "Electric trembler bell by Breguet: 'the thing that chirps'. Clean and legible."),
 "collection-house-3": (SCAM + ", p.419", "Unknown", "1897", "A man blowing through a homemade plant vaporiser. Funniest of the set (houseplant dying), but it includes a human face in profile."),
 "collection-house-4": (SCAM + ", p.422", "Unknown", "1897", "Wardian fern case (a Victorian terrarium). Pretty, a bit leafy-dense."),
 "collection-table-1": (SCAM + ", p.309", "Unknown", "1897", "TOP PICK (At the table). Epergne (tiered table centrepiece): tall, elegant, unmistakably 'dinner party', crisp at small size."),
 "collection-table-4": (SCAM + ", p.197", "Unknown", "1897", "Tipsy cake on a fluted dish. Reads well, a little heavy; good as a backup."),
 "collection-games-1": ("Copper engraving of Kempelen's Schachspieler (Commons file 'Tuerkischer schachspieler windisch4', i.e. from Karl Gottlieb von Windisch's 1783/84 Briefe über den Schachspieler); Commons gives source only as 'copper engraving from book'", "After Wolfgang von Kempelen (per Commons)", "c.1783", "TOP PICK (Games). Kempelen's chess automaton, 'the Turk': chess plus a fake machine with a person inside, which bridges to the AI collection. Only 600px source, so it is softer than the others. The figure wears an Orientalist 'Turk' costume, so check you're comfortable with that."),
 "collection-games-2": (SCAM + ", p.1071", "Unknown", "1897", "Chess board set up for play. Very legible, but plainer, more of a diagram than an object."),
 "agents-2": (FIG + ", tome 6 (1891), fig. 476", "Unknown engraver for Figuier", "1891", "TOP PICK (Agents), with caveats. Edison's phonograph talking doll: a machine dressed up as a person that talks back. Charming and a little uncanny. It has a faint vignette edge."),
 "checking-1": (FIG + ", tome 3 (1869), fig. 83", "Unknown engraver for Figuier", "1869", "TOP PICK (Checking claims). The magnifying glass: the iconic 'look closer'. Cleanest image in the whole set."),
 "checking-2": ("Pierre de Peyster Ricketts & Edmund H. Miller, Notes on Assaying (New York, 1897), p.26 (British Library scan via Flickr Commons)", "Unknown", "1897", "Assayer's analytical short-beam balance in its glass case: literally 'assaying' claims. Text above/below cropped."),
 "checking-3": ("Encyclopaedia Britannica, 11th edn, vol. 28, p.469, 'Weighing Machines'", "Unknown", "1911", "Precision balance, a clean line diagram. 1911 is later and plainer than the others; 600px source."),
 "context-1": (FIG + ", tome 6 (1891), fig. 56", "Unknown engraver for Figuier", "1891", "TOP PICK (Context). A projection lantern (magic lantern for lectures): 'what gets put up on the screen'. Strong and legible."),
 "context-5": (FIG + ", tome 6 (1891), fig. 54", "Unknown engraver for Figuier", "1891", "Morgan enlarging lantern with bellows: a wider, lower alternative."),
 "extending-1": (SCAM + ", p.784", "Unknown", "1897", "TOP PICK (Extending). Brace and interchangeable bits: one handle, swappable attachments, which is exactly the plugin/skill/MCP idea."),
 "extending-2": ("Popular Science Monthly, vol. 70 (1907), 'Early telephone switchboard'", "Unknown", "1907 (depicts c.1878 board)", "Early plug-and-peg telephone switchboard: 'connectors'. Thin and faint at small size."),
 "extending-3": (FIG + ", tome 6 (1891), fig. 352", "Signed 'Poyet' (Louis Poyet)", "1891", "Six-way rotary switch (commutateur): pick which connection is live. Bold, dark block."),
 "harnesses-1": ("Nordisk familjebok, 2nd edn ('Uggleupplagan'), art. 'Skrifmaskin' (runeberg.org/nfce/0633, 1917); depicts Thurber's 1843 patent", "Unknown (after Charles Thurber's 1843 patent)", "1843 design / 1917 print", "Thurber's Chirographer, an 1843 typewriter on carved legs. Delightfully odd 'contraption you sit at'. Fine lines read slightly light."),
 "harnesses-2": (FIG + ", tome 5 (1891), fig. 431", "Unknown engraver for Figuier", "1891", "TOP PICK (Harnesses). Baudot telegraph keyboard with a paper copy-holder: a desk you type into that talks to a remote machine. Neatly 'CLI-ish'."),
 "harnesses-3": (FIG + ", tome 5 (1891), fig. 442", "Unknown engraver for Figuier", "1891", "Hughes printing telegraph, with a piano keyboard. Great object but wide, so small on the cover."),
 "project-1": ("Encyclopaedia Britannica, 11th edn, vol. 26, 'Surveying' (via Wikisource)", "Anonymous", "1911", "TOP PICK (Project management). Theodolite: measuring and agreeing where things are. Tall and narrow but crisp."),
 "project-2": (SCAM + ", p.24", "Unknown", "1897", "Letter-copying press: the Victorian way to keep a copy of what you agreed (version control!). Bold and clean, a wry alternative."),
 "factories-1": (PSM39 + ", 'Carpet loom with Jacquard attachment'", "Unknown (signed engraver, lower left)", "1891", "TOP PICK (Software factories). Jacquard loom: punched-card-programmed manufacturing, the ur-software-factory. Strong vertical silhouette."),
 "factories-2": (PSM39 + ", 'Knowles open shed fancy loom'", "Unknown", "1891", "Power loom, but wide and low, so it reads small."),
 "harness-eng-1": (FIG + ", tome 5 (1891), fig. 56 (Denis centrifugal governor)", "Unknown engraver for Figuier", "1891", "TOP PICK (Harness engineering). Fly-ball centrifugal governor: the classic feedback regulator that keeps the engine from running away. Detail figures erased."),
 "harness-eng-2": (FIG + ", tome 5 (1891), fig. 152", "Unknown engraver for Figuier", "1891", "Thomas Adams safety valve (section and elevation): guardrails. Bold, if a bit heavy."),
}
rejected = {
 "agents-1": "Dederick & Grass 1868 'Steam Man' patent drawing (PD-US). Rejected: the figure's face reads as an ethnic caricature, and fine patent lines plus handwriting.",
 "agents-3": "Racknitz 1789 plate III (Turk with hidden operator). Rejected: the coloured plate with tiled floor turns into a grey block at cover size.",
 "collection-games-3": "Racknitz 1789 plate I. Rejected for the same reason (muddy).",
 "collection-table-2": "Scammell 'Ready for the Guests' laid table. Rejected: too wide and tiny at cover size.",
 "collection-table-3": "Gillé 1808 typefounder's vignette, wine cup with vines (Old Book Illustrations). Rejected: wide and scrappy at cover size.",
 "context-2": "Wooton patent desk (1882 mercantile register). Rejected: the low-res etching thresholds to blotches.",
 "context-3": "Kircher's Lanterna magica (1671). Rejected: dense hatching, muddy.",
 "context-4": "Scammell 'Window gardening' (1897). Rejected: too dense at cover size (a better fit for 'Around the house' anyway).",
 "harness-eng-3": "Figuier Watt governor diagram (1867). Rejected: lettered schematic, thin at small size.",
}
out = []
for f in sorted(glob.glob(os.path.join(root, "meta", "*.json"))):
    m = json.load(open(f))
    cid = f"{m['group']}-{m['n']}"
    rec = {
        "group": m["group"], "n": m["n"], "title": m["title"],
        "source_url": m.get("source_url"), "image_url": m.get("image_url"),
        "book": None, "artist": None, "year": None,
        "license": m.get("license"), "license_url": m.get("license_url"),
        "license_templates": m.get("license_templates"),
        "clean_png": None, "cover_png": None, "notes": None, "status": None,
    }
    if cid in info:
        rec["book"], rec["artist"], rec["year"], rec["notes"] = info[cid]
        rec["clean_png"] = os.path.join(root, "clean", cid + ".png")
        rec["cover_png"] = os.path.join(root, "covers", cid + ".png")
        rec["status"] = "top-pick" if rec["notes"].startswith("TOP PICK") else "candidate"
        assert os.path.exists(rec["clean_png"]) and os.path.exists(rec["cover_png"]), cid
    else:
        rec["notes"] = rejected.get(cid, "rejected")
        rec["status"] = "rejected"
        rec["year"] = m.get("year") or m.get("date_meta")
        rec["artist"] = m.get("artist") or m.get("artist_meta")
    if cid == "collection-table-3":
        rec["book"], rec["artist"], rec["year"] = m["book"], m["artist"], m["year"]
    if not rec["license_url"]:
        rec["license_url"] = rec["source_url"]
    out.append(rec)
order = ["collection-ai", "collection-house", "collection-table", "collection-games", "agents", "context", "extending", "harnesses", "project", "factories", "checking", "harness-eng"]
out.sort(key=lambda r: (order.index(r["group"]), r["status"] == "rejected", r["status"] != "top-pick", r["n"]))
json.dump(out, open(os.path.join(root, "shortlist.json"), "w"), indent=1, ensure_ascii=False)
print(len(out), "records;", sum(r["status"] != "rejected" for r in out), "kept")
