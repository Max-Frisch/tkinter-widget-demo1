import tkinter as tk
from tkinter import ttk

# window setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

# Combobox
items = ('Ice Cream', 'Pizza', 'Broccoli', 'Wurst')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
# combo.configure('values = items)
combo.pack()

# Combobox - label
combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# Combobox events
combo.bind(
    '<<ComboboxSelected>>',
    lambda event: combo_label.configure(text = f'Selected value: {food_string.get()}')
)

# Spinbox
spin_int = tk.IntVar(value = 0)
spin = ttk.Spinbox(
    window,
    from_ = 1,
    to = 31,
    increment = 1,
    command = lambda: print(f'selected value: {spin_int.get()}'),
    textvariable = spin_int
)
spin.pack()

# Spinbox events
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))


# Spinbox exercise
spin_var = tk.IntVar()
spin1 = ttk.Spinbox(window, textvariable = spin_var)
spin1['value'] = ()
spin1.pack()
spin1.bind('<<Decrement>>', lambda event: print('the value is decreased'))



# run
window.mainloop()