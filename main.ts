// news-image-20261122 entry: the picture of Sunday 22 November 2026.
// The image itself lives in entry.png beside this file (drawn by
// generate.py from that day's verified headlines). The grader runs
// this program with no network, so it simply delivers the picture:
// it copies entry.png to the output directory as entry.png, which
// the gate accepts as a whole PNG of at most 1 MiB and 1024x1024.
// Locally, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const here = new URL(".", import.meta.url);
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
copyFileSync(new URL("entry.png", here), join(targetDir, "entry.png"));
