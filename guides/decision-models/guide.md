---
title: Decision Models
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to software that answers quick questions from a fixed list.
running_footer: Decision Models
edition: friend@accidental.info · CC BY 4.0 · November 2026
cover_footer: friend@accidental.info · November 2026
collection: Accidental Intelligence
collection_mark: square
number: 16
version: 1.0.0
---

# What does a decision<br/>model do? {#why}

A decision model answers a narrow question about a message by scoring a short list of answers. The model doesn’t write anything new.

```diagram
message Support message | I was charged twice this month, and now I can’t open my account.
ask Which topics apply? | any that fit
answer billing | 0.91
answer account | 0.84
answer shipping | 0.03
answer product | 0.02
ask Is the customer locked out? | pick one
answer yes | 0.88
answer no | 0.12
ask How upset does the customer sound? | pick one
answer calm | 0.18
answer annoyed | 0.71
answer angry | 0.11
```

The decision model answered three questions about the message and scored every answer on each list. A longer bar means a better fit. The scores are made up.

The model didn’t write a reply or choose a team. The rest of the software reads the answers and decides what to do.

# Which part<br/>does what? {#fit}

```diagram
group The software sends
step Si | I was charged twice this month, and now I can’t open my account.
step Jq | Which topics apply?
step Al | billing, account, shipping, product
group Dj | The decision model returns
step Pb | billing 0.91, account 0.84, shipping 0.03, product 0.02
group The rest of the software decides
step Code | Tag the message billing and account, and send it to the billing team.
```

The software sends the first three parts and gets back the scores. Everything after that is ordinary code, so sending billing messages to another team doesn’t change the model’s answers.

# Decision model {#entry num=01 mono=Dj}

| Field | Text |
|---|---|
| Identify by | Software that returns a score for each answer on a list. |
| What | A decision model scores answers from a list that someone gave it. Some decision models also find things in photos. |
| So what | The result is always one of the answers on the list, so software can act on it right away. A chatbot’s reply needs another step first. |

```diagram
input Si | The customer’s message
input Jq | Which topics apply?
input Al | billing, account, shipping, product
output Pb | billing 0.91, account 0.84, shipping 0.03, product 0.02
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Returns | Answers from a list | Each with a score. |
> | Good at | Quick calls | A person could make the same call in a few seconds. |
> | Doesn’t | Decide what happens | |

## Confused with: Chatbot

A chatbot writes new text. A decision model only scores the answers it was given.

# State {#entry num=02 mono=Si}

| Field | Text |
|---|---|
| Identify by | The message, photo or record sent along with each question. |
| What | State is everything the model can see when it answers. The software decides what goes in it. |
| So what | The model can’t use a fact that isn’t in the state. When answers look wrong, check what was sent before you change the question. |

```diagram
message Sent with the question | I was charged twice this month, and now I can’t open my account.
missing Not sent, so the model can’t use it | Order history, payment records and earlier messages from the same customer.
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Comes from | The software | |
> | Lasts for | One question | Nothing carries over to the next message. |
> | Can’t | Fill gaps | A missing order number stays missing. |

## Confused with: Memory

State is sent with each question. Memory keeps information from one request for later ones.

# Judgment question {#entry num=03 mono=Jq}

| Field | Text |
|---|---|
| Identify by | A short question about one thing a person could tell from the state. |
| What | A judgment question asks for one call about the state. Topic and urgency are separate questions, even about the same message. |
| So what | One call per question makes mistakes easy to spot. The mixed question gets a weak yes that hides a clear topic and low urgency. |

```diagram
side One mixed question | Is this an urgent billing problem? | yes 0.55, no 0.45
side Two separate questions | Which topics apply? | billing 0.91
side Two separate questions | How urgent is it? | low 0.70, high 0.30
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Asks | One thing | |
> | Works on | The same state | |
> | Can’t | Fix a thin message | Better wording doesn’t add facts. |

## Confused with: Instruction

A judgment question asks the model to score answers. An instruction asks a chatbot to write or do something.

# Allowed answers {#entry num=04 mono=Al}

| Field | Text |
|---|---|
| Identify by | A short list, a yes or no, or a scale such as calm, annoyed and angry. |
| What | Allowed answers are the only answers the model can give. The person building the software writes the list, and the model scores each item on it. |
| So what | Every possible result is known ahead of time, so the builder can plan a next step for each. A list with no good fit still produces an answer, as the office question shows. |

```diagram
shape Any that fit | billing*, account*, shipping, product
shape Pick one | yes*, no
shape A level | calm > annoyed* > angry
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Written by | The builder | The model never adds an answer. |
> | Shape | One, several or a level | |
> | Needs | A way out | An answer named other, or a check that anything fits. |

## Confused with: Generated reply

An allowed answer is one item from a fixed list. A generated reply is new text that can say anything.

# Probability {#entry num=05 mono=Pb}

| Field | Text |
|---|---|
| Identify by | A number from 0 to 1 next to each answer. |
| What | Probability is the model’s score for how well an answer fits. Some providers call the number confidence, and each provider documents what its number means. |
| So what | The scores help software sort clear cases from close ones. A high score isn’t proof, so test the scores on messages where you already know the right answer. |

```diagram
case A clear case | billing 0.91, account 0.06, shipping 0.02, product 0.01
case A close call | billing 0.48, account 0.46, shipping 0.04, product 0.02
```

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Range | 0 to 1 | Higher means a better fit. |
> | Useful for | Sorting cases | Clear cases first, close calls later. |
> | Doesn’t | Pick the action | |

## Confused with: Certainty

Probability is the model’s score for an answer. Certainty means no chance of being wrong, and no score gives that.

# What if no<br/>answer fits? {#other}

```diagram
message Support message | Where is your office?
ask Which topic is this? | pick one
answer billing | 0.41
answer account | 0.32
answer shipping | 0.17
answer product | 0.10
```

An office address isn’t one of the four topics. The question must pick one topic, so billing still wins with a weak score.

Give the question a way out, such as an answer named other or a separate question that asks whether any topic applies. Send the messages that fit nothing to a person.

# Sources {#sources}

These public sources were checked in November 2026.

| Source | Date | Address |
|---|---|---|
| TypeSafe, Introduction to Jev | November 2026 | docs.typesafe.ai/introduction.md |
| TypeSafe, Jev agent skill | November 2026 | github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md |
| Fastino, GLiNER2.5-Decide model card | November 2026 | huggingface.co/fastino/GLiNER2.5-Decide |
| GLiNER Runner, project documentation | November 2026 | github.com/stuffbucket/gliner-runner |
