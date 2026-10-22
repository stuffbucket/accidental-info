# Edits, round 4: Agent Skills

Apply these edits in place to `packages/accidental-guides/guides/skills/guide.md` (your
working directory's `./guide.md`). Line numbers are from the file as it is now (commit
e2192be, version 0.1.0). Replace each listed line with the new text, keeping the table row
structure: label cells stay as they are unless the edit gives a new label. Lines that start
with `> ` keep the `> ` at the start. Change nothing else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

The guide now uses packed pages, and the body is about 1,040 printed words. It must stay at
five minutes or less, and this round removes repeated sentences and makes a few rows clearer
for someone new to skills. The field marks now print only their short answer, so each short
answer must make sense on its own. Work from the bottom of the file up so the line numbers
hold.

## Front matter

- Line 8: `version: 0.2.0`

## How do the parts fit together? (lines 46 to 48)

1. Lines 46 to 48: replace the two one-sentence paragraphs (line 46, the blank line 47 and
   line 48) with one paragraph on one line, word for word:
   SKILL.md is the only file a skill needs. The other folders are optional, and a step names the file it uses.

## Description (lines 64 to 80)

2. Line 76: `> | In context | Always, from the start of the session |`

## Skill instructions (lines 82 to 98)

3. Line 87: `| What | Skill instructions are the steps the agent follows once it picks the skill. A step can tell the agent to run a script or open a file. |`

## Script (lines 100 to 116)

4. Line 105: `| What | A script is code that comes with the skill, and the agent runs it as it is. Only what the script prints enters the context window. |`
5. Line 116: `A tool is something the harness lets the agent use, such as the shell. The agent runs a script with the shell tool.`

## Reference file (lines 118 to 134)

6. Line 124: `| So what | Long rules and examples can go in reference files. The skill instructions stay short, and the agent reads only the file the task needs. |`

## Asset (lines 136 to 152)

7. Line 141: `| What | An asset is a file the skill uses in what it makes. The agent copies it or fills it in. |`

## Skill or something else? (lines 169 to 180)

8. Line 180: `A skill can also tell the agent which MCP tools to call and which sub-agents to start. When you paste the same steps into a conversation for the third time, make them a skill.`

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
