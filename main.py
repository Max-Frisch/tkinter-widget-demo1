import tkinter as tk

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# create widgets
textfield = tk.Text(master = window)
textfield.pack()

# run
window.mainloop()