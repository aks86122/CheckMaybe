# Can I Resell This? v1.0 — 06 逐條核對（模板第 4 步）

- 日期：2026-09-26｜核對者：法遵檢查員（support-legal-compliance-checker）
- 對象：`products/build/resell-v1.0.json`（初稿，見 `05-draft-notes.md`）
- 唯一允許的證據：scratchpad 內創辦人存檔的官方頁面 `gumroad-prohibited.txt`、`beacons-cs.txt`、`etsy-creativity.txt`、`canva-cla-user.txt`、`canva-licensing-explained.txt`、`canva-terms.txt`、`openai-terms.txt`、`anthropic-consumer.txt`。**未使用 `first1k.txt`，未上網。**
- 方法：用腳本抽出 JSON 裡所有 “…” 引文，把彎引號／直引號，以及存檔裡的亂碼（`���`）統一視為同一字元後，對存檔做全文比對。遇到省略號就把引文拆段，逐段比對。另外逐一人工檢查每個事實句和燈號。
- 性質：教育用途的核對，**不是法律意見**，也不是上架許可。`03-reality-check.md` 的 **HOLD** 判定不受影響。
- 圖例：✅ 與存檔一致｜⚠️ 大致正確但有漏限定語、語境或過度推論（已修）｜❌ 錯誤（本輪 0 項）｜❓ 存檔無法證實

## 總覽

| 狀態 | 數量 | 處理 |
| --- | --- | --- |
| ✅ | 46 | 不動 |
| ⚠️ | 8 | 全部已在 JSON 最小修改 |
| ❌ | 0 | — |
| ❓ | 2 | 1 項已改成 VERIFY 措辭；1 項（存檔日）需創辦人補 |

機械比對結果：所有標明出自官方的引文，都在對應存檔中逐字找到（修正後重跑一次，新引文也全部找到）。沒比對到的都是加了引號的推銷話術（如 “100% profit”、“no watermark”、“luxury lifestyle”、“full resell rights”），不是在引用官方文字，屬正常。
JSON 修改：共 11 個字串（10 項修正），`python3 -c "import json;json.load(...)"` 可正常解析；所有欄位都在 SCHEMA 字數限制內（最長的卡片 407／420 字）。

---

## 一、逐條核對表

### Gumroad（gumroad-prohibited.txt，Last revised: September 16, 2026）

| # | 位置 | 句子／引文 | 狀態 | 存檔片段 | 處理 |
| --- | --- | --- | --- | --- | --- |
| G1 | p5、情境 1 | “reselling private label rights products” | ✅ | 清單項：`reselling private label rights products` | — |
| G2 | p5、p7 | “services (including, but not limited to, ‘get rich quick’ schemes, business opportunities, investment opportunities…)” | ✅ | `services (including, but not limited to, "get rich quick" schemes, business opportunities, investment opportunities, mortgage consulting…` | 內層雙引號改成單引號，後面項目用省略號代替，意思不變 |
| G3 | p5、p7 | “multi-level marketing or pyramid schemes” | ✅ | 清單項原文 | — |
| G4 | p5 note | “If you are unsure whether your content is prohibited on Gumroad, please contact us” | ✅ | 原文後面接 `at support@gumroad.com with a description…` | — |
| G5 | p5 note | “may change abruptly and without notice” | ✅ | `this list may change abruptly and without notice` | — |
| G6 | p8、情境 9 | “deceptive marketing practices” | ✅ | 清單項原文 | — |
| G7 | 情境 1 | support@gumroad.com | ✅ | 開頭段落 | — |
| G8 | p5 卡、情境 6／7／14、p3、p17 | **PLR 沒有擴大成所有轉售權**：燈號 “RED · PLR RESALE · MRR/RR: CHECK”、“MRR and plain resell rights are not named in the PLR line” | ✅ | 清單只有 `reselling private label rights products`，沒有 MRR／resell rights 字樣 | 符合 03 必要修正第 3 點 |
| G9 | 情境 1 | 改名重賣 PLR ＝ **RED ON GUMROAD**；“A new cover and title don’t tell you it has stopped being a PLR product.” | ✅ | 同 G1 | 條文點名 PLR 轉售，RED 有官方依據。「改封面不代表不再是 PLR」是推論，句子寫成「不能證明」而非「一定是」，措辭適當 |
| G10 | p21 | 網址、Last revised September 16, 2026、Saved 26 September 2026 | ✅ | `Last revised: September 16, 2026`；sources.md 存檔日 2026-09-26 | — |

### Beacons（beacons-cs.txt，Nov 22, 2025）

| # | 位置 | 句子／引文 | 狀態 | 存檔片段 | 處理 |
| --- | --- | --- | --- | --- | --- |
| B1 | p5、p7、情境 2、情境 8 | “In general, we do not allow resale; you cannot sell products you did not create. You can act as an affiliate for other creators on Beacons, but you cannot sell products that aren’t your own creation.” | ✅ | Store 段 `Things you cant sell on Beacons.ai` 下的原文 | 保留了 “In general” |
| B2 | p5、p7、情境 8 | “Multi-level marketing offers, work-at-home scams and make money online opportunities” | ✅ | 出自 `Prohibited or illegal goods and services` 段（不是 Store 段） | p5 用 “Also prohibited:” 表述，正確；卡片標籤 “(STORE)” 指的是第一句，可接受 |
| B3 | p5 note | “Unlicensed proprietary content”、“Multi-level Marketing or Pyramid Schemes” | ✅ | `High-risk products … not permitted on Beacons` 的例子 | — |
| B4 | p6、情境 12 | “We do not allow the uploading of any content that infringes on copyrights, trademarks, or patents.” | ✅ | `Copyrighted content` 段原文 | — |
| B5 | p8 平台卡 | 原稿：Beacons’ prohibited actions include putting in your “Campaigns, Websites, Ads, or account” any material “that wasn’t created by you, provided for you to use, or that would violate anyone’s rights” | ⚠️ | 此句位在 **Email Marketing** 準則的 `Prohibited Actions`：`Include in your Campaigns, Websites, Ads, or account or sell in your Store any material that wasn’t created by you, provided for you to use, or that would violate anyone’s rights.` | 原稿沒交代出處段落，也沒點出 “provided for you to use” 例外，搭配標題「Someone else’s results…」容易讓人讀成「一律禁止」。**已改**：註明 Email Marketing guidelines／Prohibited Actions，改成連續引用（補回 “or sell in your Store”），並加一句提醒例外；source 欄改成 `Beacons, Email Marketing · Prohibited Actions (Nov 22, 2025)` |
| B6 | 情境 2 | 在 Beacons 上架 MRR 課 ＝ RED | ✅ | 同 B1 | 官方明文 |
| B7 | 情境 8 | 在 Beacons 做原課程聯盟 ＝ AMBER | ✅ | B1 允許 affiliate；B2 禁止 make money online | 沒有對任何課程下結論 |
| B8 | 情境 14 | 原稿：“Beacons bans resale of products you didn’t create” | ⚠️ | 原文是 `In general, we do not allow resale` | 漏掉限定語 “In general”。**已改**為直接引用：`Beacons: “In general, we do not allow resale”;` |
| B9 | p21 | 網址、Nov 22, 2025、Saved 26 September 2026 | ✅ | 第 5 行 `Nov 22, 2025`；sources.md | — |

### Etsy（etsy-creativity.txt，Last updated on Jun 10, 2025）

| # | 位置 | 句子／引文 | 狀態 | 存檔片段 | 處理 |
| --- | --- | --- | --- | --- | --- |
| E1 | p5 | 原稿：“Designed by a seller” includes “Digital downloads of sellers’ original designs: Original content created by the seller, sold as a digital download.” | ⚠️ | `Items “designed by a seller” include only:` 之下列出三類（數位下載、生產夥伴、Seller-prompted AI creations） | 引文逐字正確，但 “include only” 被弱化成 “includes”，違反「絕對規則寫成絕對」。**已改**：`Items “designed by a seller” “include only” listed types, among them “Digital downloads…”` |
| E2 | p5、情境 3 | “A bundle, collection, scan, or PDF of someone else’s work” | ✅ | 不符合 designed by a seller 的例子 | — |
| E3 | p5 | “A PDF file of a book that the seller did not personally create or design” | ✅ | `Examples of items that do not qualify…` | — |
| E4 | p5 note | “Etsy reserves the right to remove listings that do not follow our policies.” | ✅ | 原文 | — |
| E5 | 情境 3 | “sellers’ original designs” | ✅ | `Digital downloads of sellers’ original designs` | — |
| E6 | 情境 3、p17 | AI 須在商品說明中揭露（轉述，未加引號） | ✅ | `Sellers must disclose within their listing description if an item is created with the use of AI.` | — |
| E7 | 情境 11 | “AI prompt bundles” 不符合資格 | ✅ | 不符合例子中有 `AI prompt bundles` | — |
| E8 | 情境 3 | PLR planner 原樣在 Etsy 賣 ＝ **RED ON ETSY AS-IS** | ✅ | E2 | 別人的作品不符合 designed by a seller |
| E9 | p21 | 網址、Last updated on Jun 10, 2025、Saved 25 September 2026 | ✅ | 存檔末段；sources.md | Etsy 已有存檔，03 的「Etsy 未核實」限制已解除 |

### Canva（canva-cla-user.txt；輔證 canva-licensing-explained.txt）

| # | 位置 | 句子／引文 | 狀態 | 存檔片段 | 處理 |
| --- | --- | --- | --- | --- | --- |
| C1 | p6 | §9 “definitely can’t” | ✅ | `You definitely can’t do these things with any free or Pro Content on Canva:` | — |
| C2 | p6 | “sub-license, re-sell, rent, lend, assign, gift or otherwise transfer or distribute the Content or the rights granted under this Content License Agreement (subject to section 4A)” | ✅ | §9 第一項原文 | 保留 4A 限定語 |
| C3 | p6 | “in a manner that gives the impression that the Content was created by you” | ✅ | §9 原文後面接 `or a person other than the copyright holder…` | 截斷處不改變意思 |
| C4 | 情境 10 | “non-transferable (subject to section 4A below)” | ✅ | §2（Free）和 §3（Pro）授權條文 | — |
| C5 | 情境 10 | “sub-license, re-sell … or otherwise transfer or distribute the Content” | ✅ | 同 C2，用省略號縮短 | — |
| C6 | 情境 10 | Canva 模板包附 “full resell rights” ＝ **RED · STRICTER READING** | ✅ | C2、C4；輔證 licensing explained：`Don’t resell, redistribute or take credit for content provided through Canva.` | CLA §6 允許把 Free Content 用在要販售的模板，但那是給原設計者的權利，轉售者不能把 Canva 授權往下傳（non-transferable）。RED 有依據，已標 STRICTER READING；change 欄寫明「只有賣家原創、不含 Canva 素材」時才降為 AMBER，合理 |
| C7 | p6 | §9A 字型只能在 Canva 上或匯出的 Canva 設計內使用（轉述） | ✅ | `Use the Font Software other than on Canva and/or as an integrated component of a Canva Design that is exported from Canva` 屬禁止用途 | — |
| C8 | p21 | 「No effective date shown on the saved page」 | ✅ | 存檔中找不到生效日（只有 2024 年 Disney 條款日期和 © 2026） | — |

### AI 服務條款（openai-terms.txt、anthropic-consumer.txt）

| # | 位置 | 句子／引文 | 狀態 | 存檔片段 | 處理 |
| --- | --- | --- | --- | --- | --- |
| A1 | p6 | “As between you and OpenAI, and to the extent permitted by applicable law, you (a) retain your ownership rights in Input and (b) own the Output.” | ✅ | `Ownership of content.` 段 | 限定語完整 |
| A2 | p6、情境 11 | “output may not be unique” | ✅ | `Similarity of content.` 段 | — |
| A3 | p6、情境 11 | 原稿：“That is between OpenAI and its user, not later buyers”／“it is between OpenAI and whoever generated it, not later buyers” | ⚠️ | 條文只寫 `As between you and OpenAI`，沒提到後手買家 | 「不涵蓋後手買家」是法律效果的推論，接近替買家解讀條款。**已改**成描述條文本身：`That wording is between OpenAI and its user and doesn’t mention later buyers`；情境 11 改為 `wording between OpenAI and whoever generated it, silent on later buyers` |
| A4 | p6 | 原稿：Anthropic assigns “all of our right, title, and interest—if any—in Outputs” | ⚠️ | 原文：`Subject to your compliance with our Terms, we assign to you all of our right, title, and interest—if any—in Outputs.` | 漏掉前置條件 “Subject to your compliance with our Terms”。**已改**為完整一句引用 |
| A5 | p6、p21 | Anthropic Consumer Terms §4 | ✅ | `4. Inputs, Outputs, Actions, and Materials.` | — |
| A6 | p21 | OpenAI Effective January 1, 2026；EEA、瑞士、英國另有條款 | ✅ | `Effective: January 1, 2026`；`If you reside in the European Economic Area, Switzerland, or the UK…` | — |
| A7 | p21 | Anthropic Effective October 8, 2025 | ✅ | `Effective October 8, 2025` | — |
| A8 | p21 | OpenAI／Anthropic（以及 canva-terms）的**存檔日** | ❓ | `sources.md` 沒有這三份的列 | **需創辦人**把這三份補進 sources.md 並附存檔日，Sources 頁再補日期 |

### FTC 與其他 VERIFY 項目

| # | 位置 | 句子 | 狀態 | 依據 | 處理 |
| --- | --- | --- | --- | --- | --- |
| F1 | p8 卡 1、情境 8、p17 | FTC 背書／聯盟揭露：標 VERIFY，沒有引文、條號或日期 | ✅ | 符合規則 | — |
| F2 | p8 卡 2、情境 9 | FTC 假評論／誤導性見證：標 VERIFY，沒有引文 | ✅ | 符合規則 | — |
| F3 | p8 卡 3、p21 note | 原稿：“As far as this guide has found, there is no final rule, so don’t treat it as in force.”／“no final rule found” | ❓ | 允許的證據中**沒有任何 FTC 存檔**；這個「現況」判斷來自 03 的網路查核 | 在沒有存檔的情況下斷言規則狀態，而且「別當它生效」可能讓讀者誤以為收入宣稱不受規範。**已改**：`An FTC Earnings Claim Rule has been proposed. This edition has not checked its current status, or any other FTC rule on earnings claims, against official FTC text.`；Sources 改為 `proposed; current status not checked.`（保留 03 允許的 “proposed” 一詞） |
| F4 | p5 callout、情境 4 | 付款服務商規則：VERIFY，本指南未查 | ✅ | 已標示 | — |

### 推論與一般性說明（沒有單一官方出處）

| # | 位置 | 句子 | 狀態 | 處理 |
| --- | --- | --- | --- | --- |
| R1 | p3 | PLR／MRR／RR／Personal use 用 “Usually means” 說明 | ⚠️ | 沒有官方定義來源。**已改** lead 為 `These are common trade usages, not official definitions.`，並保留「以你拿到的授權文字為準」 |
| R2 | p6 lead | 原稿：“A resell licence covers the pack seller’s own material.” | ⚠️ | 「只涵蓋賣家自己的素材」是法律效果的斷言。**已改**為事實描述：`A resell licence comes from the pack seller.` |
| R3 | 情境 12 | 原稿：“A pack licence can’t grant either brand or filmmaker rights.” | ⚠️ | 說得過頭：如果賣家自己拍攝或握有授權，就可以授出拍攝者權利。**已改**：`can’t grant brand permission, or filmmaker rights the seller doesn’t hold.` 燈號 RED · HIGH CONCERN 不變（B4＋品牌 logo） |
| R4 | 情境 4／5／6／7／13 | AMBER／GREEN-LEANING／AMBER／AMBER／AMBER，理由以授權文字為主 | ✅ | 沒有擴大任何平台條文；GREEN 都附條件 |
| R5 | 情境 9 | 重用賣家收入截圖 ＝ RED · HIGH CONCERN | ✅ | 依據 G6＋FTC VERIFY；檢查項 “Provided for you to use, in writing?” 已處理 B5 的例外 |
| R6 | 情境 11 | AI 生成包 ＝ AMBER | ✅ | A1／A2／E7 |
| R7 | 情境 14 | 轉賣 MRR ＝ RED · HIGHEST FRICTION | ✅ | 理由是權利鏈＋Beacons（限定語已補，B8），沒有寫成 Gumroad 禁止 MRR |
| R8 | p16、p17 | 紅旗、上架前清單 | ✅ | 紅旗 callout 寫明 “doesn’t prove anything is illegal or that any seller acted wrongly” |

（合計 56 行：✅ 46 = G 10 + B 7 + E 8 + C 8 + A 5 + F 3 + R 5；⚠️ 8 = B5、B8、E1、A3、A4、R1、R2、R3；❓ 2 = A8、F3。）

---

## 二、規則集檢查

| 規則 | 結果 | 依據 |
| --- | --- | --- |
| 不點名任何賣家、課程、創作者 | ✅ | 全文只提到平台和工具商名稱（都在商標聲明中） |
| 無收入宣稱 | ✅ | p8 lead 寫 “This guide makes no income claims.”；“100% profit” 只出現在紅旗描述 |
| 不對 MLM／金字塔下法律結論 | ✅ | p7 callout “not a test of whether any programme is legal, multi-level marketing or a pyramid scheme”；p16 callout；沒提任何台灣法規 |
| 不做 “licence reader”／法律解讀定位 | ✅（修正後） | p2 lead “does not read or interpret your licence for you”；A3、R2 兩處解讀式句子已改成描述條文本身 |
| FTC 只能是 VERIFY，無引文、條號、日期 | ✅（修正後） | F1–F3；Sources 的 FTC 列 date=“To be verified” |
| 免責 “does not grant any resale, PLR or MRR rights” | ✅ | p1 quote、p2 callout 逐字出現；p1 legal、p21 closing 另有 “grants no resale, PLR or MRR rights” |
| 無絕對安全用語 | ✅ | 沒有 guaranteed／100% safe／you can definitely；“definitely can’t” 是 Canva 原文；p20 寫 “None of these steps is a guarantee” |
| 封面 not affiliated＋商標聲明 | ✅ | p1 topline、legal |
| 引號風格說明 | ✅ | p21 notes 已註明只有引號／撇號改為彎引號 |

---

## 三、JSON 修改清單（`products/build/resell-v1.0.json`）

| # | 頁／欄位 | 對應核對 |
| --- | --- | --- |
| 1 | p3 `lead` | R1 |
| 2 | p5 Etsy 卡 `text` | E1 |
| 3 | p6 `lead` | R2 |
| 4 | p6 AI 卡 `text` | A3、A4 |
| 5 | p8 FTC 卡 3 `text` | F3 |
| 6 | p8 平台卡 `text` | B5 |
| 7 | p8 平台卡 `source` | B5 |
| 8 | 情境 11 `why` | A3 |
| 9 | 情境 12 `why` | R3 |
| 10 | 情境 14 `why` | B8 |
| 11 | p21 FTC `note` | F3 |

只做字串替換，保留原檔的手動排版（diff 共 11 行 → 11 行）。原檔備份在 scratchpad 的 `resell-v1.0.orig.json`。

---

## 四、需要創辦人處理（不在本步驟權限內）

1. **A8 存檔日**：把 `openai-terms.txt`、`anthropic-consumer.txt`、`canva-terms.txt` 補進 `sources.md`，附網址和存檔日。模板要求 Sources 頁每個來源都要有 `Verified` 日期；目前 p21 用的是 “Saved …”，OpenAI／Anthropic 則只有生效日。
2. **FTC**：如果要把 p8 的三張卡從 VERIFY 升級，要先存 FTC 的官方頁面（背書指南、評論規則、Earnings Claim Rule 狀態）。
3. **結構**：模板要求 15–20 個情境，本稿只有 14 個。要補一個，或由創辦人決定這次破例。
4. **上架決策**：03 判定為 HOLD，必要修正第 2 點是「不在現有 Gumroad 帳號新增含 PLR／MRR 字樣的商品」。本產品的副標就含 “PLR, MRR”，上架與否、在哪個帳號上架，要由創辦人決定。
5. 下一步（模板第 5 步）：內容創作者依本報告產出 `07-revision.md`，渲染後確認 p6、p7 沒有溢出版面。
