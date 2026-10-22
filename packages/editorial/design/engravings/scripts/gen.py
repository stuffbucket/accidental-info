import base64, html, json, re, sys
from pathlib import Path
out = Path(sys.argv[1]); fonts = Path(sys.argv[2])
data = json.loads((out / "data.json").read_text())
GROUPS = [
 ("collection-ai", "Accidental Intelligence", "Collection", "The AI guides, around the catalog."),
 ("collection-house", "Around the house", "Collection", "Smoke detectors that chirp, loading a dishwasher, is my houseplant dying."),
 ("collection-table", "At the table", "Collection", "Hosting Thanksgiving, grilled cheese, ordering wine, giving a toast."),
 ("collection-games", "Games", "Collection", "Your first D&D game, the first move and the last move in chess."),
 ("agents", "Agents", "AI group", "Agents, Harnesses, Skills, and Tools."),
 ("context", "Context", "AI group", "Context Windows."),
 ("extending", "Extending an agent", "AI group", "Agent Skills, Model Context Protocol, Plugins, Connectors, and Marketplaces."),
 ("harnesses", "Harnesses you use", "AI group", "Claude Code, Claude Desktop, GitHub Copilot CLI, OpenAI Codex, VS Code and Visual Studio."),
 ("project", "Project management", "AI group", "Specs and Reviews."),
 ("factories", "Software factories", "AI group", "Software Factories, Lights-Off Software Factories."),
 ("checking", "Checking claims", "AI group", "Software Factory Claims, coming."),
 ("harness-eng", "Harness engineering", "AI group", "Harness Engineering, coming."),
]
def b64(p): return base64.b64encode(p.read_bytes()).decode()
e = html.escape
def card(r):
    notes = (r.get("notes") or "").strip()
    top = bool(re.match(r"TOP PICK", notes))
    notes = re.sub(r"^TOP PICK \([^)]*\)(, with caveats)?\.\s*", "", notes)
    lic = ", ".join(r.get("license_templates") or []) or (r.get("license") or "")
    meta = " · ".join(x for x in [r.get("book"), r.get("year") and str(r["year"]) not in (r.get("book") or "") and str(r["year"])] if x)
    cover = f'<img class="cv" src="img/{r["key"]}-cover.jpg" alt="Sample cover with {e(r["title"])}" loading="lazy">' if r["cover"] else ""
    return f'''<figure class="plate{' top' if top else ''}" id="{r['key']}">
  <div class="sheet"><img class="en" src="img/{r['key']}.png" alt="{e(r['title'])}" loading="lazy">{cover}</div>
  <figcaption>
    <p class="id"><span class="code">{r['key']}</span>{'<span class="tile" title="Top pick">Tp</span>' if top else ''}</p>
    <p class="t">{e(r['title'])}</p>
    <p class="m">{e(meta)}</p>
    <p class="n">{e(notes)}</p>
    <p class="l"><span>{e(lic)}</span> <a href="{e(r['source_url'] or '')}" target="_blank" rel="noopener">Source</a></p>
  </figcaption>
</figure>'''
sections = []
for gid, name, kind, what in GROUPS:
    cards = [card(r) for r in data if r["group"] == gid]
    if not cards: continue
    sections.append(f'''<section class="group" aria-labelledby="h-{gid}">
  <header><p class="kind">{kind}</p><h2 id="h-{gid}">{e(name)}</h2><p class="what">{e(what)}</p></header>
  <div class="plates">{''.join(cards)}</div>
</section>''')
reg, bold = b64(fonts / "texgyreheros-regular.otf"), b64(fonts / "texgyreheros-bold.otf")
mono = b64(fonts / "LiberationMono-Regular.ttf")
page = f'''<title>Accidental Guides Engravings</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
/* Layout: a printer's specimen sheet. Each group is a row of plates; engravings sit on white paper in both themes. */
@font-face {{ font-family: "Heros"; src: url(data:font/otf;base64,{reg}) format("opentype"); font-weight: 400; }}
@font-face {{ font-family: "Heros"; src: url(data:font/otf;base64,{bold}) format("opentype"); font-weight: 700; }}
@font-face {{ font-family: "LMono"; src: url(data:font/ttf;base64,{mono}) format("truetype"); }}
:root {{
  --ground: #eef0ee; --paper: #ffffff; --ink: #121312; --muted: #5d625e; --rule: #c9cdc9;
  --tile: #0d99ff; --tile-ink: #ffffff; --link: #0b6fbd;
  --sans: "Heros", "Helvetica Neue", Helvetica, Arial, sans-serif; --mono: "LMono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --ground: #151716; --paper: #f7f7f5; --ink: #eceeec; --muted: #a2a8a3; --rule: #3a3e3b; --link: #6cbcff; color-scheme: dark; }} }}
:root[data-theme="dark"] {{ --ground: #151716; --paper: #f7f7f5; --ink: #eceeec; --muted: #a2a8a3; --rule: #3a3e3b; --link: #6cbcff; color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ background: var(--ground); color: var(--ink); font: 15px/1.5 var(--sans);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 4rem; }}
.wrap {{ max-width: 76rem; margin: 0 auto; }}
.intro {{ padding-block: 3.5rem 2rem; display: grid; gap: 1.25rem; max-width: 46rem; }}
.intro h1 {{ font-size: clamp(2rem, 5vw, 3.25rem); line-height: 1.02; margin: 0; letter-spacing: -0.02em; text-wrap: balance; }}
.intro p {{ margin: 0; color: var(--muted); max-width: 40rem; }}
.controls {{ display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; }}
.controls span {{ font-size: 0.75rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-right: 0.25rem; }}
.controls button {{ font: 600 0.875rem/1 var(--sans); padding: 0.55rem 0.9rem; border: 1px solid var(--rule); background: transparent; color: var(--ink); border-radius: 2px; cursor: pointer; }}
.controls button[aria-pressed="true"] {{ background: var(--ink); color: var(--ground); border-color: var(--ink); }}
.controls button:focus-visible, a:focus-visible {{ outline: 2px solid var(--tile); outline-offset: 2px; }}
.group {{ display: grid; grid-template-columns: minmax(0, 13rem) minmax(0, 1fr); gap: 2rem; padding-block: 2.25rem; border-top: 1px solid var(--rule); }}
.group header {{ display: grid; gap: 0.35rem; align-content: start; position: sticky; top: env(safe-area-inset-top, 0px); padding-top: 0.25rem; }}
.kind {{ margin: 0; font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); }}
.group h2 {{ margin: 0; font-size: 1.35rem; line-height: 1.15; text-wrap: balance; }}
.what {{ margin: 0; font-size: 0.85rem; color: var(--muted); }}
.plates {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr)); gap: 1.75rem; }}
.plate {{ margin: 0; display: grid; gap: 0.75rem; align-content: start; min-width: 0; }}
.sheet {{ background: var(--paper); aspect-ratio: 4 / 5; display: grid; padding: 1.25rem; overflow: hidden; min-height: 0;
  box-shadow: 0 0 0 1px rgb(0 0 0 / 0.06), 0 1px 2px rgb(0 0 0 / 0.06); }}
.sheet img {{ width: 100%; height: 100%; min-height: 0; object-fit: contain; grid-area: 1 / 1; }}
.sheet .cv {{ display: none; box-shadow: 0 0 0 1px #d9d9d9; }}
body.covers .sheet .en {{ display: none; }} body.covers .sheet .cv {{ display: block; }}
body.covers .sheet {{ padding: 0.75rem; }}
figcaption {{ display: grid; gap: 0.2rem; min-width: 0; }}
figcaption p {{ margin: 0; }}
.id {{ display: flex; align-items: center; gap: 0.5rem; }}
.code {{ font: 0.8rem/1 var(--mono); }}
.tile {{ font: 700 0.62rem/1 var(--sans); background: var(--tile); color: var(--tile-ink); padding: 0.28rem 0.3rem 0.32rem; letter-spacing: 0.02em; }}
.t {{ font-weight: 700; line-height: 1.25; }}
.m, .n, .l {{ font-size: 0.82rem; color: var(--muted); }}
.n {{ color: var(--ink); opacity: 0.86; }}
.l a {{ color: var(--link); }}
.top .sheet {{ box-shadow: 0 0 0 2px var(--tile); }}
footer {{ border-top: 1px solid var(--rule); padding-top: 1.5rem; color: var(--muted); font-size: 0.85rem; max-width: 46rem; }}
@media (max-width: 44rem) {{ .group {{ grid-template-columns: minmax(0, 1fr); gap: 1.25rem; }} .group header {{ position: static; }} }}
@media (prefers-reduced-motion: no-preference) {{ .sheet img {{ transition: opacity .2s; }} }}
</style>
<div class="wrap">
  <div class="intro">
    <h1>Engravings for the Accidental Guides</h1>
    <p>Public-domain line art for the four collections and the eight AI groups, one image per group on each guide's cover. Every licence was read on its source page. A blue edge and the Tp tile mark the top pick in each group. Reply with the codes you want, for example collection-house-2.</p>
    <div class="controls" role="group" aria-label="Show"><span>Show</span>
      <button type="button" id="show-art" aria-pressed="true">Engravings</button>
      <button type="button" id="show-covers" aria-pressed="false">On a cover</button>
    </div>
  </div>
  {''.join(sections)}
  <footer><p>Sources: Wikimedia Commons, Old Book Illustrations and the British Library. Most come from Figuier's Les Merveilles de la science (1867–91), Scammell's Cyclopedia of Valuable Receipts (1897), Popular Science Monthly (1891) and the Encyclopaedia Britannica (1911). Sample covers place the art in one fixed spot, between the subtitle and the part tiles.</p></footer>
</div>
<script>
  const a = document.getElementById("show-art"), c = document.getElementById("show-covers");
  const set = (covers) => {{ document.body.classList.toggle("covers", covers); a.setAttribute("aria-pressed", String(!covers)); c.setAttribute("aria-pressed", String(covers)); }};
  a.addEventListener("click", () => set(false)); c.addEventListener("click", () => set(true));
</script>
'''
(out / "index.html").write_text(page)
print(len(page) // 1024, "KB")
