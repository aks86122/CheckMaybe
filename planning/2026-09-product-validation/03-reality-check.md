# CheckMaybe 產品驗證 03：Reality Check（最終獨立檢查）

- 流程位置：Product Validation 第 3 步（Trend Researcher → Growth Hacker → **Reality Checker**）
- 日期：2026-09-25｜輸入：`01-trend-research.md`、`02-validation-plan.md`
- 性質：產品驗證決策的對抗式檢查，非法律意見，也不是上線認證。我另外做了 6 次 WebSearch，結果仍是搜尋摘要，**同樣未核實**。

---

## 1. 「先做 A（Can I Sell This?）」站得住嗎？

**結論：可以先測 A，但「A 比 B 好」的理由被高估了。**

- **A 的最大弱點：官方已提供不錯的免費答案。** Canva 有 [Licensing explained](https://www.canva.com/licensing-explained/) 和 [Help: products for sale](https://www.canva.com/help/using-canva-to-create-products-for-sale/)，而且有具體範例。01 說「條文分散、沒有判斷流程」，這一點沒有證據支持。「規則單一、清楚」對維護有利，但對付費意願是**不利**的：規則越清楚，越少人需要付錢。
- **B 的反論被低估。** 規則分散在多家工具、變動快，是維護上的負擔，但也正是「有人願意付錢買整理」的理由。01 只從成本角度比較兩者，沒有從付費意願比較。
- **「兩個都不做」這個選項沒有被正式考慮。** 目前付費意願的證據是**零**，需求證據只有 2 則 FB 貼文、1 則 Etsy 討論串標題和一堆 SEO 文章。所以只能判定為 TEST，不能判定為 BUILD。
- **A 仍然適合先測的真正理由**：出錯的後果比較可控，素材一頁就能做完，14 天內有機會得到訊號。這是在比「測試成本」，不是在比「市場比較好」。

## 2. 最關鍵的事實風險：Hook 1 可能本身就是錯的

搜尋摘要顯示，Canva 的限制是**「含 Pro 內容的『可編輯模板』只能用 template link 賣」**。但 Help Center 也舉例說，顧客**無法編輯的成品 printable**（例如混用 Free 與 Pro 素材的賀卡）是允許的（[來源](https://www.canva.com/help/using-canva-to-create-products-for-sale/)，未核實）。

02 的 Hook 1（"≠ you can sell it as a PDF"）和流程圖 Q1 的「flat file (PDF, PNG, printable)」都把**可編輯模板**和**成品 printable** 混在一起。如果照原樣發出去，第一則貼文就會犯下這個產品要幫人避免的錯誤，還可能被懂規則的賣家公開糾正。**必須修正**（見第 6 節）。

## 3. 14 天實驗能產生可信訊號嗎？

- **最大混淆變數：觸及量，而不是需求。** 02 假設帳號有「<2,000 追蹤」，但沒確認 CheckMaybe 是否已有**英語、Canva 賣家**受眾。如果是新帳號，14 天的自然觸及可能只有幾百人。這時「下載 <30」量到的是**發佈能力**，不是需求，卻會被判定為 HOLD。必須加一個**「觸及不足＝INCONCLUSIVE（無結論）」**的前置門檻。
- **門檻問題**：
  - 下載 ≥100 對小帳號來說很激進，建議改用「每 1,000 觸及的下載數」。
  - 「預購 ÷ 下載 ≥5%」在 30 人的樣本下等於 1.5 人，只是雜訊；應降為輔助指標。
  - 「問卷說願付 ≥US$9」是陳述性偏好，偏虛榮指標。至少 20 份回覆的條件很可能達不到，建議從判定表拿掉，只作質化參考。
  - 預購 ≥8 筆是合理的最低標準，但必須**排除親友和已認識的人**，否則會被灌水。
- **做得好的地方**：「有人付錢才算數」、按讚不列入判定、WEAK 不硬判 BUILD。「具體情境提問數」是最有價值的質化指標，應保留，並逐字記錄。

## 4. 被低估的法律／品牌／平台風險

1. **Canva 商標**：Canva 的 [Trademark Guidelines](https://s3.amazonaws.com/static-cse.canva.com/pages/media-kit/Guidelines+for+Using+Canva+Trademarks.pdf) 摘要寫明，不得把 Canva 商標用作產品名稱的一部分，也不得暗示合作關係。副標題「made with Canva」屬描述性使用，風險中低。但 Gumroad 商品名稱、URL slug、hashtag 帳號和付費版名稱都**不能**出現 "Canva"。
2. **"Can I Sell This?" 本身**：這是通用片語，幾乎無法註冊為商標，別人也可以用。這不構成侵權風險，但代表**品牌資產弱**，不應投入任何商標費用。
3. **預購**：FTC 的 30 天到貨規則通常不適用於純數位商品（[FTC](https://www.ftc.gov/legal-library/browse/rules/mail-internet-or-telephone-order-merchandise-rule)），但「不實陳述」仍然受規範。要注意：
   - 「12 個月規則更新」用 US$12 換來一年的維護義務，而且還綁著法律準確性責任，**定價低於承諾**。應改成明確的截止日。
   - Gumroad 是否支援「上市日才扣款」的預購要在 Day 0 確認。如果不支援，就改成「付款後 X 日內交付，否則自動全額退款」。
   - Gumroad 費率為 10%＋US$0.50，加上金流費用（二手資料），US$12 實拿約 US$9–10。
4. **「被下架」hook（Hook 2）**：對象是正在受損的人，容易被理解成「用這個就能恢復上架」，必須加上「this won't reinstate listings」。
5. **Email**：下載者的 email 只能透過 Gumroad 內建功能寄送（它有退訂機制），不要匯出到其他工具群發。
6. **Etsy 2025-06 規則已經是 15 個月前的事**，Hook 4 用「quietly tightened」當新聞來講已經過時，而且要先確認 2026 年之後有沒有再改。

## 5. 創辦人時間是否實際

Day 0 估 6–8 小時偏樂觀。逐條核對 4 份官方文件、存檔、製作兩頁 PDF、建立 Gumroad 頁面加試用，實際約 **10–12 小時**；全程合計約 **22–26 小時**。另外，FB 社團答題帶來的觸及取決於社團規則，應在 Day 0 先確認至少 3 個**允許分享資源**的社團，否則最大需求來源等於不存在。

## 6. 必要修正 vs. 可選改善

**必要（Day 1 前完成）**
1. 流程圖 Q1 拆成「可編輯模板（template link／可編輯檔）」和「成品、無法編輯（printable／POD／實體）」；Hook 1 改寫或暫停，等 Day 0 核對完再決定。
2. 記錄基準：英語帳號的實際追蹤數和最近 10 則貼文的平均觸及；確認 3 個允許分享的 FB 社團。
3. 加上 **INCONCLUSIVE** 規則：14 天總觸及 <3,000 或 Gumroad 頁面瀏覽 <150 時，結果不得判定為需求 HOLD，只能判定為發佈失敗。
4. 下載門檻改成「每 1,000 觸及」；刪除問卷判定列；預購排除熟人。
5. 付費版的更新承諾改為明確截止日（例如「updates through 2027-03-31」）；確認 Gumroad 預購的扣款機制。
6. 所有商品名稱、slug、handle 都不含 "Canva"；Hook 2 加上不保證恢復上架的聲明。

**可選**：B 的零製作訊號測試保留；價格 A/B 留到下一輪；對 3–5 位 Canva 賣家做 15 分鐘訪談，問「你上次怎麼查這個問題、有沒有花錢」，補上付費意願的質化證據。

---

## 最終狀態：**TEST**

**理由**：付費意願的證據是零，需求證據只有少量二手資料，所以不能判定為 BUILD SMALL。但驗證成本幾乎是零、可以回收，而且問題確實存在，也不該判定為 HOLD。先測 A 是合理的，理由是測試成本和出錯後果較可控，而不是 A 的市場比 B 好。前提是第 6 節的必要修正要先完成，尤其是 Hook 1／Q1 的事實錯誤和「觸及不足＝無結論」規則。否則 14 天後不管結果如何，都無法區分「沒人要」和「沒人看到」。

**單一最小下一步**：創辦人用一般瀏覽器開啟 [Canva Help: products for sale](https://www.canva.com/help/using-canva-to-create-products-for-sale/) 與 [Content License Agreement](https://www.canva.com/policies/content-license-agreement/)，核對「可編輯模板 vs. 成品 printable 含 Pro 內容」這一條，並記下原文、URL 和日期（約 30 分鐘）。這一條決定了流程圖的核心分支和第一則 hook。
