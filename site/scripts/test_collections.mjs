// Tests for src/lib/collections.mjs, the check that every guide is in one collection on the site. Run from site/:
//
//     node --test scripts/test_collections.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { checkCollections } from "../src/lib/collections.mjs";

const ids = (...list) => list.map((id) => ({ id }));
const flat = (id, guides, coming = []) => ({ id, name: `Collection ${id}`, code: "Ab", colour: "blue", guides, coming });
const mapped = () => ({
  id: "mapped",
  name: "Mapped",
  code: "Mp",
  colour: "green",
  page: "mapped/",
  catalog: "hub",
  codes: { hub: "Hb", a: "Aa", b: "Bb", c: "Cc", d: "Dd", e: "Ee", f: "Ff", g: "Gg", h: "Hh", v: "Vv" },
  groups: ["a", "b", "c", "d", "e", "f", "g", "h"].map((id) => ({
    id: `group-${id}`,
    name: `Group ${id}`,
    colour: "purple",
    guides: [id],
  })),
});
const guides = ids("hub", "a", "b", "c", "d", "e", "f", "g", "h", "x", "y");
const data = () => ({ collections: [mapped(), flat("home", ["x", "y"], [{ id: "z", title: "Zed" }])] });

test("returns each collection with its guides and the guides still to come", () => {
  const [map, home] = checkCollections(data(), guides);
  assert.deepEqual(home.guides, ids("x", "y"));
  assert.deepEqual(home.coming, [{ id: "z", title: "Zed" }]);
  assert.equal(home.count, 2);
  assert.equal(home.map, null);
  assert.equal(map.count, 9);
  assert.deepEqual(map.guides.map((guide) => guide.id), ["hub", "a", "b", "c", "d", "e", "f", "g", "h"]);
});

test("returns a map's catalog, its groups in order with their colours, and the codes", () => {
  const [map] = checkCollections(data(), guides);
  assert.equal(map.map.center.id, "hub");
  assert.deepEqual(
    map.map.groups.map((group) => group.id),
    ["a", "b", "c", "d", "e", "f", "g", "h"].map((id) => `group-${id}`),
  );
  assert.equal(map.map.groups[0].colour.base, "#9747FF");
  assert.deepEqual(map.map.groups[0].guides, [{ id: "a" }]);
  assert.deepEqual(map.map.groups[0].coming, []);
  assert.equal(map.map.codes.a, "Aa");
});

test("shows a coming guide as a real guide, in its place, once it is built", () => {
  const groups = data();
  groups.collections[1].coming = [
    { id: "z", title: "Zed" },
    { id: "w", title: "Double-u" },
  ];
  groups.collections[0].groups[6].coming = [{ id: "v", title: "Vee" }];
  const [map, home] = checkCollections(groups, [...guides, ...ids("z", "v")]);
  assert.deepEqual(home.guides, ids("x", "y", "z"));
  assert.deepEqual(home.coming, [{ id: "w", title: "Double-u" }]);
  assert.deepEqual(home.entries, [
    { guide: { id: "x" } },
    { guide: { id: "y" } },
    { guide: { id: "z" } },
    { coming: { id: "w", title: "Double-u" } },
  ]);
  assert.deepEqual(map.map.groups[6].guides, ids("g", "v"));
  assert.deepEqual(map.map.groups[6].coming, []);
});

test("fails when a guide is in no collection", () => {
  assert.throws(() => checkCollections(data(), [...guides, { id: "new" }]), /guide "new" is in no collection/);
});

test("fails when a collection lists a guide that isn't in guides.json", () => {
  const groups = data();
  groups.collections[1].guides.push("gone");
  assert.throws(() => checkCollections(groups, guides), /collection "Collection home" lists "gone", which is not in/);
  const inGroup = data();
  inGroup.collections[0].groups[2].guides.push("gone");
  assert.throws(() => checkCollections(inGroup, guides), /group "Group c" in collection "Mapped" lists "gone"/);
});

test("fails when a guide is listed twice", () => {
  const groups = data();
  groups.collections[1].guides.push("a");
  assert.throws(() => checkCollections(groups, guides), /"a" is listed by group "Group a" in collection "Mapped" and/);
  const coming = data();
  coming.collections[1].coming.push({ id: "x", title: "Ex again" });
  assert.throws(() => checkCollections(coming, guides), /"x" is listed by collection "Collection home" and/);
});

test("fails when the catalog is also in a group, or isn't in guides.json", () => {
  const groups = data();
  groups.collections[0].groups[0].guides.push("hub");
  assert.throws(() => checkCollections(groups, guides), /"hub" is listed by collection "Mapped" \(its catalog\) and/);
  const missing = data();
  missing.collections[0].catalog = "missing";
  assert.throws(() => checkCollections(missing, guides), /catalog guide "missing" is not in guides.json/);
});

test("fails when a guide on a map has no code, or shares one", () => {
  const groups = data();
  delete groups.collections[0].codes.c;
  groups.collections[0].codes.d = "Aa";
  assert.throws(() => checkCollections(groups, guides), /needs a two-letter code for "c"/);
  assert.throws(() => checkCollections(groups, guides), /gives "a" and "d" the same code/);
});

test("fails when a group on a map has no colour", () => {
  const groups = data();
  delete groups.collections[0].groups[3].colour;
  assert.throws(() => checkCollections(groups, guides), /group "Group d" in collection "Mapped" needs a colour/);
});

test("fails on a repeated or malformed id, code or colour", () => {
  const groups = data();
  groups.collections[1].id = "mapped";
  groups.collections[1].code = "ABC";
  groups.collections[1].colour = "teal";
  groups.collections[1].coming.push({ id: "Not A Slug", title: "Bad" });
  assert.throws(() => checkCollections(groups, guides), /two collections have the id "mapped"/);
  assert.throws(() => checkCollections(groups, guides), /two-letter code/);
  assert.throws(() => checkCollections(groups, guides), /needs a colour/);
  assert.throws(() => checkCollections(groups, guides), /coming guide without an id/);
});

test("the site's collections.json fits the guides it lists", () => {
  // guides.json is a build output, so check the data file against its own listed ids: every catalog and every
  // collection's and group's guides, each once. The coming guides need not exist.
  const data = JSON.parse(readFileSync(new URL("../src/data/collections.json", import.meta.url), "utf8"));
  const listed = data.collections.flatMap((collection) =>
    collection.groups
      ? [collection.catalog, ...collection.groups.flatMap((group) => group.guides ?? [])]
      : (collection.guides ?? []),
  );
  assert.doesNotThrow(() => checkCollections(data, ids(...listed)));
});

test("keeps a built coming guide in its place among the ones still to come", () => {
  const groups = data();
  groups.collections[1].coming = [
    { id: "w", title: "Double-u" },
    { id: "z", title: "Zed" },
    { id: "q", title: "Queue" },
  ];
  const [, home] = checkCollections(groups, [...guides, ...ids("z")]);
  assert.deepEqual(
    home.entries.map((entry) => entry.guide?.id ?? `coming ${entry.coming.id}`),
    ["x", "y", "coming w", "z", "coming q"],
  );
});
