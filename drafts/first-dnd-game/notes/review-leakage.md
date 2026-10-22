# Your First D&D Game: format leakage

A cold read of `drafts/first-dnd-game/guide.md`, version 0.1.0, and the built PDF (9 pages),
by a reader who has never seen an Accidental Guide. Every page was rendered and read. The PDF
text was compared with `guide.md` to find text that only the builders print.

Line numbers are `guide.md` lines. "PDF p. N" marks text only the build prints. Each finding
counts once, even when it covers several lines. "Low" marks a finding a reader would likely
get past.

First pass: `lint_guide.py` (9 errors, 0 warnings). All nine are the expected MD errors on "D&D" and aren’t reported. No classifier pass was run.

Kinds: SN self-narration, UV unnamed voices, PV presenter voice, BF borrowed framing, TR
trivia, JG jargon, TT terms-table commentary, MP mannered prose.

No table row sentence starts with It, Its, They or This. The rows on lines 26–29, 61–63,
82–84, 103–105, 124–126 and 147–152 all open with a named subject.

## Status of the last scan

No earlier scan.

## Findings

| Line | Text | Kind | Rewrite |
|---|---|---|---|
| 141, PDF p. 8 | "# How do you<br/>play well? {#apart}" prints as "How do you<br/>play well?" | SN | "# How do you play well? {#apart}". The title fits on one line. Or make `build_guide.py` honour `<br/>` in the `#apart` title as it does for `#why` and `#seq`. |
| 33 | "This follows one attempt to sneak past a guard." | SN | "Your character tries to sneak past a guard." |
| 50, 47, 45; PDF p. 3 | "compares 15 with the DC", "finds the modifier: +3", "asks for a Dexterity check" | JG | Keep the labels and define the terms next to the figure. Lines 33–34: "Your character tries to sneak past a guard. The outcome is uncertain, so the DM asks for a Dexterity check, a roll that tests agility." Lines 54–55: "The numbers are an example. Your modifier is the number from your character sheet that you add to the d20. The DM compares the total with a target number called the Difficulty Class (DC). A DC of 15 is medium difficulty. The DM sets the DC and tells you whether you succeed, so you don’t need to know it before you roll." |
| 62 | "The rules’ reference document also calls this role the Game Master." | JG | "The free System Reference Document calls the same role the Game Master (GM)." |
| 124, 133 | "in Initiative order", "Once each round" | JG | Line 124: "The DM calling your name during a fight. Everyone rolls Initiative when the fight starts, and that sets the order of turns." Line 133: "> \| When \| Once each round of turns \|" |
| 22 | "These four parts cover most of what you’ll use at the table." | SN | "Four things come up again and again at the table." |
| 150 | "Everyone gets room to contribute and have a good moment." | MP | "Each player gets a turn to speak and a chance to shine." |
| 104, 28 | "Dice are numbered shapes used to settle uncertain outcomes and amounts." and "The numbered shapes you roll when an outcome is uncertain." | MP | Line 104: "Dice are what you roll to settle uncertain results. The d20 usually decides success or failure, while the other dice mostly determine damage." Line 28: "The d20 and other dice you roll when an outcome is uncertain." |
| PDF p. 3 | Corner tile "Di" on "One roll, start to finish" | JG, low | The page covers the DM, the sheet and the dice, so a single Dice tile reads as "this is the Dice page". Drop the corner tile on the `#seq` page in `build_guide.py`. |
| PDF p. 9 | "· media.dndbeyond.com/…" and "· dndbeyond.com/how-to-play-dnd" | SN, low | The builder prints the date separator when the Date cell (lines 164 and 165) is empty. Print the separator in `build_guide.py` only when a date is present. |
| 65, 86, 107, 128 | "Field marks" | BF, low | "At a glance". This is a birdwatching term that a new player won’t know. If the label is fixed in the builder for every guide, leave it to the series review. |
| Cover, PDF pp. 1, 3, 4, 9 | Tile "Gm" next to "Dungeon Master" | JG, low | The reader meets "Gm" before "Game Master" appears on page 4. Line 57: "mono=Dm", if the key is free. Otherwise keep "Gm" and name the GM on line 62 as above. |

## Counts

| Kind | Count |
|---|---|
| SN | 4 |
| UV | 0 |
| PV | 0 |
| BF | 1 |
| TR | 0 |
| JG | 5 |
| TT | 0 |
| MP | 2 |
| Total | 12 |
