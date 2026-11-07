"""CheckMaybe comic #01: the "free" Threads growth ebook. 6 slides, 1080x1350.
Mascot: half-checked checkbox (Canva AI, 2026-10-17), poses in art/. Quotes are word for word
from the ebook PDF (downloaded 2026-10-16); page numbers in post.md. The creator is not named.
Edit text below, then run: python3 content/2026-10-comic-01/build.py"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ART = f"{HERE}/art"
TMP = "/tmp/cm-comic-01"; os.makedirs(TMP, exist_ok=True)

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

FOOT = '<div class="foot">Quotes are word for word from the ebook (downloaded Oct 16, 2026). Not financial advice.</div>'

def pose(name, top, width=330):
    return f'<img class="pose" src="file://{ART}/{name}.jpg" style="top:{top}px;width:{width}px">'

def pair(claim, receipt, art, claim_top=140, receipt_top=560, pose_top=880):
    return (f'<div class="card claim" style="top:{claim_top}px"><div class="lab">THE CLAIM</div><div class="q">{claim}</div></div>'
            f'<div class="card receipt" style="top:{receipt_top}px;right:64px"><div class="lab">THE RECEIPT</div><div class="t">{receipt}</div></div>'
            + pose(art, pose_top, 380) + FOOT)

SLIDES = [
    '<h1 style="position:absolute;left:64px;right:64px;top:190px;font-size:96px">A free Threads<br>growth ebook.<br><em>What is it<br>really for?</em></h1>'
      '<div class="t mute" style="position:absolute;left:64px;top:840px;width:560px">We read all 25 pages.<br>Every quote here is from<br>the ebook itself.</div>'
      + pose("think", 760, 400) + FOOT,
    pair("“But you&#39;re getting it all for FREE.”",
         "The same ebook points you to a <i>paid program</i> three times: on page 4, page 23 and the last page.",
         "magnify"),
    pair("“I’ll show you the 3 types of hooks that always hit 1M+ views.”",
         "Same page, a few lines later: <i>“Btw, I actually don’t have hooks that consistently hit 1M+ views, but you get the point:)”</i>",
         "shock", receipt_top=520),
    pair("“Made $4100+ in sales”",
         "No time period. No costs. No word on what was sold.<br>The last page says the paid program has <i>“the exact methods behind”</i> it.",
         "think", receipt_top=440),
    '<h1 style="position:absolute;left:64px;right:64px;top:150px;font-size:76px">Before you trust<br>a <em>“free”</em> guide:</h1>'
      '<ul style="position:absolute;left:64px;right:64px;top:430px"><li>Where does it send you<br>at the end?</li><li>Which numbers have<br>a date on them?</li><li>Does it contradict itself?</li></ul>'
      + pose("checklist", 880, 380) + FOOT,
    '<h1 style="position:absolute;left:64px;right:64px;top:200px;font-size:92px">Free isn’t the price.<br><em>Your attention is.</em></h1>'
      '<div class="t mute" style="position:absolute;left:64px;top:560px;width:600px">Not calling anyone a scammer. The tips inside are basic and mostly fine.<br>Just know what the free part is for.</div>'
      '<div style="position:absolute;left:64px;top:1010px;font-size:36px;font-weight:800;color:#F08A4B;width:560px">Save this for the next<br>free guide you see.</div>'
      + pose("happy", 880, 380) + '<div class="foot">Not financial advice.</div>',
]

jobs = []
for i, body in enumerate(SLIDES, 1):
    src = f"{TMP}/s{i}.html"
    with open(src, "w") as f:
        f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
                f'<div class="brand"><b>CheckMaybe</b> · Check before you trust</div>{body}</body></html>')
    jobs.append([src, f"{HERE}/comic-01-{i:02d}.png"])

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
