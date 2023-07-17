import math
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("科學計算機")

        # 設定視窗的大小
        master.geometry("300x500")  # Adjust window size to accommodate history

        self.entry = tk.Entry(master, font=('arial', 20, 'bold'), bd=15, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '+', 'sin',
            '4', '5', '6', '-', 'cos',
            '1', '2', '3', '*', 'tan',
            '0', '.', '=', '/', 'sqrt',
            '(', ')', 'C', 'exp', 'log10'  # Added log10 functionality
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            # 增大每個按鈕的大小
            tk.Button(master, text=button, command=lambda button=button: self.click(button), height=2, width=5, bg='light blue', fg='black', font=('Helvetica', '10')).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        # Create history area
        self.history = tk.Text(master, state='disabled', height=5, width=20)
        self.history.grid(row=6, column=0, columnspan=5)

        # Create help menu
        menu = tk.Menu(master)
        master.config(menu=menu)

        help_menu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=self.show_help)

        # Bind keyboard keys
        master.bind("<Return>", self.enter_key)
        master.bind("<KP_Enter>", self.enter_key)
        for i in range(10):
            master.bind(str(i), self.number_key)

    def click(self, button):
        if button == "=":
            try:
                result = eval(self.entry.get(), {"__builtins__": None}, {"math": math, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log10": math.log10, "exp": math.exp, "pi": math.pi})
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))

                # Add to history
                self.history.config(state='normal')
                self.history.insert('end', self.entry.get() + '\n')
                self.history.config(state='disabled')
            except Exception as e:
                messagebox.showerror("錯誤", str(e))
        elif button == "C":
            self.entry.delete(0, 'end')
        else:
            self.entry.insert('end', button)

    def show_help(self):
        messagebox.showinfo("Help", "This is a scientific calculator.\nYou can perform mathematical operations like addition, subtraction, etc.")

    def enter_key(self, event):
        self.click("=")

    def number_key(self, event):
        self.click(event.char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
