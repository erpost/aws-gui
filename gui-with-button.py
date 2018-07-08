import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title ('First Python GUI')

a_label = ttk.Label(win, text="A GUI Label")
a_label.grid(column=0, row=0)

def click_me():
    """Button Click Event Function"""
    action.configure(text="** I have been Clicked! **")
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')


action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=0)


if __name__ == "__main__":
    win.mainloop()
