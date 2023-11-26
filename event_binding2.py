import tkinter as tk
from tkinter import ttk

# main window
window = tk.Tk()
window.geometry('600x500')
window.title('Fun with Events')

# widgets
textfield = tk.Text(window)
textfield.pack()

button = ttk.Button(window, text = 'clear text-field', command = lambda: textfield.delete('1.0', 'end'))
button.pack()

# events
window.bind('<KeyPress-Left>', lambda event: textfield.insert('1.end', 'LEFT '))
window.bind('<KeyPress-Right>', lambda event: textfield.insert('1.end', 'RIGHT '))
window.bind('<KeyPress-Up>', lambda event: textfield.insert('1.end', 'UP '))
window.bind('<KeyPress-Down>', lambda event: textfield.insert('1.end', 'DOWN '))

# run
window.mainloop()