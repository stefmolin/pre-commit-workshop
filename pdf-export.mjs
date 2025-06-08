import puppeteer from "puppeteer";
import * as path from "path";

const browser = await puppeteer.launch();
const page = await browser.newPage();

const slidesPath = path.join(
  path.dirname(import.meta.url),
  "index.html?print-pdf"
);
console.log(`Navigating to ${slidesPath}`);

await page.goto(slidesPath);

console.log(`Generating PDF version of the slides for ${await page.title()}`);

await page.pdf({ path: "slides.pdf", format: "A4", timeout: 0 });

await browser.close();
