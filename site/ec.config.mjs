// Expressive Code reads this file for the code blocks in Markdown, MDX and the <Code> component alike,
// so plugins belong here rather than in Starlight's `expressiveCode` option.
import { createRenderer, defineEcConfig } from "@astrojs/starlight/expressive-code";

import codeFocus, { withoutTabindexScript } from "./scripts/code-focus.mjs";

// Output, plain text and JSON wrap at the edge of the box instead of scrolling sideways. Wrapping only changes
// how a line is drawn: copying still gives the original lines. A wrapped line keeps the indent of the line it
// came from, so nested JSON still lines up. Shell commands and program code do not wrap, because there a line
// that continues below looks like a second command or statement; keep those short instead (break shell
// commands with `\`). A single block can opt in or out with `wrap` or `wrap=false` after the language.
const WRAPPED = "text,txt,plaintext,plain,output,json,jsonc,log";

export default defineEcConfig({
  defaultProps: {
    overridesByLang: { [WRAPPED]: { wrap: true, preserveIndent: true } },
  },
  // Lines that still run long scroll sideways; this lets a keyboard reach and scroll them.
  plugins: [codeFocus()],
  customCreateRenderer: withoutTabindexScript(createRenderer),
});
