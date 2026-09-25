# 05 — AI Toolkit 事實查核：「Can I Use This? — AI Content Commercial Use Toolkit」v1.0

- 查核日期：2026-09-25
- 查核角色：Legal Compliance Checker（單一 specialist，依 COST-CONTROL 最小編制）
- 性質：這是對教育型工具包的事實查核，不是法律意見。
- 依據文件（僅限以下三份使用者存檔，未上網查證）：
  - OpenAI **Terms of Use**（美國頁 `openai.com/policies/terms-of-use/`，"Effective: January 1, 2026"）
  - Anthropic **Consumer Terms of Service**（"Effective October 8, 2025"）
  - Etsy **Creativity Standards**（"Last updated on Jun 10, 2025"）
- 查核範圍外（一律標 ❓）：Adobe、Midjourney、Google、U.S. Copyright Office、Anthropic Commercial Terms、Canva、Gumroad／Beacons／POD 平台政策。

圖例：✅ 正確｜⚠️ 不精確（附英文修正文字）｜❌ 錯誤或無依據（附修正）｜❓ 需要其他官方來源

---

## 1) 總結

### 各類數量（共 45 項）

| 類別 | 數量 |
| --- | --- |
| ✅ 正確 | 20 |
| ⚠️ 不精確 | 11 |
| ❌ 錯誤／無依據 | 3 |
| ❓ 需其他官方來源 | 11 |

整體來說，OpenAI 與 Anthropic 快照的方向正確，引文大致對得上原文。問題集中在四處：**引文刪掉了有實質意義的限定語**、**OpenAI 引用的條款版本不適合美國受眾**、**Anthropic 模型訓練的說明不完整**，以及**對市集規則（Etsy）的描述過於模糊，有一處嚴重低估**。

### 優先修正 Top 5

1. **❌ Scenario 13（Selling AI prompts）嚴重低估 Etsy 規則。** Etsy Creativity Standards 把 "AI prompt bundles" 列為**不**屬於 "designed by a seller" 的品項，也就是不能在 Etsy 上架。工具包只寫 "can raise issues on some marketplaces"。這個工具包的受眾正是賣 prompt 的創作者，必須最先修。
2. **❌ OpenAI 官方來源（p.7、p.32）應改為美國版 Terms of Use。** 工具包面向美國／英語創作者，卻引用 `row-terms-of-use`。應以 `openai.com/policies/terms-of-use/` 為主要來源，並註明 EEA、瑞士、英國居民適用另一份條款。英國創作者也在英語受眾內，這一點特別重要。p.7 引文也要補回 "As between you and OpenAI, and to the extent permitted by applicable law"。
3. **⚠️ Anthropic 快照（p.11）要補上訓練例外，並撤下或標註未查證的 Commercial Terms 說法。** 就算已經 opt out，只要使用者給了 Feedback（例如按讚／倒讚），或內容被標記進行 safety review，Anthropic 仍會用來訓練。產出權利引文漏掉 "Subject to your compliance with our Terms"。「Commercial Terms 有更強的 ownership／indemnification」「API 預設不訓練」兩句都不在本次查核文件中，應標為待查證。
4. **⚠️ 補上「市集層」：Etsy 的 AI 揭露、類別與生產夥伴揭露。** Etsy 把 AI 作品歸在 "designed by a seller"，要求 "disclose within their listing description"。透過 POD 生產的商品另外要揭露 production partner 和出貨地。這些規則應寫進 Scenario 1／2／3／8／12、4 Questions（新增第 5 題）和 Checklist。
5. **❌／⚠️ 清掉從 Canva 工具包沿用過來、沒有依據的說法。** Scenario 3 的 "finished, non-editable deliverable" 在 OpenAI／Anthropic 條款中找不到依據。Scenario 10 的 "Several platforms explicitly restrict reselling raw outputs" 應改成點名具體平台，或降低語氣。p.3 的 "only days of notice" 應改成「有些變更公告即生效」。

---

## 2) 逐項查核表

### A. 開場、免責聲明與 4 Questions（p.2、p.3、p.6）

| # | 頁 | 工具包說法（節錄） | 判定 | 依據與說明 | 建議英文修正 |
| --- | --- | --- | --- | --- | --- |
| 1 | p.2 | "Commercial use is not the same question as copyright ownership…" | ✅ | 兩家條款都以 "if any" 限定轉讓範圍（OpenAI *Ownership of content*："all our right, title, and interest, if any"；Anthropic §4："—if any—in Outputs"），並要求使用者擔保自己有 Input 的權利。證據支持「合約允許使用 ≠ 具著作權保護」。 | — |
| 2 | p.3 | "AI platform terms can change — sometimes with only days of notice." | ⚠️ | OpenAI *Changes to these Terms*：對使用者有重大不利影響的變更會 "at least 30 days advance notice"，但 "All other changes will be effective as soon as we post them"。Anthropic §12：更新條款公告後繼續使用即視為同意，沒有寫預告期。所以實際情況是「有些變更可能完全不預告」，不是「只預告幾天」。 | "AI platform terms can change — some changes take effect as soon as they are posted, and continued use may count as acceptance." |
| 3 | p.6 | Q1：commercial-use permission 是合約問題，由 ToS 與 usage policy 回答 | ✅ | OpenAI *What you can do*：必須遵守 "Usage Policies"；Anthropic §3："Permitted Use"，含 Acceptable Use Policy。 | — |
| 4 | p.6 | Q2：產出權利是合約上「誰被轉讓了什麼」 | ✅ | OpenAI："We hereby assign to you…"；Anthropic §4："we assign to you…". | — |
| 5 | p.6 | Q3："Purely AI-generated output currently is not protected under U.S. copyright law." | ❓ | 這三份文件都沒有處理著作權是否成立的問題。需要 U.S. Copyright Office *Copyright and AI, Part 2*（2025 年 1 月）及相關判決。另外，這句話寫成絕對句，建議改用 USCO 的立場式寫法。 | "The U.S. Copyright Office's position is that material generated purely by AI, without sufficient human authorship, is not protected by copyright; human selection, arrangement, or modification may be." |
| 6 | p.6 | Q4：第三方侵權風險和平台條款無關，取決於 input 與 output 的相似程度 | ✅ | OpenAI *Similarity of content*："output may not be unique"；OpenAI 與 Anthropic 都禁止侵害他人權利（Anthropic §3："rights of publicity or privacy"）。 | — |

### B. OpenAI 快照（p.7；p.32 來源清單）

| # | 欄位 | 工具包說法 | 判定 | 依據與說明 | 建議英文修正 |
| --- | --- | --- | --- | --- | --- |
| 7 | PRODUCT／PLAN DIFFERENCES | API／business 與 consumer Terms of Use 是不同文件，本快照只涵蓋 consumer 版本 | ✅ | 開頭段落："Our Business Terms govern use of ChatGPT Enterprise, our APIs…"。另外兩點應補充：(a) 美國版條款明列 "ChatGPT, DALL·E"，圖片生成也在範圍內；(b) "If you reside in the European Economic Area, Switzerland, or the UK" 適用另一份條款。 | 加註："Users in the EEA, Switzerland or the UK are governed by a separate OpenAI terms document. ChatGPT Business/Enterprise and the API fall under the Business Terms." |
| 8 | COMMERCIAL-USE LANGUAGE | 條款把 Output 權利轉讓給使用者，但沒有概括聲明所有下游商用都已預先核准 | ✅ | *Ownership of content* 與 *What you can do*（使用仍受 "Usage Policies" 等約束）。 | — |
| 9 | OUTPUT-RIGHTS LANGUAGE | "You retain your ownership rights in Input and own the Output... We hereby assign to you all our right, title, and interest, if any, in and to Output." | ⚠️ | 原文："As between you and OpenAI, and to the extent permitted by applicable law, you (a) retain your ownership rights in Input and (b) own the Output."。工具包刪掉前段限定語，也拿掉了 (a)(b)，但沒有用省略號標示。這段限定語說明「擁有」只在使用者與 OpenAI 之間、且在法律允許範圍內成立，正好呼應 p.6 的 Q3，不應刪除。 | "As between you and OpenAI, and to the extent permitted by applicable law, you (a) retain your ownership rights in Input and (b) own the Output. We hereby assign to you all our right, title, and interest, if any, in and to Output." |
| 10 | RESTRICTIONS | "May not represent Output as human-generated" | ✅ | *What you cannot do*："Represent that Output was human-generated when it was not." 建議補上 "when it was not"，並提醒創作者：用 AI 寫的電子書若掛名時暗示完全由人撰寫，會碰到這條。 | 可選："May not represent Output as human-generated when it was not." |
| 11 | RESTRICTIONS | "may not use Output to develop competing models" | ✅ | "Use Output to develop models that compete with OpenAI." | — |
| 12 | RESTRICTIONS | "may not automatically extract Output **at scale**" | ⚠️ | 原文："Automatically or programmatically extract data or Output"，沒有 "at scale" 的門檻。工具包的寫法讓人以為少量自動擷取可以接受。 | "may not automatically or programmatically extract data or Output." |
| 13 | THIRD-PARTY RIGHTS WARNING | "…third-party material you upload is your responsibility, **not OpenAI's**." | ⚠️ | 前半句正確（"You represent and warrant that you have all rights, licenses, and permissions needed to provide Input"）。"not OpenAI's" 是工具包的詮釋，原文沒有。原文其實更廣："You are responsible for Content"，Content 包含 Input **和** Output。另外，OpenAI 的 indemnity 只適用於 "If you are a business or organization"。 | "You are responsible for Content (Input and Output) and represent that you have all rights needed to provide your Input. If you use the Services as a business, you also indemnify OpenAI against related third-party claims." |
| 14 | OFFICIAL SOURCE（p.7、p.32） | `openai.com/policies/row-terms-of-use (Effective January 1, 2026)` | ❌ | (1) 美國版頁面上的引文與生效日（"Effective: January 1, 2026"）對得上，所以內容本身可以用美國版來源證實。但工具包引用的是 ROW 網址，本次沒有取得 ROW 原文，無法確認兩者措辭相同（❓）。(2) 對以美國為主的英語受眾，主要來源應是美國版 Terms of Use：締約方是 "OpenAI OpCo, LLC, a Delaware company"，還有美國的 arbitration 條款。美國買家點 ROW 連結，看到的是不適用於自己的文件。(3) 英國買家適用 EEA／CH／UK 版本，兩個網址都不適用。p.7 標示 "VERIFIED" 卻放了不適用的來源，對付費產品有誤導疑慮。 | "Official source: openai.com/policies/terms-of-use/ (US; Effective January 1, 2026). EEA/Switzerland/UK residents: see OpenAI's separate terms for those regions. Other countries: check which version applies to you." |

### C. Anthropic Claude 快照（p.11）

| # | 欄位 | 工具包說法 | 判定 | 依據與說明 | 建議英文修正 |
| --- | --- | --- | --- | --- | --- |
| 15 | PRODUCT／PLAN DIFFERENCES | Consumer Terms 涵蓋 Claude.ai 與 Claude Pro；API key 與 Console 適用另一份 Commercial Terms | ✅ | 開頭："Our Commercial Terms of Service govern your use of any Anthropic API key, the Anthropic Console…"，並寫明 "this does not include Claude.ai or Claude Pro use for individuals or entities"。 | — |
| 16 | PLAN DIFFERENCES | Commercial Terms "carry stronger output-ownership and indemnification language" | ❓ | Consumer Terms 只說明 Commercial Terms 管轄哪些產品，沒有提到其內容。需要查 Anthropic Commercial Terms of Service 原文。 | 查證前先改為："Check the Commercial Terms directly for their ownership and indemnity terms." |
| 17 | COMMERCIAL-USE LANGUAGE | "Consumer terms assign Anthropic's rights in Output to the user" | ⚠️ | 轉讓屬實，但原文帶條件："Subject to your compliance with our Terms"。更重要的是，這個欄位標題是「商業使用」，Consumer Terms 卻沒有明文授權商業使用；反而 §2 規定 evaluation 用途為 "personal, non-commercial use only"。 | "Consumer Terms contain no explicit commercial-use clause. Subject to your compliance with the Terms, Anthropic assigns you its rights, if any, in Outputs. Evaluation access is for personal, non-commercial use only." |
| 18 | COMMERCIAL-USE LANGUAGE | "Commercial Terms additionally state Anthropic does not train on Customer Content from the API by default" | ❓ | 本次文件無法證實。需要查 Anthropic Commercial Terms 或相關隱私文件。 | 查證前刪除，或加註 "(verify in the Commercial Terms)"。 |
| 19 | OUTPUT-RIGHTS LANGUAGE | "You retain any right, title, and interest that you have in the Inputs... we assign to you all of our right, title, and interest — if any — in Outputs." | ⚠️ | 省略號跨越兩個句子，刪掉了實質條件 "Subject to your compliance with our Terms"，也刪掉了前段的 "As between you and Anthropic, and to the extent permitted by applicable law"（§4 *Rights and Responsibilities*）。 | "As between you and Anthropic, and to the extent permitted by applicable law, you retain any right, title, and interest that you have in the Inputs you submit. Subject to your compliance with our Terms, we assign to you all of our right, title, and interest—if any—in Outputs." |
| 20 | RESTRICTIONS | "Governed by Anthropic's Usage Policy" | ⚠️ | Consumer Terms 的用詞是 "Acceptable Use Policy"（開頭與 §3）；§3 還列了 "Supported Regions Policy"。網站頁尾稱 "Usage policy"，名稱不一致，建議兩個都寫出來，方便讀者搜尋。 | "Governed by Anthropic's Acceptable Use Policy (Usage Policy) and Supported Regions Policy." |
| 21 | RESTRICTIONS | "consumer conversations may be used for model training by default unless you opt out in account settings" | ⚠️ | 核心意思正確，§4 *Our use of Materials*："including training our models, unless you opt out of training through your account settings"。不過有三個問題：(1) 漏了例外——"Even if you opt out, we will use Materials for model training when: (1) you provide Feedback… or (2) your Materials are flagged for safety review"；(2) 範圍是 "Materials"（Inputs 與 Outputs），不只是 "conversations"；(3) 這是資料使用條款，不是對使用者的 restriction，放錯欄位。 | "Data use: Anthropic may use your Materials (Inputs and Outputs) to train its models unless you opt out in your account settings. Even after opting out, Materials may still be used for training if you give Feedback (e.g., thumbs up/down) or if they are flagged for safety review." |
| 22 | THIRD-PARTY RIGHTS WARNING | 使用者要負責確保對上傳素材有權利 | ✅ | §4："you represent and warrant that you have all rights, licenses, and permissions that are necessary"；"You are responsible for all Inputs you submit"。 | — |
| 23 | OFFICIAL SOURCE | `anthropic.com/legal/consumer-terms (Effective October 8, 2025)` | ✅ | 存檔標示 "Effective October 8, 2025"。 | — |

### D. 情境頁（p.12–26）：市集揭露、POD、Etsy 等

| # | 頁／情境 | 工具包說法 | 判定 | 依據與說明 | 建議英文修正 |
| --- | --- | --- | --- | --- | --- |
| 24 | p.12 S01 | "Some marketplaces require you to disclose AI-generated content in the listing." | ✅ | Etsy *Designed by a seller*："Sellers must disclose within their listing description if an item is created with the use of AI." 建議直接點名 Etsy，並寫明揭露位置。 | "Etsy, for example, requires sellers to disclose AI use within the listing description." |
| 25 | p.12 S01 | "Beta-labelled features on some platforms restrict commercial use…" | ❓ | 需要 Adobe Generative AI User Guidelines 與相關支援頁。 | — |
| 26 | p.13 S02 | "Print-on-demand platforms enforce their own AI-content policy on top of the AI tool's terms." | ⚠️ | 本次文件只能證實 Etsy（市集，不是 POD 平台）有自己的規則。個別 POD 平台（Printful、Redbubble、Merch by Amazon 等）的政策需要另外查（❓）。Etsy 對 POD 商品還有一項工具包沒提的義務："Sellers must disclose that an item is made by a production partner, and provide accurate information about where the item will ship from." | "Marketplaces and POD services can apply their own rules on top of the AI tool's terms. On Etsy, an AI design printed by a POD partner must disclose both AI use and the production partner (and where it ships from)." |
| 27 | p.14 S03 | "Confirm this is a finished, non-editable deliverable under the platform's terms." | ❌ | OpenAI 與 Anthropic 條款都沒有「成品／不可編輯」的要求，這看起來是從 Canva 授權框架沿用過來的概念，放在 AI 工具的語境下沒有依據（Adobe／Midjourney 未查，❓）。這個情境反而漏了真正相關的規則：在 Etsy 販售 AI 數位下載商品，屬於 "Digital downloads of sellers' original designs"／"Seller-prompted AI creations"，必須在 listing description 揭露 AI。 | 改為："Check whether your AI tool's terms restrict this use, and whether your marketplace requires AI disclosure (Etsy does, in the listing description)." 如果成品內含 Canva 等設計工具的素材，再另外加上 "If you used design-tool assets (e.g. Canva), check that tool's license too." |
| 28 | p.16 S05 | "Disclose AI involvement to the client where relevant." | ✅ | OpenAI 禁止 "Represent that Output was human-generated when it was not"；Anthropic §3 禁止利用服務 "to deceive any person"。 | — |
| 29 | p.17 S06 | "Purely AI-generated marks can face weaker trademark registration prospects in some jurisdictions." | ❓ | 需要 USPTO 等商標主管機關的資料。這句疑似把著作權的人類作者要求和商標混為一談：商標權通常取決於使用與識別性，和圖是誰畫的無關。 | 查證前建議改為："Purely AI-generated logo artwork may not be protected by copyright; trademark rights depend on use and distinctiveness, so run a clearance search either way." |
| 30 | p.19 S08 | "Purely AI-generated text may not be copyrightable…" | ❓ | 需要 USCO Part 2。這句語氣已經有保留，方向與 #5 一致。 | — |
| 31 | p.19 S08／p.20 S09 | 事實需要獨立查證；"Factual accuracy is your responsibility, not the AI provider's." | ✅ | OpenAI *Accuracy*："You must evaluate Output for accuracy…"，且 "ANY USE OF OUTPUTS… IS AT YOUR SOLE RISK"；Anthropic §4："should not rely on any Outputs… without independently confirming their accuracy"。 | — |
| 32 | p.19 S08 | "Marketplaces increasingly require AI-content disclosure." | ✅ | Etsy 確實要求揭露（同 #24）。「increasingly」這個趨勢描述，本次文件無法證實，但不影響結論。 | 建議把句子換成具體規則（同 #24）。 |
| 33 | p.21 S10 | "Several platforms explicitly restrict reselling raw outputs as standalone reusable assets." | ⚠️ | OpenAI 與 Anthropic consumer 條款都沒有這種限制。它們禁止的是轉售「服務」：OpenAI "Modify, copy, lease, sell or distribute any of our Services"；Anthropic §3 "resell the Services"，不是轉售 Output。其他平台是否限制 ❓。說 "Several platforms" 而不點名，讀者無法查證。 | "Some AI tools' terms may restrict reselling outputs as standalone assets — check yours. (OpenAI's and Anthropic's consumer terms reviewed here restrict reselling the *Services*, not Outputs.)" |
| 34 | p.21 S10 | "Buyers may assume they are getting exclusive or fully cleared assets." | ✅ | OpenAI *Similarity of content*："other users may receive similar output"，且 "Our assignment above does not extend to other users' output"。建議直接引用這段作為依據。 | — |
| 35 | p.23 S12 | "A policy violation can affect your whole storefront, not just one listing." | ❓ | Etsy Creativity Standards 只寫到 listing 層級："Etsy reserves the right to remove listings…"，並要求 "Sellers remain obligated to pay any fees"。帳號或店面層級的處分要查 Etsy Terms of Use／Seller Policy。AI 帳號部分：OpenAI 與 Anthropic 都可以因違約終止帳號，這一點有依據。 | — |
| 36 | p.23 S12 | "Revenue-based ownership thresholds on some platforms…" | ❓ | 需要 Midjourney Terms of Service。 | — |
| 37 | p.24 S13 | "Prompts built around a named living artist's style can raise issues on some marketplaces." | ❌ | 嚴重低估。Etsy Creativity Standards 兩度把 "AI prompt bundles" 列為**不**屬於 "designed by a seller" 的品項，而 "all items must incorporate a human touch as outlined by the categories below"。也就是說，prompt 商品本身就不符合 Etsy 的上架類別，和藝術家風格無關。Gumroad／Beacons 的規則需要另外查（❓）。 | "Check each marketplace before listing prompt products. Etsy's Creativity Standards list 'AI prompt bundles' as items that do not qualify as 'designed by a seller', so they are not allowed there. Separately, avoid building a prompt's value around a named living artist's style." |
| 38 | p.26 S15 | "You generally need rights to whatever you upload…" | ✅ | OpenAI："all rights, licenses, and permissions needed to provide Input"；Anthropic §4 有相同意旨。 | 建議補上 #21 的訓練說明（客戶機密資料）。 |
| 45 | p.22 S11 | Canva 自身授權規則（Free vs. Pro） | ❓ | 不在本次三份文件內，需要 Canva Content License Agreement。 | — |

### E. Red Flags（p.27）、Checklist（p.28）、Sources（p.32）

| # | 頁 | 工具包說法 | 判定 | 依據與說明 | 建議英文修正 |
| --- | --- | --- | --- | --- | --- |
| 39 | p.27 | "You're assuming a paid plan automatically means you own the copyright." | ✅ | OpenAI 與 Anthropic 的轉讓都寫 "if any"，而且不因付費方案而不同。 | — |
| 40 | p.27 | "You uploaded client-confidential material as input." | ✅ | Anthropic §4 預設可用於訓練（見 #21）；OpenAI *Our use of content*：可用 Content "to… develop, and improve our Services"，並提供 *Opt out*。 | — |
| 41 | p.27 | 名人肖像、知名角色、品牌 logo | ✅ | Anthropic §3："rights of publicity or privacy"；OpenAI："infringes, misappropriates or violates anyone's rights"。 | — |
| 42 | p.28 | "Before you sell checklist — Run this before every listing." | ⚠️ | 各條目本身沒錯，但以「每次上架前必跑」的清單來說，缺了市集規則與揭露這一項（見第 3 節），會讓讀者誤以為做完就夠了。 | 新增："I checked the marketplace's own rules (e.g. Etsy requires AI disclosure in the listing description and does not allow AI prompt bundles)." |
| 43 | p.32 | "U.S. Copyright Office — Copyright and AI, Part 2 (January 2025 report)" | ❓ | 本次未取得原文。 | — |
| 44 | p.8–10 | Adobe Firefly／Midjourney／Google Gemini 快照全部內容 | ❓ | 需要 Adobe Gen AI User Guidelines（May 15, 2026 版）、Midjourney ToS（May 27, 2026 版）、Google ToS 與 Generative AI Prohibited Use Policy。 | — |

（#14 已涵蓋 p.32 的 OpenAI 網址問題。）

---

## 3) 遺漏事項與升級建議（依三份文件，對 AI 內容賣家實際重要）

### Etsy Creativity Standards（影響最大，建議新增一頁「Marketplace Snapshot: Etsy」）

1. **AI 作品的類別是 "Designed by a seller"，不是 "Made by a seller"。** "Made by a seller" 限於 "Physical items made by a seller by hand or using personal or computerized tools"，而且電腦化工具必須在 "personal shop or home" 使用。AI 圖印在 POD T 恤上，應歸入 "Sellers' original designs produced by a production partner" 或 "Seller-prompted AI creations"。建議提醒讀者不要把 AI 商品標成 handmade 或 made by me。
2. **揭露位置有明文規定：** "Sellers must disclose within their listing description if an item is created with the use of AI." 只寫在標籤或店鋪介紹裡並不符合。
3. **POD／生產夥伴揭露：** "Sellers must disclose that an item is made by a production partner, and provide accurate information about where the item will ship from." 這條直接影響 Scenario 2 和 12。
4. **"AI prompt bundles" 不符合上架類別**（見 #37）。
5. **不能打包他人的作品：** "A bundle, collection, scan, or PDF of someone else's work" 不屬於 "designed by a seller"。轉賣別人生成的 AI 圖或素材包，同樣不符合。
6. **AI 作品必須基於賣家自己的 prompt／input：** "based on a seller's original prompts"；範例 "a custom portrait of a buyer's pet generated using AI tools" 表示買家提供的照片也可以當作 input。可以接到 Scenario 15 的 input 權利檢查。
7. **Listing 圖片規則：** 客製商品的首圖必須是 "a finished, customized item rather than the blank product or placeholder text"，細節另見 Listing Image Requirements。
8. **執行後果：** "Etsy reserves the right to remove listings… Sellers remain obligated to pay any fees"。下架了已付的刊登費也不退。
9. 建議把 **Etsy Creativity Standards** 加進 p.32 的官方來源，並加註 "Last updated on Jun 10, 2025"。

### OpenAI Terms of Use

10. **Output 不具獨特性：** "output may not be unique and other users may receive similar output"，而且轉讓 "does not extend to other users' output"。這是賣素材、賣圖的人最需要知道的一條，建議放進 p.7 快照和 Scenario 10、12。
11. **地區版本：** EEA、瑞士、英國居民適用另一份條款（見 #14）。
12. **Business indemnity：** "If you are a business or organization… you will indemnify"。以商業身分使用者需要知道自己的賠償義務。
13. **必須人工審查 Output：** "You must evaluate Output for accuracy and appropriateness… including using human review"。
14. **Training opt-out 也適用於 OpenAI**（*Opt out* 段）。目前只有 Anthropic 快照提到訓練，應兩家並列。
15. **條款變更通知：** 對使用者重大不利的變更有 30 天預告，其他變更公告即生效（見 #2）。可以放進 Worksheet 2 的 "RECHECK REQUIRED BY" 欄位說明。
16. **品牌使用：** "You may only use our name and logo in accordance with our Brand Guidelines"。在商品上寫「用 ChatGPT 製作」是事實描述，但使用 logo 需要遵守品牌規範（Brand Guidelines 本身 ❓）。

### Anthropic Consumer Terms

17. **消費者也要負擔賠償責任，範圍涵蓋你賣的商品：** §11 "YOU AGREE TO INDEMNIFY… ANY PRODUCTS OR SERVICES THAT YOU DEVELOP, OFFER, OR OTHERWISE MAKE AVAILABLE USING… THE SERVICES"。OpenAI 只要求 business 使用者賠償，Anthropic 不分身分，這個差異值得寫進快照。
18. **Evaluation 用途不可商用：** §2 "for your personal, non-commercial use only"。建議在 Checklist 加一條：不要用試用或評估權限做商業作品。
19. **不得用於開發競爭模型，也不得轉售服務：** §3 "including to develop or train any artificial intelligence or machine learning algorithms or models or resell the Services"。這條和賣「AI 訓練資料集」類商品直接相關。
20. **不得欺騙：** §3 "to deceive any person"。可以支撐 AI 揭露的建議。
21. **品牌使用限制：** §12 *Use of our brand*，禁止 "in any other way that implies our affiliation, endorsement, or sponsorship"。
22. **最低年齡 18 歲（§2）**，OpenAI 則是 13 歲以上，未滿 18 歲需家長同意。對青少年創作者受眾有影響。

### 結構性升級

23. **4 Questions 新增第 5 題：** "5. Does the marketplace where you sell allow it, and what must you disclose? — A platform-policy question, independent of the AI tool's terms." 5-Check Framework 的 USE 或 VERIFY 也應該提到「市集」。
24. **Checklist 新增條目：** 市集規則與 AI 揭露已完成；沒有把 Output 說成人工創作；帳號的訓練設定已確認（特別是涉及客戶資料時）；沒有使用 evaluation 或試用權限。
25. **Worksheet 1、2 新增欄位：** "SALES PLATFORM / MARKETPLACE"、"AI DISCLOSURE MADE (where)"、"PRODUCTION PARTNER DISCLOSED"、"TRAINING OPT-OUT STATUS"。
26. **"VERIFIED" 標章改寫：** 建議改成 "Checked against [exact URL] on [date]"，並列出查核範圍，避免付費讀者把它當成保證。這點在 #14 的來源錯置修正前特別重要。
27. **Red Flags 新增：** "You're listing on a marketplace without the required AI disclosure"；"You're labelling an AI design as handmade / 'made by' you"；"You're selling AI prompt bundles on Etsy"。

---

## 4) 需要其他官方頁面才能判定的項目

| 項目 | 對應表格編號 | 需要的官方來源 |
| --- | --- | --- |
| 純 AI 生成內容在美國不受著作權保護 | #5、#30、#43 | U.S. Copyright Office *Copyright and AI, Part 2: Copyrightability*（2025 年 1 月）；copyright.gov registration guidance |
| AI 生成商標的註冊前景 | #29 | USPTO 商標審查指引（及其他目標司法管轄區的主管機關） |
| OpenAI ROW 條款與美國版措辭是否一致；EEA／CH／UK 版內容 | #14 | `openai.com/policies/row-terms-of-use`、OpenAI EU terms 頁面 |
| Anthropic Commercial Terms 的 ownership、indemnity 與 API 不訓練條款 | #16、#18 | Anthropic Commercial Terms of Service；Anthropic Privacy Policy |
| Adobe Firefly 商用與 beta 限制 | #25、#44 | Adobe Generative AI User Guidelines；Adobe Firefly 支援頁 |
| Midjourney 的方案、營收門檻與授權 | #36、#44 | Midjourney Terms of Service（May 27, 2026 版） |
| Google Gemini 的產出權利 | #44 | Google Terms of Service；Generative AI Prohibited Use Policy；Gemini API Additional Terms |
| Canva 內容授權 | #45、#27 | Canva Content License Agreement／Terms of Use |
| Etsy 帳號層級處分與 AI 政策細節 | #35 | Etsy Terms of Use、Seller Policy、Seller Handbook 中的 AI 說明（Creativity Standards 內 "Read more about our stance on AI creations here" 的連結頁）、Listing Image Requirements |
| POD 平台的 AI 政策 | #26 | 各 POD 平台（Printful、Printify、Redbubble、Merch by Amazon 等）的內容政策 |
| 工具包銷售管道與受眾販售 prompt 的規則 | #37 | Gumroad 與 Beacons 的 Terms／Prohibited Products 政策 |
| OpenAI／Anthropic 品牌規範 | 第 3 節 #16、#21 | OpenAI Brand Guidelines；Anthropic 品牌使用說明 |
