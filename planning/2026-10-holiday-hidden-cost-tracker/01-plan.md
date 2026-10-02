# 節日版 Hidden Cost Tracker 企劃 v0.1

狀態：**已核准**（2026-10-03，創辦人回覆 5 題），開始製作
產品資料夾（做好之後）：`products/holiday-hidden-cost-tracker/`
基礎：原版 `products/hidden-cost-tracker/`（`build_tracker.py` 大部分沿用）

---

## 一句話定位
聖誕送禮預算表很多，但都只管「這個月花多少」。這份多管一件事：**12 月用分期、先買後付刷的禮物，1～3 月每個月要付多少**，以及黑五開的免費試用什麼時候會開始扣錢。

## 為什麼現在做

| 依據 | 內容 | 類型 |
| --- | --- | --- |
| 先買後付在節日很普遍 | Experian 調查：43% 的消費者節日期間用過或打算用先買後付 | 證據（[Experian](https://www.experian.com/blogs/ask-experian/research/buy-now-pay-later-holiday-survey/)） |
| 有後悔、有逾期 | 26% 的使用者用完後悔；一份 2025 年調查有 41% 的人去年逾期過 | 證據，二手轉述（[Motley Fool](https://www.fool.com/money/credit-cards/articles/heres-how-many-americans-regret-using-buy-now-pay-later-right-now/)、[KOMO](https://komonews.com/news/consumer/how-to-shop-smart-for-the-holidays-credit-cards-financial-advice-retailers-consumer-reports-tis-the-season-for-debt-deferred-interest-shop-now-pay-later)）；**引用到文案前要回原始報告確認** |
| 1 月帳單衝擊 | 媒體描述去年節日的分期在 1 月一起到期，造成壓力 | 證據，媒體描述（[Empower](https://www.empower.com/the-currency/money/pay-later-holiday)） |
| Etsy 聖誕試算表很擠，但都長一樣 | 送禮清單、預算、卡片名單、食譜，13 分頁的也有；價格約 US$3～18 | 證據（[範例 1](https://www.etsy.com/listing/1796870517/christmas-planner-google-sheets-holiday)、[範例 2](https://www.etsy.com/listing/1288945992/christmas-gift-planner-budget-template)、[範例 3](https://www.etsy.com/listing/1568425470/ultimate-christmas-planner-gift-tracker)） |
| 沒人做「節日分期 → 1 月帳單」 | 上面幾個範例都沒有 | **假設**：只看了搜尋結果前幾筆。動工前用 Etsy 搜「christmas budget bnpl」「holiday payment planner」確認 |
| 美國人 10 月底～11 月開始找聖誕預算表 | 業界常識 | **假設**：沒有數據。可以看 Etsy 搜尋框的自動完成、Google Trends「christmas budget template」 |

## 買家是誰
- 美國人，有預算壓力，會在黑五／網一買大件禮物（電視、遊戲機、手機）。
- 已經在用或考慮用 Klarna、Afterpay、Affirm 這類先買後付。
- 想要「一張表搞定送禮」，但更怕 1 月信用卡帳單。

## 分頁設計（6 個分頁＋1 個隱藏小幫手）

| 分頁 | 內容 | 跟原版的關係 |
| --- | --- | --- |
| **Dashboard** | 6～8 張卡：節日總預算、已花、剩多少、**節日分期 1 月要付多少**、2 月、3 月、最高真實年利率、試用到期數；送禮進度條；「1～4 月每月帳單」長條圖 | 改原版版面 |
| **Gift List** 送禮清單 | 收禮人、關係、禮物、預算、實際花費、付款方式（現金／信用卡／先買後付／商店分期）、狀態（想法／已買／已包裝／已送） | **新的** |
| **Holiday Payments** 節日分期 | 自己填每一筆分期（Gift List 會把用分期付的禮物標成「On a plan」提醒要加；不做自動帶入，因為每筆還要填期數和日期，自動帶入的列會跟著移動、對不齊）。算每期金額、期數、第一期日期、**真實年利率**、每月付款排程 | 沿用原版 Debts 的公式 |
| **Free Trials** 黑五試用 | 開始日、試用天數、取消日、倒數、試用後月費、「Cancel it?」 | 沿用原版 Subscriptions 的試用部分 |
| **Settings** | 節日總預算、月收入、提醒天數、貨幣 | 沿用 |
| **How to Use** | 3 步驟＋常見問題 | 沿用 |
| Chart Data（隱藏） | 圖表資料 | 沿用 |

**刻意不做的：** 聖誕卡名單、食譜、菜單、裝飾清單。競品已經做很多了，做了只會讓表變長，又會模糊「隱藏成本」這個賣點。之後如果評價有人要，再加成 v1.1。

**Secret Santa（交換禮物抽籤）不做：** 開源版本都要買家自己執行腳本，違反「買家不用跑腳本」的原則；只用公式的話每次編輯都會重新抽，結果不穩定。

## 外觀
- 沿用原版的深色版面和彩色標籤，**主色換成聖誕感但不俗氣**：深綠（#1F3B2D 系）＋暖金（#E0B05A）＋莓紅（#C8475A）。配色要先通過 dataviz 規則的對比檢查。
- 圖表一樣用原生 Google 圖表，`sheets_polish.gs` 改分頁名稱就能用。

## 標題、標籤、價格（草稿，上架前由定價和 SEO 專員確認）
- 標題草稿（≤140 字元）：
  `Christmas Budget Planner Google Sheets, Gift List Tracker, Holiday BNPL Payment Planner, Black Friday Free Trial Tracker`
- 標籤方向：christmas budget、gift tracker、holiday budget、christmas planner、gift list spreadsheet、bnpl tracker、black friday budget、google sheets budget……（13 個，查完 Etsy 自動完成再定）
- 價格：**US$7**（比原版便宜一點，因為是季節商品；競品 US$3～18）。另外加**組合價**：原版＋節日版 US$12。**假設**，交給定價專員確認。
- 打折：只用 Etsy 真的特賣，寫清楚結束日，**不做假倒數**。

## 時程（目標：11/1 前上架）

| 日期 | 事項 | 誰 |
| --- | --- | --- |
| 10/3～10/5 | 創辦人看企劃、回答下面 5 題 | 創辦人 |
| 10/6～10/10 | 改 `build_tracker.py` → 節日版 xlsx；公式驗算 0 錯誤；換配色 | Claude（✅ 10/3 提前完成：`products/holiday-hidden-cost-tracker/`） |
| 10/11～10/12 | 做 Google 母版、跑美化腳本、拿 /copy 連結（同原版步驟，約 15 分鐘） | 創辦人（電腦） |
| 10/13～10/17 | 買家 PDF、10 張 Etsy 圖、Gumroad／Beacons 圖、三平台文案 | Claude |
| 10/18～10/20 | 品保：Excel 下載測試、手機 App 開啟、文案逐句對表 | Claude＋創辦人 |
| 10/21～11/1 | 上架 Gumroad；Etsy 商店通過就上 | 創辦人 |
| 1/15 | 下架或改成「新年還債版」？看銷售再決定 | 創辦人 |

## 怎麼判斷成不成功（季節商品只有 2 個月）
- 11/30 前：Etsy＋Gumroad 合計 ≥10 單 → 明年 9 月提早上架、做更多節日變化。
- 3～9 單：看是流量問題（瀏覽少）還是轉換問題（瀏覽多、沒人買），寫檢討。
- 0～2 單：明年不做節日版，資源回到原版和情侶版。
- 每週記一次：瀏覽、收藏、訂單（Etsy Stats、Gumroad Analytics）。

## 風險
| 風險 | 對策 |
| --- | --- |
| 時間太趕，Etsy 商店還沒過審 | 先上 Gumroad；Etsy 一通過就上 |
| 節日分期的利率很多是 0% | 誠實寫：0% 就顯示 0% 和綠色 OK。賣點是「1 月要付多少」，不是嚇人 |
| 引用的調查數字有誤 | 文案只用確認過原始報告的數字；不確定就不寫數字 |
| 財務建議的界線 | 照原版：「Estimates only. Not financial advice.」；不建議用不用先買後付 |
| 原版還沒賣出就做第二個 | 節日版是同一套程式改出來的，成本低；而且節日有期限，等不了 |

## 創辦人決定（2026-10-03）
1. 方向：主打「節日分期 → 1 月帳單」 ✅
2. 價格：US$7，原版＋節日版組合 US$12 ✅
3. 配色：深綠＋金＋莓紅 ✅
4. 10/11～10/12 可以用電腦做母版 ✅
5. CheckMaybe Threads 先發 1～2 篇「黑五分期、1 月帳單」試水溫 ✅（草稿：`content/2026-10-holiday-bnpl-posts.md`）
