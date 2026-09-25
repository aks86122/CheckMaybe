"""Render a CheckMaybe toolkit JSON (see SCHEMA.md) to a standalone HTML file."""
import html
import json
import sys

E = lambda s: html.escape(str(s or ""), quote=False)

SIG = {  # signal -> (css class, default label, icon)
    "GREEN": ("g", "GREEN-LEANING", "✓"),
    "AMBER": ("a", "AMBER — CHECK", "!"),
    "RED": ("r", "RED — STOP", "✕"),
    "VERIFY": ("v", "VERIFY BEFORE RELYING", "?"),
}


def pill(sig, label=None):
    cls, dflt, icon = SIG.get((sig or "VERIFY").upper(), SIG["VERIFY"])
    return f'<span class="pill {cls}"><i>{icon}</i>{E(label or dflt)}</span>'


def dot(sig):
    cls, _, icon = SIG.get((sig or "VERIFY").upper(), SIG["VERIFY"])
    return f'<span class="dot {cls}">{icon}</span>'


def callout(c):
    if not c:
        return ""
    return (f'<div class="callout {E(c.get("tone", "dark"))}"><div class="cl-label">{E(c.get("label"))}</div>'
            f'<div class="cl-text{" long" if len(c.get("text") or "") > 150 else ""}">{E(c.get("text"))}</div></div>')


def legend(items):
    if not items:
        return ""
    rows = "".join(f'<div class="lg">{pill(i.get("signal"), i.get("label"))}<span>{E(i.get("text"))}</span></div>' for i in items)
    return f'<div class="legend">{rows}</div>'


def p_cover(p, meta):
    steps = "".join(f'<div class="cv-step"><span>{i + 1:02d}</span>{E(s)}</div>' for i, s in enumerate(p.get("steps", [])))
    inside = "".join(f"<li>{E(s)}</li>" for s in p.get("inside", []))
    legal = "".join(f"<div>{E(s)}</div>" for s in p.get("legal", []))
    q = f'<p class="cv-quote">{E(p["quote"])}</p>' if p.get("quote") else ""
    return f'''<section class="page cover">
  <div class="cv-top">{E(p.get("topline"))}</div>
  <div class="cv-brand">CHECKMAYBE</div>
  <h1 class="cv-title">{E(p.get("title"))}</h1>
  <div class="cv-rule"></div>
  <p class="cv-sub">{E(p.get("subtitle"))}</p>
  <p class="cv-value">{E(p.get("value"))}</p>
  <div class="cv-steps">{steps}</div>
  {q}
  <div class="cv-key"><div class="cv-key-h">HOW TO READ THE SIGNALS</div>
    <div class="cv-key-row">{pill("GREEN","GREEN-LEANING")}<span>Official terms generally support it, under stated conditions</span></div>
    <div class="cv-key-row">{pill("AMBER","AMBER")}<span>Depends on conditions you must check</span></div>
    <div class="cv-key-row">{pill("RED","RED")}<span>Prohibited or high concern — stop</span></div>
    <div class="cv-key-row">{pill("VERIFY","VERIFY")}<span>Not yet checked against official text</span></div>
    <div class="cv-key-note">First-pass signals, not permission. Always confirm the current official terms.</div></div>
  <div class="cv-inside"><div class="cv-inside-h">WHAT’S INSIDE</div><ul>{inside}</ul></div>
  <div class="cv-legal">{legal}</div>
</section>'''


def body_steps(p):
    style = p.get("style", "numbered")
    items = []
    for i, s in enumerate(p.get("steps", [])):
        key = chr(65 + i) if style == "letters" else f"{i + 1}"
        items.append(f'<div class="st"><div class="st-n"><span>{key}</span></div><div class="st-b">'
                     f'<div class="st-t">{E(s.get("title"))}</div>'
                     + (f'<div class="st-x">{E(s.get("text"))}</div>' if s.get("text") else "") + '</div></div>')
    cls = "flow" if style == "flow" else "stack"
    cls += " many" if len(items) > 6 else ""
    return f'<div class="steps {cls}">{"".join(items)}</div>{legend(p.get("legend"))}{callout(p.get("callout"))}'


def body_cards(p):
    out = []
    for c in p.get("cards", []):
        head = f'<div class="cd-label">{E(c.get("label"))}</div>' if c.get("label") else ""
        sig = f'<div class="cd-sig">{pill(c["signal"], c.get("signal_label"))}</div>' if c.get("signal") else ""
        title = f'<div class="cd-title">{E(c.get("title"))}</div>' if c.get("title") else ""
        src = f'<div class="cd-src"><b>SOURCE</b> {E(c.get("source"))}</div>' if c.get("source") else ""
        note = f'<div class="cd-note">{E(c.get("note"))}</div>' if c.get("note") else ""
        out.append(f'<div class="card">{head}<div class="cd-body">{title}{sig}<div class="cd-text">{E(c.get("text"))}</div>{src}{note}</div></div>')
    bullets = "".join(f"<li>{E(b)}</li>" for b in p.get("bullets", []))
    bl = f'<ul class="bul">{bullets}</ul>' if bullets else ""
    n = len(p.get("cards", []))
    return f'<div class="cards n{n}">{"".join(out)}</div>{bl}{legend(p.get("legend"))}{callout(p.get("callout"))}'


def cell(v):
    if isinstance(v, dict):
        return pill(v.get("signal"), v.get("label"))
    return E(v)


def body_table(p):
    head = "".join(f"<th>{E(c)}</th>" for c in p.get("columns", []))
    rows = "".join("<tr>" + "".join(f"<td>{cell(v)}</td>" for v in r) + "</tr>" for r in p.get("rows", []))
    note = f'<p class="tnote">{E(p.get("note"))}</p>' if p.get("note") else ""
    return f'<table class="tbl"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>{note}{legend(p.get("legend"))}{callout(p.get("callout"))}'


def body_scenarios(p):
    out = []
    single = len(p.get("items", [])) == 1
    for s in p.get("items", []):
        cls = SIG.get((s.get("signal") or "VERIFY").upper(), SIG["VERIFY"])[0]
        sit = f'<p class="sc-sit"><b>THE SITUATION.</b> {E(s.get("situation"))}</p>' if s.get("situation") else ""
        why = f'<p class="sc-why"><b>WHY</b> {E(s.get("why"))}</p>' if s.get("why") else ""
        checks = "".join(f'<li><span class="box"></span>{E(c)}</li>' for c in s.get("checks", []))
        watch = "".join(f"<li>{E(w)}</li>" for w in s.get("watch", []))
        steps = "".join(f'<li><span class="nn">{i + 1}</span><span>{E(t)}</span></li>' for i, t in enumerate(s.get("steps", [])))
        cols = []
        if checks:
            cols.append(f'<div class="sc-col"><div class="sc-h">WHAT TO CHECK</div><ul class="chk">{checks}</ul></div>')
        if watch:
            cols.append(f'<div class="sc-col"><div class="sc-h">WATCH OUT FOR</div><ul class="watch">{watch}</ul></div>')
        grid = f'<div class="sc-grid c{len(cols)}">{"".join(cols)}</div>' if cols else ""
        stp = f'<div class="sc-steps"><div class="sc-h">BEFORE YOU PUBLISH</div><ol class="bsteps">{steps}</ol></div>' if steps else ""
        chg = f'<div class="sc-change"><b>WHAT COULD CHANGE THIS</b> {E(s.get("change"))}</div>' if s.get("change") else ""
        out.append(f'''<div class="scn {cls}">
  <div class="sc-head">{dot(s.get("signal"))}<div class="sc-title">{E(p.get("tag") if single and s.get("title") == p.get("title") else s.get("title"))}</div>{pill(s.get("signal"), s.get("signal_label"))}</div>
  <div class="sc-body">{sit}{why}{grid}{stp}{chg}</div></div>''')
    return f'<div class="scns n{len(out)}">{"".join(out)}</div>'


def body_snapshot(p):
    st = p.get("status") or {}
    rows = "".join(f'<tr><th>{E(k)}</th><td>{E(v)}</td></tr>' for k, v in p.get("rows", []))
    return f'<div class="snap-status">{pill(st.get("signal"), st.get("label"))}</div><table class="snap">{rows}</table>{callout(p.get("callout"))}'


def body_list(p):
    style = p.get("style", "checklist")
    items = p.get("items", [])
    if style == "checklist":
        li = "".join(f'<li><span class="box"></span><span>{E(i)}</span></li>' for i in items)
        body = f'<ul class="checklist">{li}</ul>'
    elif style == "redflags":
        li = "".join(f'<li><span class="flag">✕</span><span>{E(i)}</span></li>' for i in items)
        body = f'<ul class="redflags">{li}</ul>'
    else:
        li = "".join(f'<div class="tile"><span class="flag">!</span>{E(i)}</div>' for i in items)
        body = f'<div class="tiles">{li}</div>'
    return body + legend(p.get("legend")) + callout(p.get("callout"))


def body_worksheet(p):
    if p.get("layout") == "table":
        cols = p.get("columns", [])
        head = "".join(f"<th>{E(c)}</th>" for c in cols)
        rows = "".join("<tr>" + "<td></td>" * len(cols) + "</tr>" for _ in range(int(p.get("rows", 10))))
        return f'<table class="ws-tbl"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'
    f = "".join(f'<div class="ws-f"><div class="ws-l">{E(x)}</div><div class="ws-line"></div></div>' for x in p.get("fields", []))
    nf = len(p.get("fields", []))
    return f'<div class="ws-fields n{nf}{" two" if nf > 8 else ""}">{f}</div>'


def body_hierarchy(p):
    lv = p.get("levels", [])
    out = []
    for i, l in enumerate(lv):
        cls = SIG.get((l.get("signal") or "AMBER").upper(), SIG["AMBER"])[0]
        out.append(f'<div class="hl {cls}" style="margin-left:{i * 5}mm"><div class="hl-lab">{E(l.get("label"))}</div><div class="hl-t">{E(l.get("text"))}</div></div>')
    return f'<div class="hier-cap top">▲ CLEARER RIGHTS</div><div class="hier"><div class="hier-axis"></div><div class="hier-list">{"".join(out)}</div></div><div class="hier-cap">▼ HIGHER FRICTION</div>{callout(p.get("callout"))}'


def body_sources(p):
    s = "".join(f'<div class="src"><div class="src-n">{E(x.get("name"))}</div><div class="src-u">{E(x.get("url"))}</div>'
                f'<div class="src-d">{E(x.get("date"))}' + (f' · {E(x.get("note"))}' if x.get("note") else "") + '</div></div>'
                for x in p.get("sources", []))
    notes = "".join(f"<p class='src-note'>{E(n)}</p>" for n in p.get("notes", []))
    c = p.get("closing")
    cl = f'<div class="closing"><div class="cl-label">{E(c.get("label"))}</div><div>{E(c.get("text"))}</div></div>' if c else ""
    return f'<div class="srcs">{s}</div>{notes}{cl}'


BODY = {"steps": body_steps, "cards": body_cards, "table": body_table, "scenarios": body_scenarios,
        "snapshot": body_snapshot, "list": body_list, "worksheet": body_worksheet,
        "hierarchy": body_hierarchy, "sources": body_sources}


def page(p, meta, n, total):
    if p["type"] == "cover":
        return p_cover(p, meta)
    lead = f'<p class="lead">{E(p.get("lead"))}</p>' if p.get("lead") else ""
    red = " redtop" if p.get("style") == "redflags" else ""
    return f'''<section class="page t-{p["type"]}{red}" data-n="{n}">
  <header><span class="kick">{E(p.get("kicker"))}</span><span class="tag">{E(p.get("tag"))}</span></header>
  <div class="content"><h1>{E(p.get("title"))}</h1>{lead}<div class="main">{BODY[p["type"]](p)}</div></div>
  <footer><span>{E(meta.get("footer"))}</span><span>{n:02d} / {total:02d}</span></footer>
</section>'''


def main(src, css, out):
    d = json.load(open(src))
    meta, pages = d["meta"], d["pages"]
    body = "\n".join(page(p, meta, i + 1, len(pages)) for i, p in enumerate(pages))
    open(out, "w").write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{E(meta.get("product"))}</title>'
                         f'<style>{open(css).read()}</style></head><body>{body}</body></html>')


if __name__ == "__main__":
    main(*sys.argv[1:4])
