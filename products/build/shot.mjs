import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 });
for (const f of fs.readdirSync('img').filter(f => f.endsWith('.html'))) {
  await p.goto('file://' + process.cwd() + '/img/' + f, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  // QA: any text box leaving the frame or overlapping another text box
  const issues = await p.evaluate(() => {
    const out = []; const els = [...document.querySelectorAll('.frame *')].filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()));
    const R = els.map(e => [e, e.getBoundingClientRect()]);
    for (const [e, r] of R) if (r.left < 20 || r.right > 1260 || r.top < 16 || r.bottom > 712) out.push('edge: ' + e.textContent.trim().slice(0, 30));
    for (let i = 0; i < R.length; i++) for (let j = i + 1; j < R.length; j++) {
      const [a, ra] = R[i], [c, rc] = R[j]; if (a.contains(c) || c.contains(a)) continue;
      if (Math.min(ra.right, rc.right) - Math.max(ra.left, rc.left) > 2 && Math.min(ra.bottom, rc.bottom) - Math.max(ra.top, rc.top) > 2) out.push('overlap: ' + a.textContent.trim().slice(0, 20) + ' / ' + c.textContent.trim().slice(0, 20));
    }
    return out;
  });
  await p.screenshot({ path: 'img/' + f.replace('.html', '.png') });
  console.log(f.replace('.html', '.png'), issues.length ? issues.join(' | ') : 'OK');
}
await b.close();
