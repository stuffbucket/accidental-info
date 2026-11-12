---
title: From Judgment to Action
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to the rules that turn a model’s answers into actions.
running_footer: From Judgment to Action
edition: friend@accidental.info · CC BY 4.0 · November 2026
cover_footer: friend@accidental.info · November 2026
collection: Accidental Intelligence
collection_mark: square
number: 17
version: 1.0.0
---

# How does a judgment<br/>become an action? {#why}

A decision model answers questions about a message. Rules that people wrote decide what the software does with those answers.

```diagram
message Support message from a customer | I was charged twice this month, and now I can’t open my account.
scores The decision model answers two questions | Is it about billing? | yes 0.91 | Is the customer locked out? | yes 0.88
facts The account system adds facts the model never saw | Two charges of $18 on 3 November | Account open, not suspended
rules The rules people wrote | Refund a repeated charge when billing scores 0.85 or more and the charge is under $50. | Send a reset link when locked out scores 0.85 or more and the account isn’t suspended.
checks Code checks each rule
check 1 | 0.91 is 0.85 or more
check 1 | The $18 charge appears twice
check 1 | $18 is under $50
check 2 | 0.88 is 0.85 or more
check 2 | The account isn’t suspended
results What happens | Refund $18 | Send a password reset link
else A third rule, which sends anything else to a person, wasn’t needed.
```

# Where does a score<br/>turn into an action? {#fit}

The decision model scored nine saved messages for whether each asks for a refund. A person labeled each one by hand.

```diagram
head Score | Message | A person’s label
label yes | Refund
label no | No refund
band Refund automatically
row 0.98 | I was charged twice. Please refund one. | yes
row 0.90 | The blender arrived broken. I want a refund. | yes
row 0.88 | Do I need a receipt to return a gift? | no | Refunded, but nobody asked for a refund.
row 0.86 | Refund the extra $18, please. | yes
cut 0.85
band Rp | A person checks it
row 0.79 | This isn’t what I ordered. | yes
row 0.61 | Can I get my money back for last month? | no
row 0.55 | The charge on my card looks wrong. | yes
cut 0.50
band Nothing happens
row 0.42 | Still waiting on the $18 you owe me. | yes | Left alone, but this customer wants a refund.
row 0.07 | Where is your office? | no
```

People choose the two thresholds by checking saved messages like these.

# Policy {#entry num=01 mono=Po}

| Field | Text |
|---|---|
| Identify by | Written rules that say what happens for each mix of answers and facts. |
| What | Policy is the set of rules that turns answers and facts into actions. People write the policy, and code applies it. |
| So what | Rules kept outside the model can be read, tested and changed in one place. The rules for April change what happens without changing the model. |

```diagram
ruleset Rules in March | Any refund request | Send to a person
ruleset Rules in April | Refund above 0.85, under $50 | Refund automatically
ruleset Rules in April | Anything else | Send to a person
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Written by | People who own the outcome | |
> | Kept in | Code or settings | Each change gets a version number. |
> | Changes | Without the model | Saved answers can run through new rules. |

## Confused with: Judgment question

A judgment question asks what seems true about a message. Policy says what to do about it.

# Threshold {#entry num=02 mono=Td}

| Field | Text |
|---|---|
| Identify by | A cut-off score, such as 0.85, where one action stops and another starts. |
| What | A threshold splits model scores into actions. Each action can have its own threshold, because a wrong refund costs more than a wrong tag. |
| So what | Labeled cases show what each cut-off would do before any customer sees it. Each row shows which saved messages one cut-off would refund automatically. |

```diagram
yes Refund | 0.98, 0.90, 0.86, 0.79, 0.55, 0.42
no No refund | 0.88, 0.61, 0.07
try 0.60
try 0.85
try 0.89
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Chosen from | Labeled cases | |
> | Applies to | One action | Refunds and tags can use different cut-offs. |
> | Can’t | Remove mistakes | Raising the cut-off trades wrong refunds for missed ones. |

## Confused with: Probability

Probability is the score the model returns. A threshold is the cut-off people choose for that score.

# Review path {#entry num=03 mono=Rp}

| Field | Text |
|---|---|
| Identify by | A queue where a person looks at a message before anything happens. |
| What | A review path holds the messages that the rules don’t settle. Close scores, costly actions and messages with missing facts go there. |
| So what | Clear cases run automatically and the rest wait for a person. Each reviewed message can become a new labeled case. |

```diagram
group Waiting for review
step Message | Can I get my money back for last month? Score 0.61 for Refund requested?
group Rp | A person decides
step Person | No refund. The customer is asking how to change plans.
group Lc | The decision is saved
step Lc | The message, the question and the answer no.
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Gets | Messages the rules pick | |
> | Needs | People with time | A queue nobody clears doesn’t help. |
> | Produces | A person’s decision | Saved as a labeled case. |

## Confused with: Error log

A review path waits for a person to decide. An error log records something that broke.

# Labeled case {#entry num=04 mono=Lc}

| Field | Text |
|---|---|
| Identify by | A saved message, the question asked and the answer a person says is right. |
| What | A labeled case records what a person expected for one real message. A useful set has everyday, tricky, mixed and off-topic messages. |
| So what | Running the saved cases again shows whether a new model, question or threshold made things better or worse. Each disagreement can be read on its own. |

```diagram
record Labeled case
field Message | Can I get my money back for last month?
field Question | Refund requested?
field Person’s answer | No
field Model’s score | 0.61
field Saved with | Model name and version, rules version 4, 14 November 2026
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Holds | The exact question | So the case can run again. |
> | Labeled by | People | Disagreements stay in the record. |
> | Can’t | Cover every message | Keep sampling after launch. |

## Confused with: Demo

A demo shows that the model gives an answer. A labeled case also says what the right answer was.

# Before the rules go live {#habits}

> | Check | What to record |
> |---|---|
> | Labeled cases | Everyday messages, costly mistakes, mixed messages and messages that fit no answer. |
> | Cost of a mistake | What a wrong refund, a missed refund and a review each cost. |
> | Review time | How many messages people can review each day. |
> | Versions | Which model, question, threshold and rules were in use. |
> | Checking later | How often each action happens, and a sample of mistakes each week. |

A provider’s published test compares models on the provider’s examples. Only your own labeled cases show how a model does on your messages.

# Sources {#sources}

These public sources were checked in November 2026.

| Source | Date | Address |
|---|---|---|
| TypeSafe, Jev agent skill | November 2026 | github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md |
| TypeSafe, Introduction to Jev | November 2026 | docs.typesafe.ai/introduction.md |
| Decision Models for Humans, Mental model | November 2026 | github.com/stuffbucket/decision-models-for-humans/blob/main/docs/mental-model.md |
| Decision Models for Humans, Evidence | November 2026 | github.com/stuffbucket/decision-models-for-humans/blob/main/docs/evidence.md |
