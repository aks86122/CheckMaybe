"""Talking-video auto edit: trim pauses, word-timed captions with keyword highlight, big punch words. 9:16 1080x1920.

Usage:
  python autocut.py IN.mp4 OUT.mp4 --brand brand.json [--keywords 10萬,18期] [--punch 簡單,0元] [--fix 五千毫安=5000mAh] [--no-cut] [--model small]
  Re-run with --transcript OUT.words.json to skip transcription after fixing words by hand.

brand.json: {"font": "Noto Sans CJK TC", "fontsdir": "...", "text": "#FFFFFF", "accent": "#F7BF20",
             "outline": "#14213D", "lang": "zh", "caption_y": 520, "size": 92, "pop": true, "max_chars": 12}
Captions drop punctuation. No dashes are ever added. Keep the transcript JSON next to OUT for edits (--transcript).
"""
import argparse, json, os, re, subprocess, sys

def ass_color(hex_):  # #RRGGBB -> &H00BBGGRR
    h = hex_.lstrip("#"); return f"&H00{h[4:6]}{h[2:4]}{h[0:2]}"

def ts(t):
    t = max(t, 0); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def transcribe(wav, model, lang):
    from faster_whisper import WhisperModel
    m = WhisperModel(model, device="cpu", compute_type="int8", cpu_threads=os.cpu_count())
    prompt = "以下是繁體中文的口語，使用台灣用語。" if lang == "zh" else None
    segs, _ = m.transcribe(wav, language=lang, vad_filter=True, word_timestamps=True,
                           condition_on_previous_text=False, initial_prompt=prompt)
    conv = (lambda s: s)
    if lang == "zh":
        from opencc import OpenCC; cc = OpenCC("s2twp"); conv = cc.convert
    return [{"w": conv(w.word), "s": w.start, "e": w.end} for s in segs for w in s.words]

def keep_segments(words, dur, gap=0.55, pad=0.12):
    """Speech spans; pauses longer than `gap` are cut."""
    spans = []
    for w in words:
        s, e = max(w["s"] - pad, 0), min(w["e"] + pad, dur)
        if spans and s - spans[-1][1] <= gap: spans[-1][1] = max(spans[-1][1], e)
        else: spans.append([s, e])
    return spans

def remap(t, spans):
    acc = 0.0
    for s, e in spans:
        if t < s: return acc
        if t <= e: return acc + (t - s)
        acc += e - s
    return acc

PUNCT = re.compile(r"[﹐﹑﹒﹔﹕﹖﹗，。！？、；：,.!?;:「」『』（）()\"'…—–-]")

def chunks(words, max_chars, lang):
    out, cur = [], []
    def flush():
        if cur: out.append(cur.copy()); cur.clear()
    for i, w in enumerate(words):
        cur.append(w)
        text = "".join(x["w"] for x in cur) if lang == "zh" else " ".join(x["w"].strip() for x in cur)
        nxt_gap = words[i + 1]["s"] - w["e"] if i + 1 < len(words) else 9
        digit_run = i + 1 < len(words) and w["w"][-1:].isdigit() and words[i + 1]["w"][:1].isdigit()
        if not digit_run and (len(PUNCT.sub("", text)) >= max_chars or PUNCT.search(w["w"]) or nxt_gap > 0.35): flush()
    flush(); return out

def build_ass(words, brand, keywords, punch, fixes=(), W=1080, H=1920):
    f, size, y = brand.get("font", "Noto Sans CJK TC"), brand.get("size", 92), brand.get("caption_y", 520)
    acc, txt, ol = ass_color(brand["accent"]), ass_color(brand.get("text", "#FFFFFF")), ass_color(brand.get("outline", "#000000"))
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{f},{size},{txt},{txt},{ol},&H64000000,-1,0,0,0,100,100,2,0,1,7,3,2,60,60,{y},1
Style: Punch,{f},{int(size*2.4)},{acc},{acc},{ol},&H64000000,-1,0,0,0,100,100,4,0,1,10,4,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lang = brand.get("lang", "zh"); ev = []
    for c in chunks(words, brand.get("max_chars", 12), lang):
        s, e = c[0]["s"], c[-1]["e"] + 0.08
        sep = "" if lang == "zh" else " "
        line = sep.join(t for t in (PUNCT.sub("", w["w"]).strip() for w in c) if t)
        for a_, b_ in fixes: line = line.replace(a_, b_)
        for k in sorted(keywords, key=len, reverse=True):
            if k and k in line: line = line.replace(k, "\x00" + k + "\x01")
        line = line.replace("\x00", "{\\c" + acc + "}").replace("\x01", "{\\c" + txt + "}")
        if not line: continue
        pop = "{\\fscx88\\fscy88\\t(0,110,\\fscx100\\fscy100)}" if brand.get("pop", True) else ""
        ev.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{pop}{line}")
    # punch words: big centered, when the word is spoken
    full = [(PUNCT.sub("", w["w"]).strip(), w["s"], w["e"]) for w in words]
    joined = "".join(t for t, _, _ in full)
    for p in punch:
        start = joined.find(p)
        if start < 0: continue
        pos = 0
        for t, s, e in full:
            if pos <= start < pos + max(len(t), 1):
                ev.append(f"Dialogue: 1,{ts(s)},{ts(s + 1.1)},Punch,,0,0,0,,"
                          "{\\pos(" + f"{W//2},{int(H*0.38)}" + ")\\fscx60\\fscy60\\t(0,140,\\fscx108\\fscy108)\\t(140,240,\\fscx100\\fscy100)\\fad(0,180)}" + p)
                break
            pos += len(t)
    return head + "\n".join(ev) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp"); ap.add_argument("out"); ap.add_argument("--brand", required=True)
    ap.add_argument("--keywords", default=""); ap.add_argument("--punch", default="")
    ap.add_argument("--fix", default="", help="caption text fixes: 五千毫安=5000mAh,一百段=100段")
    ap.add_argument("--no-cut", action="store_true"); ap.add_argument("--model", default="small")
    ap.add_argument("--transcript", help="reuse/edit an existing words JSON instead of re-transcribing")
    a = ap.parse_args()
    brand = json.load(open(a.brand)); lang = brand.get("lang", "zh")
    work = os.path.splitext(a.out)[0]; os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", a.inp]))
    tj = a.transcript or work + ".words.json"
    if a.transcript and os.path.exists(a.transcript): words = json.load(open(a.transcript))
    else:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", a.inp, "-ar", "16000", "-ac", "1", work + ".wav"], check=True)
        words = transcribe(work + ".wav", a.model, lang); json.dump(words, open(tj, "w"), ensure_ascii=False, indent=1)
    spans = [[0, dur]] if a.no_cut else keep_segments(words, dur)
    mw = [{"w": w["w"], "s": remap(w["s"], spans), "e": remap(w["e"], spans)} for w in words]
    kws = [k for k in a.keywords.split(",") if k]; punch = [p for p in a.punch.split(",") if p]
    fixes = [tuple(x.split("=", 1)) for x in a.fix.split(",") if "=" in x]
    open(work + ".ass", "w").write(build_ass(mw, brand, kws, punch, fixes))
    fit = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1"
    parts, cat = [], ""
    for i, (s, e) in enumerate(spans):
        parts.append(f"[0:v]trim={s:.3f}:{e:.3f},setpts=PTS-STARTPTS,{fit}[v{i}];[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS[a{i}]")
        cat += f"[v{i}][a{i}]"
    fd = os.path.expanduser(brand.get("fontsdir", "~/.cache/reels-fonts"))
    sub = f"ass={work}.ass" + (f":fontsdir={fd}" if fd else "")
    fc = ";".join(parts) + f";{cat}concat=n={len(spans)}:v=1:a=1[cv][ca];[cv]{sub}[vo]"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", a.inp, "-filter_complex", fc, "-map", "[vo]", "-map", "[ca]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                    "-movflags", "+faststart", a.out], check=True)
    print(a.out, f"{sum(e - s for s, e in spans):.1f}s (from {dur:.1f}s)")

if __name__ == "__main__":
    main()
