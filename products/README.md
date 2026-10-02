# CheckMaybe 商品

每個商品一個資料夾，裡面放：商品檔（PDF／試算表）、`images/`（商品圖）、各平台文案。

| 資料夾 | 商品 | 商品檔 | 平台文案 |
| --- | --- | --- | --- |
| `can-i-sell-this/` | Can I Sell This?（Canva 商用授權） | `Can-I-Sell-This-v3.2.pdf` | `listing-gumroad.md`、`gumroad-fields.md` |
| `can-i-use-this/` | Can I Use This?（AI 圖片商用） | `Can-I-Use-This-v1.1.pdf` | 同上 |
| `can-i-resell-this/` | Can I Resell This?（轉售授權） | `Can-I-Resell-This-v1.0.pdf` | 同上 |
| `free-audit/` | The 5-Minute Pre-Publish Audit（免費） | `The-5-Minute-Pre-Publish-Audit-v1.1.pdf` | 同上 |
| `bundle/` | Complete Toolkit Bundle | `CheckMaybe-Complete-Toolkit-Bundle.zip` | 同上 |
| `hidden-cost-tracker/` | Hidden Cost Tracker（Google Sheets 追蹤表） | `Hidden-Cost-Tracker-Access-Guide.pdf`（買家拿到的檔案）＋ `Hidden-Cost-Tracker.xlsx` | `listing-etsy.md`、`listing-gumroad.md`、`listing-beacons.md` |

## 商品圖命名

- PDF 工具包：`images/<slug>-cover.png`（1280×720）、`-preview.png`、`-featured.png`、`-gumroad-thumb.png`（1200×1200 方形）。Beacons 用 preview 圖。
- Hidden Cost Tracker：`images/etsy/`（4:3，3000×2250）、`images/gumroad/`（封面 16:9＋方形縮圖）、`images/beacons/`（方形 1080×1080）。

## 共用工具

`build/`：PDF 工具包的產生程式（JSON → HTML → PDF、商品圖、輪播圖）。產生的中間檔不進 git。新商品照 `templates/toolkit-product-template.md` 做。
