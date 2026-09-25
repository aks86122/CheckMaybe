# CheckMaybe toolkit content schema (JSON)

One JSON file per product. UTF-8. All product copy in English. Use straight or curly quotes consistently (curly preferred: ’ “ ”).
The renderer lays out each page on A4 with body text ≥ 11pt, so KEEP TEXT TIGHT: prefer short sentences, and respect the length limits below. Do not invent facts: every word must come from the revision script's "改成 (New)" text, or from the original text where the page/block is unchanged. You may shorten wording only where a limit forces it, without changing meaning, qualifiers or citations.

```json
{
  "meta": {
    "product": "Can I Sell This?",
    "subtitle": "A Commercial Use Toolkit for Canva Sellers",
    "footer": "CAN I SELL THIS? — COMMERCIAL USE TOOLKIT FOR CANVA SELLERS · CHECKMAYBE",
    "version": "3.1"
  },
  "pages": [ PAGE, PAGE, ... ]
}
```

Every PAGE has: `"type"`, `"kicker"` (small top-left label, e.g. "02 · DECISION PATH"), `"tag"` (small top-right label, e.g. "DECISION PATH"), `"title"` (H1, ≤ 60 chars), optional `"lead"` (≤ 220 chars). Then type-specific fields:

## cover
```json
{"type":"cover","topline":"INDEPENDENT EDUCATIONAL RESOURCE — NOT AFFILIATED WITH CANVA",
 "title":"Can I Sell This?","subtitle":"...","value":"one-sentence value proposition (≤ 200 chars)",
 "quote":"optional short quote",
 "steps":["IDENTIFY","CLASSIFY","VERIFY","PUBLISH"],
 "inside":["DECISION PATH","QUICK MAPS","20 SCENARIOS","CHECKLIST + WORKSHEETS"],
 "legal":["VERSION 3.1 · CHECKMAYBE","EDUCATIONAL INFORMATION — NOT LEGAL ADVICE","CANVA IS A TRADEMARK OF ITS RESPECTIVE OWNER"]}
```

## steps  (how-to-use, frameworks, decision maps, audits)
```json
{"type":"steps","style":"flow|numbered|letters",
 "steps":[{"title":"≤ 40 chars","text":"≤ 160 chars"}],       // 3–8 steps
 "callout":{"label":"FAST RULE","text":"≤ 240 chars","tone":"dark|red|amber|green"},   // optional
 "legend":[{"signal":"GREEN|AMBER|RED|VERIFY","label":"GREEN-LEANING","text":"≤ 120 chars"}]  // optional (signal key)
}
```

## cards  (rule reference cards, "4 questions", disclaimers)
```json
{"type":"cards",
 "cards":[{"label":"CASE 04 · KNOW YOUR CONTENT","title":"optional ≤ 60","text":"≤ 420 chars",
           "signal":"optional GREEN|AMBER|RED|VERIFY","signal_label":"optional text shown in pill",
           "source":"optional, e.g. CLA §2; Licensing Explained",
           "note":"optional footer line ≤ 160, e.g. BEFORE PUBLISHING — ..."}],   // 1–4 cards per page
 "bullets":["optional list under the cards, each ≤ 160"],
 "callout":{...optional as above}}
```

## table
```json
{"type":"table","columns":["PRODUCT TYPE","FIRST-PASS SIGNAL","WHY"],
 "rows":[["Flattened PDF",{"signal":"AMBER","label":"CHECK PERMITTED USE"},"≤ 140 chars"]],   // a cell may be a string or a signal object
 "note":"optional ≤ 240"}
```

## scenarios  (exactly 1 or 2 per page, as in the revision script)
```json
{"type":"scenarios",
 "items":[{"title":"Printable planner PDF","signal":"GREEN|AMBER|RED|VERIFY","signal_label":"GREEN-LEANING",
           "situation":"optional ≤ 200",
           "why":"≤ 220","checks":["≤ 70 each, 3–6 items"],
           "watch":["optional, ≤ 160 each, ≤ 3"],
           "steps":["optional BEFORE YOU PUBLISH, ≤ 160 each, ≤ 3"],
           "change":"What could change this: ≤ 160"}]}
```

## snapshot  (AI tool terms snapshots)
```json
{"type":"snapshot","status":{"signal":"GREEN|AMBER|RED|VERIFY","label":"SOURCE-CHECKED"},
 "rows":[["PRODUCT","≤ 200"],["PLAN DIFFERENCES","..."],["COMMERCIAL-USE LANGUAGE","..."],["OUTPUT-RIGHTS LANGUAGE","..."],["RESTRICTIONS","..."],["THIRD-PARTY RIGHTS WARNING","..."],["OFFICIAL SOURCE","..."],["STATUS","..."]]}   // each value ≤ 420 chars
```

## list  (checklists, red flags, stop lists)
```json
{"type":"list","style":"checklist|redflags|grid",
 "items":["≤ 150 each"],      // up to 16
 "callout":{...optional}}
```

## worksheet
```json
{"type":"worksheet","layout":"table|fields",
 "columns":["ASSET","SOURCE","LICENSE / LABEL","DATE CHECKED","ACTION"],   // for table
 "rows":10,                                                                 // blank rows for table
 "fields":["PRODUCT NAME","WHAT THE BUYER RECEIVES"]}                       // for fields
```

## hierarchy
```json
{"type":"hierarchy","levels":[{"label":"LOWER FRICTION","signal":"GREEN|AMBER|RED","text":"≤ 140"}],
 "callout":{...optional}}
```

## sources
```json
{"type":"sources","sources":[{"name":"Canva Content License Agreement (binding)","url":"https://…","date":"Verified 25 September 2026","note":"optional ≤ 120"}],
 "notes":["optional small lines ≤ 200"],
 "closing":{"label":"VERSION 3.1 · CHECKMAYBE","text":"≤ 300"}}
```

Signals: GREEN = GREEN-LEANING (generally permitted / lower concern), AMBER = check conditions, RED = stop / high concern / not allowed, VERIFY = not verified against official text this round. Always give a text label (signal_label) — colour never carries meaning alone.
