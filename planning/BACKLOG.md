# CheckMaybe 待辦清單

最後更新：2026-10-03

## 進行中
- **Hidden Cost Tracker**：商品完成（母版、/copy 連結、正式 PDF、Excel 測試、Etsy／Gumroad／Beacons 商品圖與文案）。Gumroad（https://checkmaybe.gumroad.com/l/kofwfjf）和 Beacons 已上架（2026-10-03）；Etsy 商店審核中。進度清單：`products/hidden-cost-tracker/SETUP-zh.md`

- **節日版 Hidden Cost Tracker**（聖誕／黑五分期）：企劃 v0.1 等創辦人審閱，目標 11/1 前上架。`planning/2026-10-holiday-hidden-cost-tracker/01-plan.md`
- **《Before You Click "Pay Later"》**（12 頁免費小書，導流到 Hidden Cost Tracker）：企劃 v0.1 等創辦人審閱。`planning/2026-10-before-you-click-pay-later/01-plan.md`

## 之後再做（等前面的有銷售數據）
### 情侶版 Hidden Cost Tracker（Couples Hidden Cost Tracker）
- **由來**：2026-10-01 Threads 爆文「男友用 Excel 做感情檢討」（約 7K 讚），底下有人留言要檔案。
- **判斷**：
  - 惡搞的「感情 KPI 表」只適合當貼文素材，不做商品：大家多半是看熱鬧、不會付錢，又跟品牌無關，記錄親密行為也有隱私風險。
  - 情侶共同財務表在 Etsy 有需求，但很擠：約會追蹤表、情侶規劃表、分帳表都有很多賣家，價格約 US$1–16。
- **切入點**：沿用原版 Tracker 的差異點，不做成單純的分帳表。
  - 兩人一起看分期、訂閱、免費試用
  - 「這個月我們一起被綁住多少錢」
  - 誰的訂閱該砍、真實年利率、試用取消倒數
  - 可加：誰先付、誰該還誰
- **開工條件**：原版 Tracker 上架，並賣出幾單。
- **成本**：低，可以用 `build_tracker.py` 改出來。
- **參考**：[Etsy couples budget spreadsheet](https://www.etsy.com/market/couples_budget_spreadsheet/)、[split expense google sheet](https://www.etsy.com/market/split_expense_google_sheet)、[couple tracker](https://www.etsy.com/market/couple_tracker)

### 誠實上架文案提示詞包（Honest Listing Copy Prompts）
- **由來**：2026-10-03 創辦人分享一個 Gumroad AI 廣告提示詞包（500+ 提示詞、US$15、0 評價）。筆記：`planning/2026-09-competitor-notes/04-ai-prompt-vault-reference.md`
- **想法**：把 `listing-copy` skill 的結構做成給 Etsy／Gumroad 賣家的提示詞包，內建「不誇大、數字要對回商品、平台欄位上限」的檢查。
- **開工條件**：Hidden Cost Tracker 有銷售數據；或先發 1～2 篇 Threads 測反應。
