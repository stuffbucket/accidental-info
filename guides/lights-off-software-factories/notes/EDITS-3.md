# Edits, round 3: Lights-Off Software Factories

Apply these edits in place to
`packages/accidental-guides/guides/lights-off-software-factories/guide.md` (your working
directory's `./guide.md`). Line numbers are from the file as it is now (commit 6e2cb66,
version 0.3.0). Replace each listed line with the new text, keeping the table row structure:
label cells stay as they are unless the edit gives a new label. Change nothing else. Don't
touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

The guide is on a new layout. Two entries now share a page, and the field marks sit on a grey
block as a grid of short answers, with no Detail column. An entry fits next to another only
if it stays short: in the entries, the What and So what rows can take about two printed lines
each. The printed guide is about 1,120 words before the sources and must come under 1,100.
The lint also flagged a few phrases, including the questions in the tip. This round drops the
Detail column, trims the entries and the "What has been shown?" rows, and fixes the lint. Cut
detail and repetition, not clarity: a reader who has never seen a software factory should
still follow every row. Short is not the same as clipped: keep whole, natural sentences, and
don't drop articles to save words.

## Keep exactly

- The front matter (lines 1 to 9). The version is changed separately.
- Every `#` heading line with its `{#…}` id, and the `## Field marks` and `## Confused with: …`
  lines.
- Lines 13 to 28 (the first two sections). Line 13 is shown on its own on the site.
- The `> ` at the start of lines. A line that starts with `> ` must still start with `> `
  after your edit, and `> [!TIP]` stays on its own line.
- The sources section (lines 120 to the end), exactly as it is.
- Typographic apostrophes (’). No backticks, no emphasis, no em dashes, no semicolons.

## Scenario (lines 30 to 47)

1. Lines 40 to 43, field marks: drop the Detail column. Write exactly:
   > | Field | Short answer |
   > |---|---|
   > | Owned by | Product and engineering people |
   > | Cannot | Cover a missing story |
2. Line 47, Confused with: Test: at most 28 words. The lint flags "whole journey" as filler.
   Keep that an acceptance test checks one fixed result and often sits beside the code, where
   an agent session can change it, and that a judge model looks at a whole run of a scenario
   from start to finish.

## Digital twin (lines 49 to 66)

3. Line 54, What: at most 25 words, same meaning.
4. Lines 59 to 62, field marks: drop the Detail column. Write exactly:
   > | Field | Short answer |
   > |---|---|
   > | Owned by | The factory team |
   > | Cannot | Know behavior nobody observed |
5. Line 66, Confused with: Mock: at most 25 words, same meaning.

## Satisfaction (lines 68 to 85)

6. Line 73, What: at most 28 words, same meaning. Keep that the same scenario can go well on
   one run and badly on the next.
7. Lines 78 to 81, field marks: drop the Detail column. Write exactly:
   > | Field | Short answer |
   > |---|---|
   > | Owned by | Product and engineering people |
   > | Cannot | Speak for users or future maintainers |
8. Line 85, Confused with: Passing tests: at most 25 words, same meaning.

## Closed loop (lines 87 to 104)

9. Line 91, Identify by: at most 14 words, same meaning.
10. Line 92, What: at most 25 words, same meaning.
11. Lines 97 to 100, field marks: drop the Detail column. Write exactly:
    > | Field | Short answer |
    > |---|---|
    > | Owned by | The team that runs the software |
    > | Cannot | Recover from every failure |
12. Line 104, Confused with: Feedback path: at most 25 words, same meaning.

## What has been shown? (lines 106 to 118)

13. Line 108: at most 28 words, same meaning.
14. Lines 112 to 115, the four rows: keep the labels and every fact that a reader needs to
    judge the claim (the dates, that the company reports no defect rates, satisfaction
    numbers or shipped results, the rewrite by hand, the five months and about 1,500 pull
    requests, and that no published study reports defect, incident or cost data). Cut
    repetition and any words that don't carry a fact. About 25 words a row, at most 30.
15. Line 118, the tip (keep `> ` at the start): the lint bans questions in a paragraph, and
    "ask what…" turns them into embedded questions, which are banned too. Name the three
    things to ask for as nouns. For example:
    > When someone says their factory runs lights off, ask to see what it has shipped, the
    > evidence that the software works, and the plan for failures the agents can’t fix. An
    > Accidental Guide to: Software Factory Claims explains how to read the answers.

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people. No question marks outside
  headings.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
