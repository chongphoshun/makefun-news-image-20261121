// news-image-20261121 — Saturday 21 November 2026.
//
// The entry is a program that writes one image, /output/entry.png: a
// newspaper front page holding 37 dated stories from Saturday 21
// November 2026 — 3 leads, 12 mains, a numbered world map, a UTC
// timeline, a BY THE NUMBERS strip and 22 more one-line briefs.
//
// The picture itself lives in this repository as entry.png, drawn by
// draw_20261121.py (PIL, no network, deterministic). This program only
// checks that file is a whole 1024x1024 PNG under the 1 MiB cap and
// copies it to the output directory, so both grader runs produce the
// exact same bytes.
//
// Run it locally:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdir, readFile, stat, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

const png = await readFile(source);

// PNG signature: 89 50 4E 47 0D 0A 1A 0A. Anything else is not the file
// this entry promises, so fail loudly instead of shipping it.
const signature = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
for (let i = 0; i < signature.length; i++) {
  if (png[i] !== signature[i]) {
    throw new Error("entry.png is not a PNG file");
  }
}

// The IHDR chunk stores width at offset 16 and height at offset 20,
// both big-endian. The competition wants exactly 1024 by 1024.
const width = png.readUInt32BE(16);
const height = png.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`entry.png is ${width}x${height}, not 1024x1024`);
}

// The gate refuses anything over a mebibyte; refuse it here first.
if (png.length > 1024 * 1024) {
  throw new Error(`entry.png is ${png.length} bytes, over the 1 MiB cap`);
}

// A whole PNG ends with the IEND chunk: 00 00 00 00 49 45 4E 44 AE 42
// 60 82. A file cut short would still pass the header checks above,
// so check the tail too.
const iend = [0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82];
const tail = png.subarray(png.length - iend.length);
for (let i = 0; i < iend.length; i++) {
  if (tail[i] !== iend[i]) {
    throw new Error("entry.png is truncated: no IEND chunk at the end");
  }
}

await mkdir(outDir, { recursive: true });
await writeFile(target, png);

// Confirm the copy landed whole before reporting success.
const written = await stat(target);
if (written.size !== png.length) {
  throw new Error("entry.png copy is incomplete");
}
