# Imports tkinter, which is a built-in Python module used to make GUIs.
from tkinter import *

# Creates the window that the content of our script will sit in.
win = Tk()

# Creates an Entry field, where users can enter input.
# To get the input in other places, use (name).get()
ent = Entry(win, width=50, borderwidth=5)

# Puts the entry field into win.
ent.pack()

# Puts default text into the entry field. This is actual text that needs to be deleted by the user if it is not part of the response.
ent.insert(0, "Enter your name.")

# This function is being set up to give the button below functionality with the (command=) arguement.
# The Command function should be written as (command=x) instead of as (command=x()) like most other functions. If you include the parenthesies the function will run on program start by itself.
def myClick():
    hello = "Hello " + ent.get() + "!"
    lbl1 = Label(win, text=hello)
    lbl1.pack()

# Creates a button object. The arguements here are (<location of button>, <text shown on button>, <horizontal size of button>, <vertical size of button>)
btn = Button(win, text="Enter your name!", padx=50, pady=50, command=myClick)

# Puts the button into win
btn.pack()

# The .mainloop() part of this command starts the window's loop. This is what allows the program to run. Clicking the "X" on the window created by this script ends the loop.
win.mainloop()