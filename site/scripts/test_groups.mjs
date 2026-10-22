// Tests for src/lib/groups.mjs, the check that every guide is on the landing page's map. Run from site/:
//
//     node --test scripts/test_groups.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { checkGroups } from "../src/lib/groups.mjs";

const guides = ["hub", "a", "b", "c", "d", "e", "f", "g", "h"].map((id) => ({ id }));
const data = () => ({
  center: "hub",
  groups: ["a", "b", "c", "d", "e", "f", "g", "h"].map((id) => ({ id: `group-${id}`, name: `Group ${id}`, guides: [id] })),
});

test("places the eight groups around the center, in reading order", () => {
  const map = checkGroups(data(), guides);
  assert.equal(map.center.id, "hub");
  assert.deepEqual(
    map.groups.map((group) => [group.row, group.column]),
    [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]],
  );
  assert.deepEqual(map.groups[0].guides, [{ id: "a" }]);
  assert.deepEqual(map.groups[0].coming, []);
});

test("keeps the guides' order and the coming titles", () => {
  const groups = data();
  groups.groups[0].guides = ["b", "a"];
  groups.groups[1].guides = [];
  groups.groups[1].coming = ["Later"];
  const map = checkGroups(groups, guides);
  assert.deepEqual(map.groups[0].guides.map((guide) => guide.id), ["b", "a"]);
  assert.deepEqual(map.groups[1].coming, ["Later"]);
});

test("fails when a guide is in no group", () => {
  assert.throws(() => checkGroups(data(), [...guides, { id: "new" }]), /guide "new" is in no group/);
});

test("fails when a guide is in two groups", () => {
  const groups = data();
  groups.groups[1].guides.push("a");
  assert.throws(() => checkGroups(groups, guides), /guide "a" is in "Group a" and "Group b"/);
});

test("fails when the center guide is also in a group", () => {
  const groups = data();
  groups.groups[0].guides.push("hub");
  assert.throws(() => checkGroups(groups, guides), /guide "hub" is in the center and "Group a"/);
});

test("fails when a group lists a guide that isn't in guides.json", () => {
  const groups = data();
  groups.groups[2].guides.push("gone");
  assert.throws(() => checkGroups(groups, guides), /group "Group c" lists "gone", which is not in guides.json/);
});

test("fails when the center guide isn't in guides.json", () => {
  const groups = data();
  groups.center = "missing";
  assert.throws(() => checkGroups(groups, guides), /center guide "missing" is not in guides.json/);
});

test("fails without exactly eight groups", () => {
  const groups = data();
  groups.groups.pop();
  assert.throws(() => checkGroups(groups, guides.slice(0, -1)), /there are 7 groups/);
});

test("fails on a repeated or malformed group id", () => {
  const groups = data();
  groups.groups[1].id = "group-a";
  groups.groups[2].id = "Group C";
  assert.throws(() => checkGroups(groups, guides), /two groups have the id "group-a"/);
  assert.throws(() => checkGroups(groups, guides), /needs an id in lowercase-with-hyphens/);
});

test("the site's groups.json fits the guides it lists", () => {
  // guides.json is a build output, so check the data file against its own ids: the center and every group's
  // guides, each once.
  const groups = JSON.parse(readFileSync(new URL("../src/data/groups.json", import.meta.url), "utf8"));
  const ids = [groups.center, ...groups.groups.flatMap((group) => group.guides)];
  assert.doesNotThrow(() => checkGroups(groups, ids.map((id) => ({ id }))));
});
