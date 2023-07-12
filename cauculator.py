import math
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("科學計算機")

        # 設定視窗的大小
        master.geometry("300x400")

        self.entry = tk.Entry(master, font=('arial', 20, 'bold'), bd=15, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '+', 'sin',
            '4', '5', '6', '-', 'cos',
            '1', '2', '3', '*', 'tan',
            '0', '.', '=', '/', 'sqrt',
            '(', ')', 'C', 'exp', 'log'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            # 增大每個按鈕的大小
            tk.Button(master, text=button, command=lambda button=button: self.click(button), height=2, width=5).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click(self, button):
        if button == "=":
            try:
                result = eval(self.entry.get(), {"__builtins__": None}, {"math": math, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "exp": math.exp, "pi": math.pi})
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))
            except Exception as e:
                messagebox.showerror("錯誤", str(e))
        elif button == "C":
            self.entry.delete(0, 'end')
        else:
            self.entry.insert('end', button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
