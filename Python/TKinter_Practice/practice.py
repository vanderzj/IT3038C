# Imports tkinter, which is a built-in Python module used to make GUIs.
from tkinter import *

# Creates the window that the content of our script will sit in.
win = Tk()

# Creates a label. The arguements it used here are (<What window does this label go in?>, <What does this label contain?>)
lbl = Label(win, text="Hello World!")

# Puts the label into the window.
lbl.pack()

# The .mainloop() part of this command starts the window's loop. This is what allows the program to run. Clicking the "X" on the window created by this script ends the loop.
win.mainloop()