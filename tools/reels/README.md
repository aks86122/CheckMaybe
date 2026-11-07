# 短影音自動剪輯（CheckMaybe）

把手機錄的原始素材，自動剪成9:16、1080×1920的短影音：
- 剪掉講話中間的停頓
- 字幕跟著講話一句一句跳出來，重點字換成品牌色
- 指定的關鍵句會放大彈出

## 用法（Claude執行）
```
bash tools/reels/setup.sh          # 每個新對話跑一次
python3 tools/reels/autocut.py 原始.mp4 輸出.mp4 --brand tools/reels/brand.json \
  --keywords 關鍵字1,關鍵字2 --punch 要放大的句子 --fix 聽錯的字=正確的字
```
- 字幕有錯：改 `輸出.words.json` 或加 `--fix`，再加 `--transcript 輸出.words.json` 重跑（不用重新辨識，幾秒鐘）。
- 不要剪停頓：加 `--no-cut`。
- 字幕不加標點，也不會出現破折號。

## 品牌注意
- No face. Screen recordings, receipts, hands, plus the founder's own voice. English captions.
- Highlight dollar amounts and APR numbers with --keywords.
