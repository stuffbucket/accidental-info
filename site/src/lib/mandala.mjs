// The layout of a collection's map page: the catalog's cover in the middle and the groups down either side of it,
// each joined to the cover by a fine curve. Everything is in the units of a fixed viewBox, so the page can place
// the groups (HTML, so their titles wrap and their links are ordinary links) as percentages over an SVG that draws
// only the curves. Pure functions; runs at build time.
import { linkHorizontal } from "d3-shape";

export const WIDTH = 1000;
// The cover in the middle, in viewBox units, and the room under it for its title.
const COVER = { width: 170, height: 283 };
const COVER_TITLE = 70;
// How far the groups sit from the middle: nearest at the top and bottom of a side, furthest at its middle, so each
// side makes a gentle arc around the cover.
const NEAR = 175;
const FAR = 255;
// The room the curves fan out over where they leave the cover.
const FAN = 60;
// The gap between a curve's end and its group's tiles.
const GAP = 14;
// A group's height, from its name to its last title, in viewBox units at the narrowest width the map is drawn at
// (about 800px wide, so 1 unit is 0.8px): its name, then a row per guide, and a little more for a long title
// that wraps. Then the space between groups and the room above the first.
const NAME = 44;
const ROW = 40;
const WRAP = 24;
const LONG = 30; // characters
const BETWEEN = 56;
const TOP = 24;

/**
 * Lays out the groups in order, the first ones down the left of the cover and the rest down the right, split
 * where the two sides come out most nearly the same height. Each side is stacked by the groups' heights and
 * centred on the cover.
 *
 * @param {string[][]} groups each group's guide titles, in order
 * @returns {{ height: number, cover: { x: number, y: number, width: number, height: number },
 *   groups: { side: "left" | "right", x: number, y: number, link: string, end: [number, number] }[] }}
 *   x and y place each group: its edge nearest the cover (x) and the middle of its name (y). link is the curve's
 *   SVG path, from the cover to end, just short of the group.
 */
export function layout(groups) {
  const tall = (titles) => NAME + titles.reduce((sum, title) => sum + ROW + (title.length > LONG ? WRAP : 0), 0);
  const stack = (heights) => heights.reduce((sum, h) => sum + h, 0) + BETWEEN * Math.max(0, heights.length - 1);
  const all = groups.map(tall);
  // Where the left side ends: the split that makes the two sides most nearly the same height.
  let left = Math.ceil(groups.length / 2);
  for (let k = 1; k < groups.length; k++) {
    const worst = (n) => Math.max(stack(all.slice(0, n)), stack(all.slice(n)));
    if (worst(k) < worst(left)) left = k;
  }
  const heights = [all.slice(0, left), all.slice(left)];
  const sides = [groups.slice(0, left), groups.slice(left)];
  const total = heights.map(stack);
  const height = Math.max(...total, COVER.height + COVER_TITLE + 40) + 2 * TOP;
  const cx = WIDTH / 2;
  const cy = height / 2;
  const link = linkHorizontal()
    .source((d) => d.source)
    .target((d) => d.target);

  const placed = sides.flatMap((side, s) => {
    const sign = s === 0 ? -1 : 1;
    let y = cy - total[s] / 2;
    return side.map((_, i) => {
      // The name's middle; the group hangs below it.
      const at = y + NAME / 4;
      y += heights[s][i] + BETWEEN;
      // -1 at the top of the map, 1 at the bottom.
      const t = Math.max(-1, Math.min(1, (at - cy) / (height / 2 - TOP)));
      const x = cx + sign * (NEAR + (FAR - NEAR) * (1 - t * t));
      const fan = side.length === 1 ? 0 : (i / (side.length - 1) - 0.5) * FAN;
      const source = [cx + sign * (COVER.width / 2 + 16), cy - COVER_TITLE / 2 + fan];
      const end = [x - sign * GAP, at];
      return { side: s === 0 ? "left" : "right", x, y: at, link: link({ source, target: end }), end };
    });
  });

  return {
    height,
    cover: { x: cx - COVER.width / 2, y: cy - (COVER.height + COVER_TITLE) / 2, ...COVER },
    groups: placed,
  };
}
