# Your First D&D Game: fidelity review

Checked `drafts/first-dnd-game/guide.md`, version 0.1.0, against
`drafts/first-dnd-game/notes/sources.md`. The raw pages weren’t kept in the repository, so the
excerpts in `sources.md` are the evidence. The hype notes were not read. Sources fetched 22
October 2026.

| Verdict | Count |
|---|---|
| Wrong | 2 |
| Overreach | 3 |
| Unsourced | 1 |
| Naming | 2 |
| Non-public | 0 |
| Stale | 0 |

Each verdict section runs from most to least serious. The diagram labels (lines 37–51) and the
sources table (lines 160–166) were checked with the rest.

## Wrong

### W1. Dice names (line 103, Dice)

**Guide:** "Odd-shaped dice marked d4, d6, d8, d10, d12 and d20."

**Source** (Wizards of the Coast, Basic Rules, Playing the Game,
https://www.dndbeyond.com/sources/dnd/free-rules/playing-the-game): "The dice used in D&D are referred to by the letter d followed by the die’s number of sides: d4, d6, d8, d10, d12, and d20."

**Verdict:** wrong. The source says these are the dice’s names, not markings printed on them. A d6 is an ordinary cube, so "odd-shaped" doesn’t hold for every die.

**Corrected:** "Dice with 4, 6, 8, 10, 12 and 20 sides, called d4, d6, d8, d10, d12 and d20."

### W2. What a turn is (line 125, Your turn)

**Guide:** "Your turn is your place in the order of a fight."

**Source** (Basic Rules, Playing the Game, same URL): "every participant rolls Initiative; they make a Dexterity check that determines their place in the Initiative order." and "On your turn, you can move a distance up to your Speed and take one action."

**Verdict:** wrong. The source calls your place in the order your Initiative. A turn is when you move and act, which is how line 29 already defines it.

**Corrected:** "Your turn is your character’s chance to move and act in a fight. You can move up to your Speed and take one action, such as Attack, Dash, Help or Hide."

## Overreach

### O1. Dodge as "safe" (line 126, Your turn)

**Guide:** "Dodge is a safe action when you can’t decide."

**Source** (SRD 5.2.1, https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf, and Basic Rules, Playing the Game): "If you can’t decide what to do, consider taking the defensive Dodge action or the Ready action to delay acting."

**Verdict:** overreach. The source calls Dodge defensive and suggests it. It doesn’t call it safe.

**Corrected:** "Your turn is when you tell the DM what your character does. You can talk briefly without using your move or action. When you can’t decide, take the Dodge action to defend yourself."

### O2. The DM plays everyone (line 62, Dungeon Master; also line 14)

**Guide:** "The Dungeon Master is the player who runs the game, plays everyone except the players’ characters and applies the rules."

**Source** (Basic Rules, Playing the Game): "Although the DM controls all the monsters you encounter" and "describing locations and creatures that the adventurers face."

**Verdict:** overreach, low. The sources say monsters and creatures. "Everyone" is true at most tables but isn’t what the source says. Line 14, "plays everyone in it", can stay as the plain summary on page 2.

**Corrected:** "The Dungeon Master is the player who runs the game, applies the rules and controls every creature the characters meet."

### O3. Turns only in fights (line 29 and line 124)

**Guide:** "Your chance to move and act during a fight." and "The DM calling your name in Initiative order during a fight."

**Source** (Basic Rules, Playing the Game): "In certain situations—particularly combat—the action is more structured, and everyone takes turns."

**Verdict:** overreach, low. The source says turns are used particularly in combat, not only in combat. For a first game the simplification is fair. Keep "during a fight" on line 29 and soften line 124 only.

**Corrected (line 124):** "The DM calling your name during a fight. Everyone rolls Initiative when the fight starts, and that sets the order of turns."

## Unsourced

### U1. Sneaking is a Dexterity check (line 33 and diagram line 45)

**Guide:** "This follows one attempt to sneak past a guard. The DM asks for a Dexterity check because the outcome is uncertain."

**Verdict:** unsourced, low. `sources.md` gives Dexterity as "Agility, reflexes, and balance" but no source ties sneaking to a Dexterity check. The example is reasonable. Either add the Basic Rules line for the Hide action or Stealth skill to `sources.md`, or keep the example and tie it to the sourced gloss.

**Corrected (lines 33–34):** "Your character tries to sneak past a guard. The outcome is uncertain, so the DM asks for a Dexterity check, a roll that tests agility."

## Naming

### N1. Game Master (line 62, Dungeon Master)

**Guide:** "The rules’ reference document also calls this role the Game Master."

**Source** (SRD 5.2.1): "1: The Game Master Describes a Scene. The GM tells the players where their adventurers are". `sources.md` notes that the Basic Rules say Dungeon Master.

**Verdict:** naming. The SRD uses Game Master instead of Dungeon Master, so "also" suggests it uses both. "The rules’ reference document" isn’t the source’s name, and the short form GM, which the tile and many tables use, never appears.

**Corrected:** "The free System Reference Document calls the same role the Game Master (GM)."

### N2. DC and target (diagram line 50 and line 54)

**Guide:** "note 1: compares 15 with the DC" and "A target of 15 is medium difficulty, and you don’t need to know the target number before you roll."

**Source** (Basic Rules, Playing the Game): "The Dungeon Master determines target numbers and tells players whether their rolls are successful. The target number for an ability check or a saving throw is called a Difficulty Class (DC)." SRD 5.2.1: "Medium 15".

**Verdict:** naming. The diagram says DC and the text says target, and the guide never says they’re the same. The facts themselves are supported.

**Corrected (lines 54–55):** "The numbers are an example. Your modifier is the number from your character sheet that you add to the d20. The DM compares the total with a target number called the Difficulty Class (DC). A DC of 15 is medium difficulty. The DM sets the DC and tells you whether you succeed, so you don’t need to know it before you roll."

## Non-public

None. Only Wizards of the Coast’s public pages are used, and no people are named or quoted.

## Stale

None. The subtitle dates the guide "as of October 2026". The rules facts come from the 2024 Basic Rules and SRD 5.2.1, and `sources.md` notes that the parts used have the same shape in the 2014 rules.

## Sources page

- Listed but not used: none. All five sources support at least one claim.
- Used but not listed: none.
- Line 163 gives "September 2024" for Creating a Character, but `sources.md` records a page date only for Playing the Game ("posted Sep 1, 2024"). Confirm the date in the notes or leave the cell empty.
- Lines 117–118 are supported as written. If the natural 1 is added, the source is the same Playing the Game page: "If you roll a 1 on the d20 (a “natural 1”) for an attack roll, the attack misses regardless of any modifiers or the target’s AC."
