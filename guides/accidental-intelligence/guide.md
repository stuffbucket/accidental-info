---
title: Accidental Intelligence
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to the Accidental Guides, as of October 2026.
running_footer: Accidental Intelligence
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: hi@accidental.info · October 2026
version: 0.3.0
---

# What are the<br/>Accidental Guides? {#why}

The Accidental Guides are short guides to AI coding agents and the ways teams use
them to build software. Each one answers one question by explaining a few parts, one
at a time.

There’s a lot written about AI coding agents, and the same word often means different
things to different writers. These guides are short and use one name for each thing in
every guide, so what you learn in one carries over to the next.

The guides started by accident, when one was written to settle which words to use for
the parts of a coding agent. The title Accidental Intelligence plays on artificial
intelligence.

People often build a machine for one job and find it does another. The models that
coding agents use were trained to predict the next word, and it turned out they could
write software. Guides that started by accident are in good company.

| Guide | Answers | Version |
|---|---|---|
| Agents, Harnesses, Skills, and Tools | What are the parts of an AI coding agent, and what does each one do? | 1.0.0 |
| Specs and Reviews | How does work get from an idea to done? | 0.2.0 |
| Software Factories | What is a software factory, and what’s in one? | 0.1.0 |
| Lights-Off Software Factories | What decides if a change is right when nobody reads the code? | 0.2.0 |
| Harness Engineering | What do teams build to catch a coding agent’s mistakes? | 0.1.0 draft |
| Running a Software Factory | What does a team decide before a factory runs, and how does it know the factory works? | 0.1.0 draft |
| Software Factory Claims | How do you check a claim about AI-built software? | 0.1.0 draft |

# Where do I start? {#start}

Arrows show the order to read the guides in. A dashed box is a draft. The small squares are
each guide’s parts, colored by family.

```diagram
row Agents, Harnesses, Skills, and Tools | | Specs and Reviews
row | Software Factories |
row Running a Software Factory | Harness Engineering | Lights-Off Software Factories
row | Software Factory Claims |
next Agents, Harnesses, Skills, and Tools -> Software Factories
next Specs and Reviews -> Software Factories
next Software Factories -> Running a Software Factory
next Software Factories -> Harness Engineering
next Software Factories -> Lights-Off Software Factories
next Harness Engineering -> Lights-Off Software Factories
next Running a Software Factory -> Software Factory Claims
next Lights-Off Software Factories -> Software Factory Claims
```

| Guide | Read it if you |
|---|---|
| Agents, Harnesses, Skills, and Tools | use a coding agent and want to know how it works |
| Specs and Reviews | are new to specs, trackers and reviews |
| Software Factories | hear “software factory” and want to know what it means |
| Running a Software Factory | lead a team that runs a factory |
| Harness Engineering | build checks and limits for coding agents |
| Lights-Off Software Factories | wonder if anyone still needs to read the code |
| Software Factory Claims | read announcements about AI writing code |

# What do the colors mean? {#colours}

Each part belongs to one of six families, and each family has one color.

A part goes in the family of the job it does. A review agent runs, but its job is to judge a
change, so it sits with the checks.

| Key | Family | What it holds |
|---|---|---|
| Ru | Things that run | Programs and loops that do the work. |
| Wr | Things you write down | Text that people or agents read and keep. |
| Ck | Things that check | Whatever decides if a change is right. |
| Us | Things an agent uses | Tools an agent calls and places it works in. |
| Dm | Decisions people make | Rules a team sets before the work runs. |
| Nu | Numbers and claims | Counts and scores, and the claims built on them. |

Inside each guide, tiles are colored by their order in that guide, so a part may
have a different color there.

# Where does each part live? {#map}

Each row is one guide and the parts it defines, sorted by color.

Spec and work item are parts in two guides, once for any project and once inside a
factory.

| Guide | Part | Key | Family |
|---|---|---|---|
| Agents, Harnesses, Skills, and Tools | Model | Mo | Ru |
| Agents, Harnesses, Skills, and Tools | Harness | Ha | Ru |
| Agents, Harnesses, Skills, and Tools | Agent | Ag | Ru |
| Agents, Harnesses, Skills, and Tools | Skill | Sk | Wr |
| Agents, Harnesses, Skills, and Tools | Tool | To | Us |
| Agents, Harnesses, Skills, and Tools | MCP server | Mc | Us |
| Specs and Reviews | Spec | Sp | Wr |
| Specs and Reviews | Work item | Wi | Wr |
| Specs and Reviews | Tracker | Tr | Wr |
| Specs and Reviews | Acceptance criteria | Ac | Dm |
| Specs and Reviews | Review | Rv | Ck |
| Software Factories | Spec | Sp | Wr |
| Software Factories | Work item | Wi | Wr |
| Software Factories | Orchestrator | Or | Ru |
| Software Factories | Agent session | As | Ru |
| Software Factories | Gate | Ga | Ck |
| Lights-Off Software Factories | Scenario | Sn | Wr |
| Lights-Off Software Factories | Digital twin | Dt | Us |
| Lights-Off Software Factories | Satisfaction | Sa | Ck |
| Lights-Off Software Factories | Closed loop | Cl | Ru |
| Harness Engineering | Check | Ch | Ck |
| Harness Engineering | Review agent | Ra | Ck |
| Harness Engineering | Eval | Ev | Ck |
| Harness Engineering | Outer loop | Ol | Ru |
| Harness Engineering | Progress file | Pf | Wr |
| Harness Engineering | Sandbox | Sb | Us |
| Running a Software Factory | Accepted output | Ao | Dm |
| Running a Software Factory | Boundary | Bd | Dm |
| Running a Software Factory | Identity | Id | Dm |
| Running a Software Factory | Evidence | Ed | Ck |
| Running a Software Factory | Back pressure | Bp | Dm |
| Running a Software Factory | Metric | Me | Nu |
| Software Factory Claims | Share of code | Sc | Nu |
| Software Factory Claims | Multiplier | Mu | Nu |
| Software Factory Claims | Benchmark | Bm | Nu |
| Software Factory Claims | Demo | De | Nu |
| Software Factory Claims | Headcount | Hc | Nu |
| Software Factory Claims | Dark factory | Df | Nu |

# Guides to start with {#cards}

## Agents, Harnesses, Skills, and Tools

| Field | Text |
|---|---|
| Read next | Software Factories, where a program starts the agent sessions instead of you. |

## Specs and Reviews

| Field | Text |
|---|---|
| Read next | Software Factories. |

## Software Factories

| Field | Text |
|---|---|
| Read next | Running a Software Factory if you lead one, Harness Engineering if you build one, and Lights-Off Software Factories if you wonder whether anyone needs to read the code. |

# Guides to read next {#cards}

## Lights-Off Software Factories

| Field | Text |
|---|---|
| Read next | Software Factory Claims. |

## Harness Engineering

| Field | Text |
|---|---|
| Read next | Lights-Off Software Factories, for the checks you need before you stop reading the code. |

## Running a Software Factory

| Field | Text |
|---|---|
| Read next | Software Factory Claims, for checking the numbers other people publish. |

## Software Factory Claims

| Field | Text |
|---|---|
| Read next | Lights-Off Software Factories, since the boldest claims are about factories where nobody reads the code. |

# Versions {#end}

The version number on each guide’s cover goes up whenever the text changes. Before
1.0.0, a guide’s parts may still change.
