import tkinter as tk
import math

def append_to_display(text):
    display.insert(tk.END, text)

def calculate_result():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear_display():
    display.delete(0, tk.END)

def create_button(text, row, col, command=None):
    button = tk.Button(
        text=text,
        width=10,
        height=2,
        command=command
    )
    button.grid(row=row, column=col, padx=5, pady=5)

root = tk.Tk()
root.title("Scientific Calculator")

# Create display
display = tk.Entry(root, width=35)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
create_button("7", 1, 0, lambda: append_to_display("7"))
create_button("8", 1, 1, lambda: append_to_display("8"))
create_button("9", 1, 2, lambda: append_to_display("9"))
create_button("/", 1, 3, lambda: append_to_display("/"))

create_button("4", 2, 0, lambda: append_to_display("4"))
create_button("5", 2, 1, lambda: append_to_display("5"))
create_button("6", 2, 2, lambda: append_to_display("6"))
create_button("*", 2, 3, lambda: append_to_display("*"))

create_button("1", 3, 0, lambda: append_to_display("1"))
create_button("2", 3, 1, lambda: append_to_display("2"))
create_button("3", 3, 2, lambda: append_to_display("3"))
create_button("-", 3, 3, lambda: append_to_display("-"))

create_button("0", 4, 0, lambda: append_to_display("0"))
create_button(".", 4, 1, lambda: append_to_display("."))
create_button("=", 4, 2, calculate_result)
create_button("+", 4, 3, lambda: append_to_display("+"))

create_button("sin", 5, 0, lambda: append_to_display("math.sin("))
create_button("cos", 5, 1, lambda: append_to_display("math.cos("))
create_button("tan", 5, 2, lambda: append_to_display("math.tan("))
create_button("sqrt", 5, 3, lambda: append_to_display("math.sqrt("))

create_button("(", 6, 0, lambda: append_to_display("("))
create_button(")", 6, 1, lambda: append_to_display(")"))
create_button("log", 6, 2, lambda: append_to_display("math.log10("))
create_button("exp", 6, 3, lambda: append_to_display("math.exp("))

create_button("Clear", 7, 0, clear_display)

root.mainloop()
