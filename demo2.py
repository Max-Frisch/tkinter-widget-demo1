import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry field
    entry_text = entry.get()

    # update the label
    # label.configure(text = entry_text)
    label['text'] = entry_text
    
    # disable the entry field
    entry['state'] = 'disabled'

def button_func2():
    # set the content of the lable field back to 'Some text'
    label['text'] = 'Some text'
    # enable the entry field again
    entry['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'press me', command = button_func)
button.pack()

button2 = ttk.Button(master = window, text = 'press me too', command = button_func2)
button2.pack()
# run
window.mainloop()