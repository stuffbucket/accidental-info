# Your First D&D Game: reader panel

Reviewed: `drafts/first-dnd-game/guide.md`, version 0.1.0, and its 9-page PDF built 22 October
2026. Each page was read as three readers with no access to the sources:

- **New player.** Nervous, has never played a tabletop role-playing game. Decides whether to show up feeling ready.
- **Friend.** Plays regularly and sent the invitation. Checks that nothing is wrong or misleading at a real table.
- **Skimmer.** A busy adult reading it on the way to the game. Reads the cover, page 2, the headings and page 8.

The voice pass checks the guide against the review skill’s `checklist.md`. Rewrites use the
same text as the fidelity and leakage reports where they overlap.

## Top ten fixes

Most serious first.

**1. The page 8 title prints the line-break markup.**
Page 8, line 141: "# How do you<br/>play well? {#apart}". The PDF shows "How do you<br/>play well?". Every reader sees it, and the skimmer reads this page first.
Rewrite line 141: "# How do you play well? {#apart}"

**2. The roll page uses four terms nobody has defined.**
Page 3, lines 33, 47 and 50: "a Dexterity check", "finds the modifier: +3", "compares 15 with the DC". Then line 54 calls the same number "A target of 15". The new player stops at the first diagram in the guide and can’t tell that "DC" and "target" are the same thing.
Rewrite lines 33–34: "Your character tries to sneak past a guard. The outcome is uncertain, so the DM asks for a Dexterity check, a roll that tests agility."
Rewrite lines 54–55: "The numbers are an example. Your modifier is the number from your character sheet that you add to the d20. The DM compares the total with a target number called the Difficulty Class (DC). A DC of 15 is medium difficulty. The DM sets the DC and tells you whether you succeed, so you don’t need to know it before you roll."

**3. Dice aren’t marked "d4" or "d20", and a d6 isn’t odd-shaped.**
Page 6, line 103: "Odd-shaped dice marked d4, d6, d8, d10, d12 and d20." The new player will look for printed labels that aren’t there. The friend knows d4 and d20 are names, not markings.
Rewrite line 103: "Dice with 4, 6, 8, 10, 12 and 20 sides, called d4, d6, d8, d10, d12 and d20."

**4. The turn is defined two different ways.**
Page 7, line 125: "Your turn is your place in the order of a fight." Page 2, line 29, says "Your chance to move and act during a fight." Your place in the order is set by Initiative. Your turn is when you act. The friend would correct this at the table.
Rewrite line 125: "Your turn is your character’s chance to move and act in a fight. You can move up to your Speed and take one action, such as Attack, Dash, Help or Hide."

**5. Page 7 says to decide on your turn, and page 8 says to decide before it.**
Line 126: "Your turn is when you decide what your character does next." Line 149: "Plan before your turn". The new player gets two instructions that disagree. Line 126 also joins two ideas and calls Dodge "safe" without saying what it does.
Rewrite line 126: "Your turn is when you tell the DM what your character does. You can talk briefly without using your move or action. When you can’t decide, take the Dodge action to defend yourself."

**6. Nothing says where your character comes from.**
Page 2, lines 18–20. The new player’s first worry is whether to make a character before the game. The friend would want the reader to ask. The skimmer needs it before arriving.
Rewrite lines 18–20: "You only need a small part of the rules for your first game. Say what you want your character to do, and the DM will tell you what to roll. Your character sheet has the numbers you need. Nobody expects you to arrive knowing every rule. Before the game, ask the DM whether to make a character or use one they give you."

**7. Armor Class and Hit Points appear without a word on what they are.**
Page 5, line 83: "The numbers you’ll use most include ability modifiers, Armor Class, Hit Points, Speed and attack bonus." The new player gets five game terms in a row, two of them with no clue.
Rewrite line 83 (after the first sentence): "The numbers you’ll use most are your ability modifiers, Armor Class, Hit Points, Speed and attack bonus. Armor Class is the number an attack against you has to reach. Hit Points go down when you take damage."

**8. Initiative and round are used without explanation.**
Page 7, line 124: "The DM calling your name in Initiative order during a fight." Line 133: "Once each round". The new player doesn’t know either word.
Rewrite line 124: "The DM calling your name during a fight. Everyone rolls Initiative when the fight starts, and that sets the order of turns."
Rewrite line 133: "> | When | Once each round of turns |"

**9. The natural 20 section doesn’t say what it’s confused with, and it leaves out the natural 1.**
Page 6, lines 117–118. The confusion is between a natural 20 and a total of 20. The new player will hear "nat 1" at the table too.
Rewrite lines 117–118: "A natural 20 means the d20 itself shows 20. A total of 20 after adding your modifier isn’t a natural 20. On an attack roll, a natural 20 always hits and a natural 1 always misses."

**10. The Bonus Action section never says what a Bonus Action is.**
Page 7, lines 138–139: "An action is something every character can take on a turn. You get a Bonus Action only when…". The new player learns when they get one, but not what it is.
Rewrite lines 138–139: "Every character can take one action on each turn. A Bonus Action is something extra you can do on your turn. You get a Bonus Action only when a feature, spell or ability on your character sheet says so."

## Page by page

### Page 2: What happens at a D&D game?

| Reader | Stops at | Why |
|---|---|---|
| New player | Nothing about where the character comes from (lines 18–20) | See fix 6. |
| Friend | None | The DM, the roll and the rules load are right. |
| Skimmer | None | This page and page 8 are enough for the trip. |

Rewrite: fix 6.

### Page 3: One roll, start to finish

| Reader | Stops at | Why |
|---|---|---|
| New player | "compares 15 with the DC" (line 50) | DC, modifier and Dexterity are undefined (fix 2). |
| Friend | "asks for a Dexterity check" (line 45) | Many DMs say "Stealth check" here. A new player won’t connect the two. A nit, and fix 2’s gloss helps. |
| Skimmer | The diagram | Skips it, which is fine once the text under it explains the total and the DC. |

Rewrite: fix 2.

### Page 4: Dungeon Master

| Reader | Stops at | Why |
|---|---|---|
| New player | "The rules’ reference document also calls this role the Game Master." (line 62) | Doesn’t know what a reference document is. Will hear "GM" at many tables, and the page tile says "Gm". |
| Friend | None | |
| Skimmer | None | |

Rewrite line 62, second sentence: "The free System Reference Document calls the same role the Game Master (GM)."

### Page 5: Character sheet

| Reader | Stops at | Why |
|---|---|---|
| New player | "Armor Class, Hit Points" (line 83) | Fix 7. |
| Friend | None | |
| Skimmer | "You’re not expected to know every rule" (line 97) | Fourth time the guide says this (lines 18, 20, 147). |

Rewrite lines 96–97: "The character sheet records your character, while a rulebook explains the game. The DM applies the rules, so ask the DM when you’re unsure how one works."

### Page 6: Dice

| Reader | Stops at | Why |
|---|---|---|
| New player | "marked d4, d6…" (line 103), "For 1d8 + 2" (line 105) | Fix 3. With "1d" the example doesn’t show that the first number is how many dice to roll. |
| Friend | Line 103, lines 117–118 | Fixes 3 and 9. |
| Skimmer | None | |

Rewrite line 105: "The die’s name tells you how many sides it has. In 3d8 + 5, roll three eight-sided dice, add them together and add 5."

### Page 7: Your turn

| Reader | Stops at | Why |
|---|---|---|
| New player | "Initiative order" (line 124), "Once each round" (line 133) | Fix 8. |
| Friend | "your place in the order of a fight" (line 125) | Fix 4. |
| Skimmer | "Include unlimited actions" (line 134) | Reads oddly in bold. |

Rewrite line 134: "> | Cannot | Take more than one action |"

### Page 8: How do you play well?

| Reader | Stops at | Why |
|---|---|---|
| New player | "Plan before your turn" (line 149) | Disagrees with line 126 (fix 5). |
| Friend | None | The habits match what a regular player would say. |
| Skimmer | The title (line 141) | Fix 1. |

Rewrite: fixes 1 and 5.

## Voice pass

| Line | Text | Rule | Rewrite |
|---|---|---|---|
| 150 | "Everyone gets room to contribute and have a good moment." | Regular English that doesn’t call attention to itself | "Each player gets a turn to speak and a chance to shine." |
| 104 | "Dice are numbered shapes used to settle uncertain outcomes and amounts." | Vague stand-in | "Dice are what you roll to settle uncertain results. The d20 usually decides success or failure, while the other dice mostly determine damage." |
| 82 | "Your character’s name and numbers, printed, in an app or on plain paper." | Sentence reads on its own | "Your character’s name and numbers on a printed page, in an app or on plain paper." |
| 22 | "These four parts cover most of what you’ll use at the table." | Nothing about the guide itself | "Four things come up again and again at the table." |

No row sentence starts with It, Its, They or This.

## Verdict

All three readers would finish. The new player gets the shape of a game from page 2 and page 8 but stalls on page 3 and page 7, where DC, modifier, Initiative and round go unexplained. The friend would correct only the dice line and the turn definition. The skimmer comes away knowing to say what the character does and let the DM name the roll. Fixes 1 to 6 matter most.
