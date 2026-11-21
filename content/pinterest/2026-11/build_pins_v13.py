"""Pinterest pins v13 (1000x1500, 2:3): pins that link to Substack posts s3 and s4.

bf4 -> s3 "Is that Black Friday deal real? Three numbers to check first"
di1 -> s4 "Snowball or avalanche? Check your 0% end dates first"
Numbers and wording come from the published posts (content/2026-11-substack-schedule.md).
Copy and links: pins-v13.md.
Usage: python3 content/pinterest/2026-11/build_pins_v13.py
"""
import json, os, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ART2 = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
TMP = tempfile.mkdtemp(prefix="cm-pins-v13-")
os.makedirs(f"{HERE}/pins", exist_ok=True)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}html,body{width:1000px;height:1500px;overflow:hidden}
body{position:relative;background:#15171F;color:#EDEBF5;font-family:Inter,"Liberation Sans",sans-serif}
.k{position:absolute;left:64px;top:64px;font-size:24px;letter-spacing:.18em;font-weight:600;color:#C9C7D8;text-transform:uppercase}.k b{color:#F08A4B}
h1{position:absolute;left:64px;right:64px;top:130px;font-weight:800;line-height:1.08}h1 em{font-style:normal;color:#F08A4B}
.receipt{position:absolute;left:64px;right:64px;background:#22202A;border:3px solid #F7C948;border-radius:26px;padding:30px 40px}
.lab{font-size:22px;font-weight:800;letter-spacing:.2em;color:#F7C948}.t{font-size:35px;font-weight:600;line-height:1.36;margin-top:10px}.t i{font-style:normal;color:#F7C948}
.pose{position:absolute;-webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 72%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at center,#000 72%,transparent 100%)}
.tag{position:absolute;left:64px;bottom:110px;display:inline-block;font-weight:800;border-radius:999px;padding:12px 26px;font-size:26px;letter-spacing:.04em;color:#15171F;background:#F08A4B}
.list{position:absolute;left:64px;width:640px;background:#1C1E28;border:1px solid #33384F;border-radius:14px;padding:10px 26px;box-shadow:0 24px 70px rgba(0,0,0,.6)}
.row{display:flex;align-items:flex-start;gap:20px;padding:20px 0;border-top:1px solid #2C2F3E}.row:first-child{border-top:0}
.n{flex:none;width:50px;height:50px;border-radius:50%;background:#F7C948;color:#15171F;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center}
.q{font-size:29px;font-weight:800;line-height:1.2}.ex{font-size:22px;color:#B9B7C9;margin-top:6px;line-height:1.35}
.v{display:inline-block;font-weight:800;border-radius:8px;padding:3px 10px;font-size:21px;margin-top:8px;white-space:nowrap}.g{background:#1C3A2A;color:#74D39A}.b{background:#43202A;color:#E2687B}.y{background:#3D3218;color:#F7C948}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-size:19px;letter-spacing:.12em;text-transform:uppercase;color:#9A98AC}"""


def checklist(items, top):
    rows = "".join(
        f'<div class="row"><div class="n">{i}</div><div><div class="q">{q}</div><div class="ex">{ex}</div>'
        f'<span class="v {c}">{verdict}</span></div></div>'
        for i, (q, ex, verdict, c) in enumerate(items, 1))
    return f'<div class="list" style="top:{top}px">{rows}</div>'


def pin(kicker, title, receipt, receipt_top, body, pose, pose_style, tag, foot):
    return (f'<div class="k"><b>CheckMaybe</b> · {kicker}</div><h1>{title}</h1>'
            f'<div class="receipt" style="top:{receipt_top}px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            f'{body}<img class="pose" src="file://{pose}" style="{pose_style}">'
            f'<span class="tag">{tag}</span><div class="foot"><span>{foot}</span><span>checkmaybe</span></div>')


PINS = {
    "bf4-three-numbers": pin(
        "Black Friday · deal check",
        '<span style="font-size:88px">Is that deal real?</span><br><em style="font-size:76px">Check 3 numbers first.</em>',
        "The crossed-out price on the banner <i>isn't the usual price.</i>", 400,
        checklist([
            ("The usual price", "Headphones $199, usually $249", "20.1% below: real deal", "g"),
            ("The checkout price", "$159 vacuum + 8% tax + $15 shipping", "$186.72 at checkout", "y"),
            ("The payment-plan total", "$499 TV: $538.92 in full, 12 × $49 = $588", "$49.08 more on the plan", "b"),
        ], 640),
        f"{ART2}/check.jpg", "right:0px;top:980px;width:330px",
        "FREE READ ON SUBSTACK", "Made-up example · not financial advice"),
    "di1-zero-percent-end-dates": pin(
        "Debt payoff · before you pick",
        '<span style="font-size:84px">Snowball or avalanche?</span><br><em style="font-size:66px">Check your 0% end dates first.</em>',
        "0% with deferred interest: if any promo balance is left when it ends, <i>interest can go back to the day you bought it.</i>", 470,
        checklist([
            ("When does any 0% deal end?", "Write the month next to the debt", "Can flip the cheapest order", "y"),
            ("Deferred interest?", "Check the card or financing terms", "Clear it before the end date", "b"),
            ("Fee for paying it off early?", "Some loans charge one", "Put extra money elsewhere first", "g"),
        ], 770),
        f"{ART3}/calc.jpg", "right:0px;top:1030px;width:320px",
        "FREE READ ON SUBSTACK", "Checklist · not financial advice"),
}

jobs = []
for name, body in PINS.items():
    src = f"{TMP}/{name}.html"
    with open(src, "w") as f:
        f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
    jobs.append([src, f"{HERE}/pins/checkmaybe-pin-{name}.png"])

js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 1000, height: 1500 }} }});
  await p.goto('file://' + s); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({{ path: o }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
with open(f"{TMP}/shoot.mjs", "w") as f:
    f.write(js)
subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
