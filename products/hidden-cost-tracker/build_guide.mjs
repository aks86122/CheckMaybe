// Buyer access guide PDF for the Hidden Cost Tracker.
// Usage: node build_guide.mjs "https://docs.google.com/spreadsheets/d/<ID>/copy"
// Without a link it builds a DRAFT with a visible placeholder (never upload the draft to Etsy).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const link = process.argv[2] || '';
const draft = !/^https:\/\/docs\.google\.com\/spreadsheets\/d\/[\w-]+\/copy$/.test(link);
if (process.argv[2] && draft) { console.error('Link must look like https://docs.google.com/spreadsheets/d/<ID>/copy'); process.exit(1); }
const href = draft ? '#' : link;
const shown = draft ? 'PASTE YOUR /copy LINK HERE (draft)' : link.replace('https://', '');
const out = draft ? 'Hidden-Cost-Tracker-Access-Guide-DRAFT.pdf' : 'Hidden-Cost-Tracker-Access-Guide.pdf';

const css = `
@page { size: Letter; margin: 0; }
:root { --bg:#15171F; --panel:#1E2130; --panel2:#262A3D; --line:#33384F; --txt:#EDEBF5; --muted:#9A98AE;
  --orange:#F08A4B; --blue:#8AB4FF; --red:#FF6B6B; --amber:#F2B544; --green:#5FD38D; --purple:#B18CFF; --teal:#4FC3C7; }
* { box-sizing:border-box; margin:0; padding:0; }
body { background:var(--bg); color:var(--txt); font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif; font-size:11pt; line-height:1.45;
  -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:8.5in; height:11in; padding:0.6in 0.7in 0.8in; position:relative; overflow:hidden; page-break-after:always; display:flex; flex-direction:column; gap:18px; }
.page:last-child { page-break-after:auto; }
.kick { font-size:8pt; letter-spacing:.2em; color:var(--muted); font-weight:bold; text-transform:uppercase; }
h1 { font-size:34pt; line-height:1.05; color:var(--orange); letter-spacing:.01em; }
h2 { font-size:20pt; line-height:1.15; }
h3 { font-size:11.5pt; margin-bottom:4px; }
p.lead { color:var(--muted); font-size:12pt; max-width:6.3in; }
.card { background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:16px 18px; }
.btn { display:block; text-align:center; background:var(--orange); color:#15171F; text-decoration:none; font-weight:bold; font-size:17pt;
  letter-spacing:.04em; padding:18px; border-radius:12px; }
.url { text-align:center; font-size:8.5pt; color:${draft ? 'var(--red)' : 'var(--muted)'}; word-break:break-all; margin-top:8px; }
.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }
.num { display:inline-flex; width:30px; height:30px; border-radius:50%; align-items:center; justify-content:center; font-weight:bold;
  background:var(--panel2); color:var(--orange); border:1px solid var(--orange); margin-bottom:8px; }
.muted { color:var(--muted); } .small { font-size:9pt; }
.grid2 { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.chip { display:inline-block; font-size:8pt; font-weight:bold; padding:2px 9px; border-radius:99px; margin-right:6px; }
.c-red { color:var(--red); background:#4A1D22; } .c-amber { color:var(--amber); background:#4A3A15; } .c-green { color:var(--green); background:#173A28; }
.c-blue { color:var(--blue); background:#1C2B4A; } .c-orange { color:var(--orange); background:#4A2A18; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpi { background:var(--panel); border-radius:10px; padding:12px 14px; border:1px solid var(--line); }
.kpi b { display:block; font-size:18pt; }
.kpi span { font-size:7.5pt; letter-spacing:.14em; color:var(--muted); font-weight:bold; }
ul { padding-left:18px; } li { margin:3px 0; }
table { width:100%; border-collapse:collapse; font-size:10pt; }
td { padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top; }
td:first-child { width:30%; font-weight:bold; }
.mock td { padding:7px 6px; font-size:9.5pt; } .mock td:first-child { width:auto; } .mock tr:last-child td { border-bottom:none; }
.foot { position:absolute; left:0.7in; right:0.7in; bottom:0.35in; display:flex; justify-content:space-between; font-size:7.5pt;
  color:var(--muted); letter-spacing:.12em; border-top:1px solid var(--line); padding-top:6px; }
.draft { position:absolute; top:0.2in; right:0.3in; color:var(--red); font-weight:bold; font-size:9pt; letter-spacing:.2em; }
`;
const foot = (n) => `<div class="foot"><span>HIDDEN COST TRACKER · CHECKMAYBE</span><span>${n} / 4</span></div>${draft ? '<div class="draft">DRAFT · DO NOT UPLOAD</div>' : ''}`;

const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>

<section class="page">
  <div class="kick">Google Sheets template · also works in Excel</div>
  <h1>Hidden Cost<br>Tracker</h1>
  <p class="lead">See what your debts, installments, buy-now-pay-later plans and subscriptions really cost you, and catch the ones quietly costing the most.</p>
  <div class="kpis">
    <div class="kpi"><span>REAL APR</span><b style="color:var(--red)">worked out</b><div class="small muted">from just your monthly payment</div></div>
    <div class="kpi"><span>FREE TRIALS</span><b style="color:var(--amber)">cancel-by</b><div class="small muted">date and countdown for each trial</div></div>
    <div class="kpi"><span>EVERY MONTH</span><b style="color:var(--orange)">% committed</b><div class="small muted">of your income, before you spend</div></div>
  </div>
  <div class="card">
    <div class="kick" style="margin-bottom:10px">What it catches · from the example rows</div>
    <table class="mock">
      <tr><td>Phone installment plan</td><td class="muted">24 × $67 on a $1,200 phone</td><td>29.8% APR</td><td><span class="chip c-red">HIGH</span></td></tr>
      <tr><td>Sofa store financing</td><td class="muted">24 × $105 on a $2,000 sofa</td><td>23.3% APR</td><td><span class="chip c-red">HIGH</span></td></tr>
      <tr><td>Laptop pay-in-4</td><td class="muted">4 × $200 on an $800 laptop</td><td>0.0% APR</td><td><span class="chip c-green">OK</span></td></tr>
      <tr><td>Sports streaming</td><td class="muted">7-day free trial, then $9.99 a month</td><td>cancel in 2 days</td><td><span class="chip c-amber">TRIAL</span></td></tr>
      <tr><td>Gym + beauty box + 2 more</td><td class="muted">ticked "Cancel it?"</td><td style="color:var(--green)">save $1,104 / yr</td><td></td></tr>
    </table>
  </div>
  <div class="card" style="margin-top:auto">
    <div class="kick" style="margin-bottom:10px">Step 1 · get your own copy</div>
    <a class="btn" href="${href}">OPEN MY TRACKER →</a>
    <div class="url">${shown}</div>
    <p class="small muted" style="margin-top:12px">Click the button, then choose <b style="color:var(--txt)">Make a copy</b>. The copy is yours, saved in your own Google Drive. Nobody else can see what you enter, including us.</p>
  </div>
  ${foot(1)}
</section>

<section class="page">
  <div class="kick">How it works</div>
  <h2>Ready in about five minutes</h2>
  <div class="steps">
    <div class="card"><div class="num">1</div><h3>Make your copy</h3><p class="small muted">Open the link on page 1 while signed in to Google and press <b style="color:var(--txt)">Make a copy</b>. No Google account? Create a free one first.</p></div>
    <div class="card"><div class="num">2</div><h3>Add your numbers</h3><p class="small muted">Start with <b style="color:var(--txt)">Settings</b> (your monthly take-home pay), then add your debts and subscriptions. The example rows are made up: overwrite or delete them.</p></div>
    <div class="card"><div class="num">3</div><h3>Check the Dashboard</h3><p class="small muted">See your highest real APR, what's due next, which free trials to cancel and what you'd save each year.</p></div>
  </div>
  <div class="card">
    <h3>Colour code</h3>
    <p class="small muted" style="margin-bottom:8px">Columns with a <span class="chip c-blue">BLUE header</span> are yours to fill in. Columns with an <span class="chip c-orange">ORANGE header</span> calculate themselves: leave them alone.</p>
    <p class="small muted">Tick <b style="color:var(--txt)">Cancel it?</b> on any subscription you plan to drop. The Dashboard shows the yearly saving straight away.</p>
  </div>
  <div class="grid2">
    <div class="card"><h3>On your phone</h3><p class="small muted">Install the free Google Sheets app, open the copy from your Drive and update it anywhere. Phone in dark mode and the colours look washed out? Tap ⋮ › <b style="color:var(--txt)">View in light theme</b> to see the design as intended.</p></div>
    <div class="card"><h3>Prefer Excel?</h3><p class="small muted">In your Google copy choose File › Download › Microsoft Excel (.xlsx). Everything calculates; tick boxes become Yes/No drop-downs.</p></div>
  </div>
  <div class="card"><h3>Please don't "Request edit access"</h3><p class="small muted">The link opens a view-only master. Always use <b style="color:var(--txt)">Make a copy</b> so you have a file you can edit.</p></div>
  ${foot(2)}
</section>

<section class="page">
  <div class="kick">What's inside</div>
  <h2>Five tabs, one clear picture</h2>
  <table class="card" style="padding:4px 8px">
    <tr><td>Dashboard</td><td class="muted">Income vs money already committed each month, highest real APR, interest still to pay, next charges, free trials to cancel, yearly savings. Switch the spending chart between <i>By category</i> and <i>By subscription</i>.</td></tr>
    <tr><td>Debts &amp; Installments</td><td class="muted">Credit cards, loans, store financing, BNPL. Real APR, payments left, debt-free date, and the order to pay them off (avalanche and snowball).</td></tr>
    <tr><td>Subscriptions</td><td class="muted">Price, billing cycle, next charge date, days until it hits, free-trial cancel-by date and countdown. Filter by category, billing or status.</td></tr>
    <tr><td>Settings</td><td class="muted">Your income, the APR levels that trigger a flag, how many days' warning you want, and the drop-down lists.</td></tr>
    <tr><td>How to Use</td><td class="muted">These instructions, inside the sheet.</td></tr>
  </table>
  <div class="card">
    <h3>"Real APR": the number shops don't show</h3>
    <p class="small muted">Store financing and installment plans often show only a monthly price. Enter what you borrowed, the monthly payment and the number of payments, and the tracker works out the yearly interest rate hidden inside. Example: $1,200 paid as 24 × $67 is about <b style="color:var(--red)">29.8% APR</b>.</p>
  </div>
  <div class="card">
    <h3>What the flags mean</h3>
    <p class="small muted"><span class="chip c-red">HIGH</span> real APR at or above 20% (you can change this in Settings). Pay extra on these first.</p>
    <p class="small muted" style="margin-top:6px"><span class="chip c-amber">CHECK</span> at or above 10%. Worth a look.</p>
    <p class="small muted" style="margin-top:6px"><span class="chip c-green">OK</span> lower-cost debt. Keep paying on time.</p>
  </div>
  ${foot(3)}
</section>

<section class="page">
  <div class="kick">Questions</div>
  <h2>FAQ</h2>
  <div class="card"><h3>Is my information private?</h3><p class="small muted">Yes. Your copy lives in your own Google Drive. We never see it, and nothing is sent anywhere.</p></div>
  <div class="card"><h3>Can I add more rows?</h3><p class="small muted">There is room for 20 debts and 30 subscriptions. To add more, insert a row inside the table (not below it), then copy the row above and paste it into the new row so the formulas come with it.</p></div>
  <div class="card"><h3>My currency isn't dollars.</h3><p class="small muted">Select the money columns and choose Format › Number › Currency (or Custom currency) to switch the symbol. The maths stays the same.</p></div>
  <div class="card"><h3>I overwrote a formula by mistake.</h3><p class="small muted">Use Undo, or open the link on page 1 again and make a fresh copy. Google Sheets also shows a warning before you edit a calculated cell.</p></div>
  <div class="card"><h3>Need help?</h3><p class="small muted">Message us through Etsy and we'll reply as soon as we can.</p></div>
  <p class="small muted" style="margin-top:auto">Estimates only, not financial, legal or tax advice. Real APR is estimated from your payment schedule and does not include fees charged separately; your contract is the final word. For personal use only: please don't share or resell the template link.</p>
  ${foot(4)}
</section>
</body></html>`;

fs.writeFileSync('guide.html', html);
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/guide.html', { waitUntil: 'load' });
const over = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
  const foot = pg.querySelector('.foot').getBoundingClientRect().top;
  const last = [...pg.children].filter(e => !e.classList.contains('foot') && !e.classList.contains('draft')).pop().getBoundingClientRect().bottom;
  return last > foot - 4 ? `page ${i + 1} overflows by ${Math.round(last - foot + 4)}px` : null;
}).filter(Boolean));
await p.pdf({ path: out, width: '8.5in', height: '11in', printBackground: true });
for (let i = 0; i < 4; i++) {
  await p.setViewportSize({ width: 816, height: 1056 });
  await p.evaluate(y => window.scrollTo(0, y), i * 1056);
  await p.screenshot({ path: `${process.env.SHOTS || '.'}/guide-p${i + 1}.png`, clip: { x: 0, y: i * 1056, width: 816, height: 1056 }, fullPage: true });
}
await b.close();
fs.unlinkSync('guide.html');
console.log(out, over.length ? over : 'layout OK');
