"""CheckMaybe English Reel: "Comment to claim" — ~30s, 1080x1920, silent (add upbeat music in IG).
# Inputs (not in repo): v1.mp4/v2.mp4 = Drive 生活影片/ig常態1.mp4, ig常態2.mp4; face.onnx = OpenCV YuNet. Needs ffmpeg, Playwright, opencv-python-headless.
Chinese ad footage stays visible; each clip gets an English "Ad says" translation tag.
Pacing per founder: <=3-4s per shot, ad clips at 1.3x."""
import json, os, subprocess, glob
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
os.makedirs("ov_en", exist_ok=True); os.makedirs("seg_en", exist_ok=True)
ORANGE, INK, BG = "#F08A4B", "#15171F", "#15171F"
CSS = f"""@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;background:transparent;font-family:"Inter","DejaVu Sans",sans-serif;color:#fff}}
.sub{{position:absolute;left:60px;right:60px;top:1450px;text-align:center;font-size:54px;font-weight:900;line-height:1.25;background:rgba(21,23,31,.86);border-radius:28px;padding:24px 18px}}
.o{{color:{ORANGE}}}.r{{color:#FF6B6B}}
.tr{{position:absolute;left:60px;right:60px;top:1230px;background:#fff;color:{INK};border-radius:20px;padding:18px 24px;font-size:40px;font-weight:700;line-height:1.25;box-shadow:0 8px 30px rgba(0,0,0,.4)}}
.tr small{{display:block;font-size:24px;letter-spacing:.14em;color:{ORANGE};font-weight:900;margin-bottom:6px}}
.card{{position:absolute;left:70px;right:70px;top:430px;background:rgba(21,23,31,.9);border:3px solid {ORANGE};border-radius:36px;padding:66px 58px}}
.num{{display:inline-block;background:{ORANGE};color:{INK};font-weight:900;font-size:56px;border-radius:999px;width:96px;height:96px;line-height:96px;text-align:center;margin-bottom:30px}}
.ct{{font-size:80px;font-weight:900;line-height:1.15}}.cs{{font-size:46px;font-weight:500;line-height:1.45;margin-top:36px;color:#E3E5EC}}
.tag{{position:absolute;left:70px;top:320px;font-size:34px;font-weight:900;color:{ORANGE};letter-spacing:.14em}}
.q{{font-size:50px;font-weight:700;line-height:1.35;margin-top:30px}}.q b{{color:{ORANGE}}}
"""
def page(body, bg="transparent"):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS} body{{background:{bg}}}</style></head><body>{body}</body></html>'
def tr(t): return f'<div class="tr"><small>THE AD SAYS (TRANSLATED)</small>“{t}”</div>'
S1 = '<div class="sub">“Comment +1, I’ll send it free.”<br><span class="o">Ever fallen for it?</span></div>'
S2 = '<div class="sub">Money hacks. AI tools. Viral reach.<br><span class="o">Just comment.</span></div>'
S3 = '<div class="sub">You claim it. You follow it.<br><span class="r">Nothing like the promise.</span></div>'
TAG = '<div class="tag">CHECK BEFORE YOU TRUST</div>'
OV = {
 "a0": page(tr("Comment below and I’ll send you the tool") + S1),
 "a1": page(tr("How to make IG push your Reels to non-followers") + S1),
 "a2": page(tr("1 million subscribers with an AI-run channel") + S1),
 "b0": page(tr("I made $10,000 with my own AI product") + S2),
 "b1": page(tr("Shopee affiliate + AI-generated influencers") + S2),
 "c0": page(tr("Post to FB, IG, TikTok. Earn commission on autopilot") + S3),
 "c1": page(tr("3 short videos in 30 minutes a day") + S3),
 "k0": page(TAG+'<div class="card" style="top:660px;text-align:center"><div class="ct">Not always a scam.</div><div class="ct" style="margin-top:20px">But it’s <span class="o">never the whole picture.</span></div></div>'),
 "k1": page(TAG+'<div class="card"><div class="num">1</div><div class="ct">You see their <span class="o">best</span> result, not the average.</div><div class="cs">100 posts flop. 1 goes viral.<br>That’s the one you see.</div></div>'),
 "k2": page(TAG+'<div class="card"><div class="num">2</div><div class="ct">“Comment to claim” <span class="o">is the strategy.</span></div><div class="cs">More comments, more reach.<br>The DM is usually the start<br>of a sales funnel.</div></div>'),
 "k3": page(TAG+'<div class="card"><div class="num">3</div><div class="ct">Their starting line <span class="o">isn’t yours.</span></div><div class="cs">Followers, ad budget, years in.<br>You’re starting from zero.</div></div>'),
 "k4": page('<div class="card" style="top:620px;text-align:center"><div class="ct" style="font-size:72px">So I won’t sell you secrets.</div><div class="cs" style="font-size:40px">I’m building small tools<br>from Taiwan, from zero,<br>in public.<br><span class="o" style="font-weight:900;font-size:48px">Real numbers every week.<br>Even when it’s zero.</span></div></div>', BG),
 "k5": page('<div class="tag" style="top:380px">NEXT TIME YOU SEE “COMMENT TO CLAIM”</div><div class="card" style="top:480px"><div class="ct" style="font-size:72px">Ask 3 questions</div><div class="q">1. How do <b>they</b> actually make money?</div><div class="q">2. Is this their <b>average</b>, or their <b>best</b>?</div><div class="q">3. What do <b>I</b> have to give?</div><div class="cs" style="margin-top:50px;color:#9EA3B5;font-size:38px">CheckMaybe · Check before you pay.</div></div>', BG),
}
jobs = []
for k, h in OV.items():
    p = f"{D}/ov_en/{k}.html"; open(p, "w").write(h); jobs.append([p, f"{D}/ov_en/{k}.png"])
js = f"""import {{ chromium }} from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b=await chromium.launch();for(const [s,o] of {json.dumps(jobs)}){{const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});await p.goto('file://'+s,{{waitUntil:'networkidle'}});await p.evaluate(()=>document.fonts.ready);await p.screenshot({{path:o,omitBackground:true}});await p.close();}}await b.close();"""
open("ov_en/s.mjs", "w").write(js); subprocess.run(["node", "ov_en/s.mjs"], check=True)

FPS, SP = 30, 1.3
def run(a): subprocess.run(["ffmpeg", "-v", "error", "-y"] + a, check=True)
def clear(out, src, ss, dur, ov, extra=(), top=270):
    d = out.replace(".mp4", "_f"); os.makedirs(d, exist_ok=True)
    for f in glob.glob(d + "/*.png"): os.remove(f)
    run(["-ss", str(ss), "-t", str(dur*SP), "-i", src, "-vf", f"setpts=PTS/{SP},scale=1080:-2,crop=1080:1920,fps={FPS}", d + "/%04d.png"])
    subprocess.run(["python3", "mask_clip.py", d, json.dumps(list(extra)), f"ov_en/{ov}.png", str(top)], check=True)
    run(["-framerate", str(FPS), "-i", d + "/%04d.png", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-t", str(dur), out])
def blurbg(out, src, ss, dur, ov):
    run(["-ss", str(ss), "-t", str(dur*SP), "-i", src, "-loop", "1", "-i", f"ov_en/{ov}.png", "-filter_complex",
         f"[0:v]setpts=PTS/{SP},scale=1080:-2,crop=1080:1920,boxblur=30:2,eq=brightness=-0.35,fps={FPS}[b];[b][1:v]overlay=0:0:shortest=1,format=yuv420p",
         "-t", str(dur), "-an", "-r", str(FPS), out])
def card(out, dur, ov):
    run(["-f", "lavfi", "-i", f"color=c={BG}:s=1080x1920:d={dur}:r={FPS}", "-i", f"ov_en/{ov}.png", "-filter_complex", "[0:v][1:v]overlay=0:0,format=yuv420p", "-t", str(dur), out])
segs = []
def S(n): segs.append(f"seg_en/{n}.mp4"); return f"seg_en/{n}.mp4"
clear(S("a0"), "v2.mp4", 80.4, 1.3, "a0", top=180)
clear(S("a1"), "v1.mp4", 76.3, 1.3, "a1", top=290)
clear(S("a2"), "v2.mp4", 92.3, 1.3, "a2", [[0, 560, 1080, 940]], top=200)
clear(S("b0"), "v2.mp4", 17.3, 2.2, "b0", top=195)
clear(S("b1"), "v2.mp4", 64.0, 2.2, "b1", top=180)
clear(S("c0"), "v2.mp4", 77.6, 2.2, "c0", [[470, 1570, 680, 1670]], top=130)
clear(S("c1"), "v1.mp4", 18.3, 2.2, "c1", top=40)
blurbg(S("k0"), "v1.mp4", 41.0, 2.8, "k0")
blurbg(S("k1"), "v2.mp4", 18.5, 3.5, "k1")
blurbg(S("k2"), "v1.mp4", 52.0, 3.5, "k2")
blurbg(S("k3"), "v2.mp4", 92.0, 3.5, "k3")
card(S("k4"), 3.5, "k4")
card(S("k5"), 4.0, "k5")
open("seg_en/list.txt", "w").write("".join(f"file '{os.path.basename(s)}'\n" for s in segs))
run(["-f", "concat", "-safe", "0", "-i", "seg_en/list.txt", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "reel-comment-to-claim-EN.mp4"])
print("done")
