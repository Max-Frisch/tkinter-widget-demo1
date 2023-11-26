import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('800x600')
window.title('Event Binding')

# widgets

text = tk.Text(window)
text.pack()

entry_string = tk.StringVar(value = 'press CTL + down')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

# create a button that resets/clears the text field on click
button = ttk.Button(window, text = 'clear textfield', command = lambda: text.delete("1.0","end"))
button.pack()

# events
# add an event to the entry field, by pressing CTL + DOWN, 
# the fields content will be copied(appended) into the text field
entry.bind('<Control-KeyPress-Down>', lambda event: text.insert('1.0', entry_string.get()))

# run
window.mainloop()