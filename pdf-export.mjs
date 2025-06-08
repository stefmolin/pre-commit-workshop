import puppeteer from "puppeteer";
import * as path from "path";

const browser = await puppeteer.launch();
const page = await browser.newPage();

await page.goto(
  path.join(path.dirname(import.meta.url), "index.html?print-pdf")
);

await page.pdf({ path: "slides.pdf", format: "A4", timeout: 0 });

await browser.close();
