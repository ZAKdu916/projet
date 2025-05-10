import tkinter as tk


def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")

def add_to_expression(value):
    entry.insert(tk.END, value)

def clear_expression():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculatrice")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 0
col = 0
for button in buttons:
    if button == '=':
        tk.Button(buttons_frame, text=button, font=("Arial", 18), height=2, width=4, 
                  command=evaluate_expression).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(buttons_frame, text=button, font=("Arial", 18), height=2, width=4, 
                  command=clear_expression).grid(row=row, column=col)
    else:
        tk.Button(buttons_frame, text=button, font=("Arial", 18), height=2, width=4, 
                  command=lambda b=button: add_to_expression(b)).grid(row=row, column=col)

    col += 1
    if col == 4:
        row += 1
        col = 0

root.mainloop()
