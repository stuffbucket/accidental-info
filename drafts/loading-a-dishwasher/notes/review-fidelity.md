# Loading a Dishwasher: fidelity review

Checked `drafts/loading-a-dishwasher/guide.md`, version 0.4.0, and the rack-map labels (the
`FIT_` strings in `build_guide.py`) against `notes/sources.md`. The raw pages were not kept;
the excerpts in `sources.md` were taken as the record. The hype notes were not read. Sources
fetched 22 October 2026.

| Verdict | Count |
|---|---|
| Wrong | 0 |
| Overreach | 6 |
| Unsourced | 3 |
| Naming | 2 |
| Non-public | 0 |
| Stale | 0 |

Each verdict section runs from most to least serious.

The six `FIT_` labels were checked and need no change. `FIT_BASKET` ("mix the pieces, knives
point down") is fine as an instruction; the problem is only line 137 presenting knife
direction as settled (O1).

## Overreach

### O1. Knives presented as agreed (line 137, The usual arguments)

**Guide:** "Knives point down, and mix the rest so nothing nests. For forks and spoons, makers disagree."

**Source** (GE Appliances, Dishwasher - Loading Tips,
https://products.geappliances.com/appliance/gea-support-search-content?contentId=19573):
"Load silverware in the basket with handles facing down."
Also (Whirlpool, Getting the Best Results when Using a Dishwasher,
https://producthelp.whirlpool.com/Dishwashers/Product_Info/Dishwasher_Tips_and_Tricks/Getting_the_Best_Results_when_Using_a_Dishwasher):
"Load knives down, forks up, and alternate spoons"; (Frigidaire, Dishwasher - Loading Guide,
https://owner.frigidaire.com/support-articles/article/1834625-dishwasher-loading-guide?locale=en-US):
"mix items in each section of the basket with some pointing up and some down".

**Verdict:** overreach. Setting knives apart from "makers disagree" says the makers agree on
knives. Bosch, Miele, Cascade and GE's silverware page do say knives point down, but GE's
loading-tips page (the GE page the guide lists) says all silverware handles down, Whirlpool's
"knives down" is ambiguous and Frigidaire doesn't say. In a line meant to settle the argument,
it should say "most".

**Corrected:** "Most makers say knives point down; mix so nothing nests. Makers split on forks and spoons."

### O2. Miele's safety claim stretched to spoons (line 78, Cutlery basket)

**Guide:** "Makers disagree about forks and spoons. Miele says handles down clean better, and handles up are safer."

**Source** (Miele, Operating instructions, Dishwasher G 7106,
https://media.miele.com/downloads/c7/21/00_F61547C6F7151EEDB7BBD8C9070EC721.pdf):
"To avoid the risk of injury, knives and forks should be placed with the handles upward in the cutlery basket. However, cutlery placed handle down in the basket will come out cleaner and drier."

**Verdict:** overreach. In a sentence about forks and spoons, "handles up are safer" reads as
Miele's view on both. Miele names knives and forks for safety and says nothing about spoons.
The cleaner-handles-down point is Miele's and correctly attributed.

**Corrected:** "Makers split on forks and spoons. Miele says forks are safer handles up, cleaner handles down."

### O3. "Only when full" answered with a flat yes (line 139, The usual arguments)

**Guide:** "Yes, since a dishwasher uses about the same water and energy either way. Leave room for the water to reach everything."

**Source** (ENERGY STAR, Dishwashers, https://www.energystar.gov/products/dishwashers):
"Dishwashers use about the same amount of energy and water regardless of the number of dishes inside" so "run full loads whenever possible."

**Verdict:** overreach. The question is "only when full"; ENERGY STAR says full loads
"whenever possible", not never a part load.

**Corrected:** "When you can. A dishwasher uses about the same water and energy either way. Leave room for water to reach everything."

### O4. Disagreements said to be mostly about cutlery (line 15, opening)

**Guide:** "The makers disagree on a few details, mostly about cutlery. When they do, your own dishwasher’s manual wins."

**Source** (`sources.md`, "Where sources disagree"): cutlery is one of seven listed
disagreements; the others are large items, glasses in the bottom rack, wood, pre-rinse
exceptions, filter checks and detergent type. The guide itself raises glasses (line 58).

**Verdict:** overreach. Cutlery is the loudest disagreement, not most of them.

**Corrected:** "Makers disagree on a few details, like cutlery and glasses. When they do, your own dishwasher’s manual wins."

### O5. Top rack "stays cooler" (line 58, Top rack)

**Guide:** "The top rack stays cooler, which keeps plastic from melting."

**Source** (Cascade, Tips for Loading a Dishwasher,
https://cascadeclean.com/en-us/how-to/lessons-on-loading/how-to-load-a-dishwasher/):
"Temperatures typically remain cooler on the top rack, which will prevent plastic from melting."

**Verdict:** overreach. The only source hedges with "typically"; the guide drops it. (No
dishwasher maker in the sources says this.)

**Corrected:** "The top rack usually runs cooler, so plastic won't melt."

### O6. Every detergent uses enzymes (line 117, Detergent; also line 30, tip)

**Guide (117):** "Dishwasher detergent uses enzymes to break down starch and protein."

**Guide (30):** "and dishwasher detergent contains enzymes made to break down food."

**Source** (Bosch, Use and Care Manual, Dishwasher SHP78CF5N,
https://media3.bosch-home.com/Documents/9001906312_A.pdf):
"Modern, powerful detergents mainly use a low-alkaline formulation with enzymes."

**Verdict:** overreach. Bosch says "mainly"; the guide says all dishwasher detergent.

**Corrected (117):** "Most detergents use enzymes to break down starch and protein."

**Corrected (30):** "and most dishwasher detergents use enzymes to break down food."

## Unsourced

### U1. What a third rack is (line 70, Top rack, Confused with)

**Guide:** "A third rack, on machines that have one, is a shallow tray above the top rack. Cutlery lies flat in it, grouped by kind."

**Verdict:** unsourced. No source says the third rack is shallow, sits above the top rack, or
that cutlery lies flat in it. "Grouped by kind" is Miele's advice ("utensils should be grouped
in zones, one for knives, one for forks, one for spoons"), stated here as plain fact. Either
find a public source for the description and add it to `sources.md`, or cut it.

**Corrected:** "A third rack, on machines that have one, is a cutlery tray. Miele says to group pieces in it by kind."

### U2. Top rack "often height-adjustable" (line 56, Top rack)

**Guide:** "The upper rack, often height-adjustable."

**Verdict:** unsourced. No source mentions adjustable racks. Either find a public source and
add it to `sources.md`, or cut the claim.

**Corrected:** "The upper rack, for smaller items."

### U3. Bottom rack "bigger" (line 36, Bottom rack)

**Guide:** "The lower, bigger rack."

**Verdict:** unsourced. Sources say the lower rack takes larger items, not that it is the
bigger rack. Either find a public source and add it to `sources.md`, or cut the claim.

**Corrected:** "The lower rack."

## Naming

### N1. "Cutlery drawer" and "third rack" (line 90, Cutlery basket, Confused with)

**Guide:** "A cutlery drawer works best sorted by kind. A cutlery basket works best mixed, so water can reach between the pieces."

**Source** (Miele, Operating instructions, Dishwasher G 7106,
https://media.miele.com/downloads/c7/21/00_F61547C6F7151EEDB7BBD8C9070EC721.pdf), third-rack
cutlery tray: "utensils should be grouped in zones, one for knives, one for forks, one for spoons, etc."

**Verdict:** naming. No source uses "cutlery drawer". If it means the dishwasher's third rack,
line 70 calls the same thing "third rack"; if it means the kitchen drawer, the claim is
unsourced. "Works best" also overstates Miele's "should be grouped". The basket half is
sourced (GE: "Best washing results are obtained when the silverware is mixed").

**Corrected:** "Miele says to sort a cutlery drawer (third rack) by kind. In a basket, mix pieces so water reaches between them."

### N2. "Cutlery basket" vs "silverware basket" (line 21, terms table)

**Guide:** "The basket that holds knives, forks and spoons upright."

**Source** (Bosch, Use and Care Manual, Dishwasher SHP78CF5N,
https://media3.bosch-home.com/Documents/9001906312_A.pdf): "Arrange the silverware in the
silverware basket"; also GE ("Load silverware in the basket") and Whirlpool ("Mix different
types of silverware").

**Verdict:** naming. The guide sends readers to their manual, and the US manuals call it the
silverware basket. Only Miele says "cutlery basket". The term needs its alias.

**Corrected:** "Silverware basket in US manuals. Holds cutlery upright."

## Sources page

- Listed but not used: none. All seven listed sources are used.
- Used but not listed: GE Appliances, Dishwasher - Proper Silverware Loading
  (products.geappliances.com/appliance/gea-support-search-content?contentId=18915). Line 137's
  claim that most makers say knives point down needs it, because the listed GE page says the
  opposite. Optional: Bosch, Dishwasher Operating Instructions (9001343203), which supports
  lines 13 and 57 and Bosch's own split on forks and spoons, though listed sources already
  cover those lines. Finish, ENERGY STAR Key Product Criteria and the Journal of Extension
  study are rightly left off: the guide uses none of their claims.
