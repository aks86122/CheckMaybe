import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const [f, w, h] of [['free-audit-cover',1280,720],['free-audit-preview',1280,720],['free-audit-featured',1280,720],['free-audit-thumb',600,600]]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/img/' + f + '.html', { waitUntil: 'load' }); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: 'img/' + f + '.png' }); console.log(f); await p.close();
}
await b.close();
