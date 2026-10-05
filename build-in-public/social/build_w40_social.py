"""Week 0 social pack: Threads card, IG carousel (3:4), Reel (9:16). Numbers come from weeks/2026-W40.json + Gumroad referrer screenshot (Oct 5)."""
import os, subprocess, json
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2026-W40")
REPORT = os.path.abspath(os.path.join(OUT, "..", "..", "weeks", "2026-W40.png"))
BG, OR, MUT = "#15171F", "#F08A4B", "#9AA0AE"
CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{background:{BG};color:#fff;font-family:'Inter','DejaVu Sans',sans-serif;
width:VWpx;height:VHpx;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;position:relative}}
.tag{{color:{OR};font-weight:700;letter-spacing:.14em;font-size:30px;position:absolute;top:90px;left:90px}}
.foot{{color:{MUT};font-size:28px;position:absolute;bottom:80px;left:90px;right:90px;display:flex;justify-content:space-between}}
h1{{font-size:92px;line-height:1.08;font-weight:800;letter-spacing:-.02em}}h2{{font-size:64px;line-height:1.15;font-weight:800}}
.big{{font-size:260px;font-weight:800;color:{OR};line-height:1}}.sub{{font-size:46px;color:#D8DBE2;margin-top:28px;line-height:1.35}}
.o{{color:{OR}}}.row{{display:flex;justify-content:space-between;font-size:48px;padding:26px 0;border-bottom:2px solid #2A2E3A}}
.row b{{color:{OR}}}ul{{list-style:none;margin-top:40px}}li{{font-size:48px;line-height:1.3;margin:0 0 34px;padding-left:56px;position:relative}}
li:before{{content:'→';color:{OR};position:absolute;left:0}}.pg{{color:{MUT}}}"""
def page(body, w, h, n=None, total=None):
    pg = f'<span class="pg">{n}/{total}</span>' if n else '<span></span>'
    return f'<html><head><meta charset="utf-8"><style>{CSS.replace("VW",str(w)).replace("VH",str(h))}</style></head><body><div class="tag">CHECKMAYBE · WEEK 0</div>{body}<div class="foot"><span>Building in public from Taiwan</span>{pg}</div></body></html>'
carousel = [
 '<h1>I opened an online shop in September.</h1><div class="sub">Here is my real starting line.<br>No rounding up.</div>',
 '<div class="big">33</div><div class="sub">page views</div><h2 style="margin-top:70px">0 sales. <span class="o">0 USD.</span></h2>',
 '<h2>Where the 33 views came from</h2><div style="margin-top:50px"><div class="row"><span>Direct, email, messages</span><b>16</b></div><div class="row"><span>Facebook</span><b>15</b></div><div class="row"><span>Threads</span><b>1</b></div><div class="row"><span>My own shop page</span><b>1</b></div></div><div class="sub">24 of 33 views: <span class="o">United States</span></div>',
 '<h2>What went wrong</h2><ul><li>Applied to my first affiliate network. <span class="o">Declined.</span></li><li>My first English Reel: <span class="o">5 views.</span></li><li>My first build-in-public post had typos.</li></ul>',
 '<h2>What I learned</h2><ul><li>Views are not sales.</li><li>People came, looked, and left. The offer is not clear yet.</li><li>The product series is ready. Traffic is the missing piece.</li></ul>',
 '<h1>Next week:<br><span class="o">one product,<br>one audience.</span></h1><div class="sub">Real numbers every Sunday.<br>Even the zeros. Follow along.</div>',
]
reel = [
 '<h1>I opened an online shop in September.</h1><div class="sub">Here is my real number.</div>',
 '<div class="big">33</div><div class="sub">page views on my products</div>',
 '<div class="big">0</div><div class="sub">sales. 0 USD.</div>',
 '<h1><span class="o">24</span> of them<br>were in the US.</h1><div class="sub">I run this shop from Taiwan.</div>',
 '<h2>Also this week:</h2><ul><li>Declined by an affiliate network</li><li>5 views on my first Reel</li></ul>',
 '<h1>Next week:<br><span class="o">one product,<br>one audience.</span></h1><div class="sub">Real numbers every Sunday.</div>',
]
threads = '<div class="big" style="font-size:200px">0 sales</div><h2 style="margin-top:40px">33 page views. 0 USD.</h2><div class="sub">Week 0 of building a shop from Taiwan, in English.<br>Real numbers every Sunday.</div>'
os.makedirs(OUT+"/html", exist_ok=True)
jobs = []
def add(name, html, w, h):
    p = f"{OUT}/html/{name}.html"; open(p,"w").write(html); jobs.append([p, f"{OUT}/{name}.png", w, h])
add("threads-card", page(threads,1080,1350), 1080, 1350)
for i,b in enumerate(carousel,1): add(f"carousel-{i:02d}", page(b,1080,1440,i,len(carousel)+1), 1080, 1440)
for i,b in enumerate(reel,1): add(f"reel-shot-{i}", page(b.replace("<h1>","<h1 style='font-size:110px'>").replace('class="sub"','class="sub" style="font-size:64px"').replace("<li>","<li style='font-size:66px;padding-left:90px'>").replace("<h2>","<h2 style='font-size:84px'>").replace('class="big"','class="big" style="font-size:340px"'),1080,1920), 1080, 1920)
json.dump(jobs, open(OUT+"/html/jobs.json","w"))
js = """import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs'; import fs from 'fs';
const jobs = JSON.parse(fs.readFileSync(process.argv[2])); const b = await chromium.launch();
for (const [src,out,w,h] of jobs){ const p = await b.newPage({viewport:{width:w,height:h}}); await p.goto('file://'+src); await p.screenshot({path:out}); await p.close(); }
await b.close();"""
open(OUT+"/html/render.mjs","w").write(js)
subprocess.run(["node", OUT+"/html/render.mjs", OUT+"/html/jobs.json"], check=True)
# carousel slide 7 = the weekly report
subprocess.run(["cp", REPORT, f"{OUT}/carousel-07.png"], check=True)
# Reel: shots ~3.3s each with a slow zoom, report card as last shot; silent (add IG music)
clips = []
shots = [f"{OUT}/reel-shot-{i}.png" for i in range(1,len(reel)+1)]
rep = f"{OUT}/html/reel-report.png"
subprocess.run(["ffmpeg","-y","-v","error","-i",REPORT,"-vf",f"scale=1000:-1,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color={BG}",rep],check=True)
for k,s in enumerate(shots+[rep]):
    d = 3.3 if k < len(shots) else 3.5; c = f"{OUT}/html/c{k}.mp4"; n=int(d*30)
    subprocess.run(["ffmpeg","-y","-v","error","-loop","1","-i",s,"-vf",
      f"scale=2160:3840,zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,format=yuv420p",
      "-frames:v",str(n),"-c:v","libx264","-crf","18",c],check=True); clips.append(c)
open(f"{OUT}/html/list.txt","w").write("".join(f"file '{c}'\n" for c in clips))
subprocess.run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",f"{OUT}/html/list.txt","-c","copy",f"{OUT}/week0-reel.mp4"],check=True)
print("done")
