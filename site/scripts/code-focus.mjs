// Expressive Code gives each code block's <pre> `overflow: auto`, so a long line scrolls sideways. A keyboard
// user can only scroll it if it can take focus (axe: scrollable-region-focusable). This Expressive Code
// plugin gives every <pre> tabindex="0", role="group" and a name (the frame title, or the language) when
// the page is built, the way site/scripts/table-focus.mjs does for tables.
//
// Expressive Code also ships a browser script that adds tabindex and role="region" to blocks that overflow
// and takes them away from blocks that do not. It only runs after a resize observer and a 250 ms wait, so a
// page starts out unreachable, and when it takes the role away it leaves our name on a plain <pre>, where
// ARIA does not allow one. `withoutTabindexScript` drops that script so the built attributes stand.
//
// "group" rather than "region": a page has many blocks with the same name, and regions are landmarks, which
// should each have a unique name (axe: landmark-unique).

// Languages whose name tells a reader nothing.
const PLAIN = new Set(["", "plaintext", "text", "txt", "plain"]);

// Text found only in Expressive Code's tabindex script (from its error message).
export const TABINDEX_SCRIPT_MARKER = "tabindex-js-module";

/** The accessible name for a block: its frame title, else "Code: <language>", else "Code". */
export function codeName({ title, language }) {
  const trimmed = title?.trim();
  if (trimmed) return trimmed;
  const lang = language?.trim().toLowerCase() ?? "";
  return PLAIN.has(lang) ? "Code" : `Code: ${lang}`;
}

/** The first element with this tag name, searching depth first. */
export function findElement(node, tagName) {
  if (node?.type === "element" && node.tagName === tagName) return node;
  for (const child of node?.children ?? []) {
    const found = findElement(child, tagName);
    if (found) return found;
  }
  return null;
}

/** Give the block's <pre> what it needs to take focus and be announced. */
export function makeFocusable(blockAst, codeBlock) {
  const pre = findElement(blockAst, "pre");
  if (!pre) return;
  pre.properties ??= {};
  pre.properties.tabIndex = 0;
  pre.properties.role = "group";
  pre.properties.ariaLabel = codeName({ title: codeBlock.props?.title, language: codeBlock.language });
}

/** Wraps Expressive Code's `createRenderer` so the page does not load its tabindex script. */
export function withoutTabindexScript(createRenderer) {
  return async (options) => {
    const renderer = await createRenderer(options);
    const kept = renderer.jsModules.filter((code) => !code.includes(TABINDEX_SCRIPT_MARKER));
    if (kept.length === renderer.jsModules.length) {
      options?.logger?.warn?.("code-focus: Expressive Code's tabindex script was not found; it may undo code block focus");
    }
    renderer.jsModules = kept;
    return renderer;
  };
}

/** The Expressive Code plugin. */
export default function codeFocus() {
  return {
    name: "code-focus",
    hooks: {
      postprocessRenderedBlock: ({ codeBlock, renderData }) => makeFocusable(renderData.blockAst, codeBlock),
    },
  };
}
