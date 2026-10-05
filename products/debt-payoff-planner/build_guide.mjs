// Buyer access guide PDF for the Debt Payoff Planner.
// Usage: node build_guide.mjs "https://docs.google.com/spreadsheets/d/<ID>/copy"
// Without a link it builds a DRAFT with a visible placeholder (never upload the draft to Etsy).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const link = process.argv[2] || '';
const draft = !/^https:\/\/docs\.google\.com\/spreadsheets\/d\/[\w-]+\/copy$/.test(link);
if (process.argv[2] && draft) { console.error('Link must look like https://docs.google.com/spreadsheets/d/<ID>/copy'); process.exit(1); }
const href = draft ? '#' : link;
const shown = draft ? 'PASTE YOUR /copy LINK HERE (draft)' : link.replace('https://', '');
const out = draft ? 'Debt-Payoff-Planner-Access-Guide-DRAFT.pdf' : 'Debt-Payoff-Planner-Access-Guide.pdf';

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
const foot = (n) => `<div class="foot"><span>DEBT PAYOFF PLANNER · CHECKMAYBE</span><span>${n} / 4</span></div>${draft ? '<div class="draft">DRAFT · DO NOT UPLOAD</div>' : ''}`;

const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>

<section class="page">
  <div class="kick">Google Sheets template · also works in Excel · any currency</div>
  <h1>Debt Payoff<br>Planner</h1>
  <p class="lead">Snowball and avalanche, plus the things real contracts have: early-payoff fees, lock-in periods, 0% deals with a deadline, and debts that are already behind.</p>
  <div class="kpis">
    <div class="kpi"><span>FOUR ORDERS</span><b style="color:var(--orange)">compared</b><div class="small muted">debt-free date, interest and fees side by side</div></div>
    <div class="kpi"><span>EARLY-PAYOFF FEE</span><b style="color:var(--amber)">worth it?</b><div class="small muted">fee vs the interest you'd save</div></div>
    <div class="kpi"><span>0% DEALS</span><b style="color:var(--red)">deadline</b><div class="small muted">warns before back-interest hits</div></div>
  </div>
  <div class="card">
    <div class="kick" style="margin-bottom:10px">From the example debts · $1,500 a month</div>
    <table class="mock">
      <tr><td>Avalanche</td><td class="muted">highest APR first</td><td>$1,599 interest</td><td><span class="chip c-red">MISSES 0% DEADLINE</span></td></tr>
      <tr><td>Smart</td><td class="muted">behind → deadlines → APR</td><td>$1,679 interest</td><td><span class="chip c-green">CLEARS IT IN TIME</span></td></tr>
      <tr><td>Car loan</td><td class="muted">$400 fee to pay off early</td><td>saves about $917</td><td><span class="chip c-amber">FEE CHECK</span></td></tr>
      <tr><td>Personal loan</td><td class="muted">rule: not sure</td><td>minimums only</td><td><span class="chip c-blue">ASK LENDER</span></td></tr>
    </table>
  </div>
  <div class="card" style="margin-top:auto">
    <div class="kick" style="margin-bottom:10px">Step 1 · get your own copy</div>
    <a class="btn" href="${href}">OPEN MY PLANNER →</a>
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
    <div class="card"><div class="num">2</div><h3>List your debts</h3><p class="small muted">On <b style="color:var(--txt)">My Debts</b> you only need name, balance, APR and minimum payment. Everything else is optional: leave it blank if it doesn't apply.</p></div>
    <div class="card"><div class="num">3</div><h3>Set your plan</h3><p class="small muted">On <b style="color:var(--txt)">Plan</b>, enter what you can pay toward all debts each month and pick an order. Compare all four.</p></div>
  </div>
  <div class="card">
    <h3>Colour code</h3>
    <p class="small muted">Columns with a <span class="chip c-blue">BLUE header</span> are yours to fill in. Columns with an <span class="chip c-orange">ORANGE header</span> calculate themselves: leave them alone. Example rows are marked (sample): overwrite or clear them.</p>
  </div>
  <div class="card">
    <h3>The four payoff orders</h3>
    <table class="mock">
      <tr><td><b>Smart</b></td><td class="muted">Behind-on-payments first, then 0%/deferred-interest deadlines, then highest APR. If minimums take 35%+ of your income, it frees up monthly money first.</td></tr>
      <tr><td><b>Avalanche</b></td><td class="muted">Highest APR first. Usually the least interest on paper.</td></tr>
      <tr><td><b>Snowball</b></td><td class="muted">Smallest balance first. Quick wins.</td></tr>
      <tr><td><b>Cash-flow</b></td><td class="muted">The debt whose minimum is largest compared with its balance first, so monthly money frees up fastest.</td></tr>
    </table>
  </div>
  <div class="grid2">
    <div class="card"><h3>On your phone</h3><p class="small muted">Install the free Google Sheets app and open the copy from your Drive. Dark mode looks washed out? Tap ⋮ › <b style="color:var(--txt)">View in light theme</b>.</p></div>
    <div class="card"><h3>Prefer Excel?</h3><p class="small muted">In your Google copy choose File › Download › Microsoft Excel (.xlsx). Everything calculates.</p></div>
  </div>
  ${foot(2)}
</section>

<section class="page">
  <div class="kick">The parts other trackers skip</div>
  <h2>Real contracts have rules</h2>
  <div class="card">
    <h3>Early payoff rule</h3>
    <p class="small muted"><span class="chip c-green">Allowed, no fee</span> extra money can go here any time. Blank counts as this.</p>
    <p class="small muted" style="margin-top:6px"><span class="chip c-amber">Allowed with a fee</span> enter the fee and when it ends. The sheet compares the fee with the interest you'd save by paying early. Worth it: extra goes in now and the fee is added to your totals. Not worth it: extra waits until the fee ends.</p>
    <p class="small muted" style="margin-top:6px"><span class="chip c-orange">Locked until a date</span> minimums only until that date.</p>
    <p class="small muted" style="margin-top:6px"><span class="chip c-red">Not sure</span> minimums only. Ask your lender, then change the rule.</p>
  </div>
  <div class="card">
    <h3>0% and promo deals</h3>
    <p class="small muted">Enter when the promo ends and the APR after it: the rate switches on that date. If the deal has <b style="color:var(--txt)">deferred interest</b> (back-interest from day one if you don't clear it in time), mark it Yes. Smart pays these off before the deadline, and every order that misses a deadline gets a warning.</p>
  </div>
  <div class="card">
    <h3>Checks on the Plan tab</h3>
    <ul class="small muted">
      <li>Your monthly amount is less than your minimums.</li>
      <li>A minimum payment doesn't cover the interest (that debt grows).</li>
      <li>Some debts are locked or uncertain.</li>
      <li>A deferred-interest deadline is missed in the order you picked.</li>
    </ul>
  </div>
  ${foot(3)}
</section>

<section class="page">
  <div class="kick">Questions</div>
  <h2>FAQ</h2>
  <div class="card"><h3>Is my information private?</h3><p class="small muted">Yes. Your copy lives in your own Google Drive. We never see it, and nothing is sent anywhere.</p></div>
  <div class="card"><h3>My currency isn't dollars.</h3><p class="small muted">It works in any currency: just use the same one everywhere. Amounts have no symbol on purpose.</p></div>
  <div class="card"><h3>Dates show in another language.</h3><p class="small muted">File › Settings › Locale, pick your country. Dates and number formats follow it.</p></div>
  <div class="card"><h3>How many debts?</h3><p class="small muted">Up to 12. Blank rows anywhere in the table are fine. The plan runs up to 30 years.</p></div>
  <div class="card"><h3>Why is my debt-free date different from my lender's?</h3><p class="small muted">The planner works out interest monthly at APR ÷ 12 and doesn't include back-interest, late fees or rate changes you haven't entered. Your lender's statement is the final word.</p></div>
  <p class="small muted" style="margin-top:auto">Estimates only, not financial, legal or tax advice. Contracts differ by country and lender. For personal use only: please don't share or resell the template link.</p>
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
