# 《Before You Click "Pay Later"》企劃 v0.1

狀態：**已核准**（2026-10-03），製作中
產品資料夾（做好之後）：`products/before-you-click-pay-later/`
來源：競品筆記 D（`planning/2026-09-competitor-notes/04-ai-prompt-vault-reference.md`）「短而專一的小書」＋ Hidden Cost Tracker 已驗證的範例數字。

---

## 一句話定位
結帳時看到「分 4 期」「每月只要 $59」，按下去之前花 5 分鐘做 5 個檢查。
一本 12 頁的英文 PDF 小書，免費下載，最後一頁導到 Hidden Cost Tracker（一般版／節日版）。

## 為什麼做
| 理由 | 依據 | 類型 |
| --- | --- | --- |
| CheckMaybe 缺觀眾與名單 | Threads 追蹤數很少；兩個參考店家的付費品都 0 評價，有評價的多是免費品 | 觀察（參考商店 A、筆記 D） |
| 免費品是名單入口 | Gumroad 0 元商品下載者會變成追蹤者，之後可以發更新通知 | 參考商店 A 筆記 |
| 內容和數字已經驗證過 | 29.8%、16.4%、25.7%、$428.25 都在 Hidden Cost Tracker／節日版算過 | 證據（`products/hidden-cost-tracker/`、`products/holiday-hidden-cost-tracker/README.md`） |
| 節日時機 | 黑五／聖誕是先買後付最多的季節；可以和節日版一起推 | 節日版企劃 |
| 製作成本低 | 沿用 `build_guide.mjs` 的 HTML → PDF 流程與深色版面 | 事實 |

## 讀者
- 美國人，結帳時常看到 Klarna／Afterpay／Affirm／商店分期選項。
- 不一定在負債，只是想「按下去前知道自己在做什麼」。
- 看完會想要「自動幫我算」的工具 → Hidden Cost Tracker。

## 逐頁大綱（12 頁，US Letter，深色）
| 頁 | 內容 |
| --- | --- |
| 1 | 封面：Before You Click "Pay Later" — 5 checks in 5 minutes |
| 2 | 怎麼用這本＋免責聲明（estimates only, not financial advice） |
| 3 | Check 1｜總共付多少：月付 × 期數 − 售價。範例：$67 × 24 − $1,200 = $408 |
| 4 | Check 2｜大約的年利率：對照表（4 個範例：pay-in-4 0%、$59×12 on $649 ≈ 16.4%、$89.50×6 on $499 ≈ 25.7%、$67×24 on $1,200 ≈ 29.8%）＋「為什麼月付看起來便宜」 |
| 5 | Check 3｜晚繳會怎樣：遲繳費、「0% 方案可能追溯計息（deferred interest）」要找合約哪一段 ⚠️ 需查證 |
| 6 | Check 4｜第一期什麼時候扣、扣哪個帳戶：結帳當下付 vs 下個月付，自動扣款的卡片 |
| 7 | Check 5｜會不會疊在一起：把所有分期排在同一張月曆上（$428.25 的 1 月範例） |
| 8 | 加碼：結帳時順便開了免費試用？寫下取消日（「付費前一天」） |
| 9 | 5 個檢查一頁版（可以截圖存手機） |
| 10 | 填寫頁：我的分期清單（品項、月付、期數、第一期、最後一期） |
| 11 | 想自動算？Hidden Cost Tracker 介紹＋連結（一般版／節日版） |
| 12 | 封底：資料來源與查證日期、免責聲明、CheckMaybe |

**刻意不做：** 不叫人「不要用先買後付」；不比較品牌好壞；不點名任何先買後付公司；不寫信用分數會怎樣（規則一直在變，⚠️ 除非查到官方最新說法）。

## 需要查證（寫進頁面前）
| 項目 | 去哪查 |
| --- | --- |
| Deferred interest（0% 方案晚繳／沒繳清時追溯計息）的定義和常見寫法 | CFPB（美國消費者金融保護局）官方說明，存檔並寫查證日期 |
| 先買後付遲繳費的一般範圍 | 不寫具體金額，只寫「看你的合約」；若要寫數字，需官方或發行商公開條款 |
| 先買後付會不會影響信用報告 | 暫不寫；若要寫，需 CFPB 或三大信用機構最新官方說明 |
| 範例 APR | 已用 RATE 驗算（Hidden Cost Tracker／節日版），沿用 |

## 價格與交付
| 項目 | 建議 |
| --- | --- |
| 價格 | **免費（$0+，可自由付款）** — 目的是名單和導流 |
| 交付 | Gumroad 0 元商品（PDF）；Beacons 放同一連結 |
| 導流 | 第 11 頁連到 Hidden Cost Tracker；節日版上架後換成節日版連結 |
| 文案 | 照 `.claude/skills/listing-copy/SKILL.md` |
| 圖片 | 封面 16:9、方形縮圖、IG 輪播 5～7 張（沿用 `build_images.py` 的版型） |

## 時程（跟節日版一起，11/1 前）
| 日期 | 事項 | 誰 |
| --- | --- | --- |
| 10/4～10/5 | 創辦人回答下面 4 題 | 創辦人 |
| 10/6～10/8 | 查證 deferred interest（CFPB）；寫內容；產生 PDF 草稿 | Claude |
| 10/9 | 創辦人看草稿 | 創辦人 |
| 10/10～10/12 | 改稿、商品圖、Gumroad 文案 | Claude |
| 10/13 前 | Gumroad 上架（免費），Threads／IG 發文 | 創辦人 |
| 節日版上架後 | 第 11 頁連結改成節日版，重出 PDF | Claude |

提早到 10/13 上架，是為了在節日版上架前先累積名單和反應。

## 怎麼判斷成不成功
- 30 天內下載 ≥ 50 次 → 繼續做同系列（例如 *Before You Start a Free Trial*）。
- 下載者中有人買 Hidden Cost Tracker（Gumroad 可看來源）→ 免費品導流有效。
- 下載 < 20 次 → 問題在曝光，不是內容；檢討發文和簡介連結，不急著做新的小書。

## 風險
| 風險 | 對策 |
| --- | --- |
| 被當成財務建議 | 每頁頁尾「Estimates only, not financial advice」；只給檢查方法不給結論 |
| 規則或數字寫錯 | 只用驗算過的範例；政策類內容只寫 CFPB 查得到的，並寫查證日期 |
| 免費品下載多、付費轉換低 | 正常現象；先看名單成長，30 天後再評估 |
| 時間跟節日版、前情提要撞期 | 內容大多沿用既有素材；若來不及，節日版優先，小書順延 |

## 創辦人決定（2026-10-03）
1. 免費（$0+） ✅
2. 這幾天就上架（不等節日版） ✅
3. 第 10 頁做成可填寫的 PDF 欄位 ✅
4. 書名：*Before You Click "Pay Later"* ✅

## 查證紀錄
- Deferred interest（2026-10-03 查證）：CFPB「How to understand special promotional financing offers on credit cards」與 CFPB 新聞稿「Encourages Retail Credit Card Companies to Consider More Transparent Promotions」。重點：促銷期結束仍有餘額時，利息會從購買日起追溯計算；CFPB 建議改用不追溯的 0% 促銷。
