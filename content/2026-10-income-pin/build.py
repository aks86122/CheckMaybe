"""防詐拆解 #04 / CheckMaybe "income pin" teardown. Text-only slides (no third-party photos).
Source checked 2026-10-10: a Pinterest pin ("How I make over $9,000 from home online every month")
linking to a 2018 blog income report titled $5,532.13. The blog is not named on the slides."""
import json, os, subprocess, sys
TMP = "/tmp/income-pin"; os.makedirs(TMP, exist_ok=True)
PIN = lambda big, small: (f'<div class="pin"><div class="p1">HOW</div><div class="p2">I MAKE OVER</div><div class="p3">$9,000</div>'
                          f'<div class="p2">FROM HOME</div><div class="p4">ONLINE EVERY MONTH</div><div class="pcap">{small}</div></div>')
PIN_CSS = """.pin{background:#fff;color:#1a1a1a;border-radius:18px;text-align:center;font-family:"Liberation Sans",Arial,sans-serif;font-weight:800;box-shadow:0 10px 40px rgba(0,0,0,.45)}
.p1{font-size:1.9em;line-height:1}.p2{font-size:.95em;margin-top:.15em}.p3{font-size:1.9em;color:#e0118a;line-height:1.05}.p4{font-size:.62em;margin-top:.2em}
.pcap{font-size:.42em;color:#777;font-weight:700;margin-top:.9em;letter-spacing:.04em}"""

# ---------- 副業實驗室 (1080x1440) ----------
SH_CSS = PIN_CSS + """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1440px;overflow:hidden}
body{background:#14213D;color:#fff;font-family:"Noto Sans TC",sans-serif;padding:150px 84px 130px;position:relative;display:flex;flex-direction:column;justify-content:center}
.tag{position:absolute;left:84px;top:96px}
.tag{display:inline-block;background:#F08A3C;color:#14213D;font-weight:900;font-size:30px;padding:8px 22px;border-radius:999px}
h1{font-weight:900;font-size:92px;line-height:1.22;margin-top:36px}.g{color:#F7BF20}.o{color:#F08A3C}
p{font-size:44px;line-height:1.6;margin-top:30px}.mute{color:#C9D0DE}
.cols{display:flex;gap:28px;margin-top:56px}.col{flex:1;background:#1C2C50;border-radius:22px;padding:34px 30px}
.col h3{font-size:34px;color:#C9D0DE;font-weight:700}.col .n{font-size:84px;font-weight:900;margin-top:10px}.col .s{font-size:32px;line-height:1.55;margin-top:14px;color:#C9D0DE}
ol{list-style:none;counter-reset:n;margin-top:50px}ol li{counter-increment:n;position:relative;padding-left:100px;font-size:48px;line-height:1.45;margin-bottom:40px}
ol li:before{content:counter(n);position:absolute;left:0;top:4px;width:70px;height:70px;border-radius:50%;background:#F7BF20;color:#14213D;font-weight:900;display:flex;align-items:center;justify-content:center;font-size:40px}
.q{border-left:8px solid #F7BF20;padding:8px 0 8px 34px;font-size:46px;line-height:1.55;margin-top:40px}
.foot{position:absolute;left:84px;bottom:64px;font-size:30px;color:#C9D0DE;font-weight:700;letter-spacing:.1em}
.src{position:absolute;right:84px;bottom:66px;font-size:24px;color:#8E9AB5}"""
SRC = '<div class="src">資料：公開Pin與部落格文章（2018收入報告）</div>'
SH = [
 '<span class="tag">防詐拆解 #04</span><div style="display:flex;gap:56px;align-items:center;">'
   f'<div style="flex:0 0 380px;font-size:66px">{PIN("", "Pin上的圖（文字重製）")}</div>'
   '<div><h1 style="font-size:84px;margin-top:0">圖上寫<br><span class="g">月入$9,000</span></h1><p>點進去，<br>文章標題寫的是<br><span class="o" style="font-weight:900;font-size:60px">$5,532</span></p></div></div>'
   '<p class="mute" style="margin-top:70px">不是說作者騙人。<br>是<b style="color:#fff">圖</b>跟<b style="color:#fff">文章</b>講的不一樣。</p>',
 '<span class="tag">圖vs文章</span><div class="cols">'
   '<div class="col"><h3>Pin上寫的</h3><div class="n g">$9,000+</div><div class="s">「每個月」<br>描述還寫「超過$10,000」</div></div>'
   '<div class="col"><h3>文章寫的</h3><div class="n o">$5,532</div><div class="s">只有那1個月<br>（2018年11月）</div></div></div>'
   '<p>前4個月是：</p><p class="g" style="font-size:52px;font-weight:900;margin-top:10px">$703→$2,797→$4,509→$4,798</p><p class="mute">「每個月」，其實是一路爬上來的其中一個月。</p>' + SRC,
 '<span class="tag">錢從哪裡來</span><h1 style="font-size:76px">她的收入，<br>有一塊來自<span class="g">教你賺錢</span></h1><ol>'
   '<li>網站廣告</li><li>你透過她的連結<br>架部落格的分潤</li><li>免費課程，<br>一路帶你去註冊</li></ol>' + SRC,
 '<span class="tag">圖上沒寫的</span><h1 style="font-size:76px">作者自己<br>在文章裡寫了：</h1>'
   '<div class="q">「好幾個月，<br>收入大約是0」</div><div class="q">「流量跟收入<br>起伏很大」</div>'
   '<p class="mute">這些，不會出現在一張<br>拿著鈔票的圖上。</p>' + SRC,
 '<span class="tag">看到收入截圖，先問</span><ol style="margin-top:70px">'
   '<li>這是哪一個月？<br>平均，還是最好的那個月？</li><li>錢從哪裡來？</li><li>你照做，<br>要先付錢給誰？</li></ol>',
 '<div><h1>先實驗，<br><span class="g">再投入。</span></h1>'
   '<p>我的副業實驗，<br>數字是0也照實寫。</p><p class="mute">追蹤看實際結果。</p></div>',
]

# ---------- CheckMaybe (864x1080 @1.25) ----------
CM_CSS = PIN_CSS + """*{box-sizing:border-box;margin:0;padding:0}html,body{width:864px;height:1080px;overflow:hidden}
body{background:#15171F;color:#EDEBF5;font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif;position:relative;padding:90px 44px 70px;display:flex;flex-direction:column;justify-content:center}
.brand{position:absolute;left:44px;top:40px}
.brand{font-size:16px;letter-spacing:.18em;font-weight:700;color:#C9C7D8;text-transform:uppercase}.brand b{color:#F08A4B}
.k{font-size:22px;letter-spacing:.15em;font-weight:700;color:#D8D6E6}
h1{font-weight:800;line-height:1.1}h1 em{font-style:normal;color:#F08A4B}
.card{background:rgba(30,33,48,.92);border:1px solid #33384F;border-radius:16px;padding:32px 36px;font-size:34px;line-height:1.65}
ul{list-style:none}li{padding-left:1.3em;position:relative;margin-bottom:.45em}li:before{content:"✓";position:absolute;left:0;color:#5FD38D;font-weight:800}
.cols{display:flex;gap:22px;margin-top:40px}.col{flex:1;background:#1E2130;border:1px solid #33384F;border-radius:16px;padding:26px 26px}
.col .h{font-size:20px;letter-spacing:.12em;color:#C9C7D8;font-weight:700}.col .n{font-size:66px;font-weight:800;margin-top:6px}.col .s{font-size:24px;line-height:1.5;color:#C9C7D8;margin-top:8px}
.q{border-left:6px solid #F08A4B;padding:6px 0 6px 26px;font-size:36px;line-height:1.5;margin-top:30px}
.foot{position:absolute;left:44px;right:44px;bottom:22px;font-size:15px;color:#9A98AC}.o{color:#F08A4B}.y{color:#F7C948}
.cta{position:absolute;left:0;right:0;bottom:80px;text-align:center;font-size:32px;font-weight:800;color:#F08A4B}"""
br = '<div class="brand"><b>CheckMaybe</b> · Check before you trust</div>'
CMF = '<div class="foot">Based on a public pin and the blog post it links to (a 2018 income report). Not financial advice.</div>'
CM = [
 br + '<div style="display:flex;gap:40px;align-items:center;">'
   f'<div style="flex:0 0 330px;font-size:56px">{PIN("", "THE PIN (text recreated)")}</div>'
   '<div><div class="k">THE PIN SAYS</div><h1 style="font-size:60px;margin-top:6px"><span class="y">$9,000</span><br>every month.</h1>'
   '<div class="k" style="margin-top:40px">THE POST SAYS</div><h1 style="font-size:60px;margin-top:6px"><em>$5,532.</em></h1></div></div>'
   '<div style="margin-top:44px;font-size:30px;line-height:1.5;color:#C9C7D8">Not calling anyone a liar.<br>The picture and the post just don’t match.</div>' + CMF,
 br + '<h1 style="font-size:54px;">Picture vs. post</h1><div class="cols">'
   '<div class="col"><div class="h">THE PIN</div><div class="n y">$9,000+</div><div class="s">“every month”<br>caption: “over $10,000”</div></div>'
   '<div class="col"><div class="h">THE POST</div><div class="n o">$5,532</div><div class="s">one month<br>(November 2018)</div></div></div>'
   '<div class="card" style="margin-top:34px">The 4 months before:<br><b class="y">$703 → $2,797 → $4,509 → $4,798</b></div>' + CMF,
 br + '<h1 style="font-size:54px;">Where the money<br>came from</h1><div class="card" style="margin-top:36px"><ul>'
   '<li>Ads on the blog</li><li>Commissions when readers sign up for blog hosting through her links</li><li>A free course that leads to those sign-ups</li></ul></div>'
   '<div style="margin-top:30px;font-size:32px;line-height:1.5">Part of the income is <em class="o" style="font-style:normal;font-weight:800">teaching you to make income.</em></div>' + CMF,
 br + '<h1 style="font-size:54px;">What the pin<br>left out</h1><div style="font-size:26px;color:#C9C7D8;margin-top:14px">The author wrote these in the post herself:</div>'
   '<div class="q">“I was making ~$0 and struggling for many months”</div><div class="q">Traffic and earnings are “quite volatile”</div>'
   '<div style="margin-top:36px;font-size:30px;line-height:1.5;color:#C9C7D8">None of that fits on a photo<br>of someone holding cash.</div>' + CMF,
 br + '<h1 style="font-size:54px;">Before you trust<br>an income claim:</h1><div class="card" style="margin-top:36px"><ul>'
   '<li>Which month is it?</li><li>An average, or the best month?</li><li>Where does the money come from?</li><li>Who do you pay first?</li></ul></div>' + CMF,
 br + '<h1 style="font-size:66px;text-align:center;margin-bottom:120px">The headline number<br>is the <em>ad</em>.<br>The post is the <em>receipt</em>.</h1>'
   '<div class="cta">Save this for the next income screenshot.<br>More checks: link in bio →</div><div class="foot">Not financial advice.</div>',
]
SETS = [("sh", SH_CSS, SH, 1080, 1440, 1, "/home/user/sidehustlelab/content/instagram/2026-10-income-pin", "income-pin"),
        ("cm", CM_CSS, CM, 864, 1080, 1.25, "/home/user/checkmaybe/content/2026-10-income-pin", "income-pin")]
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
