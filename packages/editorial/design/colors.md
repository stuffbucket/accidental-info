# Colors across the Accidental Guides

Checked on 22 October 2026 against each guide's `build_guide.py` (`TOKENS`, `PART_TOKEN`,
`NAME2MONO`) and `guide.md` (`{#entry num=.. mono=..}`) in this worktree.

## How a part gets its color today

Every guide has the same six color tokens from the Figma swatch:

| Token | Color | Hex |
|---|---|---|
| brand | blue | `#0D99FF` |
| success | green | `#14AE5C` |
| figjam | purple | `#9747FF` |
| warning | yellow | `#FFCD29` |
| assistive | pink | `#E83FBF` |
| danger | red-orange | `#F24822` |

`PART_TOKEN` maps each part's two-letter key to a token. There are two rules in use.

- **Agents, Harnesses, Skills, and Tools** maps each part to the color it has in the team's
  harness diagram, which isn't in the guide. Skill is teal there and purple here, and the
  legend says so.
- **Every other guide** follows the series rule written in the comment above `PART_TOKEN`:
  the entry number sets the color. 01 blue, 02 green, 03 purple, 04 yellow, 05 pink,
  06 red-orange. The comment says the token names carry no meaning.

Names that aren't one of the guide's parts get no color. Harness Engineering and Running a
Software Factory draw some of them (agent session, gate, check, person and others) as an
empty outlined tile; the other guides print them as plain text.

## Every part and its color

| Guide | 01 | 02 | 03 | 04 | 05 | 06 |
|---|---|---|---|---|---|---|
| Agents, Harnesses, Skills, and Tools | Model, yellow | Harness, blue | Agent, green | Skill, purple | Tool, pink | MCP server, red |
| Software Factories | Spec, blue | Work item, green | Orchestrator, purple | Agent session, yellow | Gate, pink | |
| Lights-Off Software Factories | Scenario, blue | Digital twin, green | Satisfaction, purple | Closed loop, yellow | | |
| Running a Software Factory (draft) | Accepted output, blue | Boundary, green | Identity, purple | Evidence, yellow | Back pressure, pink | Metric, red |
| Harness Engineering (draft) | Check, blue | Review agent, green | Eval, purple | Outer loop, yellow | Progress file, pink | Sandbox, red |
| Software Factory Claims (draft) | Share of code, blue | Multiplier, green | Benchmark, purple | Demo, yellow | Headcount, pink | Dark factory, red |
| Specs, Work Items, Trackers, and Reviews | Spec, blue | Work item, green | Tracker, purple | Acceptance criteria, yellow | Review, pink | |

The same parts, by color:

| Color | Parts |
|---|---|
| Blue | Harness, Spec (twice), Scenario, Accepted output, Check, Share of code |
| Green | Agent, Work item (twice), Digital twin, Boundary, Review agent, Multiplier |
| Purple | Skill, Orchestrator, Tracker, Satisfaction, Identity, Eval, Benchmark |
| Yellow | Model, Agent session, Acceptance criteria, Closed loop, Evidence, Outer loop, Demo |
| Pink | Tool, Gate, Review, Back pressure, Progress file, Headcount |
| Red | MCP server, Metric, Sandbox, Dark factory |

## Do the colors mean anything?

Not across the series. Outside the base guide, a color says only where the part sits in
its guide's order of entries. Inside one guide, color tells the parts apart, and the thumb
tabs and cover grid look the same from guide to guide. That's what the rule was for.

In the base guide the colors mean something outside the guide (the team's diagram), but
nothing a reader of the series can use. Its Harness is blue like Check and Spec, and its
Model is yellow like Demo and Agent session.

## Do parts that share a color belong together?

Mostly no. There are a few partial clusters, and they come from entry order, not design:
guides tend to start with what's wanted and put the running loop fourth.

- **Yellow** has four things that run: Model, Agent session, Closed loop and Outer loop.
  Acceptance criteria, Evidence and Demo don't fit.
- **Blue** has three things written down before work starts: Spec, Scenario and Accepted
  output. Harness, Check and Share of code don't fit.
- **Purple** has three scores: Satisfaction, Eval and Benchmark. Skill, Orchestrator,
  Tracker and Identity don't fit.
- **Green** has Agent and Review agent, which is a coincidence. Work item, Digital twin,
  Boundary and Multiplier have nothing in common.
- **Pink** has Gate and Review, which both judge a change, next to Tool, Back pressure,
  Progress file and Headcount.
- **Red** has no cluster at all: Sandbox, Metric, MCP server and Dark factory.

Two things work against a reader who has more than one guide. Related parts get different
colors (Check is blue, Review agent green and Eval purple, though all three judge a change;
Agent is green and Agent session yellow). And the token names suggest meanings the colors
don't have: Multiplier and Work item are "success" green, and Metric and Sandbox are
"danger" red.

## Proposal: six color families

Give each of the six colors one meaning for the whole series: what kind of thing the part
is. A part takes its family's color in every guide. The palette, the tiles, the keys and the
thumb tabs stay as they are; the tabs still step down the page by entry number, so position
is still shown, just not by color.

| Family | Color | Key on the family tile | What belongs |
|---|---|---|---|
| Things that run | yellow | Ru | Programs and loops that do the work. |
| Things you write down | blue | Wr | Text that people or agents read and keep. |
| Things that check | purple | Ck | Whatever decides if a change is right. |
| Things an agent uses | red | Us | What an agent acts through or works inside. |
| Decisions people make | green | Dm | Rules a team sets before the work runs. |
| Numbers and claims | pink | Nu | Counts, scores and the claims built on them. |

The color for each family was picked to keep the most parts at the color they have now,
counting the published guides first (a script tried all 720 ways to pair six families with
six colors). Yellow, blue and purple already lean toward run, written and check. Of the 38
parts (36 names; Spec and Work item are parts in two guides), 13 keep their color and 25
change.

### Each part's family

| Part | Guide | Family | Color now | Color proposed | Changes |
|---|---|---|---|---|---|
| Model | Agents | Things that run | yellow | yellow | no |
| Harness | Agents | Things that run | blue | yellow | yes |
| Agent | Agents | Things that run | green | yellow | yes |
| Skill | Agents | Things you write down | purple | blue | yes |
| Tool | Agents | Things an agent uses | pink | red | yes |
| MCP server | Agents | Things an agent uses | red | red | no |
| Spec | Software Factories | Things you write down | blue | blue | no |
| Work item | Software Factories | Things you write down | green | blue | yes |
| Orchestrator | Software Factories | Things that run | purple | yellow | yes |
| Agent session | Software Factories | Things that run | yellow | yellow | no |
| Gate | Software Factories | Things that check | pink | purple | yes |
| Scenario | Lights-Off | Things you write down | blue | blue | no |
| Digital twin | Lights-Off | Things an agent uses | green | red | yes |
| Satisfaction | Lights-Off | Things that check | purple | purple | no |
| Closed loop | Lights-Off | Things that run | yellow | yellow | no |
| Accepted output | Running | Decisions people make | blue | green | yes |
| Boundary | Running | Decisions people make | green | green | no |
| Identity | Running | Decisions people make | purple | green | yes |
| Evidence | Running | Things that check | yellow | purple | yes |
| Back pressure | Running | Decisions people make | pink | green | yes |
| Metric | Running | Numbers and claims | red | pink | yes |
| Check | Harness Engineering | Things that check | blue | purple | yes |
| Review agent | Harness Engineering | Things that check | green | purple | yes |
| Eval | Harness Engineering | Things that check | purple | purple | no |
| Outer loop | Harness Engineering | Things that run | yellow | yellow | no |
| Progress file | Harness Engineering | Things you write down | pink | blue | yes |
| Sandbox | Harness Engineering | Things an agent uses | red | red | no |
| Share of code | Claims | Numbers and claims | blue | pink | yes |
| Multiplier | Claims | Numbers and claims | green | pink | yes |
| Benchmark | Claims | Numbers and claims | purple | pink | yes |
| Demo | Claims | Numbers and claims | yellow | pink | yes |
| Headcount | Claims | Numbers and claims | pink | pink | no |
| Dark factory | Claims | Numbers and claims | red | pink | yes |
| Spec | Specs, Work Items | Things you write down | blue | blue | no |
| Work item | Specs, Work Items | Things you write down | green | blue | yes |
| Tracker | Specs, Work Items | Things you write down | purple | blue | yes |
| Acceptance criteria | Specs, Work Items | Decisions people make | yellow | green | yes |
| Review | Specs, Work Items | Things that check | pink | purple | yes |

Calls that could go either way:

- **Review agent** runs, but its job is to judge a change, so it's in "things that check".
  Family follows the part's job in the factory, not what it's made of.
- **Gate** is where people approve, but it holds work until checks pass. It's a check.
- **Evidence** is what a change carries to show it works, so it sits with the checks
  rather than with the numbers.
- **Satisfaction** and **Eval** are scores, but each decides if a change or a setup is good
  enough. They're checks. Benchmark is a score someone reports about their own work, so it's
  a claim.
- **Tracker** is a program, but what matters is the list it holds, so it's written down.
- **Acceptance criteria** are written, but they record what the people asking for the work
  decided "done" means, like Accepted output. They're a decision.
- **Dark factory** is a kind of factory, but in Claims it's a kind of claim. The structure
  plan moves it out of Claims; if it comes back as a part anywhere, it's "things that run".

### What it costs

- **Some guides become one or two colors.** Claims would be all pink, Running all green
  except Evidence and Metric, and Specs, Work Items, Trackers, and Reviews blue except
  Acceptance criteria and Review. The two-letter key and the entry number on each tile
  still tell the parts apart, and the thumb tabs still step down the edge. Color inside a
  guide would then say what kind of thing a part is, which is the point.
- **The base guide loses its link to the team's diagram.** Harness, Agent, Skill and Tool
  change color. The legend row "In the diagram" would drop its sentence about colors. The
  base guide is at version 1.0.0, so the change is a version bump there.
- **The token names still mislead.** Pink "assistive" for numbers and red "danger" for tools
  and sandboxes mean nothing. Rename them in `TOKENS` to the family names when the change is
  made; nothing outside `build_guide.py` uses the names.

### The change in code

In each guide's `build_guide.py`, replace the series-rule comment and `PART_TOKEN` line with
a family table and one line per guide:

```python
# Each color is one family, the same in every guide of the series.
FAMILY_TOKEN = {"Ru": "warning", "Wr": "brand", "Ck": "figjam", "Us": "danger", "Dm": "success",
                "Nu": "assistive"}
PART_FAMILY = {"Sp": "Wr", "Wi": "Wr", "Or": "Ru", "As": "Ru", "Ga": "Ck"}
PART_TOKEN = {k: FAMILY_TOKEN[f] for k, f in PART_FAMILY.items()}
```

`colors()`, `avatar()`, the thumb tabs and `build_docx.py` don't change. Every guide's PDF
hash changes, so each gets a new `expected.sha256` and a patch version.

The catalog, `guides/accidental-intelligence/`, already draws every part this way: its
`build_guide.py` has the same `FAMILY_TOKEN`, and its `guide.md` lists each part with its
guide, key and family. When a guide is recolored, its rows there are the reference.

Parts the structure plan adds, such as Improvement loop in Harness Engineering, take a family
when they're written.

## Specs, Work Items, Trackers, and Reviews

Added on 22 October 2026 by another agent, as a first draft. It follows the entry-number
rule: Spec blue, Work item green, Tracker purple, Acceptance criteria yellow, Review pink.

Spec and Work item are keys here and in Software Factories, with the same two-letter keys
(`Sp`, `Wi`) and, because both are entries 01 and 02, the same colors. The structure plan's
rule is that a concept is a key in exactly one guide. Either Software Factories keeps them
as parts and names this guide for the general meaning, or the reverse; the catalog shows both
for now.
