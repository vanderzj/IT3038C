# Imports tkinter, which is a built-in Python module used to make GUIs.
from tkinter import *

# Creates the window that the content of our script will sit in.
win = Tk()

# Creates a label. The arguements it used here are (<What window does this label go in?>, <What does this label contain?>)
lbl1 = Label(win, text="Hello World!")
lbl2 = Label(win, text="My name is Zack.")

# The .grid() command allows us to place our objects inside the window with more control than .pack() gives us.
# .grid() uses the arguements (row = x, column = y), where x and y are the horizontal and vertical positions on the grid.
# The sizes of the rows and columns are automatically definied by the amount of space taken up. In this case, column 0 is 12 characters long because the text of lbl1 is only 12 characters long.
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=0)

# The .mainloop() part of this command starts the window's loop. This is what allows the program to run. Clicking the "X" on the window created by this script ends the loop.
win.mainloop()