# Imports tkinter, which is a built-in Python module used to make GUIs.
from tkinter import *

# Creates the window that the content of our script will sit in.
win = Tk()

# This function is being set up to give the button below functionality with the (command=) arguement.
# The Command function should be written as (command=x) instead of as (command=x()) like most other functions. If you include the parenthesies the function will run on program start by itself.
def myClick():
    lbl1 = Label(win, text="Button was clicked.")
    lbl1.pack()

# Creates a button object. The arguements here are (<location of button>, <text shown on button>, <horizontal size of button>, <vertical size of button>)
btn = Button(win, text="Click Me!", padx=50, pady=50, command=myClick)

# Puts the button into win
btn.pack()

# The .mainloop() part of this command starts the window's loop. This is what allows the program to run. Clicking the "X" on the window created by this script ends the loop.
win.mainloop()