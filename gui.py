import tkinter as tk
from tkinter import messagebox
import BakenCombinationCalculator as Calc

def calculate():
    try:
        group1 = [i + 1 for i, var in enumerate(group1_vars) if var.get()]
        group2 = [i + 1 for i, var in enumerate(group2_vars) if var.get()]
        group3 = [i + 1 for i, var in enumerate(group3_vars) if var.get()]
        bet_type = bet_type_var.get()

        if not group1 or not group2 or not group3:
            raise ValueError("各グループに少なくとも1頭選択してください。")
        
        points = 0
        if bet_type == "馬連":
            points = Calc.calculate_umaren_formation_points(group1, group2)
        elif bet_type == "馬単":
            points = Calc.calculate_umatan_formation_points(group1, group2)
        elif bet_type == "3連複":
            points = Calc.calculate_3renpuku_formation_points(group1, group2, group3)
        elif bet_type == "3連単":
            points = Calc.calculate_3rentan_formation_points(group1, group2, group3)

        print("買い目：" + str(points))

        result_label.config(text=f"{bet_type}の買い目点数: {points}点")

    except ValueError as e:
        messagebox.showerror("エラー", f"入力エラー: {e}")

# GUIの作成
root = tk.Tk()
root.title("競馬フォーメーション点数計算ツール")

# チェックボックスの作成
num_horses = 18

def create_checkboxes(frame, vars_list):
    for i in range(num_horses):
        var = tk.BooleanVar()
        vars_list.append(var)
        cb = tk.Checkbutton(frame, text=f"{i+1}", variable=var)
        cb.pack(side="left", padx=5)

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

# 投票タイプ
options_frame = tk.Frame(root)
options_frame.grid(row=3, column=0, columnspan=3, pady=10)
bet_type_var = tk.StringVar(value="3連複")
tk.Label(options_frame, text="投票タイプ:").pack(side="left")
tk.OptionMenu(options_frame, bet_type_var, "馬連", "馬単", "3連複", "3連単").pack(side="left")

# 計算ボタン
calculate_button = tk.Button(options_frame, text="計算する", command=calculate)
calculate_button.pack(side="left", padx=10)

# 結果ラベル
result_label = tk.Label(root, text="結果がここに表示されます", fg="white")
result_label.grid(row=4, column=0, columnspan=3)

# メインループ
root.mainloop()
