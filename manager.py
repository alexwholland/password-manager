from tkinter import *

window = Tk()

window.title("Password Manager")


def createMasterPassword():
    """
    Create a master password for the manager
    """
    window.geometry("250x170")

    lbl = Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter Password")
    lbl1.pack()

    txt1 = Entry(window, width=20)
    txt1.pack()
    txt1.focus()

    lbl2 = Label(window)
    lbl2.pack()

    def savePassword():
        """
        Check if the entered master password matches
        """
        if txt.get() == txt1.get():
            pass
        else:
            lbl2.config(text="Passwords do not match", fg='#FF0000')

    btn = Button(window, text="Save", command=savePassword)
    btn.pack(pady=10)


def loginScreen():
    """
    Login Screen for a user with a pre-existing master password
    """
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
        """
        Check that the master password is valid
        """
        password = "test"
        if password == txt.get():
            passwordManager()
        else:
            txt.delete(0, 'end')
            lbl1.config(text="Wrong Password")

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=10)


def passwordManager():
    """
    Main password manager interface
    """
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("700x350")

    lbl = Label(window, text="Password Manager")
    lbl.config(anchor=CENTER)
    lbl.pack()


createMasterPassword()
# loginScreen()
window.mainloop()
