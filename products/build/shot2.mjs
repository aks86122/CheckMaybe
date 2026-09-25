import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 600, height: 600 }, deviceScaleFactor: 2 });
for (const s of ['can-i-sell-this', 'can-i-use-this']) {
  await p.goto('file://' + process.cwd() + '/img/' + s + '-thumb.html'); await p.evaluate(() => document.fonts.ready);
  const bad = await p.evaluate(() => [...document.querySelectorAll('.f > div:not(.blob)')].filter(e => { const r = e.getBoundingClientRect(); return r.right > 580 || r.bottom > 580; }).map(e => e.className));
  await p.screenshot({ path: 'img/' + s + '-thumb.png' }); console.log(s, bad.length ? 'EDGE ' + bad : 'OK');
}
await b.close();
