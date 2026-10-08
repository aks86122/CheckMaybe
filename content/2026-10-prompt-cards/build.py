"""Instagram carousels (1080x1350), same dark look as the money series.

prompts-*  : 5 prompts to ask AI before you sell a digital product (creator line, save-driven)
paylater-* : 4 prompts to ask AI before you click "Pay Later" (money line, points to the free guide)
viral-*    : your most-viewed post isn't always the one that sells (audience post, no product)
Examples are made up. Usage: python3 build.py
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
TMP = "/tmp/cm-prompt-cards"; os.makedirs(TMP, exist_ok=True)
CSS = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:864px;height:1080px;overflow:hidden}
body{background:#15171F;background-image:radial-gradient(ellipse at 85% 0%,rgba(240,138,75,.18),transparent 55%);
color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:44px}
.brand{font-size:16px;letter-spacing:.18em;font-weight:700;color:#9A98AE;text-transform:uppercase}.brand b{color:#F08A4B}
.pn{position:absolute;right:44px;top:44px;font-size:18px;font-weight:700;color:#9A98AE}
.num{font-size:30px;font-weight:800;color:#F08A4B;margin-top:56px}
h1{font-weight:800;line-height:1.08;letter-spacing:-.01em}h1 em{font-style:normal;color:#F08A4B}
.sub{color:#9A98AE;line-height:1.4}
.chips{margin-top:26px}.chip{display:inline-block;background:#F08A4B;color:#15171F;font-weight:800;border-radius:999px;font-size:18px;padding:6px 14px;margin:0 8px 8px 0}
.card{background:#1E2130;border:1px solid #33384F;border-radius:16px;padding:34px 36px;margin-top:22px}
.lab{font-size:17px;font-weight:800;color:#F08A4B;letter-spacing:.08em;margin-bottom:14px}
.q{font-size:29px;line-height:1.5;font-family:"Liberation Mono","DejaVu Sans Mono",monospace}
.big{font-size:34px;line-height:1.5}
.r{color:#FF6B6B}.g{color:#5FD38D}.o{color:#F08A4B}
.foot{position:absolute;left:44px;right:44px;bottom:26px;font-size:16px;color:#9A98AE;border-top:1px solid #33384F;padding-top:14px}
"""
def page(label, n, total, body, foot):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="brand"><b>CheckMaybe</b> · {label}</div><div class="pn">{n} / {total}</div>{body}'
            f'<div class="foot">{foot}</div></body></html>')
def prompt(num, title, chips, text):
    return (f'<div class="num">{num}</div><h1 style="font-size:54px;margin-top:6px">{title}</h1>'
            f'<div class="chips">' + "".join(f'<span class="chip">[{c}]</span>' for c in chips) + '</div>'
            f'<div class="card"><div class="lab">COPY THIS PROMPT</div><div class="q">{text}</div></div>')
SAVE = "Save this. Copy it when you need it."
SETS = {
 "prompts": ("Before you sell", SAVE, [
  '<h1 style="font-size:72px;margin-top:110px">Before you sell<br>your first <em>digital<br>product</em>, ask AI<br>these 5 questions</h1>'
  '<div class="sub" style="font-size:34px;margin-top:40px">Not how to make money.<br>How not to lose it.</div>',
  prompt("01", "Can I actually<br>sell this?", ["what I used"],
    "“I made a product using [what I used: template / font / AI image / stock photo]. List every license question I need "
    "to answer before selling it commercially, and where in the license to look. Don’t assume it’s allowed.”"),
  prompt("02", "What will the<br>fees eat?", ["platform", "price"],
    "“I plan to sell on [platform] at [price]. List every fee that could apply: listing, transaction, payment, currency, "
    "ads, payouts. Show what I keep per sale, and which numbers to confirm on the platform’s fee page.”"),
  prompt("03", "What’s my real<br>hourly pay?", ["hours to make", "hours per week", "price"],
    "“It takes me [hours to make] to build this, plus [hours per week] for marketing and support. At [price], show "
    "conservative, normal and optimistic cases for the first 3 months, with the math.”"),
  prompt("04", "Is anyone going<br>to buy it?", ["product", "buyer"],
    "“Design a 7-day test, with no ad spend, to check whether [buyer] would pay for [product]. Tell me what counts "
    "as a pass and what counts as a fail.”"),
  prompt("05", "When do I stop?", ["product", "max loss"],
    "“I’m willing to lose at most [max loss] and 3 months on [product]. Write 3 clear stop rules. If any one is hit, "
    "I stop or change direction.”"),
  '<h1 style="font-size:64px;margin-top:150px">AI can misread<br>a license or<br>a fee page.</h1>'
  '<div class="big" style="margin-top:40px"><b class="o">Always check the original text</b><br>before you list anything.</div>'
  '<div class="sub" style="font-size:30px;margin-top:60px">Save this for your next product idea.</div>',
 ]),
 "paylater": ("Before you click Pay Later", "Save this. Estimates only, not financial advice.", [
  '<h1 style="font-size:72px;margin-top:110px">Before you click<br><em>“Pay Later”</em>,<br>ask AI these<br>4 questions</h1>'
  '<div class="sub" style="font-size:34px;margin-top:40px">“Only $67 a month” is<br>not the whole story.</div>',
  prompt("01", "What’s the<br>real APR?", ["price", "payment", "number of payments"],
    "“I can buy something that costs [price] as [number of payments] payments of [payment]. Work out the total I pay, "
    "the extra over the price, and the APR. Show the math.”"),
  prompt("02", "What happens if<br>I pay late?", ["plan terms"],
    "“Here are the terms of a pay-later plan: [paste terms]. List every late fee, interest charge and penalty, "
    "and what happens to my credit if I miss a payment.”"),
  prompt("03", "What’s due<br>every month?", ["all my plans"],
    "“These are all my pay-later plans and installments: [list]. Add a new one of [payment]. Show what I owe each "
    "month for the next 6 months and the heaviest month.”"),
  prompt("04", "Need it or<br>want it now?", ["item", "date I need it"],
    "“I want [item]. I need it by [date I need it]. Ask me 5 questions to check whether I should wait and save "
    "instead of splitting the payment. Don’t decide for me.”"),
  '<h1 style="font-size:62px;margin-top:150px">AI does the math.<br><em>You</em> make the call.</h1>'
  '<div class="big" style="margin-top:40px">Check the real numbers in the plan’s<br>own terms before you click.</div>'
  '<div class="sub" style="font-size:30px;margin-top:60px">Free “Before You Click Pay Later” guide:<br>link in bio →</div>',
 ]),
 "viral": ("For creators", "Examples are made up to show the idea.", [
  '<h1 style="font-size:76px;margin-top:130px">Your viral post<br>might be bringing<br>in the <em>wrong<br>people</em></h1>',
  '<h1 style="font-size:52px;margin-top:120px">Views mean people<br>like the <em>topic</em>.</h1>'
  '<div class="big" style="margin-top:40px">Not that they like <b>you</b>.<br>Not that they’ll ever <b>buy</b>.</div>',
  '<div class="num">EXAMPLE A</div><h1 style="font-size:56px;margin-top:6px">“10 free fonts”</h1>'
  '<div class="card big"><b class="o">100k views</b><br>Brings in: people looking for free stuff</div>'
  '<div class="num" style="margin-top:50px">EXAMPLE B</div><h1 style="font-size:52px;margin-top:6px">“Can I sell a design<br>made with this template?”</h1>'
  '<div class="card big"><b class="o">8k views</b><br>Brings in: people about to sell something</div>',
  '<h1 style="font-size:56px;margin-top:120px">Which one do you<br>make more of?</h1>'
  '<div class="card big" style="margin-top:40px">Check what came <b class="o">after</b> the view:<br>'
  '<span class="g">✓</span> Saves<br><span class="g">✓</span> DMs<br><span class="g">✓</span> Link clicks<br>'
  '<span class="g">✓</span> Questions about using it</div>',
  '<h1 style="font-size:60px;margin-top:170px">Grow the audience<br>you actually want<br>to <em>serve</em>.</h1>'
  '<div class="sub" style="font-size:30px;margin-top:50px">Save this for your next content review.</div>',
 ]),
}
jobs = []
for prefix, (label, foot, bodies) in SETS.items():
    out = os.path.join(HERE, prefix); os.makedirs(out, exist_ok=True)
    for i, body in enumerate(bodies, 1):
        src = os.path.join(TMP, f"{prefix}-{i}.html"); open(src, "w").write(page(label, i, len(bodies), body, foot))
        jobs.append([src, os.path.join(out, f"{prefix}-{i:02d}.png")])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)};
const b = await chromium.launch();
for (const [src, out] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 864, height: 1080 }}, deviceScaleFactor: 1.25 }});
  await p.goto('file://' + src); await p.waitForLoadState('networkidle');
  const over = await p.evaluate(() => [...document.querySelectorAll('h1,.card,.sub,.big,.chips')]
    .filter(e => {{ const r = e.getBoundingClientRect(); return r.right > 844 || r.bottom > 1010; }}).map(e => e.className || e.tagName));
  await p.screenshot({{ path: out }}); console.log(out.split('/').pop(), over.length ? 'OVERFLOW ' + over.join(',') : 'OK');
  await p.close();
}}
await b.close();"""
open(os.path.join(TMP, "shoot.mjs"), "w").write(js)
subprocess.run(["node", os.path.join(TMP, "shoot.mjs")], check=True)
