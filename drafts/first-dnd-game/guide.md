---
title: Your First D&D Game
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to sitting down at your first Dungeons & Dragons table, as of October 2026.
running_footer: Your First D&D Game
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
collection: Games
collection_mark: diamond
number: 01
version: 0.5.0
---

# What happens at<br/>a D&D game? {#why}

D&D is a story you tell together. The Dungeon Master (DM) describes the world and plays
everyone in it. Each other player controls one character and says what that character
tries to do. When the result is uncertain, the DM asks for a roll and the dice help decide
what happens.

You only need a small part of the rules for your first game. Say what you want your
character to do, and the DM tells you what to roll from the numbers on your character sheet.

These four cover most of what you’ll use.

> | Term | Meaning |
> |---|---|
> | Dungeon Master | The player who describes the world, runs the game and applies the rules. |
> | Character sheet | The page or app that holds your character’s numbers and abilities. |
> | Dice | The d20 and the other dice you roll when an outcome is uncertain. |
> | Your turn | Your chance to move and act during a fight. |

# One roll,<br/>start to finish {#seq}

Your character tries to sneak past a guard. The outcome is uncertain, so the DM asks for
a Dexterity check, a roll for moving quietly.

```diagram
part You |  | a player
part Dungeon Master | Gm | runs the game
part Character sheet | Cs | your numbers
part Dice | Di | the d20
band The scene
msg 1 -> 0: describes the scene
msg 0 -> 1: says what your character tries
band The roll
msg 1 -> 0: asks for a Dexterity check
msg 0 -> 3: rolls the d20: 12
msg 0 -> 2: finds the modifier: +3
msg 0 -> 1: says the total: 15
band The result
note 1: compares 15 with the DC
msg 1 --> 0: narrates what happens
```

The numbers are an example. The DM compares your total with a target called the
Difficulty Class (DC), where 15 is medium.

# Dungeon Master {#entry num=01 mono=Gm}

| Field | Text |
|---|---|
| Identify by | The player who describes each scene and asks what you do. |
| What | The Dungeon Master is the player who runs the game, applies the rules and plays every creature the characters meet. In the free rules reference, the role is the GM, short for Game Master. |
| So what | The DM turns everyone’s choices into one story and decides when a roll is needed. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Who | One player |
> | When | Throughout the game |
> | Cannot | Decide your character’s choices |

## Confused with: Opponent

The DM plays the monsters, but the DM isn’t your opponent. The DM applies the rules and
helps the whole table tell the story.

# Character sheet {#entry num=02 mono=Cs}

| Field | Text |
|---|---|
| Identify by | Your character’s name and numbers, printed, in an app or on plain paper. |
| What | A character sheet is the record of what your character can do. You’ll use a few numbers most: ability modifiers, attack bonus, Speed, Armor Class (what an attack on you must reach) and Hit Points (which go down as you take damage). |
| So what | The character sheet has the modifier you add when the DM asks for a roll, so keep it in front of you. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Who | You, for your character |
> | When | During play |
> | Cannot | Explain every rule |

## Confused with: Rulebook

The character sheet records your character, and a rulebook explains the game. Ask the DM
before the game whether to make a character or use one you’re given.

# Dice {#entry num=03 mono=Di}

| Field | Text |
|---|---|
| Identify by | Dice with 4, 6, 8, 10, 12 and 20 sides, called d4, d6, d8, d10, d12 and d20. |
| What | Dice are what you roll to settle uncertain results. The d20 decides success or failure, and the other dice mostly roll damage. |
| So what | In 2d6 + 1, the 2 is how many dice, the 6 is how many sides, and you add 1 to the total. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Who | Everyone at the table |
> | When | When the DM asks |
> | Cannot | Choose what you attempt |

## Confused with: Natural 20

A natural 20 means the d20 itself shows 20, before you add anything. On an attack roll, a
natural 20 always hits and a natural 1 always misses.

# Your turn {#entry num=04 mono=Tn}

| Field | Text |
|---|---|
| Identify by | The DM calling your name in a fight. Everyone rolls Initiative when the fight starts, and that sets the order of turns. |
| What | Your turn is your character’s chance to move and act in a fight. You can move up to your Speed and take one action, such as Attack, Dash, Help or Hide. |
| So what | Your turn is when you tell the DM what your character does. Talking briefly is free. When you can’t decide, the Dodge action makes you harder to hit. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Who | Your character |
> | When | Once each round of turns |
> | Cannot | Take more than one action |

## Confused with: Bonus Action

A Bonus Action is an extra action on your turn. You get one only when a feature,
spell or ability on your character sheet says so.

# How do you play well? {#apart}

Most of it is arriving ready and sharing the fun.

> | Habit | Why it helps |
> |---|---|
> | Know your character’s basics | A rough idea of what your character can do is enough. |
> | Bring dice, pencil and paper | You can roll when asked and note what changes. |
> | Plan your turn while others play | Thinking ahead keeps the fight moving when the DM calls your name. |
> | Listen before you speak | Everyone at the table gets a chance to shine. |
> | Choose actions everyone enjoys | Your character’s choices should add to the whole table’s fun. |

When you’re unsure, ask the DM.

# Sources {#sources}

These public sources were checked on 22 October 2026. Dungeons & Dragons and D&D are trademarks of Wizards of the Coast, used here only to name the game.

| Source | Date | Address |
|---|---|---|
| Wizards of the Coast, Basic Rules: Playing the Game | September 2024 | dndbeyond.com/sources/dnd/free-rules/playing-the-game |
| Wizards of the Coast, Basic Rules: Creating a Character | September 2024 | dndbeyond.com/sources/dnd/free-rules/creating-a-character |
| Wizards of the Coast, System Reference Document 5.2.1, CC BY 4.0 | April 2025 | media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf |
| D&D Beyond, How to Play D&D |  | dndbeyond.com/how-to-play-dnd |
| D&D Beyond, Playing D&D for the First Time? Here Are Some Tips | January 2018 | dndbeyond.com/posts/139-playing-d-d-for-the-first-time-here-are-some-tips |
