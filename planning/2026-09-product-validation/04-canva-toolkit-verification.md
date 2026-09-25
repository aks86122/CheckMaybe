# CheckMaybe 產品驗證 04：Canva Toolkit 事實查核（對照官方條款）

- **查核對象**：「Can I Sell This? — The Canva Commercial Use Toolkit」v3.0（27 頁 PDF 的文字擷取）
- **官方依據**：以下都是使用者於 2026-09-25 儲存的純文字快照。
  - **CLA**：Canva Content License Agreement（https://www.canva.com/policies/content-license-agreement/），是主要比對標準
  - **LE**：Canva Licensing Explained
  - **ToU**：Canva Terms of Use（2026-08-19 生效）
  - **Etsy CS**：Etsy Creativity Standards（2025-06-10 更新）
- **查核者**：Legal Compliance Checker（單一 agent；沒有上網、沒有 commit、沒有發佈）
- **性質**：針對教育型工具包做事實查核，**不是給創辦人的法律意見**。四份快照都沒有寫到的內容一律標 ❓，不憑記憶補上。Canva 商標指引目前**沒有取得**，相關項目維持 ❓。
- **圖例**：✅ 正確｜⚠️ 不精確、不完整或可能誤導｜❌ 錯誤或官方來源不支持｜❓ 手上的官方來源無法驗證
- **來源效力**：ToU §16i 規定，ToU 裡的「explanatory boxes」**不具拘束力**，只有框外文字才有拘束力。LE 是從 ToU §4b 的說明框連結過去的說明頁。本文的處理原則：**CLA 和 LE 說法不同時，以 CLA 為準，LE 當作 Canva 的官方解釋**（見 4.2）。

---

## 1) 摘要

### 各分類數量（共 65 條主張）

| 分類 | 數量 | 重點 |
| --- | --- | --- |
| ✅ 正確 | 42 | 大方向正確：most restrictive 規則、Section 6 只適用 Free Content、Pro 不可單獨散佈、4A 客戶轉讓、POD 不可單獨使用、書籍與電子出版物都是允許用途、商品化（LE FAQ 有明文）、Logo 可用 fonts／simple shapes／lines（LE） |
| ⚠️ 不精確、不完整或可能誤導 | 19 | 主要問題是**太保守、太籠統**：CLA 或 LE 寫得很明確的禁止事項（Education／Branded 不可商用、Pro 用在 Canva 以外的模板、PLR／MRR、數位貼紙）只被標成 CHECK、VERIFY 或 HIGH CAUTION；「Marketplace rules」只有一個勾選框，沒有具體內容 |
| ❌ 錯誤或官方來源不支持 | 0 | 初版把 Case 11 列為 ❌。LE 找到出處後，改列為 ⚠️：用詞弱化了官方原意，但不算錯誤 |
| ❓ 手上的官方來源無法驗證 | 4 | 產品名稱使用「Canva」、商標權人的名稱、AI Product Terms 的內容、/policies/ 索引網址 |

**章節編號對照**：工具包唯一明確引用的條號是「Section 6」（Case 05），和現行 CLA §6「Additional Permitted Uses for Free Content only」**一致** ✅。

**名稱中使用「Canva」**：CLA 和 LE 都沒有規範。ToU 只在 §5b 規定：在 **Canva Site** 上不得呈現 "misleading endorsement or affiliation with Canva"，也不得註冊含有 "CANVA" 的網域或子網域。這條只適用於 Canva Sites，不能直接套用到 Gumroad 或 Beacons 上的產品名稱，所以仍列為 ❓，需要 Canva 商標指引才能判斷（見第 4 節）。

### 前 5 項優先修正

1. **【最高】把商標／Logo 的說法改成和 LE 原文一致（Case 11、Scenario 08）。** LE 的原文是絕對的："you cannot use any Free or Pro content from Canva's library in a trademark (except for fonts, simple shapes and lines)"。工具包寫「generally cannot become an *exclusive* trademark」，同時弱化了兩件事：一是把「不可以」改成「通常不行」，二是把「不能用在商標裡」改成「不能變成獨占商標」。另外，CLA §9 的例外只有 "(excluding fonts)"，所以最保守的寫法是兩份來源都引用。Scenario 08 用 Canva 圖庫圖像做的 Logo，應改為 RED。
2. **把 Education、Branded、Disney、Editorial Use Only 改成「不可商用」（Case 04、Case 12、決策路徑 B、Red Flag 6、Hierarchy H5）。** CLA §5B：Branded 為 "personal use only"；§5C：Education 為 "non-commercial use only"；§5D：Disney 不可商用；§1 規定 most restrictive "applies to the entire design"，不是工具包寫的 "may be"；§8 和 LE 都說 Education 帳號做出來的東西只能非商業使用。
3. **把模板規則改成明確的燈號（Quick Map「Editable template」、Scenarios 02、10、16、18）。** LE 原文："Unless it's a template created for use on Canva, you can't use Pro content in templates of any nature"。CLA §5 允許所有 Content 用於 "design templates solely for use on Canva"。所以結論是：含 Pro 的模板**只能**以 Canva 內使用的形式交付（template link）；做成 PPTX、PSD 等 Canva 以外的模板就是 RED。另外還要補三點：買家如果是免費方案，會看到 Pro 浮水印（LE）；字型不能帶出 Canva（CLA §9A）；Canva 圖庫裡的模板本身就是 Content（CLA §1、§3 "Pro Template"），不能改一改就轉賣。
4. **把 PLR／MRR、數位貼紙、「flattened PDF」的判斷改嚴（Scenarios 15、20、01、Quick Map）。** 依據有三：CLA §9 明文禁止；LE 寫明 "Don't resell, redistribute"；ToU §2e(i) 禁止 "sell, distribute … sublicense … the Licensed Content"。而且依 ToU §14，違反「Restrictions on Use of the Service」**不受責任上限保護**，再加上 §13 的賠償責任，風險比工具包目前的寫法高得多。
5. **把「Marketplace rules」具體化，並補齊數字和來源。** Etsy CS 對 Canva 製作的商品有 5 個具體要求（見 3.5）：必須是 "original designs"；"A bundle, collection, scan, or PDF of someone else's work" 不符合資格；production partner 必須揭露；用 AI 做的商品必須揭露；Etsy 可以下架商品，已付的費用照收。另外要補上的數字和清單：§5A 的 480,000 像素上限（LE 確認適用於 "websites and ebooks"）；§9 的敏感用途清單；Popular Music 在 LE 中寫明 "can't be used for any commercial purposes"。來源頁要寫確切日期（CLA、LE 為 2026-09-25；ToU 為 2026-08-19 生效）。

---

## 2) 逐條對照表

| # | 頁／Case | 工具包主張（摘要） | 狀態 | 條號（來源） | 說明／建議英文措辭 |
| --- | --- | --- | --- | --- | --- |
| 1 | 封面 | 產品名稱為 "The Canva Commercial Use Toolkit" | ❓ | ToU §5b、§10（間接相關） | CLA 和 LE 都沒有規範。ToU §5b 禁止在 Canva Site 上呈現 "misleading endorsement or affiliation"，以及註冊含 "CANVA" 的網域，但範圍只到 Canva Sites。ToU §10：Service 和 Licensed Content 的智慧財產權都屬於 Canva，沒有授權第三方使用 Canva 商標。降低風險的寫法（非法律結論）："Can I Sell This? — A Commercial Use Toolkit **for Canva Users**"。**如果日後用 Canva Site 做銷售頁，網域或子網域絕對不能含 "canva"（ToU §5b）。** |
| 2 | 封面／p27 | "Canva is a trademark of its respective owner"；"not sponsored, approved, or endorsed" | ❓ | ToU §16e | 免責聲明的方向正確。ToU 只列出**簽約主體**（依帳單地址分為 Canva US, Inc、Canva UK Operations Ltd、Canva Pty Ltd），沒有寫商標權人是誰。在拿到商標指引之前，不要自行填入公司名稱。 |
| 3 | 封面 | 流程 IDENTIFY → CLASSIFY → VERIFY → PUBLISH | ✅ | CLA §2；ToU §4b | ToU §4b："hovering over the item … clicking on the info icon"。 |
| 4 | p2 | 本工具是決策輔助，不能取代現行官方條款 | ✅ | CLA §1；ToU §16n | CLA："reserves the right to cancel or change the licenses"；ToU："may modify these Terms … at any time"。 |
| 5 | p2 | 找出每個素材的來源和類別 | ✅ | CLA §2 | — |
| 6 | p2 | 檢查能否被單獨擷取、平台規則、最嚴格的類別 | ✅ | CLA §1、§9 | — |
| 7 | p2 | 成品和可編輯模板是不同的授權問題 | ✅ | CLA §5、§6；LE「Selling templates」 | — |
| 8 | p3 | 發佈前 5 分鐘自查的 5 個問題 | ✅ | CLA §1、§3、§9 | 缺少「用哪個帳號／方案 Export」這一題（CLA §4、§8），見 3.2。 |
| 9 | p4 | 決策路徑 B：「Pro, Education, Branded, or specially labelled?」 | ⚠️ | CLA §1、§5B、§5C | Pro 在成品裡可以商用，Education 和 Branded 則根本不能商用，兩者不應放在同一題。文字擷取中只有 E 有結論（若 PDF 原稿也是這樣，需要補上）。建議："B1. Any item labelled Education ('Resource' badge), Branded, Disney, or 'Editorial Use Only'? → Stop: not licensed for commercial use (CLA §5B–5D, §9). B2. Any Pro item (crown icon)? → Section 6 template rights do not apply; Pro may appear in templates only if the template is for use on Canva (LE)." |
| 10 | p4 | E = yes（可擷取）→ 強烈警訊 | ✅ | CLA §9；LE | CLA："extract or access or reproduce the content as an electronic file"。LE 說明像素限制的目的是防止 Pro 素材 "being downloaded from your website"。 |
| 11 | p5 | Flattened PDF → CHECK PERMITTED PUBLICATION USE | ⚠️ | CLA §5、§5A、§9；LE | LE 確認像素限制適用於 "Canva designs for websites and ebooks"。PDF 裡的圖片通常仍可被擷取。建議："Ebooks/PDFs are a permitted use (CLA §5). Unedited Pro media is capped at 480,000 pixels per file (CLA §5A; LE). Flattening alone does not stop extraction (CLA §9)." |
| 12 | p5 | Printed merchandise → CHECK MERCHANDISE USE | ✅ | CLA §5、§9；LE FAQ | LE："sell merchandise with your design on it"。 |
| 13 | p5 | Editable Canva template → CHECK TEMPLATE-SPECIFIC RIGHTS | ⚠️ | CLA §5、§6、§9A；LE | 官方其實已經寫得很清楚。建議："Pro content may be used only in templates made **for use on Canva** (LE; CLA §5). Templates in any other format may contain Free Content only (CLA §6). Fonts cannot leave Canva (CLA §9A)." |
| 14 | p5 | Client design → CHECK CLIENT-TRANSFER RULES | ✅ | CLA §4A | 可補上三個條件：書面協議、只能給單一客戶、責任由設計者承擔。 |
| 15 | p5 | Standalone asset resale → DO NOT PROCEED WITHOUT RIGHTS | ✅ | CLA §3、§9；LE；ToU §2e(i) | 建議把 "without rights" 改成："**Not permitted for Canva Content** (CLA §3, §9; LE 'Don't resell, redistribute'). Only CC0/Pixabay/Pexels items may differ — check that item's own license." |
| 16 | Case 04 | 混用類別時「may be」受最嚴格類別規範 | ⚠️ | CLA §1 | CLA 的規定是確定的："applies to the entire design"。建議："Under CLA §1 the most restrictive category applies to the **entire** design (from most to least restrictive: Education, Branded, Pro, Free)." |
| 17 | Case 05 | Free 有 Pro「不會自動取得」的額外權利；Section 6 模板權利不適用於 Pro | ⚠️ | CLA §6、§3 | 條號正確。"automatically" 暗示 Pro 可以透過其他方式取得這些權利，而且忽略了這是**以整個設計**為單位："If your Canva Design contains any Pro Content, you can't use it for these purposes"。 |
| 18 | Case 06 | 成品和可編輯是不同的授權情況 | ✅ | CLA §5、§6；LE | LE 對 template 的定義："a design that has a pre-determined layout and style and is intended to be further edited … by another person"。建議工具包直接採用這個定義。 |
| 19 | Case 07 | Free 有額外的模板權利；含 Pro 的設計不能援用 | ✅ | CLA §6；LE | — |
| 20 | Case 08 | 融入設計的商品化多數允許；單獨素材不能直接做成商品販售 | ✅ | CLA §5、§9；LE FAQ | LE 列出的例子是 "t-shirts, mugs, books and other merchandise"，並說明 standalone 是指 "a printout of a stock photo (without any other design elements)"。 |
| 21 | Case 09 | 電子書和電子出版物是允許用途，受 Pro 限制 | ✅ | CLA §5、§5A；LE | 建議直接寫出 480,000 像素。 |
| 22 | Case 10 | 可以在特定條件下轉讓給一位客戶；要有書面條款 | ✅ | CLA §4A | 可補上設計者要負責任（"solely responsible and liable"）。 |
| 23 | Case 11 | Canva 表示圖庫內容「通常不能成為**獨占**商標」 | ⚠️ | LE「Trademarks and logos」；CLA §9 | 出處是 LE，但用詞被弱化：LE 的原文是 "cannot use any Free or Pro content … in a trademark"，沒有「generally」，限制的是「用在商標裡」而不是「獨占」。建議："Canva's Licensing Explained says you cannot use any Free or Pro library content in a trademark, except fonts, simple shapes and lines. The binding CLA §9 lists only fonts as an exception — the safest logo uses Canva fonts plus your own uploaded graphics." |
| 24 | Case 11 | 例外包括 fonts、simple shapes、lines | ✅ | LE | LE："(except for fonts, simple shapes and lines)"。但 CLA §9 只寫 "(excluding fonts)"，兩份來源的差異見 4.2。 |
| 25 | Case 12 | Education 和其他特殊內容「可能規則較嚴」 | ⚠️ | CLA §5B、§5C、§5D、§8；LE | 嚴重低估。建議："Education Content ('Resource' badge) is **non-commercial only**; Branded Content is **personal use only** unless its source info says otherwise; Disney Content may not be used commercially. One such item makes the whole design non-commercial (CLA §1). Designs made on a Canva Education account are non-commercial (CLA §8; LE)." |
| 26 | Case 13 | Canva 生成的 AI Content 會標為 Free 或 Pro，並適用該類別的規則 | ✅ | CLA §3A | — |
| 27 | Case 13 | 「together with Canva's AI-related terms」 | ❓ | ToU §6 | ToU §6 確認 AI Products 受 **AI Product Terms** 規範（這份文件確實存在），但內容沒有取得。另外應補充兩點：CLA §9 和 ToU §2e(viii) 都禁止把 Content 用於 AI／ML 用途；Etsy CS 要求 AI 製作的商品必須揭露（見 #65）。 |
| 28 | S01 | 可列印 planner PDF → CHECK；「在可行時」讓成品無法被擷取 | ⚠️ | CLA §5、§5A、§9 | §9 是禁止條款，不是 "where practical"。見 3.1。 |
| 29 | S02 | 可編輯 planner 模板 → VERIFY | ⚠️ | CLA §5、§6；LE | 方向正確但太籠統。LE 已經提供明確規則，可以直接用，見 3.1。 |
| 30 | S03 | T-shirt：素材必須是設計的一部分 | ✅ | CLA §5、§9；LE FAQ | 如果在 Etsy 上架，要揭露 production partner（Etsy CS）。 |
| 31 | S04 | 馬克杯：原則同上 | ✅ | CLA §9；LE FAQ | 同上。 |
| 32 | S05 | 電子書封面是允許用途；商標問題另外處理 | ✅ | CLA §5 | 如果是賣現成封面給作者，屬於 4A（單一客戶）或模板情境，需要補充。 |
| 33 | S06 | 電子書內頁：Pro 有電子出版限制 | ✅ | CLA §5A；LE | — |
| 34 | S07 | 客戶 IG 素材包：適用客戶轉讓規則 | ✅ | CLA §4A | 同一套素材包賣給多位客戶時，就不是 4A，而是模板情境。 |
| 35 | S08 | 客戶 Logo → HIGH CAUTION；不要承諾獨占權 | ⚠️ | LE；CLA §9 | 太弱。使用圖庫圖像應為 RED。LE 列出的可行做法只有三種：字型、simple shapes and lines、上傳自己的圖。 |
| 36 | S09 | 含 Free Content 的模板 → POTENTIALLY VIABLE | ✅ | CLA §6、§2 | 介面上顯示為「Free」的素材，仍可能被標為 Branded、Education 或 CC0（CLA §2），要逐項確認。 |
| 37 | S10 | 含 Pro 的模板 → VERIFY | ⚠️ | LE；CLA §5、§6、§4 | 主張本身正確，但少了關鍵規則。LE 的規則：只有 Canva 內使用的模板可以放 Pro 素材。見 3.1。 |
| 38 | S11 | 單獨販售圖庫照片 printable → DO NOT PROCEED | ✅ | CLA §3、§9；LE；Etsy CS | 在 Etsy 上也不符合 "designed by a seller" 的資格（"PDF of someone else's work"）。 |
| 39 | S12 | 自家生意的社群貼文 → GENERALLY WITHIN USE | ✅ | CLA §5、§7；LE | 補充：Popular Music "can't be used for any commercial purposes, including advertising"（LE）。 |
| 40 | S13 | 課程 workbook PDF → CHECK | ✅ | CLA §5 | 用 Education 帳號製作的，應為 RED（CLA §8）。 |
| 41 | S14 | 免費 lead magnet 一樣要守授權 | ✅ | CLA §5、§9 | — |
| 42 | S15 | PLR／MRR → HIGH CAUTION | ⚠️ | CLA §9；ToU §2e(i)、§14 | PLR／MRR 的本質就是授予轉售或再授權，含 Canva Content 的產品應為 RED。違反 ToU 的使用限制時，責任不受上限保護（§14）。 |
| 43 | S16 | 簡報模板 → VERIFY | ⚠️ | LE；CLA §5 | 同 S02 和 S10。 |
| 44 | S17 | 網站圖片：未編輯的 Pro 可能有像素限制 | ✅ | CLA §5A；LE | 補充數字，以及 Canva Websites 和嵌入設計不受此限。 |
| 45 | S18 | 名片模板：Free 權利比 Pro 寬 | ✅ | CLA §6 | §6 明文列出 "business card templates"。 |
| 46 | S19 | 實體印刷書是允許用途 | ✅ | CLA §5；LE FAQ | — |
| 47 | S20 | 數位貼紙包 → HIGH CAUTION | ⚠️ | CLA §9、§3；LE；Etsy CS | 用 Canva 元素製作的應為 RED。 |
| 48 | p21 | 發佈前檢查清單 10 項 | ✅ | CLA §1、§2、§9 | 缺少的項目見 3.2 和 3.5。 |
| 49 | p22 RF1 | 「幾乎沒有加工」就販售圖庫素材 | ⚠️ | CLA §9；LE | 官方的標準是 standalone，不是加工程度。LE 對 standalone 的定義："used on its own without any other design elements"。建議："You are selling a Canva item on its own, without other design elements (LE; CLA §9)." |
| 50 | p22 RF2 | 可編輯模板含 Pro，卻援用 Free 的模板權利 | ✅ | CLA §6；LE | — |
| 51 | p22 RF3 | 無法確認素材來源 | ✅ | CLA §2 | — |
| 52 | p22 RF4 | 把其他賣家的上架商品當作可以用的證據 | ✅ | CLA §1 | — |
| 53 | p22 RF5 | 承諾 PLR／MRR 或 sublicense 權利 | ✅ | CLA §9；ToU §2e(i) | — |
| 54 | p22 RF6 | 「沒有確認限制」就商用 Education 或特殊素材 | ⚠️ | CLA §5B、§5C | 建議："You use Education, Branded, Disney or 'Editorial Use Only' Content in anything commercial or promotional." |
| 55 | p22 RF7 | 產品的價值其實是讓買家取得原始素材 | ✅ | CLA §9 | — |
| 56 | p26 H1–H2 | 原創素材或有明確權利的外部素材 → LOWER FRICTION | ✅ | 無（範圍外） | — |
| 57 | p26 H3 | 在允許用途內使用 Free／Pro 的成品 → CHECK | ✅ | CLA §5 | — |
| 58 | p26 H4 | 只含 Free 的可編輯模板 → CHECK MORE | ✅ | CLA §6 | — |
| 59 | p26 H5 | 含 Pro 或特殊素材的可編輯模板 → HIGHER RISK | ⚠️ | LE；CLA §5B、§5C | 應拆成兩層：Pro 且只以 Canva template link 交付 → CHECK；Pro 用在 Canva 以外的模板 → AVOID（LE）；含 Education 或 Branded → AVOID。 |
| 60 | p26 H6 | 把 Canva Content 本身當作可轉售的資產 → AVOID | ✅ | CLA §9 | — |
| 61 | p27 | CLA 網址 | ✅ | — | 和快照網址一致。 |
| 62 | p27 | Licensing Explained 網址 | ✅ | ToU §4b | ToU §4b 有引用 "Canva's Licensing Explained"，頁面確實存在。但純文字快照裡沒有網址本身，無法逐字驗證網址是否正確。 |
| 63 | p27 | Terms／Policies 網址 | ❓ | 無 | ToU 只提到 "Policy Archives"，沒有 /policies/ 這個網址。 |
| 64 | p27 | 「2026 年 9 月查核」 | ⚠️ | CLA §1；ToU §16n | 建議寫確切日期（2026-09-25），並列出 ToU 的生效日（2026-08-19）。應補上的來源：Popular Music License、AI Product Terms、Acceptable Use Policy（CLA §5D 和 ToU §2c 都有引用），以及 Etsy CS。 |
| 65 | S01–S20、p21 | 「Marketplace rules」勾選框；「checked the marketplace's own … rules」 | ⚠️ | Etsy CS | 方向正確，但每個情境都只有一個空白勾選框，賣家不知道要查什麼。Etsy 有明確規則可以寫進去：原創性、他人作品、production partner 揭露、AI 揭露、下架後費用照收。見 3.5。Gumroad 和 Beacons 的規則沒有取得。 |

---

## 3) 遺漏與升級建議

### 3.1 把 CHECK／VERIFY 改成有條件的燈號（仍然不保證）

每張卡片的建議格式：**"First-pass signal — not permission. GREEN-leaning / AMBER / RED if …, based on [CLA §x / LE], checked 2026-09-25."**

| Scenario | 目前 | 建議燈號與條件 | 依據 |
| --- | --- | --- | --- |
| 01 Printable PDF、13 Workbook、14 Lead magnet | CHECK | **GREEN-leaning**：素材融入自己的版面，每個未編輯的 Pro 檔案都在 480,000 像素以內，且沒有 Education、Branded、Disney 或 Editorial 素材。**AMBER**：有大張、未編輯的 Pro 照片，或單張圖片可以直接被擷取。**RED**：用 Education 帳號製作；含 Education、Branded 或 Disney 素材；一頁就是一張圖庫圖片。 | CLA §5、§5A、§5B–D、§8、§9；LE |
| 02 Planner 模板、16 簡報模板、10 Pro 模板 | VERIFY | **AMBER-GREEN**：以 Canva template link 交付，Free 和 Pro 都可以（CLA §5；LE "template created for use on Canva"）。商品頁要寫清楚："Pro elements show a watermark on free Canva plans; buyers need Canva Pro or a one-off license"（LE）。**AMBER**：只含 Free，但以 Canva 以外的格式交付（CLA §6 允許，但要注意 §9 的擷取禁止，以及 §9A 不能附字型檔）。**RED**：含 Pro 且用 Canva 以外的格式（LE "can't use Pro content in templates of any nature"）；含 Education 或 Branded 素材；直接轉賣 Canva 圖庫裡的模板（模板本身就是 Content：CLA §1、§3 "Pro Template"）。 | LE；CLA §1、§3、§5、§6、§9A |
| 03 T-shirt、04 Mug | CHECK | **GREEN-leaning**：素材和自己的文字、版面組合成新的設計（LE FAQ）。**AMBER**：圖中有真人、品牌或藝術品（CLA §12 不處理 release）。**RED**：只放一個 Canva 元素就上架 POD（LE "without any other design elements"）；使用 Branded 或 Disney 素材。 | CLA §5、§5B、§5D、§9、§12；LE |
| 05 電子書封面 | CHECK | **GREEN-leaning**：用在自己的書。**AMBER**：賣現成封面給作者（一款只能給一位客戶並有書面協議，或改用 template link）。**RED**：封面圖案被當作作者或系列的 Logo。 | CLA §4A、§5；LE |
| 06 電子書內頁、17 網站圖片 | CHECK | **GREEN-leaning**：Free 素材，或 Pro 素材已編輯過或在 480,000 像素以內。例外：透過 Canva Websites 發佈，或以 Canva 託管的設計嵌入網頁，則沒有像素上限。**RED**：網站提供 Content 讓人下載。 | CLA §5A、§9；LE |
| 07 客戶 IG 素材包 | VERIFY | **GREEN-leaning**：有書面協議、只給一位客戶、只交付 Design，且設計者承擔責任。**RED**：同一套內容給多位客戶。 | CLA §4A |
| 08 客戶 Logo | HIGH CAUTION | **RED**：含 Canva 圖庫的圖像、插畫或照片。**AMBER-GREEN**：只用 Canva 字型加上自己上傳或委託製作的圖形。**AMBER**：使用 simple shapes／lines（LE 允許，但 CLA §9 只寫 fonts）。任何情況都不要承諾獨占權。 | LE；CLA §9、§12 |
| 09 Free 模板、18 名片模板 | POTENTIALLY VIABLE / VERIFY | **AMBER-GREEN**：只含 Free，且每一項都確認過不是 Branded、Education 或 Editorial（CLA §2）。§6 有明文列出 "business card templates"。優先以 Canva template link 交付。 | CLA §2、§6、§9 |
| 11 單獨圖庫 printable | DO NOT PROCEED | **RED**：同時違反 Canva 授權（CLA §3、§9；LE），在 Etsy 也不符合資格（"PDF of someone else's work"）。 | CLA；LE；Etsy CS |
| 12 自家社群貼文 | GENERALLY WITHIN USE | **GREEN-leaning**。**AMBER**：含人像的保健品、醫療、菸草、交友或政治廣告；Editorial Use Only 素材；在付費傳統媒體（TV、電台、Podcast、看板）使用 Pro Music。**RED**：Popular Music 用於商業用途（LE）；使用 Branded、Education 或 Disney 素材。 | CLA §5、§7、§9；LE |
| 15 PLR／MRR | HIGH CAUTION | **RED**：只要含 Canva Content 就是 RED。先移除 Canva Content、全部改用自有素材，才能改為 AMBER。 | CLA §9；ToU §2e(i)、§14 |
| 19 印刷書 | CHECK | **GREEN-leaning**：印刷不受 §5A 限制；同一本書的電子版回到 06 的規則。 | CLA §5；LE FAQ |
| 20 數位貼紙包 | HIGH CAUTION | **RED**：用 Canva 元素製作，並以單張檔案交付。**GREEN-leaning**：只用自己的手繪素材。 | CLA §3、§9；LE；Etsy CS |

### 3.2 賣家需要、但工具包沒寫或寫得不夠的規則

1. **授權什麼時候產生（CLA §4；LE）**：授權在 Export 時產生；一張 Pro 授權只能用在一個 Design；resize 或做新的 Design 都要新的授權（Pro 會員自動取得，免費用戶要付費）。**建議加一項檢查**："I exported with an active Pro plan (or paid for each Pro item) and kept a record."
2. **Pro 怎麼辨識（LE）**：縮圖右下角有皇冠圖示。**其他標示（CLA §2）**：從三點選單的 source info 查看，包括 CC0、Branded、Education（"Resource"）、AI-generated、Editorial Use Only、Disney。
3. **Canva 圖庫裡的模板本身也是 Content**（CLA §1 列出 "templates"；§3 "Pro Template"）：把 Canva 現成模板改一改再當作「自己的模板」賣，是再散佈 Content。在 Etsy 上也不符合 "original designs" 的要求。
4. **§5 完整允許清單、§5A 的像素數字、§5B、§5C、§5D、§7 音樂、§9 完整禁止清單、§9A 字型、§10 和 §11 的處理程序、§12 不處理 release**：和初版相同。這些是 CLA 的原始規定，LE 沒有涵蓋 Branded、Education 標示和 Disney，所以工具包必須直接引用 CLA。
5. **違規的真實代價（ToU）**：§15b 規定可以刪除 Design、終止帳號、**永久禁用**；§15c 規定被終止後沒有退款，也不能開新帳號；§13 要賠償 Canva 的損失；§14 規定違反使用限制時**不適用責任上限**。建議新增一頁 "What's at stake"，讓 AMBER 和 RED 的差別更具體。
6. **ToU §2e(ix)**：禁止繞過防止複製的機制。例如擷取 template link 裡的素材、移除浮水印，都算違規。

### 3.3 條號和引用方式

- 「Section 6」的引用正確 ✅。建議每張 Case 卡片都補上 "CLA §x — [heading]" 或 "Licensing Explained — [heading]"，並清楚區分**拘束性條款（CLA、ToU）**和**官方解釋（LE）**。
- 工具包自己的編號（例如「14 CHECKLIST」、「CASE 09」）容易和 CLA 條號混淆，建議加上前綴，例如 "Toolkit Part 14"。
- CLA 本身有交叉引用的小瑕疵（§3 說 Pro 的允許用途見 "sections 5 and 7"，但 §7 講的是 Pro Music），工具包不要轉述交叉引用。
- CLA 說定義以 ToU 為準，但 ToU 快照只定義了 "Design"、"Licensed Content"、"User Content"，**沒有定義** "Export"、"Pro Content"、"Canva Design"。工具包不要自行補定義。

### 3.4 產品本身的自查（meta）

- 如果這份 PDF 是用 Canva 製作，它就是 ebook：未編輯的 Pro 素材要符合 §5A 的像素限制；CheckMaybe 的 Logo 不能使用圖庫圖像（LE／CLA §9）。
- 如果日後在 Etsy 販售本工具包，它屬於 "designed by a seller" 的數位下載，內容必須是原創（Etsy CS）。
- 銷售頁不要架在網域含 "canva" 的 Canva Site 上（ToU §5b）。

### 3.5 Etsy 專屬補充（取代空白的「Marketplace rules」勾選框）

建議在每個情境卡片上，把 "Marketplace rules" 換成以下具體檢查項目（出處：Etsy CS，2025-06-10 版）：

1. **分類**：Canva 製作的數位下載商品和 POD 商品，都屬於 "Designed by a seller"，要求是 "sellers' original designs"／"Original content created by the seller"。**不符合資格的例子**："A bundle, collection, scan, or PDF of someone else's work"。所以直接轉賣 Canva 現成模板、單張圖庫圖片、貼紙包，**在 Canva 授權之外，也另外違反 Etsy 規則**。建議英文措辭："Etsy: Is the listing your own original design? A PDF or bundle of someone else's work (including unmodified Canva templates or library graphics) does not qualify."
2. **POD／production partner**：T-shirt、馬克杯、印刷書（Scenarios 03、04、19）"Sellers must disclose that an item is made by a production partner"，並提供正確的出貨地點。
3. **AI 揭露**：用 Canva AI 工具產生的圖像，或 source info 標示為 AI-generated 的素材，Etsy 要求 "disclose within their listing description if an item is created with the use of AI"。至於 Canva 圖庫中的 AI-generated 素材是否也要揭露，Etsy CS 沒有明說。保守做法是揭露（這是本文的解讀）。
4. **個人化商品的主圖**：可以客製化的商品，"first image must show a finished, customized item rather than … placeholder text (e.g., 'Your Text Here')"。可編輯模板是否適用這條，Etsy CS 沒有明說，需要查 Listing Image Requirements（❓）。
5. **下架風險**："Etsy reserves the right to remove listings … Sellers remain obligated to pay any fees"。可以和 Canva 端的後果（3.2 第 5 點）放在同一頁。
6. **不在這份快照範圍內**：Etsy 智慧財產權政策（listing 標題或標籤用「Canva」一詞）、Etsy 數位商品規則、Listing Image Requirements、Gumroad 和 Beacons 的政策，都列為 ❓。

---

## 4) 其他官方頁面

### 4.1 用新來源解決或部分解決的項目

| 原本的 ❓ | 結果 | 來源 |
| --- | --- | --- |
| Logo 的「simple shapes and lines」例外 | 已解決 ✅（但和 CLA 有差異，見 4.2） | LE「Trademarks and logos」 |
| 含 Pro 的模板以 template link 販售 | 已解決：只有 Canva 內使用的模板可以放 Pro | LE「Selling templates」；CLA §5 |
| standalone 的標準 | 已解決：LE 定義為 "used on its own without any other design elements"。但加工到什麼程度才夠，LE 沒有說 | LE |
| 像素限制的適用範圍 | 已確認適用於 "websites and ebooks"。"unedited" 仍然沒有定義（❓） | LE |
| Licensing Explained 是否為官方頁面 | 已確認 | ToU §4b |
| 定義條款 | 部分解決：ToU 只定義了 Design、Licensed Content、User Content | ToU §1a |
| AI 條款 | 部分解決：確認有 AI Product Terms，但內容沒有取得 | ToU §6 |

### 4.2 各官方來源之間的差異（工具包應採用保守版本，並說明差異）

| 主題 | CLA（拘束性條款） | LE（官方解釋） | 建議 |
| --- | --- | --- | --- |
| 商標例外 | §9 只寫 "(excluding fonts)" | "fonts, simple shapes and lines" | 兩份都引用，建議以字型加自有圖形為主 |
| Education 做商業用途 | §8："create a separate Canva account" | "create a second team in your Canva account" | 兩種說法都列出，並提醒讀者兩份來源用詞不同 |
| 標註出處（attribution） | §9：編輯用途要標 "[Contributor's Name] via Canva.com" | "None of our licenses require attribution" | 工具包目前沒有處理這點。建議寫：「一般用途不用標註，但編輯用途請依 CLA §9 標註」 |
| Branded、Education 素材、Disney | §5B–5D 都有規範 | LE 沒有提到 | 工具包必須直接引用 CLA |

### 4.3 仍然需要的官方頁面

| 項目 | 需要的頁面 | 原因 |
| --- | --- | --- |
| 產品名稱和封面使用「Canva」、商標權人名稱 | Canva 商標／品牌指引（**尚未取得**）；Gumroad、Beacons、Etsy 的智慧財產權政策 | CLA 和 LE 都沒有規範；ToU §5b 只適用於 Canva Sites；ToU §16e 列的是簽約主體，不是商標權人 |
| 使用者用 Canva AI 工具產出的內容 | AI Product Terms | ToU §6 有引用，內容未取得 |
| §5A 中 "un-edited" 的定義；CLA §6 和 §9 之間的張力（Free 模板在 Canva 以外交付） | Help Center（products for sale） | CLA 和 LE 都沒有說明 |
| Popular Music 的細節 | Popular Music License | LE 只說不可商用 |
| Disney 和一般使用規範 | Acceptable Use Policy | CLA §5D、ToU §2c 都有引用 |
| Education 帳號 | Canva Education Additional Terms | ToU §1a 有引用 |
| 字型 | Fontsmith Collection EULA | 列在 Other policies 清單中 |
| CC0、Pixabay、Pexels 素材 | 各素材的原始授權 | CLA §9 最後一句 |
| Etsy 其他規則 | Etsy IP Policy、Listing Image Requirements、Seller Handbook | 見 3.5 第 6 點 |
| Gumroad／Beacons | 各平台的服務條款和禁售規範 | 沒有取得 |

---

## 5) 假設、風險與下一步

- **證據**：以上判斷依據四份 2026-09-25 快照和 v3.0 的文字擷取。文字擷取可能漏掉版面上的元素，例如決策路徑 A 到 D 的結論。
- **假設**：(1) CLA 和 LE 衝突時以 CLA 為準（依據是 ToU §16i 的類比，LE 本身沒有說明自己是否具拘束力）。(2) 可列印 PDF 適用 §5A（LE 寫到 "ebooks"，所以這個假設有支持）。(3) Canva 圖庫中的 AI 素材在 Etsy 上應該揭露，這是保守解讀。
- **風險**：燈號仍然只是初步判斷，文案必須保留 "not permission / not legal advice"。商標（產品名稱）的問題在拿到 Canva 商標指引之前無法定案。
- **建議**：先修正第 1 節的 5 項（其中第 1 到第 3 項只要改文字，不用改版面），再做燈號改版和 Etsy 檢查項目。
- **最小的下一步**：用新措辭改寫 Case 11、Case 12、S08、S10 這 4 張卡片，並取得 Canva 商標指引，確認產品名稱是否可以繼續使用「Canva」。
