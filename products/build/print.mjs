// Usage: node print.mjs in.html out.pdf report.json
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const [,, inHtml, outPdf, reportPath] = process.argv;
const b = await chromium.launch({ headless: true });
const p = await b.newPage();
await p.goto('file://' + inHtml, { waitUntil: 'load' });
await p.evaluate(() => document.fonts.ready);

const report = await p.evaluate(() => {
  const MM = 96 / 25.4, SAFE = 8 * MM;
  const out = [];
  const pages = [...document.querySelectorAll('.page')];
  const fits = (pg) => { const m = pg.querySelector('.main'); return !m || m.scrollHeight <= m.clientHeight + 1; };
  pages.forEach((pg, i) => {
    // auto-fit: shrink the content block slightly (never below 88%) before failing
    let z = 1; const main = pg.querySelector('.main');
    while (main && !fits(pg) && z > 0.885) { z = +(z - 0.02).toFixed(2); main.style.zoom = z; }
    const issues = [];
    if (!fits(pg)) issues.push('main overflows by ' + Math.round(main.scrollHeight - main.clientHeight) + 'px');
    const pr = pg.getBoundingClientRect();
    const els = [...pg.querySelectorAll('*')];
    for (const el of els) {
      if (getComputedStyle(el).overflow === 'hidden' && el !== pg && (el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1))
        issues.push('clipped: ' + el.className + ' ' + (el.textContent || '').trim().slice(0, 40));
    }
    // text overlap between leaf text boxes
    const leaves = els.filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()));
    const rects = leaves.map(e => { const rg = document.createRange(); rg.selectNodeContents(e); return [...rg.getClientRects()].map(r => ({ e, r })); }).flat();
    for (const { e, r } of rects) {
      if (r.left < pr.left + SAFE - 1 || r.right > pr.right - SAFE + 1 || r.top < pr.top + 4 * MM || r.bottom > pr.bottom - 4 * MM)
        issues.push('text outside safe zone: ' + e.textContent.trim().slice(0, 40));
    }
    for (let a = 0; a < rects.length; a++) for (let c = a + 1; c < rects.length; c++) {
      const A = rects[a], C = rects[c];
      if (A.e === C.e || A.e.contains(C.e) || C.e.contains(A.e)) continue;
      const ix = Math.min(A.r.right, C.r.right) - Math.max(A.r.left, C.r.left);
      const iy = Math.min(A.r.bottom, C.r.bottom) - Math.max(A.r.top, C.r.top);
      if (ix > 2 && iy > 2) issues.push('text overlap: "' + A.e.textContent.trim().slice(0, 25) + '" / "' + C.e.textContent.trim().slice(0, 25) + '"');
    }
    const used = main ? Math.round(100 * [...main.children].reduce((s, ch) => s + ch.getBoundingClientRect().height, 0) / main.clientHeight) : null;
    out.push({ page: i + 1, zoom: z, fill_pct: used, issues: [...new Set(issues)] });
  });
  return out;
});
await p.pdf({ path: outPdf, format: 'A4', printBackground: true, preferCSSPageSize: true });
fs.writeFileSync(reportPath, JSON.stringify(report, null, 1));
const bad = report.filter(r => r.issues.length);
console.log(`pages=${report.length} failing=${bad.length} zoomed=${report.filter(r => r.zoom < 1).map(r => r.page + '@' + r.zoom).join(',')}`);
for (const r of bad) console.log('p' + r.page, r.issues.slice(0, 4).join(' | '));
console.log('low fill (<45%):', report.filter(r => r.fill_pct !== null && r.fill_pct < 45).map(r => r.page + ':' + r.fill_pct + '%').join(', '));
await b.close();
