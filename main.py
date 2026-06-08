import tkinter as tk
from Add_operation import add
from Sub_operation import subt
from mult_operation import multi
from divn_operation import div

# GUI setup
root = tk.Tk()
root.title("OOP Calculator")

entry_x = tk.Entry(root, width=10, font=('Arial', 16))
entry_x.grid(row=0, column=0, padx=5, pady=5)
entry_y = tk.Entry(root, width=10, font=('Arial', 16))
entry_y.grid(row=0, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="Result:", font=('Arial', 16))
result_label.grid(row=1, column=0, columnspan=2)

def perform_operation(operation_class):
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        op = operation_class()
        result = op.calc(x, y)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

# Buttons
tk.Button(root, text="+", width=5, height=2, command=lambda: perform_operation(add)).grid(row=2, column=0)
tk.Button(root, text="-", width=5, height=2, command=lambda: perform_operation(subt)).grid(row=2, column=1)
tk.Button(root, text="×", width=5, height=2, command=lambda: perform_operation(multi)).grid(row=3, column=0)
tk.Button(root, text="÷", width=5, height=2, command=lambda: perform_operation(div)).grid(row=3, column=1)

root.mainloop()