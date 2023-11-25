import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Buttons!')
window.geometry('600x400')

# button
def button_func():
    print('A basic button..')

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(
    window,
    text = 'A simple button',
    textvariable = button_string,
    command = button_func
)
button.pack()

# checkbutton
check_var = tk.IntVar()
check = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 1,
    offvalue = 0
)
check.pack()

# radiobuttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'radiobutton 1',
    value = 1,
    variable = radio_var,
    command = lambda: print(radio_var.get())
)
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'radiobutton 2',
    value = 2,
    variable = radio_var,
    command = lambda: print(radio_var.get())
)
radio2.pack()

# run
window.mainloop()