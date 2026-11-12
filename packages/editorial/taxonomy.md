# Guide taxonomy

The taxonomy helps a newcomer find the next useful question. It is not a catalog of products or an organization chart.

`site/src/data/collections.json` is the source of truth for placement and display order. Every built guide and draft appears there exactly once.

## Levels

### Collection

A collection is a broad shelf that makes sense before someone knows the subject's vocabulary. Examples are Accidental Intelligence, Around the house, At the table and Games.

Create a collection only when its guides share a reader and no existing collection can hold them without changing its meaning.

### Group

A group is a stable subject area inside a collection. A group can hold several guide questions and several products. Product names do not make useful groups on their own.

The Accidental Intelligence groups cover:

- agents;
- harnesses people use;
- ways to extend an agent;
- context;
- project management;
- software factories;
- checking claims;
- harness engineering;
- models.

The Models group covers what a model does, how software uses its output and, later, distinct model families whose behavior needs its own guide. Provider comparisons and changing model catalogs belong in companion references unless one plain reader question can support a five-minute guide.

### Guide

A guide answers one question for one newcomer in five minutes or less. Five or fewer key concepts answer that question. A guide owns each concept it defines; other guides refer to that owner.

A broad subject may need several guides. Split it where the reader's question changes. Decision Models explains the bounded judgment. From Judgment to Action explains how software turns that judgment into a visible policy and outcome.

## Placement rules

1. Name the reader and their question before choosing a group.
2. Put the guide in the group that owns the question, not the group that owns a product mentioned in an example.
3. List a planned guide under `coming`. The site promotes it in place when a matching draft or guide is built.
4. Keep each guide in one place. Use links for related questions in other groups.
5. Add new groups and guides after existing published entries. Cover numbers currently follow taxonomy order, so moving a published entry is a renumbering change.
6. Give every guide on a map a unique two-letter map code. Map codes identify guides; concept codes identify concepts and come from `registry.json`. Avoid reusing a family or concept code even though the validators treat those namespaces separately.
7. Use one of the six series colours. A group colour shows its place on the map; concept colours still come from the concept registry.

## Names

Collection and group names are short noun phrases. Guide titles are six words or fewer. A title names the subject; the opening page supplies the reader's question.

Avoid category names that depend on a vendor, release or temporary market label. Put dates and provider details in guide text or a checked reference.

## Lifecycle

A proposal receives a slug, collection, group and provisional map code before its draft folder is created. The portfolio check verifies placement. The registry check reserves the guide's concept codes before writing begins.

A draft stays under `drafts/<slug>/`. Publication moves it to `guides/<slug>/` without changing the slug, placement or codes. Removing a guide does not make its concept or map codes available for reuse.

The `accidental-guide-manage` skill holds the portfolio workflow. The `accidental-guide-registry` skill holds concept ownership and code allocation.
