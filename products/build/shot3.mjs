import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
for (const f of fs.readdirSync('car').filter(f => f.endsWith('.html')).sort()) {
  await p.goto('file://' + process.cwd() + '/car/' + f); await p.evaluate(() => document.fonts.ready);
  const over = await p.evaluate(() => { const b = document.querySelector('.body'); return b.scrollHeight > b.clientHeight + 1 ? b.scrollHeight - b.clientHeight : 0; });
  await p.screenshot({ path: 'car/' + f.replace('.html', '.png') }); if (over) console.log(f, 'OVERFLOW', over);
}
console.log('done'); await b.close();
