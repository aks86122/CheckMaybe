# CheckMaybe 工具包產品模板

所有 CheckMaybe 決策工具包（PDF／Workbook）都照這份模板製作與更新。
範例：`Can I Sell This?`（Canva 版，v3.1）、`Can I Use This?`（AI 版，v1.1）。
產品內文一律英文；本說明為繁體中文。

---

## 一、製作流程（每個新產品、每次改版都走一遍）

| 步驟 | 做什麼 | 誰 | 產出（存在 `planning/<YYYY-MM>-<product>/`） |
| --- | --- | --- | --- |
| 1. 定題 | 目標買家、要回答的「能不能賣／能不能用」問題、涵蓋哪些平台 | 趨勢研究員 | `01-research.md` |
| 2. 存官方來源 | 創辦人把每個要引用的官方頁面存成網頁檔／PDF 上傳（環境會被 Cloudflare 擋，不能自動抓） | 創辦人 | 上傳檔 + 來源清單（網址、生效日、存檔日） |
| 3. 寫初稿 | 照下方「頁面結構」寫英文內容 | 內容創作者 | 產品檔 |
| 4. 逐條核對 | 每一句事實對照官方原文，分 ✅ ⚠️ ❌ ❓ | 法遵檢查員 | `0X-verification.md` |
| 5. 逐頁修改稿 | 原文 → 改成 → 原因，創辦人照著換字 | 內容創作者 | `0X-revision.md` |
| 6. 上架前檢查 | 跑完第四節「上架前檢查清單」 | 創辦人 | — |
| 7. 上架素材 | 商品說明、封面圖／預覽圖／精選內容圖、Gumroad 方形縮圖、Gumroad 欄位（Additional details、Button text ≤26 字、Custom message ≤500 字） | 內容創作者 | `products/listings/`、`products/images/`、`products/gumroad/` |
| 8. 發布 | 創辦人自己上傳 Gumroad／Beacons（團隊不代發） | 創辦人 | — |

**規則：** 沒有 ✅ 或官方依據的句子不上架；❓ 的句子要改成「VERIFY BEFORE RELYING」或刪掉。

---

## 二、頁面結構（標準順序）

| # | 頁面 | 必要內容 |
| --- | --- | --- |
| 1 | **Cover** | 產品名 `Can I ___ This?`、副標 `A ___ Toolkit for ___`（第三方品牌只能出現在 `for ___ Sellers/Creators` 這種描述位置）、`CHECKMAYBE` 品牌、版本號、`EDUCATIONAL INFORMATION, NOT LEGAL ADVICE`、`NOT AFFILIATED WITH ___`、`___ IS A TRADEMARK OF ITS RESPECTIVE OWNER` |
| 2 | **Start Here / Disclaimer** | 怎麼用這本、這是決策輔助不是判決、使用者要自己確認最新官方條款、何時該找專業意見 |
| 3 | **Key distinctions** | 容易混為一談的幾個問題（例：商用許可 ≠ 著作權歸屬 ≠ 第三方權利 ≠ 平台／市集規則） |
| 4 | **Decision path / Quick map** | 5–8 步的判斷流程，每個出口對應燈號 |
| 5 | **Rules reference（Cases）** | 每張卡：規則一句話 + 官方出處（文件名＋節次）+ `BEFORE PUBLISHING` 提醒 |
| 6 | **Platform / tool snapshots**（需要時） | PRODUCT · PLAN DIFFERENCES · COMMERCIAL-USE LANGUAGE · OUTPUT/CONTENT RIGHTS · RESTRICTIONS · THIRD-PARTY WARNING · OFFICIAL SOURCE（網址＋生效日）· VERIFIED（月份）＋ 狀態標籤 |
| 7 | **Marketplace layer** | 賣場規則（至少 Etsy；之後加 Gumroad、Amazon KDP、POD 平台）：原創要求、揭露要求、禁止品項 |
| 8 | **Scenarios（15–20 個）** | 每個情境：THE SITUATION · 燈號 · WHY（一行）· WHAT TO CHECK（具體，不要每個都一樣）· WATCH OUT FOR · BEFORE YOU PUBLISH 1-2-3 · WHAT COULD CHANGE THIS |
| 9 | **Red flags** | 任一出現就停下來 |
| 10 | **Pre-publish checklist** | 10 項左右，含「市集規則」具體項目 |
| 11 | **Worksheets** | 素材／來源追蹤表、產品稽核表、給買家的權利聲明 |
| 12 | **Hierarchy / quick reference** | 風險由低到高的一頁總覽 |
| 13 | **Sources** | 每個官方來源：名稱、網址、生效／更新日、`Verified <日期>`；官方說法互相矛盾時列出並註明採用較嚴格解讀 |

頁尾格式：`<PRODUCT NAME> — <SUBTITLE> · CHECKMAYBE` ＋ 頁碼。

---

## 三、寫作規則

### 燈號（取代籠統的 CHECK / VERIFY）

| 燈號 | 意思 | 必附 |
| --- | --- | --- |
| **GREEN-LEANING** | 官方條款明確支持，一般情況可行 | 條件（在什麼前提下成立） |
| **AMBER** | 取決於具體條件，或官方沒有明說 | 要確認的那一點 |
| **RED** | 官方明文禁止，或高風險 | 官方出處 |
| **VERIFY BEFORE RELYING** | 這一輪沒拿到官方原文核對 | 下次要補的來源 |

每個燈號都加一行 `What could change this:`。永遠不寫「guaranteed」「100% safe」「you can definitely」。

### 引用
- 引官方條款要保留限定語（例：`As between you and OpenAI, and to the extent permitted by applicable law`），不可為了簡短刪掉。
- 用買家所在地區適用的版本（美國市場用美國版，註明歐盟／英國另有條款）。
- 官方來源互相矛盾時：採較嚴格解讀，並寫 `Official sources differ on this point`。
- 絕對規則就寫成絕對（官方寫 cannot 就不要寫 generally）。

### 品牌與法律
- 第三方品牌名不放在產品名稱、網址、帳號；只用描述性寫法（`for Canva Sellers`）。
- 不用第三方標誌。
- 每頁頁尾有 `CHECKMAYBE`；封面有 not affiliated + trademark 聲明。
- 定位是教育工具，不是法律代理；不承諾更新期限以外的服務。

### 版本
- 小修（改字、補來源）：`x.1`、`x.2`；結構或規則大改：`x+1.0`。
- 每次改版都要重新核對 Sources 頁的每個日期。

---

## 四、上架前檢查清單

- [ ] 核對報告中沒有未處理的 ❌
- [ ] 所有 ❓ 已改成 `VERIFY BEFORE RELYING` 或刪除
- [ ] Sources 頁每個來源都有網址、生效日、`Verified` 日期
- [ ] 封面／頁尾：產品名、副標、CHECKMAYBE、版本號、免責聲明、not affiliated、trademark
- [ ] 產品名稱、商品網址、Gumroad／Beacons 標題沒有把第三方品牌當成產品名
- [ ] 至少有一頁市集規則（Etsy 起跳）
- [ ] 每個情境都有燈號 + WHY + What could change this
- [ ] Gumroad／Beacons 的商品說明和 PDF 內容一致（版本號、承諾）
- [ ] Gumroad 欄位齊全：Additional details（Format、Includes、Best for、Language、Version、Note）、Button text、Custom message（寫明從第幾頁開始、不是法律建議），字數在限制內
- [ ] Gumroad 方形縮圖（≥600×600）放在 `products/gumroad/thumbnails/`

---

## 五、逐頁修改稿格式（改版時用）

```markdown
## Page N — <頁面標題>
狀態：不變／修改／新增

**原文 (Current):** <目前的英文原文>
**改成 (New):** <新的英文>
**原因:** <一行中文，註明核對報告或官方節次，例如 CLA §9>
```

新頁面標 `NEW PAGE — insert after page N`。
