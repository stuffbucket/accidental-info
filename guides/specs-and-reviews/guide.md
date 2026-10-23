---
title: Specs and Reviews
kicker: An Accidental Guide to…
subtitle: A pocket-sized guide to agreeing on work as a team and checking when it’s done.
running_footer: Specs and Reviews
edition: oops@accidental.info · CC BY 4.0 · October 2026
cover_footer: friend@accidental.info · October 2026
version: 0.4.0
---

# How does work get<br/>from an idea to done? {#why}

When several people share the work on one thing, they need to agree on what they’re
making, who is doing which part and when each part is finished. If your experience of a
team is one person doing most of the heavy lifting, you may not have needed much of this.
Once the work is shared, a spec, work items, a tracker, acceptance criteria and
reviews keep everyone on the same page.

You define the result in a spec, split it into work items, and keep them in a tracker. Before work
starts, you agree on acceptance criteria, so the person doing it and the reviewer use the
same test.

> | Term | Meaning |
> |---|---|
> | Spec | What you want built and why. |
> | Work item | One piece of work one person can finish. |
> | Tracker | The shared list of work, owners and statuses. |
> | Acceptance criteria | Conditions the finished work must meet. |
> | Review | Someone else checks, then approves or requests changes. |

# How do the parts fit together? {#fit}

Every step updates the tracker, so anyone can see who has each item and where it stands.
Requested changes send the item back to in progress.

> [!TIP]
> When review keeps sending work back, check the acceptance criteria and the spec before
> the work itself. One of them may be unclear.

# Spec {#entry num=01 mono=Sp}

| Field | Text |
|---|---|
| Identify by | Requirements, a design or a brief in a shared document. |
| What | A spec says what you want built and why. The spec also says what the work covers and leaves out. |
| So what | A shared spec keeps everyone working toward the same result. The people asking and those doing the work agree before it is split up. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Owned by | The person asking for the work |
> | Kept in | A shared document |
> | Cannot | Cover what nobody wrote down |

## Confused with: Work item

A spec describes the whole result and why it’s wanted. A work item is one piece of that work, sized for one person.

# Work item {#entry num=02 mono=Wi}

| Field | Text |
|---|---|
| Identify by | A task, ticket, issue or story in a tracker. |
| What | A work item is one piece of a larger job, small enough for one person to finish in days. The item links to the spec and holds its acceptance criteria. |
| So what | Small work items show progress and problems early. Problems get fixed while they’re still small. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Owned by | One person |
> | Kept in | The tracker |
> | Cannot | Replace a missing spec |

## Confused with: Milestone

A milestone is a date or release for finishing several items, not work itself.

# Tracker {#entry num=03 mono=Tr}

| Field | Text |
|---|---|
| Identify by | A shared tool such as GitHub Issues, Jira or a spreadsheet. |
| What | A tracker is the shared list of work items. Each item has an owner and a status. |
| So what | A current tracker makes progress visible. Anyone can see who has what, what is stuck and what is done. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Owned by | Everyone using it |
> | Kept in | One shared tool |
> | Cannot | Judge the result |

## Confused with: Backlog

A backlog holds unstarted work. A tracker also holds work in progress, review or done.

# Acceptance criteria {#entry num=04 mono=Ac}

| Field | Text |
|---|---|
| Identify by | Short statements in the work item, each one true or false. |
| What | Acceptance criteria state what must be true for a work item to be accepted. For example, a user can reset a password from the sign-in page. |
| So what | Agreed criteria give the person doing the work and the reviewer the same test. Set them before work starts. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Owned by | The person asking for the work |
> | Kept in | The work item |
> | Cannot | Catch an unwritten case |

## Confused with: Definition of done

Acceptance criteria apply to one item. A definition of done is a checklist for every item.

# Review {#entry num=05 mono=Rv}

| Field | Text |
|---|---|
| Identify by | A code review, design review or sign-off in the work item. |
| What | A review checks work against its acceptance criteria. The reviewer, who didn’t do the work, approves it or asks for specific changes. |
| So what | A second person catches a missed condition or mistake. Mistakes are hard to see in your own work. |

## Field marks

> | Field | Short answer |
> |---|---|
> | Owned by | The reviewer |
> | Kept in | The work item |
> | Cannot | Find every problem |

## Confused with: Approval

A review is the check, and approval is the decision it can end in. If someone approves
work without checking it, there was no review.

# One work item,<br/>start to finish {#seq}

The work item keeps its owner, status, criteria and review together in the tracker.

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

Approval closes the item. A request for changes sends it back to in progress with the
reviewer’s comments, then back to review.

# Easy to mix up {#apart}

> | Question | Answer |
> |---|---|
> | Spec or acceptance criteria? | The spec covers the whole result. Acceptance criteria say what one finished item must meet. |
> | Review or testing? | Testing checks behavior. Review lets another person judge the result and the evidence. |
> | Done or released? | Done means the item was accepted. Released means its result has reached its users. |

# Sources {#sources}

These public sources were checked in October 2026.

| Source | Date | Address |
|---|---|---|
| Ken Schwaber and Jeff Sutherland, The Scrum Guide | November 2020 | scrumguides.org/scrum-guide.html |
| Agile Alliance, Agile Glossary | October 2026 | agilealliance.org/agile101/agile-glossary/ |
| GitHub Docs, Issues | October 2026 | docs.github.com/en/issues |
| Google, Engineering Practices: Code Review | October 2026 | google.github.io/eng-practices/review/ |
