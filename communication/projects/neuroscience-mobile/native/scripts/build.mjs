import { cpSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const native = resolve(here, "..");
const source = resolve(native, "..");
const output = resolve(native, "dist");
mkdirSync(output, { recursive: true });
cpSync(resolve(source, "index.html"), resolve(output, "index.html"));
cpSync(resolve(source, "manifest.webmanifest"), resolve(output, "manifest.webmanifest"));
console.log(`Copied mobile demo into ${output}`);
