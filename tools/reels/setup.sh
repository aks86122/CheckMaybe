#!/usr/bin/env bash
# One-time setup per cloud session (the container is reset between sessions).
set -e
pip install -q faster-whisper opencc-python-reimplemented
mkdir -p ~/.cache/reels-fonts
for w in Black Bold; do
  f=~/.cache/reels-fonts/NotoSansCJKtc-$w.otf
  [ -s "$f" ] || curl -sSL -o "$f" "https://cdn.jsdelivr.net/gh/notofonts/noto-cjk@main/Sans/OTF/TraditionalChinese/NotoSansCJKtc-$w.otf"
done
echo "reels tools ready"
