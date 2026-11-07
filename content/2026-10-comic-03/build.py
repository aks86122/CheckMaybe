"""CheckMaybe receipt comic #03: four small holiday plans, one big January. 6 slides, 1080x1350.
Mascot: receipt (Canva AI, 2026-10-17, reference MAHYRYx0qyo), poses in art/.
Numbers: holiday made-up example (January $428.25 = 10.2% of the example income).
Edit text below, then run: python3 content/2026-10-comic-03/build.py"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ART = f"{HERE}/art"
TMP = "/tmp/cm-comic-03"; os.makedirs(TMP, exist_ok=True)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#15171F;color:#EDEBF5;font-family:Inter,"Liberation Sans",Arial,sans-serif;position:relative}
.brand{position:absolute;left:64px;top:52px;font-size:22px;letter-spacing:.18em;font-weight:600;color:#C9C7D8;text-transform:uppercase}.brand b{color:#F08A4B}
.card{position:absolute;left:64px;right:64px;border-radius:28px;padding:40px 46px}
.claim{background:#1E2130;border:2px solid #33384F}.receipt{background:#22202A;border:3px solid #F7C948}
.lab{font-size:24px;font-weight:800;letter-spacing:.2em}.claim .lab{color:#F08A4B}.receipt .lab{color:#F7C948}
.q{font-size:52px;font-weight:800;line-height:1.22;margin-top:16px}.t{font-size:44px;font-weight:600;line-height:1.38;margin-top:16px}
.t i{font-style:normal;color:#F7C948}.mute{color:#C9C7D8}
.pose{position:absolute;right:40px;width:330px;-webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 72%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at center,#000 72%,transparent 100%)}
h1{font-weight:800;line-height:1.12}h1 em{font-style:normal;color:#F08A4B}
ul{list-style:none}li{position:relative;padding-left:62px;font-size:44px;font-weight:600;line-height:1.35;margin-bottom:30px}
li:before{content:"";position:absolute;left:0;top:8px;width:38px;height:38px;border:4px solid #F08A4B;border-radius:9px}
.foot{position:absolute;left:64px;right:64px;bottom:38px;font-size:19px;color:#9A98AC}"""

FOOT = '<div class="foot">Made-up example. Estimates only, not financial advice.</div>'

def pose(name, top, width=330):
    return f'<img class="pose" src="file://{ART}/{name}.jpg" style="top:{top}px;width:{width}px">'

def pair(claim, receipt, art, claim_top=140, receipt_top=380, pose_top=740):
    return (f'<div class="card claim" style="top:{claim_top}px"><div class="lab">THE CLAIM</div><div class="q">{claim}</div></div>'
            f'<div class="card receipt" style="top:{receipt_top}px;right:64px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            + pose(art, pose_top, 470) + FOOT)

SLIDES = [
    '<h1 style="position:absolute;left:64px;right:64px;top:190px;font-size:100px">Four small<br>holiday plans.<br><em>One big<br>January.</em></h1>'
      '<div class="t mute" style="position:absolute;left:64px;top:900px;width:560px">A made-up holiday<br>budget, added up<br>in one place.</div>'
      + pose("gifts", 800, 400) + FOOT,
    pair("“Just pay in 4. It’s only a little each time.”",
         "Made-up example: four plans like that land in January together: <i>$428.25</i> that month, <i>10.2%</i> of the example income.",
         "snow", receipt_top=430, pose_top=800),
    pair("“Start your free trial today.”",
         "It’s free until the date you forget. Write down the <i>cancel-by date</i> the day you start.",
         "trial"),
    pair("“It’s a gift. It doesn’t count.”",
         "Every plan counts in the month it’s due. Add them up <i>before</i> you check out.",
         "calc"),
    '<h1 style="position:absolute;left:64px;right:64px;top:150px;font-size:76px">Before the<br><em>holiday checkout</em>:</h1>'
      '<ul style="position:absolute;left:64px;right:64px;top:430px"><li>Which month is<br>each payment due?</li><li>What’s January’s total?</li><li>Which trials end,<br>and when?</li></ul>'
      + pose("check", 880, 380) + FOOT,
    '<h1 style="position:absolute;left:64px;right:64px;top:200px;font-size:88px">Small in November.<br><em>Real in January.</em></h1>'
      '<div class="t mute" style="position:absolute;left:64px;top:560px;width:600px">Holiday Hidden Cost Tracker adds up gifts, plans and free trials month by month.</div>'
      '<div style="position:absolute;left:64px;top:1010px;font-size:36px;font-weight:800;color:#F08A4B;width:560px">Tracker → link in bio</div>'
      + pose("happy", 880, 380) + FOOT,
]

jobs = []
for i, body in enumerate(SLIDES, 1):
    src = f"{TMP}/s{i}.html"
    with open(src, "w") as f:
        f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
                f'<div class="brand"><b>CheckMaybe</b> · Check before you trust</div>{body}</body></html>')
    jobs.append([src, f"{HERE}/comic-03-{i:02d}.png"])

js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 1080, height: 1350 }} }});
  await p.goto('file://' + s); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({{ path: o }}); console.log(o.split('/').pop()); await p.close(); }}
await b.close();"""
with open(f"{TMP}/shoot.mjs", "w") as f:
    f.write(js)
subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
