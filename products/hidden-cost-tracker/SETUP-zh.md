# Hidden Cost Tracker 上架前設定（賣家自己做，一次就好）

> **目前進度（2026-10-03 更新）**
> - [x] 追蹤表 v2（深色、彩色標籤、儀表板、圖表），公式驗算 0 錯誤
> - [x] Google Sheets 一次性美化腳本 `sheets_polish.gs`
> - [x] 買家說明 PDF 草稿（連結是佔位字）
> - [x] 母版做好（語言設成美國、時區美東、腳本已刪），`/copy` 連結測試成功
> - [x] 正式版 PDF：`Hidden-Cost-Tracker-Access-Guide.pdf`（這份才上傳 Etsy）
> - [x] Etsy 商品頁文案（標題、13 個標籤、說明、10 張圖規劃）→ `listing-etsy.md`
> - [ ] 照 `listing-etsy.md` 第 5 節的清單截圖 → 做 10 張商品圖
> - [x] Excel 測試（2026-10-03）：數字、圖表正常；勾選框變成 Yes/No 文字（沒有下拉選單，PDF 已改寫）；打勾列的深色底已修正
> - [x] Gumroad 上架（2026-10-03）：https://checkmaybe.gumroad.com/l/kofwfjf
> - [x] Beacons 上架（2026-10-03）：https://shop.beacons.ai/checkmaybe/32876c16-76e3-411e-844c-02265774d312
> - [ ] Etsy 上架（商店審核中；建議 US$8）

## 資料夾內容

| 檔案 | 用途 |
| --- | --- |
| `Hidden-Cost-Tracker.xlsx` | 追蹤表本體。上傳到 Google 雲端硬碟做成母版；也可以附給 Excel 買家 |
| `sheets_polish.gs` | 一次性美化腳本：勾選框、篩選列、深色圖表、公式防誤改提醒 |
| `Hidden-Cost-Tracker-Access-Guide.pdf` | 買家說明 PDF 正式版（連結已填好，上傳到各平台的就是這份） |
| `images/` | 商品圖：`etsy/`、`gumroad/`、`beacons/` 各一個資料夾 |
| `listing-etsy.md` / `listing-gumroad.md` / `listing-beacons.md` | 各平台的商品文案 |
| `build_tracker.py` / `build_guide.mjs` | 重新產生 xlsx / PDF 的程式 |

## 步驟一：做出 Google Sheets 母版（需要電腦，約 5 分鐘）

1. 把 `Hidden-Cost-Tracker.xlsx` 上傳到 Google 雲端硬碟 → 開啟 → 「檔案」→「**儲存為 Google 試算表**」。
2. 在新的試算表點「擴充功能」→「Apps Script」→ 刪掉範例程式 → 貼上 `sheets_polish.gs` 的全部內容 → 儲存。
3. 上方的函式選單選 `polishTemplate` → 按「執行」。
   - 第一次會要求授權。如果出現「Google 尚未驗證這個應用程式」，點「進階」→「前往（不安全）」。這是你自己的腳本，只會存取這一份檔案。
4. 右下角出現「Hidden Cost Tracker polished」就完成了。
5. 回到 Apps Script，**把程式碼刪掉並儲存**。勾選框和圖表已經存在檔案裡，刪掉程式碼不會讓它們消失。

## 步驟二：設定分享、取得 /copy 連結

1. 右上角「共用」→「一般存取權」改成「**知道連結的使用者**」，角色選「**檢視者**」。
2. 複製連結，把結尾的 `/edit...` 改成 `/copy`：
   ```
   https://docs.google.com/spreadsheets/d/檔案ID/copy
   ```
3. 用無痕視窗開這個連結測試：應該會跳出「建立副本」。

## 步驟三：產生正式版買家 PDF

把 /copy 連結給我，或在電腦上執行：
```
node build_guide.mjs "https://docs.google.com/spreadsheets/d/檔案ID/copy"
```
會產生 `Hidden-Cost-Tracker-Access-Guide.pdf`（沒有 DRAFT 字樣），這份才是要上傳到 Etsy 的數位檔案。

## 注意

- 母版只當「模具」，自己記帳請另外複製一份。
- 改了母版之後，舊買家不會自動更新；他們重新點連結就能拿到新版。
- 上架前先用手機的 Google Sheets App 開一次副本，確認顯示正常。
