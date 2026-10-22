# Accidental Guides: engraving shortlist

Every kept image is public domain. I read the licence template on each source page. Full records (source URL, image URL, book, artist, year, licence, licence URL, paths, notes) are in `shortlist.json`.

- `clean/<group>-<n>.png`: black line art on transparency, high resolution
- `covers/<group>-<n>.png`: sample covers
- `rejected/`: candidates I dropped, with the reasons in `shortlist.json`
- `raw/<group>/<n>/original.*`: untouched downloads
- `meta/`: per-file Commons metadata, including licence templates
- `scripts/`: the scripts used

Most images come from four sources, so the set has a consistent house style:
- Louis Figuier, *Les Merveilles de la science* (1867–91), using the Wikisource-cleaned figures on Commons
- Scammell's *Cyclopedia of Valuable Receipts* (1897)
- *Popular Science Monthly* (1891)
- *Encyclopaedia Britannica* (1911)

## Collections (home page)

| Collection | Top pick | Why | Backups |
|---|---|---|---|
| Accidental Intelligence | `collection-ai-1`: Babbage's Difference Engine (Harper's, 1864) | The ancestor of the calculating machine. It is dense, so it needs the larger collection size. | `-2`: Ferguson's orrery (1794), wide and low |
| Around the house | `collection-house-1`: the "Universal" clothes wringer (Scammell, 1897) | A bold, slightly absurd household contraption with a strong silhouette | `-2`: Breguet electric trembler bell, "the thing that chirps" (Figuier); `-3`: a man blowing through a plant vaporiser, the funniest one for "is my houseplant dying"; `-4`: Wardian fern case |
| At the table | `collection-table-1`: epergne, a tiered table centrepiece (Scammell, 1897) | Tall and elegant, unmistakably a dinner party, and crisp at small size | `-4`: tipsy cake on a fluted dish |
| Games | `collection-games-1`: Kempelen's chess automaton, "the Turk" (copper engraving, c.1783) | Chess plus a fake machine with a person inside, so it also bridges to the AI collection | `-2`: chess board set for play (Scammell); legible but plain |

## AI series groups

| Group | Top pick | Why | Backups |
|---|---|---|---|
| Agents | `agents-2`: Edison's phonograph talking doll (Figuier, 1891) | A machine dressed as a person that talks back; charming and a bit uncanny | None I'd keep (see the rejected list). The Turk works here too if Games uses the chess board. This is the weakest group. |
| Context | `context-1`: projection lantern (Figuier, 1891) | It decides what goes up on the screen | `-5`: Morgan enlarging lantern |
| Extending | `extending-1`: brace with interchangeable bits (Scammell) | One handle with swappable attachments, i.e. plugins, skills and MCP | `-3`: six-way rotary switch (Figuier, signed Poyet); `-2`: early plug-board telephone switchboard (thin at small size) |
| Harnesses you use | `harnesses-2`: Baudot telegraph keyboard with copy-holder (Figuier, 1891) | A desk you type into that drives a remote machine | `-1`: Thurber's 1843 Chirographer typewriter on carved legs (delightfully odd); `-3`: Hughes piano-keyboard printing telegraph (wide) |
| Project management | `project-1`: theodolite (EB 1911) | Measuring and agreeing where things are | `-2`: letter-copying press (Scammell), the Victorian way to keep a copy of what was agreed |
| Software factories | `factories-1`: Jacquard carpet loom (PSM, 1891) | Punched-card-programmed manufacturing | `-2`: Knowles power loom (wide, reads small) |
| Checking claims | `checking-1`: magnifying glass (Figuier, 1869) | The cleanest image in the set | `-2`: assayer's short-beam balance (*Notes on Assaying*, 1897, British Library scan); `-3`: precision balance (EB 1911) |
| Harness engineering | `harness-eng-1`: fly-ball centrifugal governor (Figuier, 1891) | A feedback regulator that stops the engine running away | `-2`: Thomas Adams safety valve, a guardrail |

## Placement on the sample covers

The brief asked for the art top-right, beside the title. On the real covers that spot doesn't exist:
- Titles run to about x≈460 ("Skills and Tools").
- Subtitles wrap to about x≈480 on a 648-wide page.
- So there are only about 90–150px free, not the 175px needed.

All samples therefore use one fixed position instead: right-aligned to the 48px margin, top at y=360, in the empty band between the subtitle and the part tiles. Sizes:
- Group images: 27% of page width (175px), at most 240px tall.
- Collection images: 32% of page width (207px), at most 250px tall.

If you want art beside the title, the title and subtitle measure (wrap width) would need to drop to about 380px.

The covers for Checking claims, Harness engineering, Around the house, At the table and Games are retitled canvases. The text is redrawn in Helvetica and the tiles are blanked.

## Cautions

- **The Turk** wears an Orientalist "Turk" costume. It is the standard historical image of the automaton, but decide whether you're comfortable with it. The source is only 600px, so it is softer than the rest.
- **The plant vaporiser** includes a human face.
- **The phonograph doll** has a faint vignette edge.
- **Credit lines** aren't legally required for public domain, but they're good practice, e.g. "Engraving from L. Figuier, *Les Merveilles de la science*, 1891".

## Rejected after viewing

- **Dederick's Steam Man patent drawing (1868):** the face reads as an ethnic caricature.
- **Racknitz Turk plates (1789):** muddy at cover size.
- **Kircher's magic lantern (1671):** too dense.
- **Wooton desk (1882):** too dense.
- **Scammell "Window gardening":** too dense.
- **Scammell laid table, "Ready for the Guests":** too wide and tiny at cover size.
- **Gillé wine-cup vignette (1808):** too wide and scrappy at cover size.
- **Figuier Watt governor diagram:** a thin, lettered schematic.

## What's kept here

The cleaned art, sample covers, contact sheet, metadata, shortlist and scripts. The untouched downloads (`raw/`), the previews and the rejected candidates are not kept in the repository; every kept image's source and image URLs are in `shortlist.json`, so `scripts/` can fetch them again.
