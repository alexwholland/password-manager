import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Manager")


def loginScreen():
    window.geometry("250x120")

    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    # Should be txt = Entry(window, width=20, show="*") in final product
    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def checkPassword():
        password = "test"
        if password == txt.get():
            passwordVault()
        else:
            lbl1.config(text="Wrong Password")

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=10)


def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("700x350")

    lbl = Label(window, text="Password Manager")
    lbl.config(anchor=CENTER)
    lbl.pack()


loginScreen()
window.mainloop()
