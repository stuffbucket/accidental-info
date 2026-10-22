# Grilled Cheese: reader panel

Reviewed: `drafts/grilled-cheese/guide.md`, version 0.2.0, and its 7-page PDF built October
2026. Each page was read as three readers with no access to the sources:

- **Teen.** A teenager making a first grilled cheese. Follows the steps literally and knows
  few kitchen words.
- **Mayo cook.** A confident home cook who spreads mayonnaise on the bread and argues about
  it. Reads for the reasoning and checks it.
- **Parent.** A parent skimming it with lunch already on the stove. Reads the steps page,
  glances at the rest, and needs to know what to do right now.

The voice pass checks the guide against the review skill’s `checklist.md`.

## Top ten fixes

Most serious first.

**1. The flip step can’t be done as written.**
Page 3, line 38: "Lift the sandwich with a spatula. Melt another half tablespoon of butter,
then lay the sandwich back down on its other side." The teen and the parent stop here. One
hand holds a spatula with a hot sandwich on it while the butter is meant to melt. Neither
knows where to put the sandwich meanwhile.
Rewrite line 38: "| Flip | Turn the sandwich over with a spatula. Add another half tablespoon of butter to the pan and let it melt under the bread. |"

**2. The steps never say lid on or lid off.**
Page 3, lines 34 to 39 have no lid instruction. Page 6 (line 122 and line 132) gives both
sides. The parent, lid in hand, can’t tell what to do. The method should pick one.
Rewrite line 37: "| Cook the first side | Cook uncovered and without pressing until the bottom is golden, about 3 to 5 minutes. |"

**3. The guide makes the case for mayonnaise and not for butter.**
Page 5, lines 102 to 103: "Mayonnaise has a higher smoke point than butter, so it browns
without burning." Page 5, line 98: "Butter getting dark too quickly". Page 6, line 131:
"Butter gives the usual buttery result." The mayo cook reads this as a win: mayonnaise gets
a reason, butter gets a warning and a tautology. A reader who keeps burning sandwiches would
switch to mayonnaise.
Rewrite line 131: "| Butter or mayonnaise? | Butter soaks into the bread and tastes of butter. Mayonnaise has a higher smoke point, so it can brown the bread without burning. |"

**4. There is no step for putting the sandwich together.**
Page 3, line 36: "Lay the assembled sandwich in the melted butter." The teen hasn’t been
told to assemble anything, or that the cheese goes between the slices before the pan.
Rewrite line 36: "| Add the sandwich | Put the cheese between two slices of bread. Lay the sandwich in the melted butter. |"

**5. "Low" heat on the Heat page contradicts medium-low.**
Page 6, line 111: "Low, steady heat gives the cheese time to melt." The teen turns the knob
to low. Every other line says medium-low.
Rewrite line 111: "| So what | Medium-low heat gives the cheese time to melt. High heat can brown the bread before the cheese melts. |"

**6. The tip reads like a warning.**
Page 3, lines 42 to 43: "Shredded cheese melts faster than sliced cheese, so it can melt
before the bread finishes toasting." In a guide about burnt bread, "can melt before the
bread finishes" sounds like a problem. The parent skips shredded cheese, which is the
opposite of the point.
Rewrite lines 42 to 43: "Shredded cheese melts faster than sliced cheese, so all of it melts before the bread finishes toasting."

**7. "Every camp" is followed by a row with no camps.**
Page 6, line 126: "Every camp makes a good sandwich" and line 133: "Don’t press the sandwich.
Let each side cook undisturbed until it is golden." The mayo cook notices the only rule on
the page arrives without a reason or another side.
Rewrite line 133: "| Press it flat? | The one recipe that mentions pressing says not to. Let each side turn golden undisturbed. |"

**8. Aged cheese is ruled out and recommended on the same page.**
Page 5, lines 82 to 83: "Parmesan and Manchego are hard, aged cheeses kept for a cheese
board." Line 70 recommends sharp cheddar, an aged cheese. The mayo cook stops believing
the cheese advice.
Rewrite lines 82 to 83: "Parmesan and Manchego are hard cheeses best kept for a cheese board. A melting cheese such as American or sharp cheddar goes in the sandwich."

**9. Butter on the bread gets one bare sentence.**
Page 6, line 130: "Buttering the outside of the bread works." The mayo cook, who spreads fat
on the bread, sees the guide brush off the method most cooks know. Saying one recipe does
both is fair and keeps the argument light.
Rewrite line 130: "| Butter the bread or the pan? | Spreading butter on the outside of each slice works. Melting it in the pan works too, and the bread soaks it up. One recipe does both. |"

**10. "The slices" means bread on one line and cheese on the line before.**
Page 5, lines 69 to 70: "Slices or a handful of shredded cheese." then "Cheese is the
filling that melts between the slices." The teen reads "the slices" as cheese slices.
Rewrite line 70: "| What | Cheese is the filling that melts between the bread. American, sharp cheddar and Swiss all melt well. |"

## Page by page

### Page 1: cover

| Reader | Stops at | Why |
|---|---|---|
| Teen | "Cs" tile (line 65) | Expects "Ch" for cheese. A small puzzle, not a stop. |
| Mayo cook | none | |
| Parent | Tiles list Bread, Cheese, Butter, Heat | Wants the steps, which are on page 3 and not listed. Turns pages to find them. |

Rewrite: none in `guide.md`. The cover lists only entries, which is a builder choice.

### Page 2: What makes a good grilled cheese?

| Reader | Stops at | Why |
|---|---|---|
| Teen | none | Clear. The terms table helps. |
| Mayo cook | "Butter melted in the pan does the browning." (line 14 to 15) | Disbelieves. Browns with fat on the bread and sees no hint that it works. |
| Parent | none | Takes "medium-low" and moves on. |

Rewrite lines 14 to 15: "Butter melted in the pan does the browning. Butter spread on the bread works too."

### Page 3: How does it come together?

| Reader | Stops at | Why |
|---|---|---|
| Teen | "Set a skillet over medium-low heat." (line 34) | May not know a skillet is a frying pan. The next row says "pan". |
| Teen | "Lay the assembled sandwich in the melted butter." (line 36) | Never told to assemble it. Fix 4. |
| Teen | Flip row (line 38) | Can’t do it as written. Fix 1. |
| Mayo cook | none | Follows the steps. Waits for the mayonnaise question. |
| Parent | Flip row (line 38) | Same as the teen, with the pan already hot. |
| Parent | No lid instruction (lines 34 to 39) | Fix 2. |
| Parent | Tip (lines 42 to 43) | Reads it as a warning. Fix 6. |

Rewrite line 34: "| Heat the pan | Set a skillet, or frying pan, over medium-low heat. |"

### Page 4: Bread

| Reader | Stops at | Why |
|---|---|---|
| Teen | "Bread is the outside of the sandwich, which turns crisp in the pan." (line 50) | "Which" could mean the sandwich. A small stumble. |
| Mayo cook | "Confused with: Panini" (line 60) | A panini is a pressed sandwich, not a kind of bread. The pairing feels off on a Bread page. |
| Parent | none | Skips the page. |

Rewrite line 50: "| What | Bread is the outside of the sandwich and turns crisp in the pan. Sliced white bread is the usual choice, and sourdough or potato bread work too. |" (Rye is also unsourced. See the fidelity review.)

Rewrite lines 60 to 63: "## Confused with: Focaccia" then "Focaccia is an airy bread. Melted cheese might seep through it and burn in the pan."

### Page 5: Cheese and Butter

| Reader | Stops at | Why |
|---|---|---|
| Teen | "melts between the slices" (line 70) | Fix 10. |
| Mayo cook | "hard, aged cheeses kept for a cheese board" (line 82) | Fix 8. |
| Mayo cook | "so it browns without burning" (line 103) | Agrees, then asks why the guide uses butter. Fix 3. |
| Parent | "Butter getting dark too quickly" (line 98) | Sees the problem in the pan but no action. |

Rewrite line 98: "| Watch for | Butter browning fast, so turn the heat down |"

### Page 6: Heat, and What’s worth arguing about?

| Reader | Stops at | Why |
|---|---|---|
| Teen | "Low, steady heat" (line 111) | Fix 5. |
| Mayo cook | "Butter gives the usual buttery result." (line 131) | An empty answer. Fix 3. |
| Mayo cook | "Don’t press the sandwich." (line 133) | Fix 7. |
| Parent | "Medium-low gives each side 3 to 5 minutes" (line 110) | Page 3 says 3 to 4 for the second side. A small mismatch. |
| Parent | Lid row (line 132) and Lid entry (line 122) | Same two sentences twice, and still no answer for the pan in front of them. |

Rewrite line 110: "| What | Heat is how hot the skillet gets while the sandwich cooks. Medium-low gives each side about 3 to 5 minutes to turn golden. |"

### Page 7: Sources

| Reader | Stops at | Why |
|---|---|---|
| Teen | none | |
| Mayo cook | "October 2026" for the Grilled Cheese Sandwiches recipe (line 142) | Reads it as a brand-new recipe. The page has no date. |
| Parent | none | |

Rewrite line 142: "| Food Network Kitchen, Grilled Cheese Sandwiches | Undated | foodnetwork.com/recipes/food-network-kitchen/grilled-cheese-sandwiches-recipe2-1944002 |"

## Voice pass

| Line | Text | Rule | Rewrite |
|---|---|---|---|
| 17 to 18 | "Strong opinions about each are available, but lunch only needs all four working together." | No personification or kicker endings | "The job comes down to bread, cheese, butter and heat. All four have to work together." |
| 34, 35 | "skillet" then "pan" | One name per part | "Set a skillet, or frying pan, over medium-low heat." |
| 50 | "Bread is the outside of the sandwich, which turns crisp in the pan." | First sentence of What reads correctly in bold | "Bread is the outside of the sandwich and turns crisp in the pan." |
| 70 | "Cheese is the filling that melts between the slices." | One name per part | "Cheese is the filling that melts between the bread." |
| 111 | "Low, steady heat" | One name per part | "Medium-low heat gives the cheese time to melt." |
| 131 | "Butter gives the usual buttery result." | No inflated or empty words | "Butter soaks into the bread and tastes of butter." |
| 14, 43, 71 | "burns", "finishes toasting", "gets too dark" | One name per part | Line 14: "give the cheese time to melt before the bread gets too dark." |

No row sentence starts with "It", "Its", "They" or "This". No em dashes, semicolons or
straight apostrophes. Short answers have no full stops in `guide.md`.

## Verdict

The teen would finish and make a decent sandwich, but would fumble the flip and might turn
the heat to low. The parent gets what they need from page 3 once the flip and lid are
fixed. The mayo cook would enjoy the arguments page, then leave convinced that the guide
proves mayonnaise is better. Fixes 3 and 9 give butter its sourced reason and keep the
argument fair and light.
