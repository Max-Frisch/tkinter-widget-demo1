import tkinter as tk
from tkinter import ttk

def button_func():
    # print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar()

# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise

string_var2 = tk.StringVar(value = 'wurst')

entry2 = ttk.Entry(master = window, textvariable = string_var2)
entry2.pack()

entry3 = ttk.Entry(master = window, textvariable = string_var2)
entry3.pack()

label2 = ttk.Label(master = window, text = 'wurst', textvariable = string_var2)
label2.pack()

# run
window.mainloop()