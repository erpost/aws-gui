import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")


# Modified Button Click Function
def click_me():
    action.configure(text='Hello ' + name.get() + number_chosen.get())
    print(number)
    print(number.get())


# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)                          # column 0
name_entered.focus()

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)                                # <= change column to 2

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)                         # <= Combobox in column 1
number_chosen.current(0)


if __name__ == "__main__":
    win.mainloop()
