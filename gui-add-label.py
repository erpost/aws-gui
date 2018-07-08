import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title ('First Python GUI')

ttk.Label(win, text = 'A GUI Label').grid(column=0, row=0)

if __name__ == "__main__":
    win.mainloop()
