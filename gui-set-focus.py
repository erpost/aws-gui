import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Modified Button Click Function
def click_me():
    action.configure(text='Hello ' + name.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=1, row=0)
# Set Cursor in Textbox
name_entered.focus()

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)
action.configure(state='enabled')


if __name__ == "__main__":
    win.mainloop()
