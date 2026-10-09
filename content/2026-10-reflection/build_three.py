"""Three photo-background carousels from the founder's Unsplash picks (Unsplash License: free commercial use, no attribution needed).
Photos stay in the scratchpad (unsplash/full). Credits are written next to each output."""
import json, os, subprocess
U = os.path.dirname(os.path.abspath(__file__)) + "/full"
P = lambda n: f"file://{U}/{n}-unsplash.jpg"
CAVE, SUNRISE, LANTERN, MARKET, GATE = (P("romeo-a-CkoEF2PHuy0"), P("chunchia-ZFddx3rGaow"), P("bas-glaap-wKCfza2HZL4"),
                                        P("k-x-i-t-h-v-i-s-u-a-l-s-nYq3nW9Z9ok"), P("timo-volz-Ha6n8MNgEbQ"))
TMP = "/tmp/three-carousels"; os.makedirs(TMP, exist_ok=True)
def bg(url, dim=.55, blur=0, pos="center", grad="to bottom", rgb="14,12,20"):
    if not url: return ""
    return (f'<div style="position:absolute;inset:-20px;background:url(\'{url}\') {pos}/cover;filter:blur({blur}px) saturate(.95);z-index:-2"></div>'
            f'<div style="position:absolute;inset:0;z-index:-1;background:linear-gradient({grad},rgba({rgb},{dim*.7}),rgba({rgb},{min(dim+.3,.95)}))"></div>')

# ---------- 重生引路人 (same look as prequel carousels: 720x960 @1.5) ----------
RG_CSS = """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
*{box-sizing:border-box;margin:0;padding:0}html,body{width:720px;height:960px;overflow:hidden}
body{background:#16141c;color:#f2f0eb;font-family:"Noto Sans TC",sans-serif;position:relative;padding:64px 56px}
.tag{position:absolute;left:56px;top:48px;font-size:20px;font-weight:700;letter-spacing:.08em;color:#c4b5fd;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.big{font-size:62px;font-weight:900;line-height:1.35;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.mid{font-size:42px;font-weight:700;line-height:1.5;text-shadow:0 2px 12px rgba(0,0,0,.55)}
.sub{font-size:29px;color:#d6d3cc;line-height:1.7;text-shadow:0 1px 8px rgba(0,0,0,.7)}
.hl{color:#c4b5fd}.warn{color:#f5a97f}
.row{display:flex;align-items:center;gap:18px;font-size:31px;line-height:1.4;background:rgba(22,20,28,.78);border:1px solid rgba(167,139,250,.35);border-radius:14px;padding:18px 22px}
.n{flex:0 0 auto;font-size:22px;font-weight:900;color:#16141c;background:#a78bfa;border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center}
.arrow{color:#c4b5fd;font-size:28px;text-align:center;line-height:1}.stack{display:flex;flex-direction:column;gap:10px}
.foot{position:absolute;left:56px;right:56px;bottom:52px;font-size:23px;color:#d6d3cc;line-height:1.6;text-shadow:0 1px 8px rgba(0,0,0,.8)}
.line{width:64px;height:4px;background:#a78bfa;border-radius:2px;margin:32px 0}.bottom{position:absolute;left:56px;right:56px;bottom:96px}"""
T = "借錢之前，先算這個"
row = lambda n, t, c="": f'<div class="row"><span class="n" {c}>{n}</span>{t}</div>'
RG = [
 bg(CAVE, .4, pos="center") + f'<div class="tag">{T}</div><div class="bottom"><div class="big">能借到10萬，<br>不等於你<br><span class="warn">拿到10萬</span>。</div></div>',
 bg(CAVE, .72, 3) + f'<div class="tag">{T}</div><div class="mid" style="margin-top:150px">最缺錢的時候，<br>人只聽得到一句話：</div><div class="big hl" style="margin-top:24px">「可以借你多少」</div>'
   '<div class="foot">實際拿到多少、總共要還多少，<br>很少有人先問。</div>',
 f'<div class="tag">{T}</div><div class="mid" style="margin-top:110px;margin-bottom:26px">試算給你看</div><div class="stack">'
   + row(1, "借10萬，綁18期") + '<div class="arrow">↓</div>' + row(2, "代辦先抽1～2成") + '<div class="arrow">↓</div>'
   + row(3, "再先扣第一期利息") + '<div class="arrow">↓</div>' + row(4, '<span class="warn">實際拿到：約7.2～8.2萬</span>', 'style="background:#f5a97f"') + '</div>'
   '<div class="foot">試算示意，不是任何一家的實際報價。</div>',
 f'<div class="tag">{T}</div><div class="mid" style="margin-top:170px">但每期1萬多，<br>18期繳完，</div><div class="big warn" style="font-size:84px;margin-top:10px">總共18萬。</div>'
   '<div class="line"></div><div class="sub">拿7、8萬，還18萬。<br>為了撐過一兩個月，背一年半的高利。</div>',
 bg(CAVE, .78, 4) + f'<div class="tag">{T}</div><div class="mid" style="margin-top:120px;margin-bottom:30px">下次有人說「可以借你」，<br>先問三個數字：</div><div class="stack">'
   + row("✓", "實際拿到多少") + row("✓", "每期多少、繳幾期") + row("✓", "總共要還多少") + '</div>'
   '<div class="foot">代辦要你先付錢、交存摺或證件，<br>都不要給。</div>',
 bg(SUNRISE, .42, pos="60% center") + f'<div class="tag">{T}</div><div class="bottom"><div class="big" style="font-size:54px">不知道該先處理<br>哪一筆？</div><div class="line"></div>'
   '<div class="sub">先做免費重生檢測，<br>把現在的狀況整理出來。</div><div class="mid hl" style="margin-top:18px">→ 首頁連結</div></div>',
]

# ---------- 副業實驗室 (1080x1440, brand navy/gold/orange) ----------
SH_CSS = """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1440px;overflow:hidden}
body{background:#14213D;color:#fff;font-family:"Noto Sans TC",sans-serif;padding:96px 84px;position:relative}
.tag{display:inline-block;background:#F08A3C;color:#14213D;font-weight:900;font-size:30px;padding:8px 22px;border-radius:999px}
h1{font-weight:900;font-size:100px;line-height:1.2;margin-top:36px;text-shadow:0 3px 18px rgba(0,0,0,.5)}.g{color:#F7BF20}
p{font-size:46px;line-height:1.6;margin-top:34px;text-shadow:0 2px 12px rgba(0,0,0,.6)}.mute{color:#C9D0DE}
ol{list-style:none;counter-reset:n;margin-top:44px}ol li{counter-increment:n;position:relative;padding-left:100px;font-size:50px;line-height:1.45;margin-bottom:36px;text-shadow:0 2px 10px rgba(0,0,0,.5)}
ol li:before{content:counter(n);position:absolute;left:0;top:4px;width:70px;height:70px;border-radius:50%;background:#F7BF20;color:#14213D;font-weight:900;display:flex;align-items:center;justify-content:center;font-size:40px}
.bottom{position:absolute;left:84px;right:84px;bottom:150px}
.foot{position:absolute;left:84px;bottom:64px;font-size:30px;color:#C9D0DE;font-weight:700;letter-spacing:.1em}"""
NAVY = "12,22,45"
SH = [
 bg(LANTERN, .25, pos="center 40%", rgb=NAVY) + '<div class="bottom"><span class="tag">副業觀察</span><h1>「每天5分鐘<br><span class="g">月入六位數</span>」</h1><p>這種影片，賣的其實是願望。</p></div>',
 bg(LANTERN, .8, 6, rgb=NAVY) + '<span class="tag">願望很好賣</span><ol style="margin-top:80px"><li>不用經驗</li><li>不用時間</li><li>不用成本</li></ol><p class="mute">但影片從來不給你看<br>收款紀錄。</p>',
 bg(MARKET, .45, rgb=NAVY) + '<div class="bottom"><span class="tag">真的在做生意</span><h1>是這個樣子</h1><p>備料、顧攤、算成本，<br>收入要一筆一筆算出來。</p></div>',
 '<span class="tag">開始之前，先問3題</span><ol style="margin-top:70px"><li>照做的人，<br>有人公開結果嗎？</li><li>一週要花多少<br>真實時間？</li><li>要你先付錢的，<br>是誰？</li></ol>',
 bg(MARKET, .6, 2, rgb=NAVY) + '<div class="bottom"><h1>先實驗，<br><span class="g">再投入。</span></h1><p>我的副業實驗，數字是0也照實寫。<br>追蹤看實際結果。</p></div>',
]

# ---------- CheckMaybe (864x1080 @1.25, money-series look) ----------
CM_CSS = """*{box-sizing:border-box;margin:0;padding:0}html,body{width:864px;height:1080px;overflow:hidden}
body{background:#15171F;color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:44px}
.brand{font-size:16px;letter-spacing:.18em;font-weight:700;color:#C9C7D8;text-transform:uppercase}.brand b{color:#F08A4B}
.k{font-size:22px;letter-spacing:.15em;font-weight:700;color:#D8D6E6;text-shadow:0 1px 8px rgba(0,0,0,.7)}
h1{font-weight:800;line-height:1.07;text-shadow:0 2px 16px rgba(0,0,0,.6)}h1 em{font-style:normal;color:#F08A4B}
.card{background:rgba(30,33,48,.92);border:1px solid #33384F;border-radius:16px;padding:36px 40px;font-size:38px;line-height:1.7}
ul{list-style:none}li{padding-left:1.3em;position:relative;margin-bottom:.5em}li:before{content:"✓";position:absolute;left:0;color:#5FD38D;font-weight:800}
.foot{position:absolute;left:44px;bottom:24px;font-size:15px;color:#C9C7D8}.r{color:#FF6B6B}.o{color:#F08A4B}
.cta{position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:34px;font-weight:800;color:#F08A4B;text-shadow:0 2px 10px rgba(0,0,0,.6)}"""
CMF = "Made-up example. Estimates only, not financial advice."
br = '<div class="brand"><b>CheckMaybe</b> · Money tools</div>'
CM = [
 bg(GATE, .45, pos="center", grad="to bottom", rgb="10,10,18") + br +
   '<div style="position:absolute;left:44px;right:44px;top:110px"><div class="k">WHAT YOU SEE</div><h1 style="font-size:84px;margin-top:8px">“Only $67<br>a month.”</h1></div>'
   '<div style="position:absolute;left:44px;right:44px;top:690px"><div class="k">WHAT YOU PAY</div><h1 style="font-size:84px;margin-top:8px"><em>$1,608</em> total.</h1></div>'
   f'<div class="foot">{CMF}</div>',
 br + '<div class="k" style="margin-top:60px">THE REFLECTION</div><h1 style="font-size:56px;margin-top:10px">A $1,200 phone,<br>24 payments of $67</h1>'
   '<div class="card" style="margin-top:44px">$67 × 24 = <b>$1,608</b><br>− price $1,200<br>= <b class="r">$408 extra</b></div>'
   f'<div style="margin-top:34px;font-size:40px;font-weight:800">That’s about <span class="o">29.8% APR</span>.</div><div class="foot">{CMF}</div>',
 br + '<h1 style="font-size:56px;margin-top:70px">Check the reflection<br>before you click:</h1><div class="card" style="margin-top:44px"><ul>'
   '<li>Total you’ll pay</li><li>The real APR</li><li>Late fees</li><li>What else is due that month</li></ul></div>'
   f'<div class="foot">{CMF}</div>',
 bg(GATE, .6, 3, rgb="10,10,18") + br + '<h1 style="font-size:64px;margin-top:220px;text-align:center">The monthly number<br>is only <em>half</em><br>the picture.</h1>'
   '<div class="cta">Free “Before You Click Pay Later” guide<br>Link in bio →</div><div class="foot">Estimates only, not financial advice.</div>',
]

SETS = [("rg", RG_CSS, RG, 720, 960, 1.5, "/home/user/Website-Landing-Complete/generated_assets/social/borrow-check-01", "borrow"),
        ("sh", SH_CSS, SH, 1080, 1440, 1, "/home/user/sidehustlelab/content/instagram/2026-10-wish", "wish"),
        ("cm", CM_CSS, CM, 864, 1080, 1.25, "/home/user/checkmaybe/content/2026-10-reflection", "reflection")]
jobs = []
for key, css, bodies, w, h, sc, out, prefix in SETS:
    for i, b in enumerate(bodies, 1):
        src = f"{TMP}/{key}-{i}.html"
        open(src, "w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{b}'
                             + ('<div class="foot">副業實驗室</div>' if key == "sh" else "") + '</body></html>')
        jobs.append([src, f"{out}/{prefix}-{i:02d}.png", w, h, sc])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [s, o, w, h, sc] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: w, height: h }}, deviceScaleFactor: sc }});
  await p.goto('file://' + s); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.screenshot({{ path: o }}); console.log(o.split('/').slice(-2).join('/')); await p.close(); }}
await b.close();"""
open(f"{TMP}/shoot.mjs", "w").write(js); subprocess.run(["node", f"{TMP}/shoot.mjs"], check=True)
