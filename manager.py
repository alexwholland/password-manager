import sqlite3, hashlib
from tkinter import *

window = Tk()

window.title("Password Manager")

def loginScreen():
    window.geometry("250x100")

    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20)
    txt.pack()

    btn = Button(window, text="Submit")
    btn.pack(pady=10)

loginScreen()
window.mainloop()