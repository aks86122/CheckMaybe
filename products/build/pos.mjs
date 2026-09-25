import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [,, html, pageNo, ...sels] = process.argv;
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready);
const r = await p.evaluate(([n, sels]) => {
  const pg = document.querySelectorAll('.page')[n - 1]; const pr = pg.getBoundingClientRect();
  const main = pg.querySelector('.main'); if (main) main.style.zoom = 1;
  return sels.map(s => { const e = pg.querySelector(s); if (!e) return [s, null]; const r = e.getBoundingClientRect();
    return [s, +((r.left - pr.left) / pr.width).toFixed(3), +((r.top - pr.top) / pr.height).toFixed(3), +((r.right - pr.left) / pr.width).toFixed(3), +((r.bottom - pr.top) / pr.height).toFixed(3)]; });
}, [+pageNo, sels]);
console.log(JSON.stringify(r)); await b.close();
