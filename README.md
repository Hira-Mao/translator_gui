# スウェーデン語翻訳ツール（GUI）

日本語→スウェーデン語の翻訳を行うGUIツールです。
翻訳結果を画面上に表示し、音声で読み上げも行えます。

## 🛠 使用技術・ライブラリ

- Python
- tkinter（GUI）
- deep-translator（翻訳）
- gTTS（音声生成）
- playsound（音声再生）

## 💻 使い方（ローカル実行）

1. 以下をインストールしてください
pip install deep-translator gTTS playsound==1.2.2 pyobjc

2. スクリプトを実行
python translator_gui.py

※ `pyobjc` はMacで音声再生に必要です

## 📌 注意点

- `playsound` は1.2.2以外だと動作不安定になることがあります
- Windowsでは音声再生部分が異なる挙動になる可能性があります

## 📄 ライセンス

MIT
