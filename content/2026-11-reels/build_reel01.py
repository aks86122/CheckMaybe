"""Reel 01 (Black Friday deal check): renders hook A and hook B as 1080x1920 30 fps MP4, no audio.

Script: 01-deal-check-reel.md. Numbers: s3 / Holiday Hidden Cost Tracker Deal Check example rows.
Each frame is drawn by render(t) in a Playwright page and piped into ffmpeg.
Usage: python3 content/2026-11-reels/build_reel01.py
"""
import json, os, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ART2 = f"{ROOT}/content/2026-10-comic-02/art"
ART3 = f"{ROOT}/content/2026-10-comic-03/art"
OUT = f"{HERE}/out"
os.makedirs(OUT, exist_ok=True)
TMP = tempfile.mkdtemp(prefix="cm-reel01-")
FPS = 30

CSS = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#15171F;color:#EDEBF5;font-family:Inter,"Liberation Sans",sans-serif}
#glow{position:absolute;inset:0;background:radial-gradient(ellipse 70% 40% at 80% 8%,rgba(240,138,75,.16),transparent 70%)}
#kick{position:absolute;left:80px;top:250px;font-size:30px;letter-spacing:.16em;font-weight:600;color:#9A98AC;text-transform:uppercase}#kick b{color:#F08A4B}
#cap{position:absolute;left:80px;right:80px;top:320px;font-size:74px;font-weight:800;line-height:1.16;min-height:200px}
.hl{white-space:nowrap;background:#F08A4B;color:#15171F;border-radius:16px;padding:0 16px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hl.red{background:#E2687B}
#stage{position:absolute;left:80px;right:80px;top:620px}
.card{background:#1C1E28;border:3px solid #33384F;border-radius:30px;padding:44px 52px;box-shadow:0 30px 80px rgba(0,0,0,.55)}
.card.red{border-color:#E2687B}
.lab{font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#9A98AC;font-weight:600;margin-bottom:18px}
.row{display:flex;justify-content:space-between;align-items:baseline;font-size:54px;font-weight:600;padding:14px 0}
.row .v{font-weight:800}
.big{font-size:150px;font-weight:800;line-height:1}
.strike{position:relative;color:#9A98AC}.strike i{position:absolute;left:-6px;top:50%;height:10px;background:#E2687B;border-radius:5px}
.pill{display:inline-block;font-weight:800;font-size:46px;border-radius:16px;padding:10px 26px;margin-top:22px}
.g{background:#1C3A2A;color:#74D39A}.b{background:#43202A;color:#E2687B}.o{background:#3D2A1C;color:#F08A4B}
.div{height:3px;background:#33384F;margin:14px 0}
.chip{display:flex;align-items:center;gap:30px;font-size:62px;font-weight:800;background:#1C1E28;border:3px solid #33384F;border-radius:26px;padding:30px 40px;margin-bottom:26px}
.chip .n{width:86px;height:86px;border-radius:50%;background:#F7C948;color:#15171F;display:flex;align-items:center;justify-content:center;font-size:52px;flex:none}
.split{display:flex;gap:30px}.split .card{flex:1;padding:40px 36px}
.q{font-size:120px;font-weight:800;line-height:1.1;margin-top:120px}.q em{font-style:normal;color:#F08A4B}
.ck{font-size:60px;font-weight:700;padding:16px 0}.ck b{color:#74D39A;margin-right:24px}
.small{font-size:38px;color:#B9B7C9;margin-top:10px}
#mas{position:absolute;left:40px;top:1180px;width:360px;transform-origin:50% 90%;
 -webkit-mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at center,#000 70%,transparent 100%)}
#foot{position:absolute;left:440px;right:80px;top:1440px;font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:#7F7D92;line-height:1.4}"""

JS = r"""
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const eo=x=>1-Math.pow(1-clamp(x),3);
const back=x=>{x=clamp(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const money=v=>'$'+v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
const money0=v=>'$'+Math.round(v).toLocaleString('en-US');
const pop=(lt,at,html)=>{const p=clamp((lt-at)/0.28);if(p<=0)return '';return `<div style="transform:scale(${0.6+0.4*back(p)});opacity:${p};transform-origin:left center">${html}</div>`};
const fade=(lt,at,html)=>{const p=eo((lt-at)/0.25);if(p<=0)return `<div style="opacity:0">${html}</div>`;return `<div style="opacity:${p};transform:translateY(${(1-p)*24}px)">${html}</div>`};

const CARDS={
 tv:(lt)=>{const s=eo((lt-0.35)/0.35);return `<div class="card"><div class="lab">TV · Black Friday</div>
   <div class="row"><span class="strike big" style="font-size:110px">$549<i style="width:${s*104}%"></i></span>
   ${pop(lt,0.7,'<span class="big" style="color:#F08A4B">$499</span>')}</div><div class="small">$50 off the usual price</div></div>`},
 tvred:(lt)=>`<div class="card red"><div class="lab">Same TV · on a plan</div>
   <div class="row"><span>Pay in full</span><span class="v">$538.92</span></div>
   ${fade(lt,0.25,'<div class="row"><span>12 × $49</span><span class="v">$588.00</span></div>')}
   ${pop(lt,0.75,'<span class="pill b">+$49.08 on the plan</span>')}</div>`,
 chips:(lt)=>['Usual price','Checkout price','Plan total'].map((x,i)=>pop(lt,0.1+i*0.15,`<div class="chip"><span class="n">${i+1}</span>${x}</div>`)).join(''),
 usual:(lt)=>`<div class="card"><div class="lab">Headphones</div>
   <div class="row"><span>Sale price</span><span class="v">$199</span></div>
   ${fade(lt,0.5,'<div class="row"><span>Usually sells for</span><span class="v">$249</span></div>')}
   ${pop(lt,1.4,'<span class="pill g">20.1% below: real deal</span>')}</div>`,
 checkout:(lt)=>{const p=eo((lt-1.1)/1.2);return `<div class="card"><div class="lab">Robot vacuum</div>
   ${fade(lt,0.1,'<div class="row"><span>Sale price</span><span class="v">$159.00</span></div>')}
   ${fade(lt,0.4,'<div class="row"><span>+ 8% tax</span><span class="v">$12.72</span></div>')}
   ${fade(lt,0.7,'<div class="row"><span>+ shipping</span><span class="v">$15.00</span></div>')}
   <div class="div"></div><div class="row"><span>At checkout</span><span class="v" style="color:#F08A4B;font-size:72px">${money(159+27.72*p)}</span></div></div>`},
 plan:(speed)=>(lt)=>{const a=0.5*speed,b=2.2*speed;const k=lt<a?0:Math.min(12,1+Math.floor((lt-a)/((b-a)/11)));
   return `<div class="card red"><div class="lab">TV · $499 sale</div>
   <div class="row"><span>Pay in full</span><span class="v">$538.92</span></div>
   <div class="row"><span>12 × $49</span><span class="v" style="color:#E2687B;font-size:72px">${money(49*k)}</span></div>
   <div class="small">${k?`payment ${k} of 12`:'&nbsp;'}</div>
   ${pop(lt,b+0.25*speed,'<span class="pill b">+$49.08 for the same TV</span>')}</div>`},
 question:(lt)=>fade(lt,0.05,'<div class="q">Wanted it <em>before</em> the sale?</div>'),
 cta:(lt)=>`<div class="card"><div class="lab">Deal Check tab · Google Sheets</div>
   ${['Usual price','Checkout price','Plan total'].map((x,i)=>pop(lt,0.15+i*0.18,`<div class="ck"><b>✓</b>${x}</div>`)).join('')}
   ${fade(lt,0.8,'<div class="small">Holiday Hidden Cost Tracker</div>')}</div>`,
 quiz:(lt)=>`<div class="split"><div class="card"><div class="lab">Pay today</div><div class="big" style="font-size:96px">$538.92</div></div>
   ${fade(lt,0.35,'<div class="card"><div class="lab">12 easy payments</div><div class="big" style="font-size:96px">$49<span style="font-size:48px">/mo</span></div></div>')}</div>`,
 quiz2:(lt)=>{const k=Math.min(12,1+Math.floor(clamp((lt-0.15)/1.3)*11.999));return `<div class="split"><div class="card"><div class="lab">Pay today</div><div class="big" style="font-size:96px">$538.92</div></div>
   <div class="card red"><div class="lab">12 × $49</div><div class="big" style="font-size:96px;color:#E2687B">${money0(49*k)}</div></div></div>
   ${pop(lt,1.65,'<span class="pill b">+$49.08 for the "easy" one</span>')}`},
};

let SC=[];let lastMas=null,masT=0;
function render(t){
  const s=SC.find(x=>t>=x.t0&&t<x.t1)||SC[SC.length-1];const lt=t-s.t0;
  // caption: typewriter
  const parts=s.cap;const total=parts.reduce((n,p)=>n+p[0].length,0);let n=Math.floor(lt/0.028);let html='';
  for(const [txt,cls] of parts){const shown=txt.slice(0,Math.max(0,Math.min(txt.length,n)));n-=txt.length;
    if(!shown)continue; html+=cls?`<span class="hl ${cls==='red'?'red':''}">${shown}</span>`:shown;}
  document.getElementById('cap').innerHTML=html;
  // card with enter animation unless continuing
  const st=document.getElementById('stage');const c=CARDS[s.card]?CARDS[s.card]:null;
  const body=s.fn?s.fn(lt):(c?c(lt):'');const p=s.cont?1:eo(lt/0.3);
  st.innerHTML=body;st.style.opacity=p;st.style.transform=`translateY(${(1-p)*50}px)`;
  // mascot pop when it changes
  const m=document.getElementById('mas');
  if(!s.mas){m.style.opacity=0;}else{m.src=s.mas;const mp=back(lt/0.3);m.style.opacity=clamp(lt/0.12);m.style.transform=`scale(${0.7+0.3*mp})`;}
}
"""

def scenes(kind):
    m = lambda d, f: f"file://{ART2 if d == 2 else ART3}/{f}.jpg"
    body = [
        dict(d=1.5, cap=[["Check ", ""], ["3 numbers", "o"]], card="chips", mas=m(2, "check")),
        dict(d=3.5, cap=[["1. The ", ""], ["usual", "o"], [" price", ""]], card="usual", mas=m(2, "asterisk")),
        dict(d=3.5, cap=[["2. The ", ""], ["checkout", "o"], [" price", ""]], card="checkout", mas=m(2, "calc")),
    ]
    if kind == "a":
        head = [
            dict(d=2.5, cap=[["This TV is ", ""], ["$50 off", "o"]], card="tv", mas=m(2, "tag")),
            dict(d=2.5, cap=[["and costs ", ""], ["$49.08 more", "red"]], card="tvred", mas=m(2, "unroll"), cont=True),
        ]
        plan = dict(d=4.5, cap=[["3. The ", ""], ["plan total", "o"]], card="plan1", mas=m(3, "calc"))
    else:
        head = [
            dict(d=2.5, cap=[["Which costs ", ""], ["less", "o"], ["?", ""]], card="quiz", mas=m(2, "asterisk")),
            dict(d=2.5, cap=[['The "easy" one: ', ""], ["$588", "red"]], card="quiz2", mas=m(2, "unroll"), cont=True),
        ]
        plan = dict(d=2.0, cap=[["3. The ", ""], ["plan total", "o"]], card="plan2", mas=m(3, "calc"))
    tail = [
        dict(d=2.0, cap=[], card="question", mas=None),
        dict(d=3.0, cap=[["Every deal, ", ""], ["one sheet", "o"]], card="cta", mas=m(2, "happy")),
    ]
    out, t = [], 0.0
    for s in head + body + [plan] + tail:
        s = dict(s); s["t0"], s["t1"] = t, t + s.pop("d"); t = s["t1"]; out.append(s)
    return out, t


def page(kind):
    sc, dur = scenes(kind)
    js_sc = json.dumps(sc)
    extra = "CARDS.plan1=CARDS.plan(1);CARDS.plan2=CARDS.plan(0.5);"
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            '<div id="glow"></div><div id="kick"><b>CheckMaybe</b> · Black Friday deal check</div>'
            '<div id="cap"></div><div id="stage"></div><img id="mas"><div id="foot">Made-up example<br>Not financial advice</div>'
            f'<script>{JS}{extra}SC={js_sc};render(0);</script></body></html>')
    path = f"{TMP}/reel01-{kind}.html"
    with open(path, "w") as f:
        f.write(html)
    return path, dur


jobs = []
for kind in ("a", "b"):
    src, dur = page(kind)
    jobs.append([src, f"{OUT}/checkmaybe-reel01-hook-{kind}.mp4", round(dur * FPS)])

node = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
import {{ spawn }} from 'child_process';
const jobs = {json.dumps(jobs)}; const b = await chromium.launch();
for (const [src, out, n] of jobs) {{
  const p = await b.newPage({{ viewport: {{ width: 1080, height: 1920 }} }});
  await p.goto('file://' + src); await p.evaluate(() => document.fonts.ready);
  const ff = spawn('ffmpeg', ['-y','-v','error','-f','image2pipe','-framerate','{FPS}','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-movflags','+faststart', out]);
  for (let i = 0; i < n; i++) {{
    await p.evaluate(t => render(t), i / {FPS});
    const buf = await p.screenshot({{ type: 'jpeg', quality: 92 }});
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }}
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
  console.log(out.split('/').pop(), n, 'frames'); await p.close();
}}
await b.close();"""
with open(f"{TMP}/render.mjs", "w") as f:
    f.write(node)
subprocess.run(["node", f"{TMP}/render.mjs"], check=True)
