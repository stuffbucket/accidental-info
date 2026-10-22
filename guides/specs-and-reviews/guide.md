---
title: Specs and Reviews
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to agreeing on work as a team and checking when it’s done.
running_footer: Specs and Reviews
edition: [Co]Lab · bstucker · October 2026
cover_footer: October 2026
version: 0.2.0
---

# How does work get<br/>from an idea to done? {#why}

When several people share the work on one thing, they need to agree on what they’re
making, who is doing which part and when each part is finished. If your experience of a
team is one person doing most of the heavy lifting, you may not have needed much of this.
Once the work is actually shared, a spec, work items, a tracker, acceptance criteria and
reviews keep everyone on the same page.

You can keep a small job in your head when you’re doing it alone. Once other people are
involved, or the work takes more than a few days, writing down the result you want gives
everyone the same starting point, and that written description is the spec.

A spec is usually too big for one person to finish, so you split it into work items. You
keep them in a tracker so anyone can see who has what and what is stuck.

You agree on acceptance criteria before the work starts so the person doing it and the
person checking it use the same test. A software factory uses the same parts, and An
Accidental Guide to: Software Factories explains what it does with them.

| Term | Meaning |
|---|---|
| Spec | A written description of what you want built and why, agreed before work starts. |
| Work item | One piece of the work, small enough for one person to finish, with a clear way to tell when it is done. |
| Tracker | The shared list of work items that shows who has each one and its status. |
| Acceptance criteria | The conditions the finished work has to meet, agreed before work starts. |
| Review | A check by someone other than the person who did the work, ending in approval or a request for changes. |

# How do the parts fit together? {#fit}

Every step of the work updates the tracker. It shows who has each item and whether the
work is in progress, in review or done, so anyone can look there instead of asking.

The reviewer is someone other than the person who did the work. If the reviewer requests
changes, the item goes back to in progress.

When review keeps sending the same work back, the problem may have started earlier.
The acceptance criteria may be open to interpretation, or the spec may not say enough
about the intended result.

# Spec {#entry num=01 mono=Sp}

| Field | Text |
|---|---|
| Identify by | A document, often called requirements, a design or a brief, that describes one result and why it’s wanted. |
| What | A spec says what you want built and why. The spec also says what the work covers and leaves out. |
| So what | A shared spec keeps everyone working toward the same result. The person asking for the work and the people doing it agree on the spec before they split it into work items. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Owned by | The person asking for the work | The people doing it help write the spec and agree to it. |
| Started by | A need or decision | A new product, feature, repair or other change needs a shared description. |
| Lasts | While the decision applies | A small change may need a few lines. A product may need a longer document that changes over time. |
| Kept in | A shared document | The spec may live in the tracker, with the project files or in a document linked from both. |
| Can | Set a shared direction | Everyone can go back to the same description when a question comes up. |
| Cannot | Cover what nobody wrote down | A missing case or limit leaves the people doing the work to guess. |

## Confused with: Work item

A spec describes the whole result and the reason for it. A work item is one piece taken
from that spec, small enough for one person to finish.

# Work item {#entry num=02 mono=Wi}

| Field | Text |
|---|---|
| Identify by | A task, ticket, issue or story in a tracker, assigned to one person. |
| What | A work item is one piece of a larger job. The item links back to the spec and includes its acceptance criteria, with enough detail for one person to finish it in days rather than weeks. |
| So what | Smaller pieces make progress visible and expose problems early. One owner knows what to do next, while everyone else can see when the work stops moving. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Owned by | One person | That person takes responsibility for moving the item to review. |
| Started by | Splitting the spec | The people planning the work turn the agreed result into pieces that can be finished separately. |
| Lasts | Until done or dropped | The item closes when its result is accepted, or when the work is no longer needed. |
| Kept in | The tracker | The task, owner, status, criteria and links stay together. |
| Can | Deliver useful results early | A finished item can be checked and used right away, before the rest of the work is done. |
| Cannot | Replace a missing spec | A clear task can still miss the point if nobody wrote down what the whole thing is for. |

## Confused with: Milestone

A milestone is a point in the schedule, such as a date or a release, by which a set of
work items should be finished. It isn’t a piece of work itself.

# Tracker {#entry num=03 mono=Tr}

| Field | Text |
|---|---|
| Identify by | A shared tool such as GitHub Issues, Jira or a spreadsheet, with a row or page for each work item. |
| What | A tracker is the shared list of work items. Each item shows its owner and a status such as to do, in progress, in review or done. |
| So what | One current tracker lets anyone see who has what, what is stuck and what has finished. The history also shows how a decision or status changed without relying on memory. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Owned by | Everyone using it | Each person keeps the items they touch current, while a project lead maintains the overall list. |
| Started by | The first work item | A tracker becomes useful as soon as work needs to be shared or followed. |
| Lasts | The life of the project | The record remains useful after the last item closes. |
| Kept in | One shared tool | Projects may use different tools, but each project needs one place people trust. |
| Can | Show where work stands | Owners, statuses, links and past changes make progress and problems visible. |
| Cannot | Judge the result | The tracker cannot tell whether work is good, and it becomes misleading when people stop updating it. |

## Confused with: Backlog

A backlog is the work that has not started yet. It usually lives inside the tracker,
which also holds work that is in progress, under review or done.

# Acceptance criteria {#entry num=04 mono=Ac}

| Field | Text |
|---|---|
| Identify by | Short statements about the result that can each be judged true or false. |
| What | Acceptance criteria state what must be true for a work item to be accepted. A criterion might say that a user can reset a password from the sign-in page. |
| So what | Agreed criteria give the person doing the work and the reviewer the same test. Writing them before work starts also exposes disagreements while they are easier to settle. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Owned by | The person asking for the work | The person doing it agrees to the criteria, and the reviewer checks the work against them. |
| Started by | Creating a work item | Each item gets the conditions that apply to its result. |
| Lasts | Until the item closes | Criteria may be clarified before work begins, but changing them during the work changes the agreement. |
| Kept in | The work item | Keeping the criteria beside the task gives the person doing the work and the reviewer one place to look. |
| Can | Make acceptance concrete | A reviewer can check each statement instead of relying on a general impression. |
| Cannot | Catch an unwritten case | Criteria only cover the conditions people thought to include. |

## Confused with: Definition of done

Acceptance criteria belong to one work item and describe its particular result. A
definition of done is a standing checklist the team uses for every work item.

# Review {#entry num=05 mono=Rv}

| Field | Text |
|---|---|
| Identify by | A code review, design review or sign-off done by someone who did not do the work. |
| What | A review checks finished work against its acceptance criteria. The reviewer either approves the result or requests specific changes. |
| So what | A second person can spot a missed condition, a mistake or a result that solves the wrong problem. In software, the tool that holds the code can require an approval before a change goes in. |

## Field marks

| Field | Short answer | Detail |
|---|---|---|
| Owned by | The reviewer | Someone other than the person who did the work is responsible for the check. |
| Started by | Work ready to check | The person doing the work asks for review after checking their own result. |
| Lasts | Until a decision | Approval ends the review. A request for changes starts another round after the work is revised. |
| Kept in | The work item | Comments, changes and the final decision stay with the record of the work. |
| Can | Check the agreed result | The reviewer compares what was delivered with the acceptance criteria and explains any gap. |
| Cannot | Find every problem | A reviewer can only check the work and evidence in front of them. |

## Confused with: Approval

A review is the check, and approval is the decision it ends in. If someone approves work
without checking it, there was no review.

# One work item,<br/>start to finish {#seq}

Everything about one piece of work stays on its work item in the tracker, so the people
involved never have to ask where it stands.

```diagram
part Person asking |  | needs the result
part Tracker | Tr | status and history
part Person doing it |  |
part Reviewer | Rv | checks it
band Plan
msg 0 -> 1: add the work item
msg 2 -> 1: take the work
msg 2 -> 1: mark in progress
band Work
note 2: checks own work first
msg 2 -> 1: mark in review
msg 2 -> 3: ask for review
band Review
msg 3 --> 2: request changes
msg 2 -> 3: send revised work
msg 3 -> 1: approve and close
msg 1 --> 0: work is done
```

Approval closes the item when the result meets the agreed criteria. If the reviewer asks
for changes, the item goes back to in progress with the reviewer’s comments on it, then
comes back for review when it is fixed.

# More terms {#apart}

## Easy to mix up

| Question | Answer |
|---|---|
| Spec or acceptance criteria? | The spec describes the whole intended result. Acceptance criteria state the conditions one finished work item must meet. |
| Spec or plan? | A spec says what to build and why. A plan says who does which work items and when. |
| Review or testing? | Testing checks behavior through planned steps or automated checks. Review lets another person judge the result and the evidence, which may include test results. |
| Done or released? | Done means the work item was accepted. Released means its result has reached the people who will use it, which may happen later. |

# Related terms {#other}

| Term | Meaning |
|---|---|
| Blocked | A status for work that cannot move until something outside it changes, often a dependency. |
| Status | A short label for where a work item stands, such as to do, in progress, in review or done. |
| Owner | The person responsible for moving a work item to its next step. |
| Dependency | Another piece of work that must finish before this work item can move forward. |
| Scope | What the work covers and what it leaves out, usually stated in the spec. |
| Priority | The agreed order for taking up work when several items are ready. |

# Sources {#sources}

These public sources were checked in October 2026.

| Source | Date | Address |
|---|---|---|
| Ken Schwaber and Jeff Sutherland, The Scrum Guide | November 2020 | scrumguides.org/scrum-guide.html |
| Agile Alliance, Agile Glossary | October 2026 | agilealliance.org/agile101/agile-glossary/ |
| GitHub Docs, Issues | October 2026 | docs.github.com/en/issues |
| Google, Engineering Practices: Code Review | October 2026 | google.github.io/eng-practices/review/ |
