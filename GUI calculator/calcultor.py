import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")

        label_result.config(text=f"Result: {result}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operator.set("")
    label_result.config(text="Result:")

# Main Window
window = tk.Tk()
window.title("GUI Calculator")
window.geometry("300x250")
window.resizable(False, False)

# Input Fields
entry1 = tk.Entry(window, font=("Arial", 12))
entry1.pack(pady=5)

entry2 = tk.Entry(window, font=("Arial", 12))
entry2.pack(pady=5)

# Operator Dropdown
operator = tk.StringVar()
operator.set("+")  # default
operators = ["+", "-", "*", "/"]
op_menu = tk.OptionMenu(window, operator, *operators)
op_menu.pack(pady=5)

# Buttons
btn_calculate = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_calculate.pack(pady=5)

btn_clear = tk.Button(window, text="Clear", command=clear_all, font=("Arial", 12), bg="#f44336", fg="white")
btn_clear.pack(pady=5)

# Result Display
label_result = tk.Label(window, text="Result:", font=("Arial", 14))
label_result.pack(pady=10)

# Run the app
window.mainloop()
