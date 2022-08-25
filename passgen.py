from tkinter import *


def passGenerator():
    # Password Generator window.
    window = Tk()

    window.title("Password Generator")

    # Label frame.
    lf = LabelFrame(window, text="How many characters?")
    lf.pack(pady=20)


    # Create Entry Box for number of characters.
    myEntry = Entry(lf, font=("Helvetica", 12))
    myEntry.pack(pady=20, padx=20)

    # Create entry box for returned password.
    pwEntry = Entry(window, text="", font=("Helvetica", 12), bd=0, bg="systemTransparent")
    pwEntry.pack(pady=20)

    # Frame for buttons.
    myFrame = Frame(window)
    myFrame.pack(pady=20)

    # Create buttons
    myButton = Button(myFrame, text="Generate Password")
    myButton.grid(row=0, column=0, padx=10)

    clipBtn = Button(myFrame, text="Copy to Clipboard")
    clipBtn.grid(row=0, column=1, padx=10)


    window.mainloop()