# CheckMaybe：平台互相導流（2026-11-07，J決定照這個做）

原則：陌生人從搜尋進來 → 先拿免費的 → 留下email → 再買付費的。每一步只多一次點擊。

## 每個平台的角色

| 平台 | 角色 | 導去哪 |
|---|---|---|
| Pinterest | 帶陌生人進來（搜尋） | 直接連Gumroad商品頁（不經過Beacons），網址加UTM |
| FB | 信任、觀點 | Substack文章，或Beacons |
| Substack | 長文、收email | 每篇文末只放一個對應的Gumroad商品 |
| Beacons | IG／FB／Threads簡介的總入口 | 免費商品、付費商品、Substack訂閱 |
| Gumroad | 結帳、拿到買家email | 收據和PDF邀請訂閱Substack；Workflows自動信推下一個商品 |

```
Pinterest Pin ───────────→ Gumroad（免費小書或付費試算表）
FB貼文 ─→ Substack文章 ──→ Gumroad
IG / Threads簡介 ─→ Beacons ─→ Gumroad / Substack
Gumroad收據、PDF、自動信 ─→ Substack ─→ 下一個商品
```

## 商品網址（Gumroad）

| 商品 | 網址 |
|---|---|
| Before You Click "Pay Later"（免費） | https://checkmaybe.gumroad.com/l/cbmfye |
| Hidden Cost Tracker | https://checkmaybe.gumroad.com/l/kofwfjf |
| Holiday Hidden Cost Tracker | https://checkmaybe.gumroad.com/l/nhbkwx |
| Debt Payoff Planner | https://checkmaybe.gumroad.com/l/ddktis |
| Debt Toolkit Bundle | https://checkmaybe.gumroad.com/l/gdaiyy |

Substack：https://checkmaybe.substack.com · Beacons：https://beacons.ai/checkmaybe

## 每個平台要做的事

**Pinterest**
- Pin的連結直接放Gumroad網址，加 `?utm_source=pinterest&utm_medium=social&utm_campaign=<pin id>`。
- 一半推免費小書（cbmfye），一半推付費商品。
- 第一批：`content/pinterest/2026-11/pins-v12.md`（Print塗色表3張，連Debt Payoff Planner）。
- 個人檔案網站連結維持 checkmaybe.gumroad.com。

**Substack**
- 每篇文末只放一個相關商品：先買後付 → Hidden Cost Tracker；還債 → Debt Payoff Planner；節日 → Holiday tracker。
- 文章裡可以放Pin的圖。About頁放Beacons連結。

**FB**
- 短版重點，連Substack全文；粉專按鈕和簡介放Beacons。

**Beacons（由上到下）**
1. 免費：Before You Click "Pay Later"
2. Debt Payoff Planner（用 `-beacons-print.png`）
3. Debt Toolkit Bundle
4. 訂閱Substack

**Gumroad**
- 每個商品的收據訊息最後加Substack邀請（`02-gumroad-emails.md`）。
- Workflows自動信：免費小書下載後第3天、第7天各一封；Debt Payoff Planner買家第2天一封。
- 每個商品頁最下面放Substack連結。

## 每月檢查一次
- Gumroad › Analytics：每筆銷售的來源網站（pinterest.com、substack.com、beacons.ai、facebook.com）。
- Pinterest Analytics：曝光、儲存、外連點擊。外連點擊最多的Pin，做2到3個新版本。
- 帶單最多的來源加碼內容，沒有點擊的停掉。
