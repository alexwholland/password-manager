from tkinter import *
from random import randint

global_label = None


def passGenerator():
    # Password Generator window.
    window = Tk()

    window.title("Password Generator")

    def copyToClipboard():
        """
        Copy the generated password to the users clipboard
        """
        window.clipboard_clear()
        window.clipboard_append(pwEntry.get())

    def createRandomPass():
        """
        Generate a password with random ASCII characters
        """
        # TODO remove global variable and reposition the label location
        pwEntry.delete(0, END)

        password = ""

        maxCount = int(myEntry.get())
        global global_label
        if maxCount > 128:
            if not global_label:
                global_label = Label(window, text="Too many characters")
                global_label.pack(pady=20)
            return

        # Ideally the global label should be removed after a valid password number is entered
        # global_label.after(0, global_label.destroy)
        for x in range(maxCount):
            password += chr(randint(33, 126))

        pwEntry.insert(0, password)

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
    myButton = Button(myFrame, text="Generate Password", command=createRandomPass)
    myButton.grid(row=0, column=0, padx=10)

    clipBtn = Button(myFrame, text="Copy to Clipboard", command=copyToClipboard)
    clipBtn.grid(row=0, column=1, padx=10)

    window.mainloop()
