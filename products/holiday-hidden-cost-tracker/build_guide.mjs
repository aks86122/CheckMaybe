// Buyer access guide PDF for the Holiday Hidden Cost Tracker.
// Usage: node build_guide.mjs "https://docs.google.com/spreadsheets/d/<ID>/copy"
// Without a link it builds a DRAFT with a visible placeholder (never upload the draft to Etsy).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const link = process.argv[2] || '';
const draft = !/^https:\/\/docs\.google\.com\/spreadsheets\/d\/[\w-]+\/copy$/.test(link);
if (process.argv[2] && draft) { console.error('Link must look like https://docs.google.com/spreadsheets/d/<ID>/copy'); process.exit(1); }
const href = draft ? '#' : link;
const shown = draft ? 'PASTE YOUR /copy LINK HERE (draft)' : link.replace('https://', '');
const out = draft ? 'Holiday-Hidden-Cost-Tracker-Access-Guide-DRAFT.pdf' : 'Holiday-Hidden-Cost-Tracker-Access-Guide.pdf';

const css = `
@page { size: Letter; margin: 0; }
:root { --bg:#101A14; --panel:#17251D; --panel2:#1F3127; --line:#2C4436; --txt:#F3EFE4; --muted:#A9B5AC;
  --orange:#E0B05A; --blue:#8AB4FF; --red:#FF6B6B; --amber:#F2B544; --green:#5FD38D; --purple:#B18CFF; --teal:#4FC3C7; }
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
.btn { display:block; text-align:center; background:var(--orange); color:#101A14; text-decoration:none; font-weight:bold; font-size:17pt;
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
const foot = (n) => `<div class="foot"><span>HOLIDAY HIDDEN COST TRACKER · CHECKMAYBE</span><span>${n} / 4</span></div>${draft ? '<div class="draft">DRAFT · DO NOT UPLOAD</div>' : ''}`;

const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>

<section class="page">
  <div class="kick">Google Sheets template · also works in Excel</div>
  <h1>Holiday Hidden<br>Cost Tracker</h1>
  <p class="lead">Your gift budget, and what the holidays will still cost you in January. Gifts, pay-in-4 and store financing, and free trials, in one place.</p>
  <div class="kpis">
    <div class="kpi"><span>JANUARY</span><b style="color:var(--red)">what's due</b><div class="small muted">from every holiday plan, month by month</div></div>
    <div class="kpi"><span>REAL APR</span><b style="color:var(--orange)">worked out</b><div class="small muted">from just the payment and the price</div></div>
    <div class="kpi"><span>FREE TRIALS</span><b style="color:var(--amber)">cancel-by</b><div class="small muted">date and countdown for each trial</div></div>
  </div>
  <div class="card">
    <div class="kick" style="margin-bottom:10px">From the example rows</div>
    <table class="mock">
      <tr><td>Gift budget</td><td class="muted">$1,500 planned, $1,734 spent</td><td>$234 over</td><td><span class="chip c-red">OVER</span></td></tr>
      <tr><td>Game console</td><td class="muted">6 × $89.50 on a $499 console</td><td>25.7% APR</td><td><span class="chip c-red">HIGH</span></td></tr>
      <tr><td>4K TV</td><td class="muted">12 × $59 on a $649 TV</td><td>16.4% APR</td><td><span class="chip c-amber">CHECK</span></td></tr>
      <tr><td>Smart watch</td><td class="muted">pay-in-4, first payment at checkout</td><td>0.0% APR</td><td><span class="chip c-green">OK</span></td></tr>
      <tr><td>January</td><td class="muted">all holiday plans together</td><td style="color:var(--red)">$428.25 due</td><td></td></tr>
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
  <h2>Ready in about ten minutes</h2>
  <div class="steps">
    <div class="card"><div class="num">1</div><h3>Make your copy</h3><p class="small muted">Open the link on page 1 while signed in to Google and press <b style="color:var(--txt)">Make a copy</b>.</p></div>
    <div class="card"><div class="num">2</div><h3>Settings</h3><p class="small muted">Enter your holiday budget, your monthly take-home pay and the first month to plan (usually December).</p></div>
    <div class="card"><div class="num">3</div><h3>Add gifts &amp; plans</h3><p class="small muted">One row per person on <b style="color:var(--txt)">Gift List</b>, one row per payment plan on <b style="color:var(--txt)">Holiday Payments</b>. Example rows are made up: overwrite or delete them.</p></div>
  </div>
  <div class="card">
    <h3>Colour code</h3>
    <p class="small muted">Columns with a <span class="chip c-orange">GOLD header</span> are yours to fill in. Columns with a <span class="chip c-red">BERRY header</span> calculate themselves: leave them alone.</p>
  </div>
  <div class="grid2">
    <div class="card"><h3>On your phone</h3><p class="small muted">Install the free Google Sheets app and open the copy from your Drive. Dark mode looks washed out? Tap ⋮ › <b style="color:var(--txt)">View in light theme</b>.</p></div>
    <div class="card"><h3>Prefer Excel?</h3><p class="small muted">In your Google copy choose File › Download › Microsoft Excel (.xlsx). Everything calculates. Tick boxes turn into TRUE/FALSE cells.</p></div>
  </div>
  <div class="card"><h3>Please don't "Request edit access"</h3><p class="small muted">The link opens a view-only master. Always use <b style="color:var(--txt)">Make a copy</b> so you have a file you can edit.</p></div>
  ${foot(2)}
</section>

<section class="page">
  <div class="kick">What's inside</div>
  <h2>Six tabs, one holiday budget</h2>
  <table class="card" style="padding:4px 8px">
    <tr><td>Dashboard</td><td class="muted">Budget, spent, left, gifts sorted. What your holiday plans charge next month and the month after, highest real APR, trials ending soon, a month-by-month chart, and what's still to buy.</td></tr>
    <tr><td>Gift List</td><td class="muted">Recipient, relationship, gift, budget, actual cost, paid with, status. Gifts bought on a plan are marked.</td></tr>
    <tr><td>Holiday Payments</td><td class="muted">Price, payment, number of payments, every 2 weeks or monthly, first payment date. Works out total, extra cost, real APR, last payment and what each plan charges in each month.</td></tr>
    <tr><td>Free Trials</td><td class="muted">Holiday streaming and shipping trials: cancel-by date, countdown and yearly cost if you keep it.</td></tr>
    <tr><td>Settings</td><td class="muted">Budget, income, first month to plan, APR levels for the flags.</td></tr>
    <tr><td>How to Use</td><td class="muted">These instructions, inside the sheet.</td></tr>
  </table>
  <div class="card">
    <h3>Why January matters</h3>
    <p class="small muted">Pay-in-4 and store financing split one price into small payments, and several small plans tend to land in the same months. The tracker adds them up so you can see January's total before you check out.</p>
  </div>
  <div class="card">
    <h3>What the flags mean</h3>
    <p class="small muted"><span class="chip c-red">HIGH</span> real APR at or above 20%. <span class="chip c-amber">CHECK</span> at or above 10%. <span class="chip c-green">OK</span> little or no extra cost, still a bill to plan for. You can change the levels in Settings.</p>
    <p class="small muted" style="margin-top:6px">0% store offers can charge back-dated interest if a payment is late or the balance isn't cleared in time: check your agreement.</p>
  </div>
  ${foot(3)}
</section>

<section class="page">
  <div class="kick">Questions</div>
  <h2>FAQ</h2>
  <div class="card"><h3>Is my information private?</h3><p class="small muted">Yes. Your copy lives in your own Google Drive. We never see it, and nothing is sent anywhere.</p></div>
  <div class="card"><h3>Dates or months show in another language.</h3><p class="small muted">File › Settings › Locale, pick your country. Dates and currency follow it.</p></div>
  <div class="card"><h3>My currency isn't dollars.</h3><p class="small muted">Select the money columns and choose Format › Number › Currency (or Custom currency). The maths stays the same.</p></div>
  <div class="card"><h3>I overwrote a formula by mistake.</h3><p class="small muted">Use Undo, or open the link on page 1 again and make a fresh copy.</p></div>
  <div class="card"><h3>Already have Hidden Cost Tracker?</h3><p class="small muted">This is its holiday edition: same "real cost" maths, built around gifts and the January bills.</p></div>
  <p class="small muted" style="margin-top:auto">Estimates only, not financial, legal or tax advice. Real APR is estimated from your payment schedule and does not include fees charged separately; your agreement is the final word. For personal use only: please don't share or resell the template link.</p>
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
