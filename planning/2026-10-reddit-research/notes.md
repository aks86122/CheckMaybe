# Reddit research: Canva, AI labels, print, UGC (2026-10-24)

Source: threads the founder pasted (Reddit is blocked from this environment, so nothing here was re-checked on Reddit). Everything below is what commenters said about themselves, not verified facts. Analysis first drafted in ChatGPT, reviewed here.

| ID | Thread | What people actually asked for | Paying signal | Tool idea |
| --- | --- | --- | --- | --- |
| CM-RD-001 | "WTF happened to Canva" | AI assets crowding search; Instagram "AI info" label after Canva Magic edits; want to leave Canva | none | Creator Asset Audit (what in the file could make a platform label it AI) |
| CM-RD-002 | "Why does my company insist on Canva" | non-designers edit files; wrong fonts/old logos; print files without bleed | indirect (teams, print shops lose time) | Brand consistency / print preflight |
| CM-RD-003 | "Best Canva alternative, no AI, premium too expensive" | free, no generative AI; one user already cancelled Pro | negative (wants free) | Alternative finder: free content only |
| CM-RD-004 | "DO NOT PRINT FROM CANVA" | lost parcels, crooked cuts, colour off, thin paper; others had good orders/refunds | none for a file tool; most problems happen after the file | Print-ready file check (only the file part) |
| CM-RD-005 | UGC creator recruitment (app, pay per view, "up to $2,000") | creators want work; one agency asked thresholds/payment terms | none for a tool | UGC deal calculator: watch only |

## Checked facts (2026-10-24)
- Meta says it reads C2PA and IPTC metadata to apply "AI info"; it also uses other signals, so a file check can't predict the label. Reports say some Canva AI tools write C2PA metadata (secondary sources).
- `exifr` MIT; `contentauth/c2pa-js` (incl. `c2pa-web`, WebAssembly) MIT, active (repo merge June 2026).
- Can I Use This? v1.1 has nothing on AI labels, C2PA or metadata. No listing may claim it solves AI labels until a page is added.

## Decision so far
- No hosted website: if built, a single HTML file sold/given as a download (desktop browsers; phones can't run downloaded HTML well).
- Best fit for CheckMaybe's own buyers (Etsy/digital sellers): a preflight for printable PDFs (page size Letter/A4, image resolution, file size), not a general print or brand tool.
- No build before the Black Friday work is done. Paying demand not shown in any thread.
- No promotional replies on these threads.

## Etsy AI/photo policy update (announced 2026-10-22)
Etsy's own pages return 403 to automated reads; the points below agree across Value Added Resource, Inkfluence and EcomCrew. Founder should open the Seller Handbook article once to confirm.
- Most listings need one unedited photo of the actual item on a real background; exceptions include some print-on-demand, digital downloads and made-to-order.
- Digital downloads with visual content: show a preview or excerpt of what buyers get.
- AI-made items still allowed with disclosure and a clear creative role; AI-generated functional instructions (patterns, recipes, manuals, "guides intended to help buyers complete a specific task") are banned.
- New "misleading AI images" report option: no immediate enforcement at first. No deadline announced for old listings.

### CheckMaybe's own Etsy listings (checked 2026-10-24)
Founder 2026-10-24: CheckMaybe does not sell on Etsy (Gumroad and Beacons only). The listing-etsy.md files are drafts for a possible later shop; the edits below only matter if that ever happens.
- Images for the 3 spreadsheet products are real sheet renders of the example rows: preview rule met.
- AI disclosure ("How this was made") was only in Hidden Cost Tracker; added to Holiday Hidden Cost Tracker and Debt Payoff Planner.
- PDF guides (Can I Sell/Use/Resell This?) are not planned for Etsy. If ever listed there, check the "guides to complete a task" ban first.
- Holiday image 10 tab list updated with Deal Check.

### Product read
Policy is 2 days old and affects digital sellers, CheckMaybe's buyers. Cheapest first move is content, not a tool: an "Etsy's new AI rules for digital sellers" page in Can I Use This? (v1.2), plus pins and a Substack post (volume plan topic 9). Tool (listing preflight) only if that content gets clicks.

### Tested 2026-10-24: Etsy strips listing images
Etsy re-encodes listing photos (1140 px) and keeps only an ICC profile: no camera data, AI markers or Content Credentials survive. Buyer-side value is a checklist plus asking the seller for originals, not file analysis of listing images.
