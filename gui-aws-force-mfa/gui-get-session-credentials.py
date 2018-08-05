import tkinter as tk
from tkinter import ttk
from creds import getsession


def submit():
    getsession(username_entered.get(), mfa_entered.get())

win = tk.Tk()
win.title('AWS MFA Credentials')
# win.resizable(False, False)

# Create Labels
ttk.Label(win, text='Username:').grid(column=0, row=0)
ttk.Label(win, text='MFA Code:').grid(column=0, row=1)

# Create Text Boxes
username = tk.StringVar()
username_entered = ttk.Combobox(win, width=12, textvariable=username)
username_entered['values'] = ('epost', 'jviar')
username_entered.grid(column=1, row=0)
username_entered.current(0)

mfa = tk.StringVar()
mfa_entered = ttk.Entry(win, width=12, textvariable=mfa)
mfa_entered.grid(column=1, row=1)
mfa_entered.focus()

# Adding a Button
action = ttk.Button(win, text="Submit", command=submit)
action.grid(column=3, row=0)


if __name__ == "__main__":
    win.mainloop()
