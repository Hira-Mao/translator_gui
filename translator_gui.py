import tkinter as tk
from tkinter import messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

def translate_text():
    japanese = input_text.get("1.0", "end").strip()
    if not japanese:
        messagebox.showwarning("入力エラー", "日本語のテキストを入力してね！")
        return
    try:
        swedish = GoogleTranslator(source='ja', target='sv').translate(japanese)
        output_text.delete("1.0", "end")
        output_text.insert("end", swedish)
    except Exception as e:
        messagebox.showerror("翻訳エラー", str(e))

def play_audio():
    swedish = output_text.get("1.0", "end").strip()
    if not swedish:
        messagebox.showwarning("音声エラー", "翻訳結果がありません。まず翻訳してね。")
        return
    try:
        tts = gTTS(swedish, lang='sv')
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
    except Exception as e:
        messagebox.showerror("音声再生エラー", str(e))

# GUI設定
root = tk.Tk()
root.title("スウェーデン語翻訳ツール")
root.geometry("600x500")
root.configure(bg="#e0f7fa")

font_main = ("Helvetica", 13)

# スタイル用カラー
btn_color = "#4dd0e1"  # 明るい水色
btn_hover = "#26c6da"
text_bg = "#ffffff"

# 日本語入力
tk.Label(root, text="日本語入力", bg="#e0f7fa", font=("Helvetica", 14, "bold")).pack(pady=(15, 5))
input_text = tk.Text(root, height=5, font=font_main, wrap="word", bg=text_bg, relief="groove", bd=2)
input_text.pack(padx=20, fill="x")

# ボタンエリア
btn_frame = tk.Frame(root, bg="#e0f7fa")
btn_frame.pack(pady=15)

translate_btn = tk.Button(
    btn_frame, text="翻訳する", command=translate_text,
    font=font_main, bg=btn_color, fg="white", padx=20, pady=10,
    relief="flat", bd=0, highlightthickness=0
)
translate_btn.pack(side="left", padx=10)
translate_btn.configure(cursor="hand2")

speak_btn = tk.Button(
    btn_frame, text="音声を再生", command=play_audio,
    font=font_main, bg=btn_color, fg="white", padx=20, pady=10,
    relief="flat", bd=0, highlightthickness=0
)
speak_btn.pack(side="left", padx=10)
speak_btn.configure(cursor="hand2")


# 出力欄
tk.Label(root, text="スウェーデン語出力", bg="#e0f7fa", font=("Helvetica", 14, "bold")).pack(pady=(5, 5))
output_text = tk.Text(root, height=5, font=font_main, wrap="word", bg=text_bg, relief="groove", bd=2)
output_text.pack(padx=20, fill="x")

root.mainloop()
