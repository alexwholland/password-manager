import sqlite3, hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial
import uuid
import pyperclip

# database code
with sqlite3.connect('password_vault.db') as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL,
recoveryKey TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")


# Create PopUp
def popUp(text):
    answer = simpledialog.askstring("input string", text)

    return answer


# Initiate window
window = Tk()
window.update()

window.title("Password Vault")


def hashPassword(input):
    hash1 = hashlib.sha256(input)
    hash1 = hash1.hexdigest()

    return hash1


def createMasterPassword():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('250x125')
    lbl = Label(window, text="Choose a Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-enter password")
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack()

    def savePassword():
        """
        Check if the entered master password matches
        """
        if txt.get() == txt1.get():
            sql = "DELETE FROM masterpassword WHERE id = 1"

            cursor.execute(sql)

            hashedPassword = hashPassword(txt.get().encode('utf-8'))
            key = str(uuid.uuid4().hex)
            recoveryKey = hashPassword(key.encode('utf-8'))


            insert_password = """INSERT INTO masterpassword(password, recoveryKey)
            VALUES(?, ?) """
            cursor.execute(insert_password, ((hashedPassword), (recoveryKey)))
            db.commit()

            recoveryScreen(key)
        else:
            lbl.config(text="Passwords dont match")

    btn = Button(window, text="Save", command=savePassword)
    btn.pack(pady=5)


def recoveryScreen(key):
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('250x125')
    lbl = Label(window, text="Save this key to be able to recover account")
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl1 = Label(window, text=key)
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    def copyKey():
        pyperclip.copy(lbl1.cget("text"))

    btn = Button(window, text="Copy Key", command=copyKey)
    btn.pack(pady=5)

    def done():
        mainScreen()

    btn = Button(window, text="Done", command=done)
    btn.pack(pady=5)


def resetScreen():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('250x125')
    lbl = Label(window, text="Enter Recovery Key")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20)
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    def getRecoveryKey():
        recoveryKeyCheck = hashPassword(str(txt.get()).encode('utf-8'))
        cursor.execute('SELECT * FROM masterpassword WHERE id = 1 AND recoveryKey = ?', [(recoveryKeyCheck)])
        return cursor.fetchall()

    def checkRecoveryKey():
        checked = getRecoveryKey()

        if checked:
            createMasterPassword()
        else:
            txt.delete(0, 'end')
            lbl1.config(text='Wrong Key')

    btn = Button(window, text="Check Key", command=checkRecoveryKey)
    btn.pack(pady=5)


def loginScreen():
    """
    Login Screen for a user with a pre-existing master password
    """
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry('250x125')

    lbl = Label(window, text="Enter  Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.config(anchor=CENTER)
    lbl1.pack(side=TOP)

    def getMasterPassword():
        checkHashedPassword = hashPassword(txt.get().encode('utf-8'))
        global encryptionKey
        #encryptionKey = base64.urlsafe_b64encode(kdf.derive(txt.get().encode()))
        cursor.execute('SELECT * FROM masterpassword WHERE id = 1 AND password = ?', [(checkHashedPassword)])
        return cursor.fetchall()

    def checkPassword():
        password = getMasterPassword()

        if password:
            mainScreen()
        else:
            txt.delete(0, 'end')
            lbl1.config(text="Wrong Password")

    def resetPassword():
        resetScreen()

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=5)

    btn = Button(window, text="Reset Password", command=resetPassword)
    btn.pack(pady=5)


def mainScreen():
    for widget in window.winfo_children():
        widget.destroy()

    def addEntry():
        text1 = "Website"
        text2 = "Username"
        text3 = "Password"

        website = popUp(text1)
        username = popUp(text2)
        password = popUp(text3)

        insert_fields = """INSERT INTO vault(website, username, password) 
        VALUES(?, ?, ?) """
        cursor.execute(insert_fields, (website, username, password))
        db.commit()

        mainScreen()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()
        mainScreen()

    window.geometry('750x550')
    window.resizable(height=None, width=None)
    lbl = Label(window, text="Password Vault")
    lbl.grid(column=1)

    btn = Button(window, text="+", command=addEntry)
    btn.grid(column=1, pady=10)

    lbl = Label(window, text="Website")
    lbl.grid(row=2, column=0, padx=80)
    lbl = Label(window, text="Username")
    lbl.grid(row=2, column=1, padx=80)
    lbl = Label(window, text="Password")
    lbl.grid(row=2, column=2, padx=80)

    cursor.execute('SELECT * FROM vault')
    if (cursor.fetchall() != None):
        i = 0
        while True:
            cursor.execute('SELECT * FROM vault')
            array = cursor.fetchall()

            if (len(array) == 0):
                break

            lbl1 = Label(window, text=(array[i][1], encryptionKey), font=("Helvetica", 12))
            lbl1.grid(column=0, row=(i + 3))
            lbl2 = Label(window, text=(array[i][2], encryptionKey), font=("Helvetica", 12))
            lbl2.grid(column=1, row=(i + 3))
            lbl3 = Label(window, text=(array[i][3], encryptionKey), font=("Helvetica", 12))
            lbl3.grid(column=2, row=(i + 3))

            btn = Button(window, text="Delete", command=partial(removeEntry, array[i][0]))
            btn.grid(column=3, row=(i + 3), pady=10)

            i = i + 1

            cursor.execute('SELECT * FROM vault')
            if (len(cursor.fetchall()) <= i):
                break


cursor.execute('SELECT * FROM masterpassword')
if (cursor.fetchall()):
    loginScreen()
else:
    createMasterPassword()
window.mainloop()