# Registry of key concepts

One list of the key concepts in the Accidental Guides, so a concept has the same tile code,
the same color and one owning guide everywhere. Written on 22 October 2026 from each guide's
`guide.md` and `build_guide.py`, and from the plan skill's `list_concepts.py`.
`registry.json` holds the same table for a builder to read.

"Changes per guide" lists the work each guide needed on that date. Some of it is done, such
as the code changes in the drafts, so check a guide's `guide.md` and `build_guide.py` before
you act on it. harness-engineering, running-a-software-factory and software-factory-claims
are planned guides that aren't in this repository yet. Their codes are reserved.

## Rules

- Each concept is defined in one owning guide. Another guide may show its tile (the
  per-harness guides do, as reference cards), but it points to the owner for the definition
  and covers only how that product does it.
- A concept has one two-letter code and one color family in every guide.
- No two concepts share a code. The six family codes on the catalog's tiles (`Ru`, `Wr`,
  `Ck`, `Us`, `Dm`, `Nu`) are taken too.
- Agents, Harnesses, Skills, and Tools stays as it is. Where its colors differ from the
  families, that's listed under Exceptions.

## Color families

The six families are the ones on the catalog's tiles in Accidental Intelligence. The
pairing of family and color below leaves three of the base guide's six concepts off their
family's color, the fewest possible: its three things that run already have three different
colors, and its two things an agent uses have two. Of the 720 pairings that leave three,
this one recolors the fewest tiles in the other guides (58 of 75). An earlier proposal would
have left four of the base guide's concepts off their family's color.

| Code | Family | Color | Token | Hex | Earlier proposal |
|---|---|---|---|---|---|
| Ru | Things that run | yellow | warning | `#FFCD29` | yellow |
| Wr | Things you write down | purple | figjam | `#9747FF` | blue |
| Ck | Things that check | green | success | `#14AE5C` | purple |
| Us | Things an agent uses | red-orange | danger | `#F24822` | red-orange |
| Dm | Decisions people make | pink | assistive | `#E83FBF` | green |
| Nu | Numbers and claims | blue | brand | `#0D99FF` | pink |

Hex values are the `TOKENS` in every `build_guide.py`.

## Concepts

54 concepts. "Appears in" lists the guides other than the owner that show the tile now
(tiles in entries and tiles the builders draw from `NAME2MONO`). The catalog, Accidental
Intelligence, shows the parts of its seven guides on its map and isn't listed in each row.

| Concept | Code | Family | Color | Hex | Owner | Appears in |
|---|---|---|---|---|---|---|
| Model | `Mo` | Ru | yellow | `#FFCD29` | agents-harnesses-skills-tools | — |
| Harness | `Ha` | Ru | yellow | `#FFCD29` | agents-harnesses-skills-tools | harness-engineering (outlined now) |
| Agent | `Ag` | Ru | yellow | `#FFCD29` | agents-harnesses-skills-tools | copilot-cli, visual-studio-and-vs-code (both "Custom agent"), harness-engineering (outlined now) |
| Tool | `To` | Us | red-orange | `#F24822` | agents-harnesses-skills-tools | plugins-and-marketplaces, harness-engineering (outlined now) |
| Instructions file | `In` | Wr | purple | `#9747FF` | agents-harnesses-skills-tools | claude-code, claude-desktop ("Instructions"), codex, copilot-cli, visual-studio-and-vs-code, plugins-and-marketplaces ("Instructions"), harness-engineering (outlined now) |
| Permissions | `Pe` | Dm | pink | `#E83FBF` | agents-harnesses-skills-tools | codex, harness-engineering (outlined now) |
| Settings | `Se` | Dm | pink | `#E83FBF` | none yet | claude-code, claude-desktop ("Settings and permissions"), codex ("Config file"), copilot-cli, visual-studio-and-vs-code |
| Skill | `Sk` | Wr | purple | `#9747FF` | skills | agents-harnesses-skills-tools, claude-code, claude-desktop, codex, copilot-cli, visual-studio-and-vs-code, harness-engineering (outlined now) |
| Description | `Ds` | Wr | purple | `#9747FF` | skills | — |
| Skill instructions | `Is` | Wr | purple | `#9747FF` | skills | — |
| Script | `Sr` | Us | red-orange | `#F24822` | skills | — |
| Reference file | `Rf` | Wr | purple | `#9747FF` | skills | — |
| Asset | `At` | Wr | purple | `#9747FF` | skills | — |
| MCP server | `Mc` | Us | red-orange | `#F24822` | mcp | agents-harnesses-skills-tools, claude-code, claude-desktop ("Connectors"), codex, copilot-cli, visual-studio-and-vs-code |
| Client | `Ct` | Ru | yellow | `#FFCD29` | mcp | — |
| Server entry | `En` | Dm | pink | `#E83FBF` | mcp | — |
| Transport | `Tp` | Us | red-orange | `#F24822` | mcp | — |
| Hook | `Hk` | Ru | yellow | `#FFCD29` | plugins-and-marketplaces | — |
| Plugin | `Pl` | Us | red-orange | `#F24822` | plugins-and-marketplaces | claude-code, claude-desktop |
| Marketplace | `Mk` | Wr | purple | `#9747FF` | plugins-and-marketplaces | — |
| Token | `Tk` | Nu | blue | `#0D99FF` | context-windows | — |
| Startup context | `St` | Wr | purple | `#9747FF` | context-windows | — |
| Compaction | `Cp` | Ru | yellow | `#FFCD29` | context-windows | — |
| New session | `Ns` | Ru | yellow | `#FFCD29` | context-windows | — |
| Spec | `Sp` | Wr | purple | `#9747FF` | specs-and-reviews | software-factories |
| Work item | `Wi` | Wr | purple | `#9747FF` | specs-and-reviews | software-factories |
| Tracker | `Tr` | Wr | purple | `#9747FF` | specs-and-reviews | — |
| Acceptance criteria | `Ac` | Dm | pink | `#E83FBF` | specs-and-reviews | — |
| Review | `Rv` | Ck | green | `#14AE5C` | specs-and-reviews | — |
| Orchestrator | `Or` | Ru | yellow | `#FFCD29` | software-factories | — |
| Agent session | `As` | Ru | yellow | `#FFCD29` | software-factories | harness-engineering (outlined now) |
| Gate | `Ga` | Ck | green | `#14AE5C` | software-factories | harness-engineering, running-a-software-factory (both outlined now) |
| Scenario | `Sn` | Wr | purple | `#9747FF` | lights-off-software-factories | — |
| Digital twin | `Dt` | Us | red-orange | `#F24822` | lights-off-software-factories | — |
| Satisfaction | `Sa` | Ck | green | `#14AE5C` | lights-off-software-factories | — |
| Closed loop | `Cl` | Ru | yellow | `#FFCD29` | lights-off-software-factories | — |
| Check | `Ch` | Ck | green | `#14AE5C` | harness-engineering | running-a-software-factory (outlined now) |
| Review agent | `Ra` | Ck | green | `#14AE5C` | harness-engineering | — |
| Eval | `Ev` | Ck | green | `#14AE5C` | harness-engineering | — |
| Outer loop | `Ol` | Ru | yellow | `#FFCD29` | harness-engineering | — |
| Progress file | `Pf` | Wr | purple | `#9747FF` | harness-engineering | — |
| Sandbox | `Sb` | Us | red-orange | `#F24822` | harness-engineering | running-a-software-factory (outlined now) |
| Accepted output | `Ao` | Dm | pink | `#E83FBF` | running-a-software-factory | — |
| Boundary | `Bd` | Dm | pink | `#E83FBF` | running-a-software-factory | — |
| Identity | `Id` | Dm | pink | `#E83FBF` | running-a-software-factory | — |
| Evidence | `Ed` | Ck | green | `#14AE5C` | running-a-software-factory | — |
| Back pressure | `Bp` | Dm | pink | `#E83FBF` | running-a-software-factory | — |
| Metric | `Me` | Nu | blue | `#0D99FF` | running-a-software-factory | — |
| Share of code | `Sc` | Nu | blue | `#0D99FF` | software-factory-claims | — |
| Multiplier | `Mu` | Nu | blue | `#0D99FF` | software-factory-claims | — |
| Benchmark | `Bm` | Nu | blue | `#0D99FF` | software-factory-claims | — |
| Demo | `De` | Nu | blue | `#0D99FF` | software-factory-claims | — |
| Headcount | `Hc` | Nu | blue | `#0D99FF` | software-factory-claims | — |
| Dark factory | `Df` | Nu | blue | `#0D99FF` | software-factory-claims | — |

### How the clashes were settled

Same name, same concept, one code:

- **Custom agent** (copilot-cli, visual-studio-and-vs-code) is the Agent concept. The base
  guide's Agent entry already says GitHub Copilot calls agent definitions custom agents. It
  keeps `Ag`.
- **Instructions** in claude-desktop and plugins-and-marketplaces is the instructions file
  concept, so it keeps `In`. Instructions in skills is the body of SKILL.md, a different
  concept; it becomes Skill instructions, `Is`.
- **Connectors** (claude-desktop) are MCP servers, so `Cn` becomes `Mc`. **Server** in mcp is
  the MCP server concept, so `Sv` becomes `Mc`.
- **Config file** (codex) is that product's settings, so `Cf` becomes `Se`. Permissions stays
  its own concept, `Pe`, because codex has both entries.
- **Tools** (plugins-and-marketplaces) is the Tool concept, `Tl` to `To`. **Packages** there
  is the Plugin concept, `Pk` to `Pl`.

Same code, different concepts. The newer guide changes, since the older code is already on
the catalog's map or in more guides:

| Code | Kept by | Changed |
|---|---|---|
| `As` | Agent session (software-factories) | Asset (skills) to `At` |
| `Cl` | Closed loop (lights-off-software-factories) | Client (mcp) to `Ct` |
| `De` | Demo (software-factory-claims) | Description (skills) to `Ds` |
| `In` | Instructions file (six guides) | Instructions (skills) to `Is` |
| `Sc` | Share of code (software-factory-claims) | Script (skills) to `Sr` |
| `Se` | Settings (five guides) | Server entry (mcp) to `En` |
| `Tr` | Tracker (specs-and-reviews) | Transport (mcp) to `Tp` |

### Calls that could go either way

- **Plugin** is "things an agent uses", as a bundle of tools and parts. **Marketplace** is
  "things you write down", like Tracker: what matters is the list it holds.
- **Hook** is "things that run". It can make a check binding, but its job is to run a
  command at a set moment.
- **Settings**, **Permissions** and **Server entry** are "decisions people make": values
  someone sets before the agent runs.
- **Token** is "numbers and claims". **Startup context** is "things you write down".
  **Compaction** and **New session** are "things that run".
- **Script** is "things an agent uses"; the other parts of a skill are written down.
- **Client** is "things that run" (part of the harness). **Transport** is "things an agent
  uses".

## Exceptions: Agents, Harnesses, Skills, and Tools

The base guide doesn't change. Three of its tiles stay off their family's color:

| Concept | Kept in the base guide | Family color elsewhere |
|---|---|---|
| Harness | blue | yellow |
| Agent | green | yellow |
| Tool | pink | red-orange |

Model (yellow), Skill (purple) and MCP server (red-orange) already match. The base guide also
keeps full entries for Skill and MCP server, whose owners are now skills and mcp, and keeps
one-line definitions of instructions file, plugin and hook under "Other terms". Those lines
agree with the owners and stay.

## Changes per guide

Counts are code changes, color changes, tiles that become "see the owning guide", and
outlined tiles to replace. Every guide whose colors change also needs its `build_guide.py`
`PART_TOKEN` replaced by the family table (with the pairing above),
`NAME2MONO` updated for any code change, a new `expected.sha256` and a patch version.

| Guide | Codes | Colors | See owner | Outlined |
|---|---|---|---|---|
| agents-harnesses-skills-tools | 0 | 0 | 0 | 0 |
| accidental-intelligence (catalog) | 0 | 4 families | 0 | 0 |
| claude-code | 0 | 4 | 4 | 0 |
| claude-desktop | 1 | 4 | 4 | 0 |
| codex | 1 | 4 | 4 | 0 |
| context-windows | 0 | 2 | 0 | 0 |
| copilot-cli | 0 | 3 | 4 | 0 |
| harness-engineering | 0 | 3 | 0 | 8 |
| lights-off-software-factories | 0 | 3 | 0 | 0 |
| mcp | 4 | 4 | 0 | 0 |
| plugins-and-marketplaces | 2 | 5 | 2 | 0 |
| running-a-software-factory | 0 | 5 | 0 | 3 |
| skills | 4 | 5 | 0 | 0 |
| software-factories | 0 | 4 | 2 | 0 |
| software-factory-claims | 0 | 5 | 0 | 0 |
| specs-and-reviews | 0 | 4 | 0 | 0 |
| visual-studio-and-vs-code | 0 | 3 | 4 | 0 |
| Total | 12 | 58 tiles | 24 | 11 |

### agents-harnesses-skills-tools

No changes. See Exceptions.

### accidental-intelligence (catalog)

- `FAMILY_TOKEN` in `build_guide.py`: Wr blue to purple, Ck purple to green, Dm green to pink,
  Nu pink to blue. Ru and Us stay.
- Cut "Inside each guide, tiles are colored by their order in that guide…" once the guides
  are recolored, and the sentence that Spec and work item are parts in two guides.
- Map: list Spec and Work item under Specs and Reviews only. Skill and MCP server belong to
  skills and mcp; the map has no rows for skills, mcp, context-windows or
  plugins-and-marketplaces yet.

### claude-code

- Colors: Instructions file blue to purple; Skill green to purple; MCP server purple to
  red-orange; Plugin yellow to red-orange. Settings stays pink.
- See the owning guide: Instructions file (agents-harnesses-skills-tools), Skill (skills),
  MCP server (mcp), Plugin (plugins-and-marketplaces). Settings has no owner yet.

### claude-desktop

- Codes: Connectors `Cn` to `Mc`.
- Colors: Instructions blue to purple; Skills green to purple; Connectors purple to
  red-orange; Plugins yellow to red-orange. Settings and permissions stays pink.
- See the owning guide: Instructions (agents-harnesses-skills-tools), Skills (skills),
  Connectors (mcp), Plugins (plugins-and-marketplaces).

### codex

- Codes: Config file `Cf` to `Se`.
- Colors: Instructions file blue to purple; Skill green to purple; MCP server purple to
  red-orange; Config file yellow to pink. Permissions stays pink.
- See the owning guide: Instructions file and Permissions (agents-harnesses-skills-tools),
  Skill (skills), MCP server (mcp).

### context-windows

- Colors: Startup context green to purple; Compaction purple to yellow. Token stays blue,
  New session stays yellow.

### copilot-cli

- Colors: Instructions file blue to purple; Skill green to purple; MCP server purple to
  red-orange. Custom agent stays yellow, Settings stays pink.
- See the owning guide: Instructions file and Custom agent (agents-harnesses-skills-tools),
  Skill (skills), MCP server (mcp).

### harness-engineering

- Colors: Check blue to green; Eval purple to green; Progress file pink to purple. Review
  agent, Outer loop and Sandbox keep their colors.
- Outlined tiles (`OUTLINED` in `NAME2MONO`): the series rules say no outlined tiles. Draw
  these as the owner's filled tile: Harness `Ha`, Agent and Main agent `Ag`, Tool `To`,
  Instructions file `In`, Permissions `Pe` (agents-harnesses-skills-tools); Skill `Sk`
  (skills); Agent session `As`, Gate `Ga` (software-factories). Make the rest plain text:
  Agent loop, Acceptance test, Repo, Repo owner, Person, Build-time eval.

### lights-off-software-factories

- Colors: Scenario blue to purple; Digital twin green to red-orange; Satisfaction purple to
  green. Closed loop stays yellow.

### mcp

- Codes: Server `Sv` to `Mc`; Client `Cl` to `Ct`; Server entry `Se` to `En`; Transport
  `Tr` to `Tp`.
- Colors: Server blue to red-orange; Client green to yellow; Server entry purple to pink;
  Transport yellow to red-orange.
- mcp now owns MCP server. Its entry could be named "MCP server" to match the other guides.

### plugins-and-marketplaces

- Codes: Tools `Tl` to `To`; Packages `Pk` to `Pl`.
- Colors: Tools blue to red-orange; Instructions green to purple; Hooks purple to yellow;
  Packages yellow to red-orange; Marketplaces pink to purple.
- See the owning guide: Tools and Instructions (agents-harnesses-skills-tools). It owns
  Hook, Plugin and Marketplace.
- Its cross-references say "An Accidental Guide to: Skills" and "…: MCP"; the titles are
  Agent Skills and Model Context Protocol.

### running-a-software-factory

- Colors: Accepted output blue to pink; Boundary green to pink; Identity purple to pink;
  Evidence yellow to green; Metric red-orange to blue. Back pressure stays pink.
- Outlined tiles: draw Gate `Ga` (software-factories), Check `Ch` and Sandbox `Sb`
  (harness-engineering) as the owner's filled tile. Make the rest plain text: Handoff
  artifact, Requester, Trigger, Feedback path.

### skills

- Codes: Description `De` to `Ds`; Instructions `In` to `Is`; Script `Sc` to `Sr`; Asset
  `As` to `At`. Reference file keeps `Rf`.
- Colors: Description blue to purple; Instructions green to purple; Script purple to
  red-orange; Reference file yellow to purple; Asset pink to purple.
- skills owns Skill but has no Skill tile. The per-harness guides will point here for it.

### software-factories

- Colors: Spec blue to purple; Work item green to purple; Orchestrator purple to yellow;
  Gate pink to green. Agent session stays yellow.
- See the owning guide: Spec and Work item (specs-and-reviews). Their entries keep the
  tiles but cover only what a factory does with them.

### software-factory-claims

- Colors: Multiplier, Benchmark, Demo, Headcount and Dark factory to blue. Share of code
  stays blue. The whole guide becomes one color.

### specs-and-reviews

- Colors: Spec blue to purple; Work item green to purple; Acceptance criteria yellow to pink;
  Review pink to green. Tracker stays purple.

### visual-studio-and-vs-code

- Colors: Instructions file blue to purple; Custom agent green to yellow; MCP server yellow
  to red-orange. Skill stays purple, Setting stays pink.
- See the owning guide: Instructions file and Custom agent (agents-harnesses-skills-tools),
  Skill (skills), MCP server (mcp).

## Open

- **Settings has no owner.** No guide defines settings in general; the base guide defines
  only permissions, and it isn't changing. Until one does, each per-harness guide defines
  its own settings and the tile points nowhere.
- **`Is` is close to `In`**, and both are purple. Another code, or another entry name in
  skills (such as Body), would read more clearly.
- **Trigger and Feedback path** were proposed as Software Factories parts with codes `Tr`
  and `Fp`. `Tr` is Tracker. If Trigger becomes a key, it
  needs another code.
- **Context window** has no tile in any guide. If one is added, its owner is
  context-windows.
