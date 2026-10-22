---
title: Lights-Off Software Factories
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to software factories where nobody reads the code, as of October 2026.
running_footer: Lights-Off Software Factories
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.3.0
---

# What is a lights-off<br/>software factory? {#why}

In a software factory, a program starts the agent sessions, and a person still reads each change and approves it at a gate. An Accidental Guide to: Software Factories covers that kind of factory.

A factory that runs with nobody on the floor can turn the lights off. A lights-off software factory is one where nobody writes or reads the code, sometimes called a dark factory.

At the gate, a person decides whether a change does what you wanted and whether it breaks anything. When nobody reads the code, these four parts make those decisions.

> | Term | Meaning |
> |---|---|
> | Scenario | A story of someone using the software from start to finish, kept where agent sessions can’t see or change it. |
> | Digital twin | A working copy of an outside service that scenarios can use thousands of times. |
> | Satisfaction | The share of scenario runs that a model, asked to judge each run, says a user would accept. |
> | Closed loop | The route from a failure in use back to a released fix with no person in it. |

# How do the parts fit together? {#fit}

Agent sessions write the code. Each change runs against scenarios the sessions couldn’t see, with digital twins in place of outside services. If the satisfaction score is high enough, the change goes to users. Nobody reads the code at any step.

# Scenario {#entry num=01 mono=Sn}

| Field | Text |
|---|---|
| Identify by | A user story kept outside the code and run from start to finish. |
| What | A scenario describes someone using the software to get a result. A judge model decides whether each run would satisfy that user. |
| So what | The agent session can’t see hidden scenarios, so it can’t write code that only passes them. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Owned by | People | Product and engineering people write each story. |
> | Cannot | Cover a missing story | Behavior nobody put in a scenario may still be wrong. |

## Confused with: Test

An acceptance test checks one fixed result and often lives beside the code, where an agent session can change it. A judge model assesses a scenario’s whole journey.

# Digital twin {#entry num=02 mono=Dt}

| Field | Text |
|---|---|
| Identify by | A working copy of an outside service’s API and observed behavior. |
| What | A digital twin copies a service the software calls. The copy is built from the service’s API and observed edge cases, then checked against the real service. |
| So what | Scenarios can run thousands of times without rate limits, usage costs or risk to real accounts. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Owned by | The factory team | The team records the service’s public behavior and keeps the copy current. |
> | Cannot | Know behavior nobody observed | The copy can miss an edge case nobody has seen yet. |

## Confused with: Mock

A mock returns canned answers for one test. A digital twin copies enough of a service’s behavior for many scenarios and is checked against the real service.

# Satisfaction {#entry num=03 mono=Sa}

| Field | Text |
|---|---|
| Identify by | A percentage calculated from judged runs through all the scenarios. |
| What | Satisfaction is the share of scenario runs that a judge model says would satisfy a user. The same scenario can go well on one run and badly on the next. |
| So what | You can judge a change across many user journeys, with more to go on than one pass or fail. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Owned by | People | Product and engineering people choose the scenarios, judge and score needed for release. |
> | Cannot | Speak for users or future maintainers | A high score doesn’t show what real users think or whether the code will be easy to change. |

## Confused with: Passing tests

Passing tests means the software produced the fixed result each test checks. Satisfaction says how often a judge model accepted the result across many runs.

# Closed loop {#entry num=04 mono=Cl}

| Field | Text |
|---|---|
| Identify by | Monitoring that files work items, followed by fixes that reach users with no person approving them. |
| What | A closed loop carries failures from software in use back into the factory as work for agent sessions. The fix then goes through scenarios and release. |
| So what | The factory can repair a failure after release without waiting for someone to file or approve the fix. |

## Field marks

> | Field | Short answer | Detail |
> |---|---|---|
> | Owned by | The team that runs the software | The team chooses which signals create work and which changes may release automatically. |
> | Cannot | Recover from every failure | The retry limit still stops work that agent sessions and checks can’t resolve. |

## Confused with: Feedback path

A feedback path turns a failure into a work item, and a person still approves the fix at the gate. A closed loop releases the fix with no person approving it.

# What has been shown? {#shown}

As of October 2026 there are three published examples: a company that says it runs lights off, a startup that tried it and stopped, and a large build that came close.

> | Claim | What has been shown |
> |---|---|
> | A factory runs lights off | One software company has said since February 2026 that no person writes or reviews its code. The company reports no defect rates, satisfaction numbers or shipped results. |
> | Unread code stays maintainable | One startup stopped reading its code in July 2025. By November, changing the code was hard enough that a founder rewrote the core by hand over two weeks. The startup now reads the code. |
> | Agents can do almost all review | A team at a large AI lab built a product with no hand-written code over five months and merged about 1,500 pull requests. Agents did most of the review. The team says it doesn’t know how the design will hold up over years. |
> | The results are measured | No published study reports defect, incident or cost data for a factory where no person reads the code. |

> [!TIP]
> When someone says their factory runs lights off, ask three questions: What has it shipped? How do they know the software works? What happens when the agents can’t fix a failure? An Accidental Guide to: Software Factory Claims explains how to read the answers.

# Sources {#sources}

These public sources were checked in October 2026.

| Source | Date | Address |
|---|---|---|
| StrongDM AI, Software factories and the agentic moment | February 2026 | factory.strongdm.ai/ |
| StrongDM AI, Digital Twin Universe | February 2026 | factory.strongdm.ai/techniques/dtu |
| Dex Horthy, Why Software Factories Fail | July 2026 | github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md |
| OpenAI, Harness engineering: leveraging Codex in an agent-first world | February 2026 | openai.com/index/harness-engineering/ |
