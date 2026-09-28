import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const [f, w, h] of [['bundle-cover', 1280, 720], ['bundle-portrait', 512, 768], ['bundle-thumb', 600, 600]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/img/' + f + '.html', { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
  const bad = await p.evaluate(([w, h]) => [...document.querySelectorAll('.frame *')].filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
    .filter(e => { const r = e.getBoundingClientRect(); return r.left < 16 || r.right > w - 16 || r.bottom > h - 8; }).map(e => e.textContent.trim().slice(0, 25)), [w, h]);
  await p.screenshot({ path: 'img/' + f + '.png' }); console.log(f, bad.length ? 'EDGE ' + bad.join(' | ') : 'OK'); await p.close();
}
await b.close();
