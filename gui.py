import tkinter as tk
from tkinter import font
from tkinter import messagebox
import BakenCombinationCalculator as Calc

def calculate():
    try:
        group1 = [i + 1 for i, var in enumerate(group1_vars) if var.get()]
        group2 = [i + 1 for i, var in enumerate(group2_vars) if var.get()]
        group3 = [i + 1 for i, var in enumerate(group3_vars) if var.get()]
        
        #馬連
        umaren_label.config(text=f"　馬連：{Calc.calculate_umaren_formation_points(group1, group2)}点")

        #馬単
        umatan_label.config(text=f"　馬単：{Calc.calculate_umatan_formation_points(group1, group2)}点")

        #3連複
        sanrenpuku_label.config(text=f"３連複：{Calc.calculate_3renpuku_formation_points(group1, group2, group3)}点")

        #3連単
        sanrentan_label.config(text=f"３連単：{Calc.calculate_3rentan_formation_points(group1, group2, group3)}点")

    except ValueError as e:
        messagebox.showerror("エラー", f"入力エラー: {e}")

# GUIの作成
root = tk.Tk()
root.title("競馬フォーメーション点数計算ツール")

# チェックボックスの作成
num_horses = 18

# チェックボックスが変化した時のイベントハンドラ
def on_check_change(var):
    calculate()

# チェックボックス作成
def create_checkboxes(frame, vars_list):
    for i in range(num_horses):
        var = tk.BooleanVar()
        var.trace_add("write", lambda *args: on_check_change(var))
        vars_list.append(var)
        cb = tk.Checkbutton(frame, text=f"{i+1}", variable=var)
        cb.pack(side="left", padx=5, pady=5)

# グループ1
group1_frame = tk.LabelFrame(root, text="1着・1頭目")
group1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
group1_vars = []
create_checkboxes(group1_frame, group1_vars)

# グループ2
group2_frame = tk.LabelFrame(root, text="2着・2頭目")
group2_frame.grid(row=1, column=0, padx=10, pady=10, sticky="n")
group2_vars = []
create_checkboxes(group2_frame, group2_vars)

# グループ3
group3_frame = tk.LabelFrame(root, text="3着・3頭目")
group3_frame.grid(row=2, column=0, padx=10, pady=10, sticky="n")
group3_vars = []
create_checkboxes(group3_frame, group3_vars)

# フォントを作成
default_font = font.nametofont("TkDefaultFont")
result_label_font = default_font.copy()
result_label_font.configure(size=18)

# 馬連
umaren_label = tk.Label(root, text="　馬連：", fg="white", font=result_label_font)
umaren_label.grid(row=4, column=0, sticky="w", padx=30)

# 馬単
umatan_label = tk.Label(root, text="　馬単：", fg="white", font=result_label_font)
umatan_label.grid(row=5, column=0, sticky="w", padx=30)

# 3連複
sanrenpuku_label = tk.Label(root, text="３連複：", fg="white", font=result_label_font)
sanrenpuku_label.grid(row=6, column=0, sticky="w", padx=30)

# 3連単
sanrentan_label = tk.Label(root, text="３連単：", fg="white", font=result_label_font)
sanrentan_label.grid(row=7, column=0, sticky="w", padx=30)

# メインループ
root.mainloop()
