# Edits, round 4: Lights-Off Software Factories

Apply these edits in place to
`packages/accidental-guides/guides/lights-off-software-factories/guide.md` (your working
directory's `./guide.md`). Line numbers are from the file as it is now (after round 3,
version 0.3.0). Replace each listed line with the new text, keeping the table row structure:
label cells stay as they are. Change nothing else. Don't touch any other file.

No mannered prose: the writing must not call attention to itself. Make no assumption that the
reader is an expert.

Read `packages/editorial/skills/accidental-guide-write/references/author-feedback.md`
and `packages/editorial/skills/accidental-guide-write/references/voice.md`
first. Every rule there applies to any text you write or shorten.

## Why

Two entries share a page only if each one is short enough, and none of them is yet. The
entries need to lose about two printed lines each. A printed line in a What or So what row
holds about 50 characters, and in Identify by or Confused with about 60. Field marks answers
sit in narrow columns that hold about 22 characters a line.

The builder also prints the first sentence of What and So what in bold, as the row's short
answer. A row with one long sentence prints with no bold. So each What and So what row is
two sentences: a short first sentence that answers the row on its own, then one more.

The last round also clipped some sentences too far. "Often kept with the code, agent
sessions can change it" has a dangling modifier, and "Long-term design quality remains
unknown" and "a startup that stopped" leave the reader to fill in words. Fix those.

The examples below fit the budgets. Use them, or write your own that say the same and fit.
Keep whole, natural sentences. Don't drop articles to save characters.

## Scenario (lines 30 to 47)

1. Line 34, Identify by: at most 55 characters. For example:
   | Identify by | A user story run from start to finish. |
2. Line 35, What: two sentences, at most 120 characters. For example:
   | What | A scenario is a story of someone using the software. A judge model decides whether each run would satisfy that person. |
3. Line 36, So what: two sentences, at most 100 characters. Keep the reason scenarios are hidden.
   Don't start the second sentence with "They" or "So they". For example:
   | So what | Agent sessions never see the scenarios. An agent can’t write code just to pass a test it can’t see. |
4. Line 47, Confused with: Test: one or two sentences, at most 115 characters. For example:
   > An acceptance test checks one fixed result and often sits beside the code, where agent sessions can change it.

   (Written as a plain paragraph line, with no `>`.)

## Digital twin (lines 49 to 66)

5. Line 53, Identify by: at most 55 characters. For example:
   | Identify by | A working copy of a service the software calls. |
6. Line 54, What: two sentences, at most 115 characters. For example:
   | What | A digital twin copies an outside service. The copy is built from its API and checked against the real service. |
7. Line 55, So what: two sentences, at most 100 characters. For example:
   | So what | Scenarios can run thousands of times. There are no rate limits, usage costs or risks to real accounts. |
8. Line 66, Confused with: Mock: at most 115 characters. For example:
   A mock returns canned answers for one test. A digital twin acts like the real service across many scenarios.

## Satisfaction (lines 68 to 85)

9. Line 72, Identify by: at most 55 characters. For example:
   | Identify by | A percentage worked out from judged scenario runs. |
10. Line 73, What: two sentences, at most 115 characters. For example:
    | What | Satisfaction is the share of runs a judge model accepts. The same scenario can pass on one run and fail the next. |
11. Line 74, So what: two sentences, at most 100 characters. For example:
    | So what | You see how a change does across many user journeys. One pass or fail tells you much less. |
12. Line 80: `> | Owned by | Product and engineering |`
13. Line 81: `> | Cannot | Speak for real users |`
14. Line 85, Confused with: Passing tests: at most 115 characters, same meaning.

## Closed loop (lines 87 to 104)

15. Line 91, Identify by: at most 55 characters. For example:
    | Identify by | Fixes that reach users with nobody approving them. |
16. Line 92, What: two sentences, at most 105 characters. For example:
    | What | A closed loop turns failures in use into new work. Each fix then goes through the scenarios and out to users. |
17. Line 93, So what: two sentences, at most 95 characters. For example:
    | So what | The factory can fix a failure after release. Nobody has to file the fix or approve it. |

## What has been shown? (lines 106 to 118)

18. Line 108: put back "tried it and stopped", with the commas. Write exactly:
    As of October 2026, three examples are public: a company that says it runs lights off, a startup that tried it and stopped, and a large build that came close.
19. Line 113: say what made the founder rewrite the core. Write exactly:
    > | Unread code stays maintainable | In July 2025, one startup stopped reading its code. By November, the code was so hard to change that a founder spent two weeks rewriting the core by hand. The startup now reads the code. |
20. Line 114: plain sentences, with the team as the subject of the last one. Write exactly:
    > | Agents can do almost all review | A team at a large AI lab spent five months building a product with no hand-written code and merged about 1,500 pull requests. Agents did most of the review. The team says it doesn’t know how the design will hold up over the years. |

## Check before you finish

- Every line not named above is unchanged.
- No sentence in a row starts with "It", "Its", "They" or "This".
- No em dashes, semicolons, quotes of people or names of people. No question marks outside
  headings.
- Typographic apostrophes (’) everywhere.

When you're done, reply with one line: done.
