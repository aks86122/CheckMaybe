# CheckMaybe｜Building in public（英文週報＋英文 Reels）｜v1 2026-10-04

創辦人提議：用英文公開 CheckMaybe 的真實創業過程（週報、踩坑），英文 Reels 也一起發。

## 為什麼可行
- CheckMaybe 最大的問題是沒有英文受眾。「從台灣一個人做英文數位商品」的真實紀錄，本身就是英文社群會追的內容（build in public），比單純推商品容易被看見。
- 也符合品牌：Check before you pay／先檢查再投入。

## 規則
- **只寫 CheckMaybe 自己的事**：商品、上架、平台審核、流量、銷售、時間、花費。不提重生引路人、不提負債或個人財務、不提副業實驗室（三個品牌分開）。
- **數字只用真的**：Gumroad／Etsy／Beacons 後台、社群洞察。沒有就寫 0 或留空，不估算。收入只算已入帳（扣掉平台手續費、退款）。
- 不寫收入保證、不炫耀、不拿別人的收入比較。
- 英文要自然、短句；每篇都由 Claude 產出、創辦人確認後再發。

## 每週流程
1. 日誌（https://claude.ai/artifact/4BP7drVyBctBXe9dVrUyki）選品牌「CheckMaybe」記錄時間、花費、收入、踩坑。
2. 週日把後台數字（page views、sales、free downloads、revenue）給 Claude。
3. Claude 產生 `weeks/<年>-W<週>.json` → `python3 build-in-public/weekly_report_en.py build-in-public/weeks/<檔名>.json` → 週報圖。
4. 同時產出 Threads／IG／FB 英文文案，踩坑寫成一則短文或一支 Reels。

## 英文 Reels
- 剪輯節奏同副業實驗室（20～30 秒、每畫面 3～4 秒、1.25～1.3 倍速、IG 內建輕快音樂）。
- 字幕英文、品牌色：深底 `#15171F`＋橘 `#F08A4B`。
- 題材：上架被拒、商品頁改版前後、第一筆銷售、平台規則（例如新帳號留言被判垃圾訊息）。

## 已有、可以寫成英文踩坑的素材（創辦人確認後再發）
| 日期 | 坑 | 可寫成 |
| --- | --- | --- |
| 2026-10-04 | 申請 Impact 時誤點品牌方價目表；推廣者 Marketplace 申請被拒 | "I applied to an affiliate network on day 1. Here's why it said no." |
| 2026-10-04 | YNAB 聯盟計畫只接受邀請 | "Not every affiliate program is open. What I learned." |
| 2026-10 | 定位太散（Canva 授權＋分期成本＋節日版） | "I had 3 products for 3 different people. Here's how I'm narrowing it." |

## 第一篇草稿（Threads，待創辦人確認）
```
I'm building small money tools from Taiwan, in English, with zero audience.

So far: 1 Google Sheets tracker, 1 free PDF guide, 0 followers to speak of.

Every Sunday I'll post the real numbers: time in, money spent, sales, mistakes.
Even when it's zero.

Week 1 starts now.
```
