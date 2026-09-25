# CheckMaybe 06：「Can I Sell This?」v3.0 → v3.1 逐頁修改腳本

- **依據**：`04-canva-toolkit-verification.md`（事實查核），以及 2026-09-25 儲存的官方快照：CLA（Content License Agreement）、LE（Licensing Explained）、ToU（Terms of Use，2026-08-19 生效）、Etsy CS（Creativity Standards，2025-06-10 更新）。
- **性質**：產品文案修改稿。這是教育型工具包，不是法律意見。本文沒有 commit，也沒有發佈。
- **使用方式**：「原文」是 v3.0 PDF 文字擷取的內容（`C H E C K` 這類字距是排版造成的，設計檔裡請直接找對應文字）。把「改成」的英文整段貼進設計檔即可。

---

## 摘要（繁體中文）

### 改了什麼、為什麼（10 點）

1. **品牌和名稱**：副標改成 "A Commercial Use Toolkit for Canva Sellers"，頁尾統一加上 "· CHECKMAYBE"，版本改為 3.1。產品名稱不再以「Canva」開頭，降低看起來像官方產品的風險（查核報告 #1：Canva 商標指引還沒取得，仍列為 ❓）。
2. **商標／Logo 改成和 LE 原文一致**（報告前 5 項第 1 項）：從 "generally cannot become an exclusive trademark" 改成 LE 的絕對說法。另外註明 CLA §9 的例外只有 fonts，兩份來源說法不同。Scenario 08 改為 RED。
3. **Education、Branded、Disney、Editorial Use Only 明確寫成不可商用**（第 2 項）：依據 CLA §5B–5D、§9。CLA §1 的 "may be governed" 改成 "applies to the entire design"。
4. **模板規則寫明確**（第 3 項）：含 Pro 的模板只能以 Canva template link 交付（LE；CLA §5）；其他格式只能放 Free（CLA §6）；字型不能帶出 Canva（CLA §9A）。
5. **PLR／MRR、數位貼紙、單獨販售素材改為 RED**（第 4 項）：依據 CLA §3、§9，以及 ToU §2e(i)、§14。
6. **CHECK／VERIFY 全部改成燈號**：GREEN-LEANING／AMBER／RED。每張卡片都有 "Why"（依據）和 "Could change this"（什麼情況下燈號會變），並在第 2 頁和情境頁標題寫明「first-pass signal, not permission」。
7. **空白的「Marketplace rules」勾選框**改成各情境具體的檢查項目。Etsy 相關的寫 Etsy CS 規則；不在 Etsy 販售的情境（客戶案、自家社群貼文）則改成對應的實際檢查。
8. **補上數字和清單**（第 5 項）：480,000 像素上限（CLA §5A）、§9 的敏感廣告用途、Popular Music 不可商用（LE）、授權在 Export 時產生（CLA §4）。
9. **每張 Case 卡片**都把重複出現的 "BEFORE PUBLISHING…" 一行改成實際條號加查核日期（報告 3.3）。
10. **來源頁**：每個來源都標 "Verified 25 September 2026"，新增 ToU 和 Etsy CS，拿掉無法驗證的 /policies/ 索引網址（報告 #63）。

### 新增頁面（共 2 頁，全書從 27 頁變成 29 頁）

| 新頁 | 插入位置 | 內容 | 原因 |
| --- | --- | --- | --- |
| **NEW PAGE A — "Read the label before you design"** | 第 5 頁（Quick Map）**之後**、第 6 頁（Case 04–05）**之前** | 各種素材標示（Free／Pro／AI／CC0／Education／Branded／Disney／Editorial／Popular Music／Canva 圖庫模板）的燈號對照，以及授權在 Export 時產生 | LE 沒有涵蓋 Branded、Education、Disney，必須直接引用 CLA（報告 4.2、3.2） |
| **NEW PAGE B — "Etsy checks & what's at stake"** | 第 22 頁（Red Flags）**之後**、第 23 頁（W1 Tracker）**之前** | Etsy CS 的 5 項具體規則，以及違反 Canva 條款的後果（ToU §13–15、CLA §10） | 報告 3.5、3.2 第 5 點 |

> 如果版面真的放不下兩頁新頁：NEW PAGE A 優先保留（影響判斷正確性）；NEW PAGE B 的「What's at stake」可以縮成第 22 頁底部的一行字（備用文字寫在第 22 頁）。

### 編輯檢查清單

- [ ] **全部頁面**：頁尾換成新文字（見下方「全域修改」）
- [ ] 封面：副標、CheckMaybe 品牌、版本 3.1、功能標籤
- [ ] 第 2 頁：加入燈號說明（legend）
- [ ] 第 4 頁：決策路徑 A–E 重寫，紅旗框改成 B 或 E
- [ ] 第 5 頁：5 個 verdict 改成燈號，表頭改成 "FIRST-PASS SIGNAL"
- [ ] 第 6–10 頁：10 張 Case 卡片的內文和來源行
- [ ] 第 11–20 頁：20 張情境卡片（燈號標籤、內文、第 4 個勾選框、圖示）以及頁面副標
- [ ] 圖示對照：✓ = GREEN-LEANING；! = AMBER；✕ = RED（如果設計檔有顏色，建議用綠／黃／紅）
- [ ] 第 21、22、24、26、27 頁的文字
- [ ] 插入 NEW PAGE A（第 5 頁後）和 NEW PAGE B（第 22 頁後），然後**重新編頁碼**（原第 6–27 頁會往後移）
- [ ] 貼上前確認 ToU 和 Etsy CS 的網址（快照只存了內文，沒有網址，見第 27 頁說明）
- [ ] 如果這份 PDF 是用 Canva 做的：確認 CheckMaybe Logo 沒有使用圖庫圖像，而且未編輯的 Pro 圖片在 480,000 像素以內（報告 3.4）
- [ ] 匯出後把全文搜尋一次 "CHECK"、"VERIFY"、"3.0"、"THE CANVA COMMERCIAL"，確認沒有漏改的地方

---

## 全域修改（每一頁都要套用）

**原文 (Current):** CAN I SELL THIS? — CANVA COMMERCIAL USE TOOLKIT
**改成 (New):** CAN I SELL THIS? — COMMERCIAL USE TOOLKIT FOR CANVA SELLERS · CHECKMAYBE
**原因:** 創辦人決定；產品名稱不以 Canva 開頭（報告 #1，ToU §5b、§10 只間接相關，商標指引仍是 ❓），並和姊妹產品 "Can I Use This? … · CHECKMAYBE" 的格式一致。

**情境頁（第 11–20 頁）副標**
**原文 (Current):** Real-world seller scenarios
**改成 (New):** Real-world seller scenarios · first-pass signals, not permission
**原因:** 燈號只是初步判斷，不是授權保證（報告 3.1、第 5 節風險）。

> 下面各頁寫「不變」的，意思是**除了頁尾以外**都不用改。

---

## Page 1 — Cover

狀態：修改

**原文 (Current):** INDEPENDENT EDUCATIONAL RESOURCE — NOT AFFILIATED WITH CANVA
**改成 (New):** （不變）INDEPENDENT EDUCATIONAL RESOURCE — NOT AFFILIATED WITH CANVA
**原因:** 創辦人決定保留。

**新增品牌字（放在標題 "Can I Sell This?" 上方或下方的小字，位置比照姊妹產品）**
**改成 (New):** CHECKMAYBE
**原因:** 創辦人決定；和 "Can I Use This? … · CHECKMAYBE" 一致。

**原文 (Current):** The Canva Commercial Use Toolkit — a practical decision guide for digital product sellers, creators, and small businesses working out what they can actually publish.
**改成 (New):** A Commercial Use Toolkit for Canva Sellers — a practical first-pass decision guide for digital product sellers, creators, and small businesses working out what they can actually publish.
**原因:** 創辦人決定的新副標；加上 "first-pass"，和燈號的定位一致（報告 #1）。

**原文 (Current):** "Know what you used, know what you're selling, verify before you list it."
**改成 (New):** （不變）
**原因:** 流程正確（報告 #3）。

**原文 (Current):** DECISION PATH / QUICK MAPS / 20 SCENARIOS / CHECKLIST + WORKSHEETS
**改成 (New):** DECISION PATH / QUICK MAPS / 20 TRAFFIC-LIGHT SCENARIOS / ETSY CHECKS + WORKSHEETS
**原因:** 反映 v3.1 新增的燈號和 Etsy 檢查頁（報告 3.1、3.5）。

**原文 (Current):** VERSION 3.0 — EDUCATIONAL INFORMATION, NOT LEGAL ADVICE — CANVA IS A TRADEMARK OF ITS RESPECTIVE OWNER
**改成 (New):** VERSION 3.1 — SOURCES VERIFIED 25 SEPTEMBER 2026 — EDUCATIONAL INFORMATION, NOT LEGAL ADVICE — CANVA IS A TRADEMARK OF ITS RESPECTIVE OWNER
**原因:** 版本 3.1，並寫出確切查核日期（報告 #64）；商標聲明保留，不自行填入商標權人名稱（報告 #2）。

IDENTIFY / CLASSIFY / VERIFY / PUBLISH：不變（報告 #3 ✅）。

---

## Page 2 — Start here: How to use this toolkit

狀態：修改

**原文 (Current):** Use this as a decision aid, not as a substitute for the current official license terms.
**改成 (New):** Use this as a decision aid, not as a substitute for the current official license terms. Every verdict is a first-pass signal, never a guarantee: GREEN-LEANING = likely fits the license as described · AMBER = fix or confirm first · RED = stop or redesign.
**原因:** 燈號說明放在書的開頭；CLA §1 寫明 Canva 可隨時變更授權，ToU §16n 也寫明可隨時修改條款（報告 #4、3.1）。

**原文 (Current):** Identify the source and category of every asset.
**改成 (New):** Identify the source and label of every asset (open its source info via the ⋯ menu).
**原因:** CLA §2 的查看方式；ToU §4b（報告 #5、3.2 第 2 點）。

**原文 (Current):** Confirm whether the buyer receives a finished product, physical item, or editable/source file.
**改成 (New):** （不變）
**原因:** 報告 #7 ✅。

**原文 (Current):** Check standalone extractability, marketplace rules, and the most restrictive content category.
**改成 (New):** Check standalone extractability, the most restrictive content label, and your sales platform's own rules (e.g. Etsy).
**原因:** 「marketplace rules」改成具體指向 Etsy 等平台（報告 #65、3.5）。

**原文 (Current):** FAST RULE — A finished design and an editable template are not the same licensing problem.
**改成 (New):** （不變）
**原因:** 報告 #7 ✅（CLA §5、§6；LE「Selling templates」）。

---

## Page 3 — The 5-minute pre-publish audit

狀態：修改

**原文 (Current):** 1 What did I use?
**改成 (New):** 1 What did I use — and what label does each item carry?
**原因:** CLA §2 規定要從 source info 查看每個素材的標示（報告 #8）。

2、3、4：不變（報告 #8 ✅）。

**原文 (Current):** 5 Which rule is the most restrictive in this product?
**改成 (New):** 5 Which label is most restrictive — and which account and plan did I export from?
**原因:** 補上漏掉的「用哪個帳號／方案 Export」這一題（CLA §4、§8；報告 #8、3.2 第 1 點）。

---

## Page 4 — Decision path: Can I sell this?

狀態：修改（5 題重寫，紅旗框改寫）

> 文字擷取裡只有 E 有結論。如果原稿的 A–D 也有結論，請一併刪掉或改成下面的版本。

**原文 (Current):** A Does the design contain Canva library Content?
**改成 (New):** A Does the design contain Canva library Content (including a Canva template)?
**原因:** Canva 圖庫模板本身就是 Content（CLA §1、§3 "Pro Template"；報告 3.2 第 3 點）。

**原文 (Current):** B Is any Content Pro, Education, Branded, or specially labelled?
**改成 (New):** B Is any item labelled Education ("Resource"), Branded, Disney, or Editorial Use Only?
**原因:** Pro 可以商用，Education 和 Branded 不行，不能放在同一題（CLA §5B–5D、§9；報告 #9、前 5 項第 2 項）。

**原文 (Current):** C Is the buyer receiving a finished, non-editable output?
**改成 (New):** C Is any item Pro (crown icon on the thumbnail)?
**原因:** 把 Pro 獨立成一題（報告 #9；LE FAQ 說明皇冠圖示）。

**原文 (Current):** D Is the buyer receiving an editable template or source file?
**改成 (New):** D Will the buyer receive an editable template or source file?
**原因:** 維持原題，只改時態。「成品」這題由 D 的否定答案涵蓋。

**原文 (Current):** E Could the buyer extract Canva Content for standalone reuse?
**改成 (New):** E Could the buyer extract any Canva item as a standalone file?
**原因:** 用 CLA §9 的說法 "extract … as an electronic file"（報告 #10 ✅）。

**原文 (Current):** IF E = YES — RED FLAG
**改成 (New):** IF B OR E = YES — RED
**原因:** B 是 yes 代表不可商用（CLA §5B–5D、§9），和 E 一樣是紅燈（報告 #9、#10）。

**原文 (Current):** Treat a "yes" on E as a strong warning. Redesign the product or use assets for which you actually hold suitable redistribution rights.
**改成 (New):** B = not licensed for commercial use (CLA §5B–5D, §9). E = prohibited extraction (CLA §9). Redesign with assets you own or can redistribute. If C and D are both YES: Pro may ship only as a Canva template link (Licensing Explained).
**原因:** 把 Pro 模板的規則寫進決策路徑（LE「Selling templates」；CLA §5；報告前 5 項第 3 項）。

---

## Page 5 — Quick map: Finished products vs. editable products

狀態：修改

**原文 (Current):** FIRST-PASS VERDICT
**改成 (New):** FIRST-PASS SIGNAL (NOT PERMISSION)
**原因:** 燈號不是授權（報告 3.1）。

**原文 (Current):** Flattened PDF — CHECK PERMITTED PUBLICATION USE
**改成 (New):** Flattened PDF — GREEN-LEANING · UNEDITED PRO ≤ 480,000 PX
**原因:** CLA §5 允許電子出版；§5A 設有像素上限，LE 確認適用於 ebooks（報告 #11）。

**原文 (Current):** Printed merchandise — CHECK MERCHANDISE USE
**改成 (New):** Printed merchandise — GREEN-LEANING · A REAL DESIGN, NOT ONE ITEM
**原因:** LE FAQ："sell merchandise with your design on it"；CLA §9 禁止單獨素材做成 POD 商品（報告 #12）。

**原文 (Current):** Editable Canva template — CHECK TEMPLATE-SPECIFIC RIGHTS
**改成 (New):** Editable template — AMBER · PRO ONLY VIA A CANVA LINK
**原因:** LE："Unless it's a template created for use on Canva, you can't use Pro content in templates of any nature"；CLA §5、§6（報告 #13）。

**原文 (Current):** Client design — CHECK CLIENT-TRANSFER RULES
**改成 (New):** Client design — GREEN-LEANING · ONE CLIENT, WRITTEN TERMS
**原因:** CLA §4A 的條件（報告 #14）。

**原文 (Current):** Standalone asset resale — DO NOT PROCEED WITHOUT RIGHTS
**改成 (New):** Standalone asset resale — RED · NOT PERMITTED FOR CANVA CONTENT
**原因:** CLA §3、§9；LE "Don't resell, redistribute"；ToU §2e(i)（報告 #15）。

**新增表格下方一行小字（放得下再加）**
**改成 (New):** Flattening alone does not stop extraction (CLA §9). Pro in a PPTX, PSD or other non-Canva template = RED (Licensing Explained). CC0/Pixabay/Pexels items: check their own license.
**原因:** 報告 #11、#13、#15。

---

## NEW PAGE A — Read the label before you design

狀態：新增（插在第 5 頁之後、第 6 頁之前；版型建議沿用第 5 頁的兩欄表格）

**Section tag:** 03B LABELS
**Title:** Read the label before you design
**Intro:** Hover over an item, click the three dots (⋯) and read its source information. If a design mixes labels, the most restrictive one applies to the entire design (CLA §1): Education → Branded → Pro → Free.

**Table header:** LABEL — FIRST-PASS SIGNAL FOR SELLING

- **Free** — GREEN-LEANING · Extra template and resale-template rights (CLA §6), lost if the design contains any Pro.
- **Pro (crown icon)** — GREEN-LEANING in finished designs · Templates: Canva link only · Never standalone (CLA §3; Licensing Explained).
- **AI-generated** — Follows its Free or Pro label (CLA §3A).
- **CC0 / Public Domain / Pixabay / Pexels** — Check that item's own license (CLA §2, §9).
- **Education ("Resource" badge)** — RED · Non-commercial use only (CLA §5C).
- **Branded** — RED · Personal use only unless its source info says otherwise (CLA §5B).
- **Disney** — RED · Personal or educational use only (CLA §5D).
- **Editorial Use Only** — RED · No commercial, promotional or merchandising use (CLA §9).
- **Popular Music** — RED · "Can't be used for any commercial purposes" (Licensing Explained).
- **Canva library template** — AMBER · It is Content itself: a lightly edited copy is not your template to resell (CLA §1, §3).

**Footnote box — WHEN THE LICENSE STARTS:** A license is issued when you Export. One Pro license covers one design; a new or Magic Resized design needs a new one (CLA §4). Pro plans get these automatically; free users pay per item. Attribution: Licensing Explained says none is required, but CLA §9 requires "[Contributor's Name] via Canva.com" for editorial use. The sources differ, so credit editorial uses.

**原因:** CLA §1–§5D、§9；LE（Pro 皇冠圖示、Popular Music、attribution）。LE 沒有涵蓋 Branded、Education、Disney，所以要直接引用 CLA。Attribution 依兩份來源中較嚴格的說法處理，並註明兩者不同（報告 3.2 第 1–3 點、4.2、前 5 項第 2 項）。

---

## Page 6 — Guide: Case 04–05

狀態：修改

**原文 (Current):** CASE 04 / KNOW YOUR CONTENT — Canva content can carry different rules. A design that mixes categories may be governed by the most restrictive category.
**改成 (New):** CASE 04 / KNOW YOUR CONTENT — Each Canva item carries a label with its own rules. Under CLA §1, the most restrictive category applies to the entire design. From most to least restrictive: Education, Branded, Pro, Free.
**原因:** CLA §1 寫的是 "applies to the entire design"，不是 "may be"（報告 #16）。

**原文 (Current):** BEFORE PUBLISHING — Open the Content source information · Verify the current Canva Content License Agreement · Record the verification date
**改成 (New):** SOURCE — CLA §1, §2 · Verified 25 Sep 2026 · Re-check before you publish
**原因:** 每張卡片寫出條號和查核日期（報告 3.3、#64）。

**原文 (Current):** CASE 05 / FREE VS. PRO — Free Content has additional permissions that Pro Content does not automatically share. Free Content may be used in templates for distribution/sale under Section 6; do not assume Section 6 template rights apply to Pro Content, whose standalone redistribution is prohibited.
**改成 (New):** CASE 05 / FREE VS. PRO — Free Content has extra rights under CLA §6, including templates for distribution or sale. If a design contains any Pro Content, those §6 rights do not apply to that design. Pro Content may never be copied or distributed as a standalone item (CLA §3).
**原因:** 刪掉 "automatically"（容易讓人以為有別的方法可以取得），並寫明是以整個設計為單位（CLA §6 "If your Canva Design contains any Pro Content, you can't use it for these purposes"；報告 #17）。

**原文 (Current):** BEFORE PUBLISHING — …（同上）
**改成 (New):** SOURCE — CLA §3, §6 · Verified 25 Sep 2026 · Re-check before you publish
**原因:** 同上（報告 3.3）。

---

## Page 7 — Guide: Case 06–07

狀態：修改

**原文 (Current):** CASE 06 / FINISHED VS. EDITABLE — A flattened PDF, image, printed item, and editable Canva template are different licensing situations. EDITABLE means the buyer can modify the source design; FINISHED means the buyer primarily receives the final output.
**改成 (New):** CASE 06 / FINISHED VS. EDITABLE — A flattened PDF, image, printed item and editable template are different licensing situations. Canva defines a template as "a design that has a pre-determined layout and style and is intended to be further edited or customised by another person" (Licensing Explained). FINISHED means the buyer receives the final output.
**原因:** 直接採用 LE 對 template 的定義（報告 #18）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §5, §6 · Licensing Explained · Verified 25 Sep 2026
**原因:** 報告 3.3。

**原文 (Current):** CASE 07 / TEMPLATE RULES — Canva's current license gives Free Content additional template rights, while designs containing Pro Content cannot rely on those additional Free Content permissions.
**改成 (New):** CASE 07 / TEMPLATE RULES — Pro Content may appear only in templates made for use on Canva (CLA §5; Licensing Explained). Templates in any other format (PPTX, PSD, etc.) may contain Free Content only (CLA §6). Canva fonts cannot be used outside Canva (CLA §9A).
**原因:** LE："Unless it's a template created for use on Canva, you can't use Pro content in templates of any nature"（報告前 5 項第 3 項、#13）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §5, §6, §9A · Licensing Explained · Verified 25 Sep 2026
**原因:** 報告 3.3。

---

## Page 8 — Guide: Case 08–09

狀態：修改

**原文 (Current):** CASE 08 / MERCHANDISE & POD — Canva permits many commercial merchandise uses when content is incorporated into a design, but standalone content cannot simply be resold on merchandise.
**改成 (New):** CASE 08 / MERCHANDISE & POD — Designs printed on t-shirts, mugs, books and other merchandise for sale are permitted (Licensing Explained FAQ). A Canva item used on its own, "without any other design elements", cannot be sold on print-on-demand products (CLA §9).
**原因:** 引用 LE FAQ 原文和 LE 對 standalone 的定義（報告 #20）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §5, §9 · Licensing Explained FAQ · Verified 25 Sep 2026
**原因:** 報告 3.3。

**原文 (Current):** CASE 09 / EBOOKS & PDFS — Books, ebooks, and electronic publications are recognized permitted uses, subject to content-specific restrictions and Pro Content limits.
**改成 (New):** CASE 09 / EBOOKS & PDFS — Books, ebooks and electronic publications are permitted uses (CLA §5). In digital publications, each unedited Pro media file is capped at 480,000 total pixels, e.g. 600 × 800 px (CLA §5A). Printed books have no pixel cap.
**原因:** 寫出 §5A 的數字（報告 #21、前 5 項第 5 項）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §5, §5A · Verified 25 Sep 2026 · Re-check before you publish
**原因:** 報告 3.3。

---

## Page 9 — Guide: Case 10–11

狀態：修改

**原文 (Current):** CASE 10 / CLIENT WORK — A Canva design containing Content can be transferred to one client under specific conditions. Keep written terms, transfer the Design, and do not sublicense standalone Canva Content.
**改成 (New):** CASE 10 / CLIENT WORK — You may transfer a design containing Free or Pro Content to a single client, under a written agreement limiting use to that client. You remain solely responsible for their compliance. Never hand over standalone Canva Content (CLA §4A).
**原因:** 補上 CLA §4A 的三個條件，包括 "solely responsible and liable"（報告 #14、#22）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §4A · Verified 25 Sep 2026 · Re-check before you publish
**原因:** 報告 3.3。

**原文 (Current):** CASE 11 / LOGOS & TRADEMARKS — Canva explains that library content generally cannot become an exclusive trademark, except for limited elements such as fonts, simple shapes, and lines.
**改成 (New):** CASE 11 / LOGOS & TRADEMARKS — Licensing Explained says you "cannot use any Free or Pro content from Canva's library in a trademark (except for fonts, simple shapes and lines)". The binding CLA §9 excludes only fonts. The sources differ, so the safest logo uses Canva fonts plus graphics you made or commissioned.
**原因:** 前 5 項第 1 項（最高優先）：拿掉 "generally" 和 "exclusive"，改用 LE 原文；CLA §9 只寫 "(excluding fonts)"，採用較嚴格的說法，並註明兩份來源不同（報告 #23、#24、4.2）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §9 · Licensing Explained · Verified 25 Sep 2026
**原因:** 報告 3.3。

---

## Page 10 — Guide: Case 12–13

狀態：修改

**原文 (Current):** CASE 12 / EDUCATION & SPECIAL CONTENT — Education Content and other specially labelled content can have tighter rules. Commercial sellers should verify the source information for each asset.
**改成 (New):** CASE 12 / EDUCATION, BRANDED & SPECIAL LABELS — Education ("Resource" badge): non-commercial only (§5C). Branded: personal use only unless its source info says otherwise (§5B). Disney: no commercial use (§5D). Editorial Use Only: no commercial use (§9). Pro used on an Education account is non-commercial (§8).
**原因:** 前 5 項第 2 項：原文嚴重低估，這些素材是明文不可商用（CLA §5B–5D、§8、§9；報告 #25）。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §1, §5B–5D, §8, §9 · Verified 25 Sep 2026. For commercial work, CLA §8 says use a separate account; Licensing Explained says a second team. The sources differ.
**原因:** Education 帳號的處理方式，CLA 和 LE 說法不同，兩者都列出（報告 4.2）。

**原文 (Current):** CASE 13 / AI-GENERATED CONTENT — Canva-generated AI Content is labelled as Free or Pro Content and follows the applicable category rules, together with Canva's AI-related terms.
**改成 (New):** CASE 13 / AI-GENERATED CONTENT — Canva's library AI Content is marked Free or Pro and follows that label's rules (CLA §3A). Output from Canva's AI tools is covered by separate AI Product Terms (Terms of Use §6); read them before selling. No Content may be used for AI or machine-learning purposes (CLA §9).
**原因:** 報告 #26 ✅、#27 ❓：寫明 AI Product Terms 是另一份文件（內容未取得，所以不轉述內容），並補上 CLA §9 和 ToU §2e(viii) 的 AI／ML 禁止規定。

**原文 (Current):** BEFORE PUBLISHING — …
**改成 (New):** SOURCE — CLA §3A, §9 · Terms of Use §6 · Verified 25 Sep 2026. Selling on Etsy? Disclose AI use (see Etsy page).
**原因:** Etsy CS 要求 AI 製作的商品揭露（報告 #27、3.5 第 3 點）。

---

## Page 11 — Scenarios 01–02

狀態：修改（副標見「全域修改」）

**Scenario 01 — Printable planner PDF**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Finished publication. Verify each embedded asset and keep the final deliverable non-extractive where practical.
**改成 (New):** Why: a finished PDF is a permitted electronic publication (CLA §5). Could change this: AMBER if unedited Pro images exceed 480,000 px or can be pulled out as files (§5A, §9). RED with any Education, Branded or Disney item, or a page that is just one library image.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: my original design, not a PDF of others' work
**原因:** §9 是禁止條款，不是 "where practical"（報告 #28、3.1）；Etsy CS 規定 "A bundle, collection, scan, or PDF of someone else's work" 不符合資格。

**Scenario 02 — Editable planner template**（圖示 !）

**原文 (Current):** V E R I F Y
**改成 (New):** AMBER
**原文 (Current):** Template rights are different from finished-product rights. Check whether any Pro or specially restricted Content is present.
**改成 (New):** Why: template rights depend on format and labels (CLA §5, §6; Licensing Explained). Could change this: GREEN-LEANING if delivered only as a Canva template link. RED if it contains Pro and ships in another format, or if it is a resold Canva library template.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: my own layout, not an edited Canva template
**原因:** 報告 #29、3.1；Canva 圖庫模板本身就是 Content（CLA §1、§3）；Etsy CS 要求 "original designs"。

---

## Page 12 — Scenarios 03–04

狀態：修改

**Scenario 03 — T-shirt design**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Merchandise can be permitted when content is part of a genuine design, not a disguised resale of standalone Content.
**改成 (New):** Why: merchandise with your design on it is permitted (Licensing Explained FAQ). Could change this: RED if the shirt is one Canva item with no other design elements (CLA §9), or uses Branded or Disney Content. AMBER if it shows real people, brands or artworks (no releases, CLA §12).
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: disclose production partner + ship-from location
**原因:** 報告 #30、3.1；Etsy CS："Sellers must disclose that an item is made by a production partner"。

**Scenario 04 — Mug design**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Same principle as merchandise: create a distinct design and avoid standalone-content resale.
**改成 (New):** Why: same as T-shirts, a genuine design on a product is permitted (Licensing Explained FAQ). Could change this: RED if a single library item is simply placed on the mug (CLA §9) or it uses Branded or Disney Content (§5B, §5D).
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: disclose production partner + ship-from location
**原因:** 報告 #31、3.1、3.5 第 2 點。

---

## Page 13 — Scenarios 05–06

狀態：修改

**Scenario 05 — Ebook cover**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Book covers are a recognized use. Trademark/exclusivity concerns are separate if the design is intended as a brand identifier.
**改成 (New):** Why: books and book covers are permitted uses (CLA §5). Could change this: AMBER if you sell premade covers to authors (one design per client with written terms, CLA §4A, or a Canva template link). RED if the cover art becomes an author or series logo (CLA §9).
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: premade covers are my original designs
**原因:** 報告 #32、3.1。

**Scenario 06 — Ebook interior**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Electronic publication use is recognized, but Pro Content can carry additional online/electronic restrictions.
**改成 (New):** Why: ebooks are permitted electronic publications (CLA §5). Could change this: AMBER if an unedited Pro image exceeds 480,000 total pixels per file, e.g. 600 × 800 px (§5A). RED if images can be extracted as reusable files (§9).
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: the book is my own work, not someone else's PDF
**原因:** 報告 #33、3.1；Etsy CS 舉例 "A PDF file of a book that the seller did not personally create or design" 不符合資格。

---

## Page 14 — Scenarios 07–08

狀態：修改

**Scenario 07 — Client Instagram pack**（圖示 改成 ✓）

**原文 (Current):** V E R I F Y
**改成 (New):** GREEN-LEANING
**原文 (Current):** Client-transfer rules apply. Use written terms and transfer the design, not standalone Canva Content.
**改成 (New):** Why: CLA §4A lets you transfer a design to one client under a written agreement, with you responsible for their compliance. Could change this: RED if the same pack goes to more than one client (that makes it a template) or you hand over standalone Content.
**原文 (Current):** Marketplace rules
**改成 (New):** Written client agreement signed
**原因:** 報告 #34、3.1。這不是平台販售情境，所以勾選框改成 §4A 要求的書面協議。

**Scenario 08 — Logo for a client**（圖示 改成 ✕）

**原文 (Current):** H I G H  C A U T I O N
**改成 (New):** RED
**原文 (Current):** Do not promise exclusive trademark rights in Canva library content.
**改成 (New):** Why: no Free or Pro library content may be used in a trademark (Licensing Explained; CLA §9). Could change this: GREEN-LEANING only with Canva fonts plus your own or commissioned graphics. Simple shapes and lines: allowed by Licensing Explained, not CLA §9. Never promise exclusivity.
**原文 (Current):** Marketplace rules
**改成 (New):** Only fonts + own graphics used
**原因:** 前 5 項第 1 項：使用圖庫圖像做的 Logo 應為 RED；CLA 和 LE 說法不同，採用較嚴格的說法並註明（報告 #35、4.2）。

---

## Page 15 — Scenarios 09–10

狀態：修改

**Scenario 09 — Canva template with Free Content**（圖示 ✓）

**原文 (Current):** P O T E N T I A L L Y  V I A B L E
**改成 (New):** GREEN-LEANING
**原文 (Current):** Free Content has additional template distribution permissions, subject to the full current license.
**改成 (New):** Why: CLA §6 lets Free Content be used in templates for sale; a Canva template link is the cleanest delivery. Could change this: AMBER in other formats (files may be extractable, §9; fonts can't leave Canva, §9A). RED if any item is really Pro, Branded or Education.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: my own original template design
**原因:** 介面上顯示 Free 的素材仍可能是 Branded 或 Education，要逐項確認（CLA §2；報告 #36、3.1）。

**Scenario 10 — Canva template with Pro Content**（圖示 !）

**原文 (Current):** V E R I F Y
**改成 (New):** AMBER
**原文 (Current):** Do not rely on Free Content's additional template permissions when the design contains Pro Content.
**改成 (New):** Why: Pro may appear only in templates made for use on Canva (Licensing Explained; CLA §5). Could change this: RED in any non-Canva format (PPTX, PSD, editable PDF). With a Canva link, tell buyers: "Pro elements show a watermark on free plans; buyers need Canva Pro or a one-off license."
**原文 (Current):** Marketplace rules
**改成 (New):** Listing says Pro elements need Canva Pro
**原因:** 報告 #37、前 5 項第 3 項；LE 說明免費用戶看到 Pro 素材會有浮水印。

---

## Page 16 — Scenarios 11–12

狀態：修改

**Scenario 11 — Standalone stock photo printable**（圖示 改成 ✕）

**原文 (Current):** D O  N O T  P R O C E E D
**改成 (New):** RED
**原文 (Current):** Standalone Canva Content cannot simply be resold as the product.
**改成 (New):** Why: selling a Canva item on its own is prohibited (CLA §3, §9; Licensing Explained "Don't resell, redistribute"). Could change this: only if the item is CC0, Pixabay or Pexels and its own license allows it. Check that license (CLA §9).
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: a PDF of someone else's work doesn't qualify
**原因:** 報告 #38；同時違反 Canva 授權和 Etsy CS。

**Scenario 12 — Social media post for own business**（圖示 ✓）

**原文 (Current):** G E N E R A L L Y  W I T H I N  U S E
**改成 (New):** GREEN-LEANING
**原文 (Current):** Marketing and social media are recognized uses, subject to special-content restrictions.
**改成 (New):** Why: social media and promotion are permitted uses (CLA §5). Could change this: RED for images of people in tobacco, dating, political or health/supplement ads (§9); Pro Music in paid TV, radio, podcast or billboard ads (§7); Popular Music in any commercial use (Licensing Explained).
**原文 (Current):** Marketplace rules
**改成 (New):** Music + sensitive-ad limits checked
**原因:** 報告 #39、3.1。報告原本把敏感廣告標為 AMBER，但 CLA §9 和 §7 的原文是禁止規定，依「較嚴格解讀」改為 RED。這不是平台販售情境，所以勾選框改成對應的檢查。

---

## Page 17 — Scenarios 13–14

狀態：修改

**Scenario 13 — Course workbook PDF**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Treat as a finished publication; verify embedded assets and distribution method.
**改成 (New):** Why: a finished publication is a permitted use (CLA §5). Could change this: RED if it was made with Pro on a Canva Education account (§8) or contains Education ("Resource") items (§5C). AMBER if unedited Pro images exceed 480,000 px (§5A).
**原文 (Current):** Marketplace rules
**改成 (New):** Exported from a commercial (non-Education) account
**原因:** 報告 #40、3.1。

**Scenario 14 — Lead magnet PDF**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Free distribution does not remove licensing obligations. Verify content exactly as you would for a paid PDF.
**改成 (New):** Why: promotional materials are permitted (CLA §5), and free distribution follows the same rules as paid. Could change this: AMBER if unedited Pro images exceed 480,000 px or can be extracted (§5A, §9). RED with Branded, Education or Disney items.
**原文 (Current):** Marketplace rules
**改成 (New):** Same checks as a paid PDF
**原因:** 報告 #41 ✅、3.1。

---

## Page 18 — Scenarios 15–16

狀態：修改

**Scenario 15 — PLR/MRR bundle**（圖示 改成 ✕）

**原文 (Current):** H I G H  C A U T I O N
**改成 (New):** RED
**原文 (Current):** Do not grant resale or sublicensing rights over Canva Content unless you actually have authority to do so.
**改成 (New):** Why: PLR/MRR grants resale or sublicensing rights, which CLA §9 and Terms of Use §2e(i) prohibit for Canva Content. Breaches of those use restrictions fall outside Canva's liability cap (ToU §14). Could change this: only after replacing all Canva Content with assets you own.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: bundles of others' work don't qualify
**原因:** 前 5 項第 4 項；報告 #42。

**Scenario 16 — Presentation template**（圖示 !）

**原文 (Current):** V E R I F Y
**改成 (New):** AMBER
**原文 (Current):** Editable-template rules apply; audit every asset category before distribution.
**改成 (New):** Why: same template rules as Scenario 02 (CLA §5, §6; Licensing Explained). Could change this: GREEN-LEANING if delivered as a Canva template link. RED if Pro Content ships as PPTX, Keynote or Google Slides, or any item is Education or Branded.
**原文 (Current):** Marketplace rules
**改成 (New):** Delivery format: Canva link only
**原因:** 報告 #43、3.1。

---

## Page 19 — Scenarios 17–18

狀態：修改

**Scenario 17 — Website graphic**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Web use is recognized, but Pro unedited media can be subject to pixel-size restrictions.
**改成 (New):** Why: web pages are permitted electronic publications (CLA §5). Could change this: AMBER if an unedited Pro image exceeds 480,000 px per file. There is no cap on Canva Websites or embedded Canva designs (§5A). RED if the site offers Content for download (§9).
**原文 (Current):** Marketplace rules
**改成 (New):** Unedited Pro ≤ 480,000 px (e.g. 600 × 800)
**原因:** 補上數字和兩個例外（報告 #44、3.1）。

**Scenario 18 — Business card template**（圖示 ✓）

**原文 (Current):** V E R I F Y
**改成 (New):** GREEN-LEANING
**原文 (Current):** This is an editable template; Free Content has broader rights than Pro Content.
**改成 (New):** Why: CLA §6 names "business card templates" as an allowed use of Free Content. Could change this: AMBER if it contains Pro (Canva link only; buyers may need Pro). RED if Pro ships in another format (Licensing Explained) or it is a resold Canva library template.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: my own original card layout
**原因:** 報告 #45、3.1。

---

## Page 20 — Scenarios 19–20

狀態：修改

**Scenario 19 — Printed book**（圖示 ✓）

**原文 (Current):** C H E C K
**改成 (New):** GREEN-LEANING
**原文 (Current):** Books are recognized permitted uses. Verify the content category and any special restrictions.
**改成 (New):** Why: books are permitted uses, and print is not subject to the §5A pixel cap (CLA §5). Could change this: the ebook edition follows Scenario 06. RED with any Branded, Education or Disney item.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: disclose print partner if third-party printed
**原因:** 報告 #46、3.1、3.5 第 2 點。

**Scenario 20 — Digital sticker pack**（圖示 改成 ✕）

**原文 (Current):** H I G H  C A U T I O N
**改成 (New):** RED
**原文 (Current):** If the product effectively redistributes individual Canva graphics, redesign using assets you own or can redistribute.
**改成 (New):** Why: delivering individual Canva graphics as separate files is standalone redistribution (CLA §3, §9; Licensing Explained). Could change this: GREEN-LEANING only if every sticker is your own artwork, drawn by you or commissioned with rights.
**原文 (Current):** Marketplace rules
**改成 (New):** Etsy: stickers are my original designs
**原因:** 前 5 項第 4 項；報告 #47。

---

## Page 21 — Checklist: Pre-publish checklist

狀態：修改（仍然是 10 項，每項長度和原文接近）

"Run this before every listing."：不變。

| # | 原文 (Current) | 改成 (New) |
| --- | --- | --- |
| 1 | I identified every third-party asset used. | I identified every asset and removed any I can't trace. |
| 2 | I checked the category and special label of every Canva asset. | I opened the source info (⋯) and label of every Canva item. |
| 3 | I know whether the buyer receives a finished output or editable/source file. | （不變） |
| 4 | I checked whether Content can be extracted or reused standalone. | No Canva item can be extracted as a file or sold on its own. |
| 5 | I verified current official terms rather than an old article or another seller's listing. | No item is Education, Branded, Disney or Editorial Use Only. |
| 6 | I checked the marketplace's own product and license rules separately. | Unedited Pro media is ≤ 480,000 px; Pro templates ship only as Canva links. |
| 7 | I removed assets whose redistribution rights are unclear. | I exported with an active Pro plan (or paid per Pro item) on a non-Education account. |
| 8 | I saved the source, license category, and date checked. | I checked the current official terms, not old articles or other listings, and saved the date. |
| 9 | I did not promise PLR, MRR, resale, or sublicensing rights I do not control. | I checked my platform's rules (Etsy: original design, partner and AI disclosure). |
| 10 | I prepared a clear buyer-facing Read Me / license note. | No PLR/MRR/resale rights promised, and my buyer Read Me says so. |

**原因:** 補上報告指出缺少的項目：Export 帳號和方案（CLA §4、§8；報告 3.2 第 1 點）、不可商用的標示（CLA §5B–5D、§9）、像素上限和 Pro 模板（CLA §5A；LE）、具體的平台規則（Etsy CS；報告 #48、#65）。原本的第 1、7 項合併；原本的第 8、9、10 項分別併入新的第 8、10 項。

---

## Page 22 — Red flags: Stop before you publish

狀態：修改

**原文 (Current):** You are selling a Canva library asset with little or no transformation.
**改成 (New):** You are selling a Canva item on its own, without other design elements.
**原因:** 官方的標準是 standalone，不是加工程度（LE；CLA §9；報告 #49）。

第 2–5 項：不變（報告 #50–53 ✅）。

**原文 (Current):** You commercially use Education or other special Content without checking its restrictions.
**改成 (New):** You use Education, Branded, Disney or "Editorial Use Only" Content in anything commercial or promotional.
**原因:** 這些是明文禁止，不是「沒有確認限制」的問題（CLA §5B–5D、§9；報告 #54）。

第 7 項（"The product's real value is effectively giving the buyer access to the original Canva asset."）：不變（報告 #55 ✅）。

**原文 (Current):** SIMPLIFY BEFORE YOU SELL — If the licensing story requires a chain of assumptions, simplify the product before you sell it.
**改成 (New):** （不變）
**原因:** 維持品牌訊息。

> **備用文字（只有在不加 NEW PAGE B 時使用，放在 SIMPLIFY 框下方）：** At stake: Canva may delete designs or permanently ban your account with no refund (Terms of Use §15), and Etsy may remove listings and still charge fees.

---

## NEW PAGE B — Etsy checks & what's at stake

狀態：新增（插在第 22 頁之後、第 23 頁 W1 之前；版型建議沿用第 22 頁）

**Section tag:** 15B MARKETPLACE
**Title:** Etsy checks & what's at stake
**Intro:** Canva's license and your marketplace's rules are two separate tests. Pass both. (Etsy Creativity Standards, last updated 10 June 2025.)

**ETSY — FIVE CHECKS**
1. **Original design.** Canva-made downloads and print-on-demand items fall under "Designed by a seller": they must be your original designs. "A bundle, collection, scan, or PDF of someone else's work" does not qualify, and that includes unmodified Canva templates or library graphics.
2. **Production partner.** Printed by a third party (POD shirts, mugs, books)? Disclose the production partner and where the item ships from.
3. **AI disclosure.** Made with AI tools? Say so in the listing description. Our cautious reading: also disclose Canva library items marked AI-generated.
4. **Personalised items.** For custom items, the first image must show a finished, customised item, not placeholder text like "Your Text Here".
5. **Removal.** Etsy may remove listings that break its policies, and listing fees remain payable.

Selling on Gumroad, Beacons or elsewhere? Check that platform's own rules separately.

**WHAT'S AT STAKE ON CANVA'S SIDE**
- Canva may delete designs, suspend or terminate your account, or permanently ban you (Terms of Use §15b).
- After termination for a violation: no refund, and no new account without Canva's written permission (ToU §15c).
- If your license ends, you must stop using and delete the Content and designs (CLA §10).
- Breaching the "Restrictions on Use of the Service" is excluded from the liability cap, and you indemnify Canva (ToU §13–14).

**原因:** 報告 3.5 第 1–5 點（Etsy CS 原文）；第 3 點「Canva 圖庫中的 AI 素材也要揭露」是保守解讀，文案中已標明 "Our cautious reading"；第 4 點是否適用於可編輯模板，Etsy CS 沒有明說（❓），所以只寫「custom items」。「What's at stake」依據報告 3.2 第 5 點（ToU §13、§14、§15b、§15c；CLA §10）。

---

## Page 23 — Worksheet W1: License source tracker

狀態：修改（只改一個欄位標題）

**原文 (Current):** ACTION
**改成 (New):** SIGNAL / ACTION
**原因:** 讓工作表和燈號系統一致（報告 3.1）。

ASSET／SOURCE／LICENSE / LABEL／DATE CHECKED：不變。

---

## Page 24 — Worksheet W2: Product audit worksheet

狀態：修改

**原文 (Current):** CANVA CONTENT USED
**改成 (New):** CANVA CONTENT USED + EXPORT ACCOUNT / PLAN
**原因:** CLA §4、§8（報告 3.2 第 1 點）。

**原文 (Current):** MOST RESTRICTIVE CONTENT CATEGORY
**改成 (New):** MOST RESTRICTIVE LABEL (APPLIES TO WHOLE DESIGN)
**原因:** CLA §1（報告 #16）。

**原文 (Current):** MARKETPLACE / SALES CHANNEL
**改成 (New):** SALES CHANNEL + ITS RULES CHECKED (E.G. ETSY)
**原因:** 報告 #65、3.5。

**原文 (Current):** DECISION / CHANGES REQUIRED
**改成 (New):** SIGNAL (GREEN-LEANING / AMBER / RED) + CHANGES REQUIRED
**原因:** 報告 3.1。

PRODUCT NAME、WHAT THE BUYER RECEIVES、FINISHED OR EDITABLE?、CAN CONTENT BE EXTRACTED?、OFFICIAL TERMS CHECKED ON：不變。

---

## Page 25 — Worksheet W3: Buyer-facing rights statement builder

狀態：修改（小改）

**原文 (Current):** Use this page only to describe rights you actually control in your original material.
**改成 (New):** Use this page only to describe rights you actually control in your original material. Canva Content inside your product stays under Canva's license; you cannot grant rights over it.
**原因:** CLA §9 禁止 sub-license；ToU §2e(i)（報告 #53）。

**原文 (Current):** WHICH THIRD-PARTY ASSETS REMAIN SUBJECT TO SEPARATE TERMS?
**改成 (New):** WHICH THIRD-PARTY ASSETS (E.G. CANVA CONTENT) REMAIN UNDER SEPARATE TERMS?
**原因:** 讓買家知道 Canva 素材另有條款（CLA §1、§9）。

其他 5 個問題：不變。

---

## Page 26 — Quick reference: A safer product-building hierarchy

狀態：修改

"Move from clearer rights at the top toward higher-friction situations at the bottom."：不變。

第 1、2 列（LOWER FRICTION）：不變（報告 #56 ✅）。

**原文 (Current):** CHECK — Finished designs using Canva Free/Pro Content within permitted uses
**改成 (New):** GREEN-LEANING — Finished designs using Canva Free/Pro Content within permitted uses (CLA §5)
**原因:** 改用燈號（報告 #57 ✅、3.1）。

**原文 (Current):** CHECK MORE — Editable templates using Canva Free Content
**改成 (New):** AMBER — Editable templates: Free-only, or Pro delivered only as a Canva link
**原因:** CLA §6；LE「Selling templates」（報告 #58、#59）。

**原文 (Current):** HIGHER RISK — Editable templates containing Pro or specially restricted Content
**改成 (New):** RED — Pro in non-Canva template formats, or any Education, Branded or Disney Content in a product for sale
**原因:** 報告 #59：H5 拆層；LE "can't use Pro content in templates of any nature"；CLA §5B–5D。

**原文 (Current):** AVOID — Treating Canva Content itself as a resellable or sublicensable asset
**改成 (New):** （不變）
**原因:** 報告 #60 ✅。

---

## Page 27 — Sources: Official references & update note

狀態：修改

**原文 (Current):** Prepared against Canva's official licensing materials checked in September 2026. Re-check before publishing and after material policy updates.
**改成 (New):** Prepared against the official sources below, each verified on 25 September 2026. Where Canva's binding agreement and its explainer differ, this guide follows the stricter reading and says so. Rules change: re-check before publishing and after policy updates.
**原因:** 寫出確切日期（報告 #64）；說明來源不同時的處理原則（報告 4.2）。

**原文 (Current):** Canva Content License Agreement — https://www.canva.com/policies/content-license-agreement/
**改成 (New):** Canva Content License Agreement (binding) — https://www.canva.com/policies/content-license-agreement/ — Verified 25 September 2026
**原因:** 網址和快照一致（報告 #61 ✅）。

**原文 (Current):** Canva Licensing Explained — https://www.canva.com/licensing-explained/
**改成 (New):** Canva Licensing Explained (Canva's explainer) — https://www.canva.com/licensing-explained/ — Verified 25 September 2026
**原因:** ToU §4b 確認這是官方頁面；純文字快照裡沒有網址本身（報告 #62）；網址已對照創辦人 2026-09-25 存檔的頁面來源資訊（Snapshot-Content-Location）確認。

**原文 (Current):** Canva Terms / Policies — https://www.canva.com/policies/
**改成 (New):** Canva Terms of Use (effective 19 August 2026) — https://www.canva.com/policies/terms-of-use/ — Verified 25 September 2026
**原因:** /policies/ 索引網址無法驗證（報告 #63 ❓）。改成 ToU，並寫出生效日（ToU 快照第一行）。網址已對照創辦人 2026-09-25 存檔的頁面來源資訊（Snapshot-Content-Location）確認。

**新增一列**
**改成 (New):** Etsy Creativity Standards (last updated 10 June 2025) — https://www.etsy.com/legal/creativity/ — Verified 25 September 2026
**原因:** 創辦人決定新增；更新日期來自快照 "Last updated on Jun 10, 2025"。網址已對照創辦人 2026-09-25 存檔的頁面來源資訊（Snapshot-Content-Location）確認。

**新增一行小字（放在來源清單下方）**
**改成 (New):** Not covered here, so read them if relevant: Canva AI Product Terms, Popular Music License, Acceptable Use Policy, and your sales platform's own policies.
**原因:** 這些文件 CLA 或 ToU 有引用，但內容沒有取得（報告 #64、4.3）。

**原文 (Current):** VERSION 3.0
**改成 (New):** VERSION 3.1 · CHECKMAYBE
**原因:** 創辦人決定。

**原文 (Current):** Canva is a trademark of its respective owner. This independent guide is not sponsored, approved, or endorsed by Canva.
**改成 (New):** （不變）
**原因:** 創辦人決定保留；在拿到商標指引前，不要自行填入商標權人名稱（報告 #2）。

---

## 更新後的 Gumroad／Beacons 商品頁文字

**Title:**
Can I Sell This? — A Commercial Use Toolkit for Canva Sellers | CheckMaybe

**Description (3 lines):**
A 29-page first-pass decision toolkit for selling what you make in Canva: printables, templates, print-on-demand, client work and more.
Traffic-light signals (GREEN-LEANING / AMBER / RED) for 20 real scenarios, a content-label guide, Etsy checks and worksheets, each tied to the official source section.
Checked against Canva's Content License Agreement, Licensing Explained, Terms of Use and Etsy's Creativity Standards on 25 Sep 2026. Independent educational resource, not affiliated with Canva, not legal advice.

---

## 假設、風險與下一步

- **假設**：(1) CLA 和 LE 說法不同時，採用較嚴格的說法並註明（創辦人決定；報告 4.2）。(2) Scenario 12 的敏感廣告和 Pro Music 限制依 CLA 原文改為 RED，比報告建議的 AMBER 更嚴格。(3) 新增 2 頁，全書變成 29 頁，所以商品頁寫 "29-page"。如果最後沒有加頁，請改回 "27-page"。
- **風險**：(1) 燈號仍然只是初步判斷，全書都保留 "not permission / not legal advice"。(2) 產品名稱中的「Canva」要等拿到 Canva 商標指引才能定案（報告 ❓ #1）。(3) ToU、Etsy、LE 的網址不在快照內，需要在瀏覽器確認。(4) 部分卡片內文比原文長約 1 行，版面可能需要把字級縮小 0.5–1pt。
- **最小的下一步**：先改第 9 頁（Case 11）、第 10 頁（Case 12）、第 14 頁（S08）、第 15 頁（S10），加上全域頁尾和封面，就能涵蓋前 5 項中的第 1–3 項。
