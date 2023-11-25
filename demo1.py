import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed!')

def button_func2():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# tk.text
textfield = tk.Text(master = window)
textfield.pack()

# ttk label
label = ttk.Label(master = window, text= 'This is a test')
label.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# another ttk label
label2 = ttk.Label(master = window, text = 'my label')
label2.pack()
# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

# another ttk button
button2 = ttk.Button(master = window, text = 'press me', command = button_func2)
button2.pack()

# run
window.mainloop()