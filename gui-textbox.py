import tkinter as tk
from tkinter import ttk


def click_me():
    action.configure(text='Hello ' + name.get())


win = tk.Tk()
win.title("Python GUI")

a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)


if __name__ == "__main__":
    win.mainloop()
