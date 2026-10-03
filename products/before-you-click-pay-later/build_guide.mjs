// Before You Click "Pay Later" — free 12-page mini guide (US Letter, dark).
// Usage: node build_guide.mjs   → Before-You-Click-Pay-Later.pdf (no form fields) + fields.json
// Then:  python3 add_fields.py  → adds the fillable fields on page 10 and writes the final PDF.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';

const TRACKER = 'https://checkmaybe.gumroad.com/l/kofwfjf';
const CFPB_BLOG = 'https://www.consumerfinance.gov/archive/blog/how-understand-special-promotional-financing-offers-credit-cards/';
const CFPB_NEWS = 'https://www.consumerfinance.gov/archive/newsroom/consumer-financial-protection-bureau-encourages-retail-credit-card-companies-consider-more-transparent-promotions/';
const PAGES = 12;

const css = `
@page { size: Letter; margin: 0; }
:root { --bg:#15171F; --panel:#1E2130; --panel2:#262A3D; --line:#33384F; --txt:#EDEBF5; --muted:#9A98AE;
  --orange:#F08A4B; --blue:#8AB4FF; --red:#FF6B6B; --amber:#F2B544; --green:#5FD38D; --purple:#B18CFF; }
* { box-sizing:border-box; margin:0; padding:0; }
body { background:var(--bg); color:var(--txt); font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif; font-size:13pt; line-height:1.55;
  -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:8.5in; height:11in; padding:0.7in 0.75in 0.9in; position:relative; overflow:hidden; page-break-after:always; display:flex; flex-direction:column; gap:18px; }
.page:last-child { page-break-after:auto; }
.kick { font-size:8.5pt; letter-spacing:.2em; color:var(--muted); font-weight:bold; text-transform:uppercase; }
h1 { font-size:40pt; line-height:1.05; letter-spacing:-.01em; }
h1 em, h2 em { font-style:normal; color:var(--orange); }
h2 { font-size:27pt; line-height:1.15; }
h3 { font-size:12pt; margin-bottom:4px; }
p.lead { color:var(--muted); font-size:14.5pt; max-width:6.5in; }
.muted { color:var(--muted); } .small { font-size:9.5pt; }
.card { background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:20px 22px; }
.card h3 { font-size:13.5pt; }
.big { font-size:23pt; font-weight:bold; line-height:1.35; }
.r { color:var(--red); } .g { color:var(--green); } .a { color:var(--amber); } .o { color:var(--orange); } .b { color:var(--blue); }
.checknum { display:inline-flex; align-items:center; justify-content:center; width:34px; height:34px; border-radius:50%; background:var(--orange);
  color:#15171F; font-weight:bold; font-size:14pt; margin-right:10px; vertical-align:middle; }
.list5 { display:flex; flex-direction:column; gap:10px; }
.list5 div { background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:10px 14px; font-size:12.5pt; }
table { width:100%; border-collapse:collapse; font-size:12pt; }
th { text-align:left; font-size:8pt; letter-spacing:.14em; color:var(--muted); padding:8px 10px; border-bottom:2px solid var(--orange); text-transform:uppercase; }
td { padding:10px; border-bottom:1px solid var(--line); }
td.num, th.num { text-align:right; }
ul { padding-left:20px; } li { margin:5px 0; }
.box { display:inline-block; width:14px; height:14px; border:2px solid var(--orange); border-radius:3px; margin-right:10px; vertical-align:-2px; }
.fill { table-layout:fixed; } .fill td { height:40px; padding:0 6px; border:1px solid var(--line); background:var(--panel2); }
.fill th { border-bottom:2px solid var(--orange); padding:8px 6px; }
.btn { display:block; text-align:center; background:var(--orange); color:#15171F; text-decoration:none; font-weight:bold; font-size:17pt;
  letter-spacing:.04em; padding:18px; border-radius:12px; }
a { color:var(--blue); }
.foot { position:absolute; left:0.75in; right:0.75in; bottom:0.4in; display:flex; justify-content:space-between; font-size:7.5pt;
  color:var(--muted); letter-spacing:.12em; border-top:1px solid var(--line); padding-top:6px; }
`;
const foot = (n) => `<div class="foot"><span>BEFORE YOU CLICK "PAY LATER" · CHECKMAYBE · ESTIMATES ONLY, NOT FINANCIAL ADVICE</span><span>${n} / ${PAGES}</span></div>`;
const check = (n, title) => `<div class="kick">Check ${n} of 5</div><h2><span class="checknum">${n}</span>${title}</h2>`;
const rows = 8;
const fillRows = Array.from({ length: rows }, (_, i) =>
  `<tr>${['item', 'pay', 'every', 'count', 'first', 'last', 'total'].map(c => `<td class="f" data-name="r${i + 1}_${c}"></td>`).join('')}</tr>`).join('');

const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>

<section class="page">
  <div class="kick">Free mini guide · CheckMaybe</div>
  <h1>Before You Click<br><em>"Pay Later"</em></h1>
  <p class="lead">Five checks in five minutes, before a small monthly payment turns into a bill you didn't see coming.</p>
  <div class="list5">
    <div><span class="checknum">1</span>What will I pay in total?</div>
    <div><span class="checknum">2</span>Roughly what yearly rate is that?</div>
    <div><span class="checknum">3</span>What happens if I'm late, or don't finish on time?</div>
    <div><span class="checknum">4</span>When does the first payment leave, and from where?</div>
    <div><span class="checknum">5</span>What else is due that month?</div>
  </div>
  <p class="small muted">Plus: the free trial you started at checkout, and a one-page list to keep every plan in one place.</p>
  ${foot(1)}
</section>

<section class="page">
  <div class="kick">Start here</div>
  <h2>How to use this guide</h2>
  <p>Open it when you're about to pick a payment plan: pay-in-4, "only $X a month", store financing, a 0% promotion. Go through the five checks. Each one takes about a minute and needs only the numbers on the checkout screen or the agreement.</p>
  <div class="card">
    <h3>What this guide is</h3>
    <ul>
      <li>A way to see the full cost before you agree to it.</li>
      <li>Simple maths you can do on your phone's calculator.</li>
      <li>Questions to ask, and words to look for in the agreement.</li>
    </ul>
  </div>
  <div class="card">
    <h3>What it isn't</h3>
    <ul>
      <li>Financial, legal or tax advice. It doesn't tell you whether to use a plan.</li>
      <li>A review of any company. Every plan is different: your agreement is the final word.</li>
    </ul>
  </div>
  <p class="small muted">All examples in this guide are made up. Rates are rounded estimates worked out from the payment schedule and don't include fees charged separately.</p>
  ${foot(2)}
</section>

<section class="page">
  ${check(1, 'What will I pay <em>in total</em>?')}
  <p class="lead">The monthly price is only part of the story. Multiply it out.</p>
  <div class="card big">payment × number of payments<br>− price<br>= <span class="o">what the plan costs you</span></div>
  <div class="card">
    <div class="kick" style="margin-bottom:8px">Example (made up)</div>
    <table>
      <tr><td>Phone price</td><td class="num">$1,200</td></tr>
      <tr><td>Plan: $67 a month × 24 payments</td><td class="num">$1,608</td></tr>
      <tr><td><b>Extra you pay</b></td><td class="num r"><b>$408</b></td></tr>
    </table>
  </div>
  <p>If the answer is <b class="g">$0</b>, the plan costs nothing extra as long as every payment is on time. If it's more than $0, that difference is the price of paying later.</p>
  ${foot(3)}
</section>

<section class="page">
  ${check(2, 'Roughly what <em>yearly rate</em> is that?')}
  <p class="lead">$408 on $1,200 doesn't sound like much until you see it as a yearly rate (APR). That's the number you can compare with a credit card or a loan.</p>
  <table>
    <tr><th>Example plan (made up)</th><th class="num">Total paid</th><th class="num">Extra</th><th class="num">About</th></tr>
    <tr><td>$279 watch, pay-in-4, first payment at checkout, no fee</td><td class="num">$279</td><td class="num g">$0</td><td class="num g"><b>0% APR</b></td></tr>
    <tr><td>$649 TV, 12 × $59 a month</td><td class="num">$708</td><td class="num">$59</td><td class="num a"><b>16.4% APR</b></td></tr>
    <tr><td>$499 console, 6 × $89.50 a month</td><td class="num">$537</td><td class="num">$38</td><td class="num r"><b>25.7% APR</b></td></tr>
    <tr><td>$1,200 phone, 24 × $67 a month</td><td class="num">$1,608</td><td class="num">$408</td><td class="num r"><b>29.8% APR</b></td></tr>
  </table>
  <div class="card">
    <h3>Why a short plan can have a high rate</h3>
    <p class="muted">The console plan only costs $38 extra, but you're borrowing for six months and paying it back a little at a time, so the yearly rate comes out higher than the TV's.</p>
  </div>
  <p class="small muted">Rates worked out with the RATE() spreadsheet function from price, payment and number of payments. Fees charged separately are not included. If the checkout page states an APR, use that one.</p>
  ${foot(4)}
</section>

<section class="page">
  ${check(3, 'What if I\'m <em>late</em>, or don\'t finish on time?')}
  <p class="lead">This is where "0%" can stop being 0%. Before you agree, find these two things in the agreement.</p>
  <div class="card">
    <h3>1. The late fee</h3>
    <p class="muted">Search the terms for "late fee" or "missed payment". Note the amount and when it's charged.</p>
  </div>
  <div class="card">
    <h3>2. "Deferred interest" or "no interest if paid in full"</h3>
    <p class="muted">Some store cards and financing offers work like this: if any of the promotional balance is still unpaid when the promotion ends, interest can be charged going back to the day you bought it, not just on what's left. The US Consumer Financial Protection Bureau (CFPB) has warned that these charges can catch people by surprise.</p>
    <p style="margin-top:8px">Words that mean <b class="r">look closer</b>: <i>deferred interest</i>, <i>no interest if paid in full</i>.<br>
    Words that usually mean <b class="g">no back-dated interest</b>: <i>0% APR</i> for a set period, where interest only starts on what's left afterwards. Always confirm in your own agreement.</p>
  </div>
  <p class="small muted">Source: CFPB, "How to understand special promotional financing offers on credit cards" and CFPB press release on retail card promotions (checked October 3, 2026). Links on page 12.</p>
  ${foot(5)}
</section>

<section class="page">
  ${check(4, 'When does the <em>first payment</em> leave, and from where?')}
  <p class="lead">Two plans with the same price can hit your account at very different times.</p>
  <div class="card">
    <h3>At checkout, or later?</h3>
    <p class="muted">Many pay-in-4 plans take the first payment the moment you buy. Others start a month later. Write down the first date.</p>
  </div>
  <div class="card">
    <h3>Which card or account?</h3>
    <p class="muted">If payments come off a debit card, make sure the money is there on each date. If they come off a credit card, the plan is now part of that card's bill too.</p>
  </div>
  <div class="card">
    <h3>Autopay on or off?</h3>
    <p class="muted">Autopay helps you avoid late fees, but only if the account has enough in it. Either way, put a reminder in your phone two days before each payment.</p>
  </div>
  ${foot(6)}
</section>

<section class="page">
  ${check(5, 'What else is <em>due that month</em>?')}
  <p class="lead">One plan is easy. Four plans landing in the same month is where it hurts. Line them up.</p>
  <table>
    <tr><th>Made-up example, January</th><th class="num">Payments that month</th><th class="num">Due</th></tr>
    <tr><td>Smart watch, pay-in-4, every 2 weeks from Nov 27</td><td class="num">1</td><td class="num">$69.75</td></tr>
    <tr><td>Flights, pay-in-4, every 2 weeks from Dec 15</td><td class="num">2</td><td class="num">$210.00</td></tr>
    <tr><td>TV, $59 a month from Dec 27</td><td class="num">1</td><td class="num">$59.00</td></tr>
    <tr><td>Game console, $89.50 a month from Dec 27</td><td class="num">1</td><td class="num">$89.50</td></tr>
    <tr><td><b>January total</b></td><td></td><td class="num r"><b>$428.25</b></td></tr>
  </table>
  <div class="card">
    <h3>Quick way to do this</h3>
    <p class="muted">Use the list on page 10. For each plan, write the first and last payment date, then count how many payments fall in each of the next three months.</p>
  </div>
  ${foot(7)}
</section>

<section class="page">
  <div class="kick">Bonus check</div>
  <h2>Did you also start a <em>free trial</em>?</h2>
  <p class="lead">Checkout pages, especially around sales, often bundle a free trial: shipping memberships, streaming, apps. They turn into charges on their own.</p>
  <div class="card big">Cancel-by date = <span class="o">the day before it bills</span></div>
  <ul>
    <li>Write the cancel-by date down now, not later.</li>
    <li>Put a phone reminder two days before it.</li>
    <li>Note what it costs after the trial, and how often (monthly or yearly).</li>
    <li>If you decide to keep it, that's fine. Just make it a choice, not a surprise.</li>
  </ul>
  ${foot(8)}
</section>

<section class="page">
  <div class="kick">Screenshot this page</div>
  <h2>The 5 checks, <em>on one page</em></h2>
  <div class="list5">
    <div><span class="box"></span><b>Total:</b> payment × number of payments − price = ______</div>
    <div><span class="box"></span><b>Rate:</b> is the extra $0? If not, roughly what APR? (see page 4)</div>
    <div><span class="box"></span><b>Late / unpaid:</b> late fee? "deferred interest" or "no interest if paid in full"?</div>
    <div><span class="box"></span><b>First payment:</b> date ______ · from which card or account?</div>
    <div><span class="box"></span><b>Same month:</b> what else is due? Added to my list on page 10?</div>
    <div><span class="box"></span><b>Free trial?</b> Cancel-by date ______</div>
  </div>
  <p class="small muted">If any box makes you pause, it's fine to close the tab and decide tomorrow. The offer will usually still be there.</p>
  ${foot(9)}
</section>

<section class="page">
  <div class="kick">Fill this in · works in most PDF apps</div>
  <h2>My <em>pay-later</em> plans</h2>
  <table class="fill">
    <colgroup><col style="width:24%"><col style="width:12%"><col style="width:13%"><col style="width:9%"><col style="width:13%"><col style="width:13%"><col style="width:16%"></colgroup>
    <tr><th>Item</th><th>Payment</th><th>How often</th><th># left</th><th>First</th><th>Last</th><th>Total left</th></tr>
    ${fillRows}
  </table>
  <div class="card">
    <h3>Due in each of the next 3 months</h3>
    <table class="fill"><tr><th>Month</th><th>Total due</th><th>Month</th><th>Total due</th><th>Month</th><th>Total due</th></tr>
    <tr>${['m1', 'm1_total', 'm2', 'm2_total', 'm3', 'm3_total'].map(n => `<td class="f" data-name="${n}"></td>`).join('')}</tr></table>
  </div>
  <p class="small muted">Tap a box to type. On a phone, open the PDF in a PDF app (Adobe Acrobat Reader, Apple Books / Files or Google Drive) and save after filling in.</p>
  ${foot(10)}
</section>

<section class="page">
  <div class="kick">Want it worked out for you?</div>
  <h2>Hidden Cost <em>Tracker</em></h2>
  <p class="lead">The same checks, done automatically in a Google Sheet (also works in Excel).</p>
  <ul>
    <li>Enter price, payment and number of payments: get the real APR and a HIGH / CHECK / OK flag.</li>
    <li>Debt-free date, payments left and interest still to pay.</li>
    <li>Subscriptions and free trials with next charge and cancel-by countdowns.</li>
    <li>One dashboard: how much of your income is already spoken for each month.</li>
  </ul>
  <a class="btn" href="${TRACKER}">SEE HIDDEN COST TRACKER →</a>
  <p class="small muted" style="text-align:center">${TRACKER.replace('https://', '')}</p>
  <p class="small muted">Your copy lives in your own Google Drive. Estimates only, not financial advice.</p>
  ${foot(11)}
</section>

<section class="page">
  <div class="kick">Sources and notes</div>
  <h2>Where this comes from</h2>
  <div class="card">
    <h3>Deferred interest (page 5)</h3>
    <p class="small">Consumer Financial Protection Bureau, "How to understand special promotional financing offers on credit cards":<br><a href="${CFPB_BLOG}">${CFPB_BLOG.replace('https://', '')}</a></p>
    <p class="small" style="margin-top:6px">CFPB press release, "Consumer Financial Protection Bureau Encourages Retail Credit Card Companies to Consider More Transparent Promotions":<br><a href="${CFPB_NEWS}">${CFPB_NEWS.replace('https://', '')}</a></p>
    <p class="small muted" style="margin-top:6px">Checked October 3, 2026. Rules and offers change: read your own agreement.</p>
  </div>
  <div class="card">
    <h3>The example numbers</h3>
    <p class="small muted">All plans in this guide are made up. Yearly rates were worked out with the spreadsheet RATE() function from price, payment and number of payments, and rounded to one decimal. They exclude any fees charged separately.</p>
  </div>
  <div class="card">
    <h3>Not advice</h3>
    <p class="small muted">This guide is for general information. It is not financial, legal or tax advice and doesn't recommend for or against any payment plan or company. Free to keep and share as a whole; please don't sell it.</p>
  </div>
  <p class="small muted">CheckMaybe · Check before you click. · v1.0, October 2026</p>
  ${foot(12)}
</section>
</body></html>`;

fs.writeFileSync('guide.html', html);
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/guide.html', { waitUntil: 'load' });
const report = await p.evaluate(() => {
  const pages = [...document.querySelectorAll('.page')];
  const over = pages.map((pg, i) => {
    const foot = pg.querySelector('.foot').getBoundingClientRect().top;
    const last = [...pg.children].filter(e => !e.classList.contains('foot')).pop().getBoundingClientRect().bottom;
    return last > foot - 4 ? `page ${i + 1} overflows by ${Math.round(last - foot + 4)}px` : null;
  }).filter(Boolean);
  const fields = [...document.querySelectorAll('td.f')].map(td => {
    const r = td.getBoundingClientRect(); const pg = td.closest('.page'); const pr = pg.getBoundingClientRect();
    return { name: td.dataset.name, page: pages.indexOf(pg), x: r.left - pr.left, y: r.top - pr.top, w: r.width, h: r.height };
  });
  return { over, fields };
});
fs.writeFileSync('fields.json', JSON.stringify(report.fields));
await p.pdf({ path: 'base.pdf', width: '8.5in', height: '11in', printBackground: true });
if (process.env.SHOTS) {
  await p.setViewportSize({ width: 816, height: 1056 });
  for (let i = 0; i < PAGES; i++) {
    await p.screenshot({ path: `${process.env.SHOTS}/p${String(i + 1).padStart(2, '0')}.png`, clip: { x: 0, y: i * 1056, width: 816, height: 1056 }, fullPage: true });
  }
}
await b.close();
fs.unlinkSync('guide.html');
console.log('base.pdf', report.fields.length, 'fields', report.over.length ? report.over : 'layout OK');
