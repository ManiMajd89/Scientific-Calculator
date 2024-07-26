import tkinter as tk
from tkinter import ttk, messagebox
import math

# Initialize the main window
root = tk.Tk()
root.title("Graphical Calculator")
root.geometry("400x600")

style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="#ccc")
style.configure("TEntry", padding=10, font=("Helvetica", 24))

# Entry field
entry = ttk.Entry(root, width=15, font=("Helvetica", 24), justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20)


# Function to update the entry field
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)


# Function to round result to 3 decimal places if it's a decimal
def round_result(value):
    if isinstance(value, float) and not value.is_integer():
        return round(value, 5)
    return value


# Function to handle the evaluation of expressions
def button_equal():
    try:
        current = entry.get()
        expression = current.replace('^', '**') \
            .replace('√', 'math.sqrt') \
            .replace('sin', 'math.sin(math.radians') \
            .replace('cos', 'math.cos(math.radians') \
            .replace('tan', 'math.tan(math.radians') \
            .replace('log', 'math.log10') \
            .replace('^2', '**2') \
            .replace('^3', '**3') \
            .replace('10^', '10**')
        if 'math.sin' in expression or 'math.cos' in expression or 'math.tan' in expression:
            expression += '))' if expression.count('(') < expression.count(')') else ')'

        # Handle special cases like tan(90)
        if 'math.tan' in expression:
            angle = float(current.split('tan(')[1].split(')')[0])
            if angle % 180 == 90:
                raise ValueError("Undefined")

        result = eval(expression)
        result = round_result(result)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input or undefined result")


# Define button layout and colors
button_colors = {
    'default': '#f0f0f0',
    'operator': '#ffcccb',
    'function': '#add8e6'
}

buttons = [
    ('7', 1, 0, button_colors['default']), ('8', 1, 1, button_colors['default']), ('9', 1, 2, button_colors['default']),
    ('/', 1, 3, button_colors['operator']), ('C', 1, 4, button_colors['operator']),
    ('4', 2, 0, button_colors['default']), ('5', 2, 1, button_colors['default']), ('6', 2, 2, button_colors['default']),
    ('*', 2, 3, button_colors['operator']), ('√', 2, 4, button_colors['function']),
    ('1', 3, 0, button_colors['default']), ('2', 3, 1, button_colors['default']), ('3', 3, 2, button_colors['default']),
    ('-', 3, 3, button_colors['operator']), ('(', 3, 4, button_colors['operator']),
    ('0', 4, 0, button_colors['default']), ('.', 4, 1, button_colors['default']),
    ('+', 4, 2, button_colors['operator']), ('=', 4, 3, button_colors['operator']),
    (')', 4, 4, button_colors['operator']),
]

for (text, row, col, color) in buttons:
    if text == '=':
        ttk.Button(root, text=text, command=button_equal, style="TButton").grid(row=row, column=col, sticky="nsew")
    elif text == 'C':
        ttk.Button(root, text=text, command=button_clear, style="TButton").grid(row=row, column=col, sticky="nsew")
    elif text == '√':
        ttk.Button(root, text=text, command=lambda: button_click('√('), style="TButton").grid(row=row, column=col,
                                                                                              sticky="nsew")
    else:
        ttk.Button(root, text=text, command=lambda txt=text: button_click(txt), style="TButton").grid(row=row,
                                                                                                      column=col,
                                                                                                      sticky="nsew")

# Additional scientific functions
scientific_buttons = [
    ('x^2', 5, 0, button_colors['function']), ('x^3', 5, 1, button_colors['function']),
    ('10^x', 5, 2, button_colors['function']), ('1/x', 5, 3, button_colors['function']),
    ('sin', 6, 0, button_colors['function']), ('cos', 6, 1, button_colors['function']),
    ('tan', 6, 2, button_colors['function']), ('log', 6, 3, button_colors['function'])
]

for (text, row, col, color) in scientific_buttons:
    if text == 'x^2':
        ttk.Button(root, text=text, command=lambda: button_click('^2'), style="TButton").grid(row=row, column=col,
                                                                                              sticky="nsew")
    elif text == 'x^3':
        ttk.Button(root, text=text, command=lambda: button_click('^3'), style="TButton").grid(row=row, column=col,
                                                                                              sticky="nsew")
    elif text == '10^x':
        ttk.Button(root, text=text, command=lambda: button_click('10^'), style="TButton").grid(row=row, column=col,
                                                                                               sticky="nsew")
    elif text == '1/x':
        ttk.Button(root, text=text, command=lambda: button_click('1/'), style="TButton").grid(row=row, column=col,
                                                                                              sticky="nsew")
    elif text == 'sin':
        ttk.Button(root, text=text, command=lambda: button_click('sin('), style="TButton").grid(row=row, column=col,
                                                                                                sticky="nsew")
    elif text == 'cos':
        ttk.Button(root, text=text, command=lambda: button_click('cos('), style="TButton").grid(row=row, column=col,
                                                                                                sticky="nsew")
    elif text == 'tan':
        ttk.Button(root, text=text, command=lambda: button_click('tan('), style="TButton").grid(row=row, column=col,
                                                                                                sticky="nsew")
    elif text == 'log':
        ttk.Button(root, text=text, command=lambda: button_click('log('), style="TButton").grid(row=row, column=col,
                                                                                                sticky="nsew")

# Configure grid layout
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()
