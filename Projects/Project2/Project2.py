# Simple Calculator w/ GUI by Zack Vanderpool
# Based on the tutorials by John Elder for his Youtube Channel, Codemy.com
# His channel can be found at https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw
# I used videos 1 through 7 of the playlist "Python GUI's with TKinter," which can be found at https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# This program builds a Calculator that can add, subtract, multiply, and divide using a GUI.
# The number buttons (0-9) provide the numbers for the operations.
# Type in a number and select which operation you would like to perform (add/subtract/multiply/divide).
# When you do so, the number you typed is stored and the display is cleared to make room for the second number. 
# Clicking an operation button also sets a status to tell the equals button which operation to perform.
# Once you click the equals button, the equals button looks to the status to tell which operation to perform and then uses the two numbers to get your result.
# Your result is then placed back into the display. You can use your result as the next number, or click clear to start over.

# Imports tkinter, which is a built-in Python module used to make GUIs.
from tkinter import *

# Creates the window that the content of our script will sit in.
win = Tk()
win.title("Easy Calculator")

# Creates a display for the numbers the user is calculating to be shown.
disp = Entry(win, width=40, borderwidth=5)

# Puts the display into win, defines its size, and places it within the grid system.
disp.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# This function allows you to enter numbers into the display. num is the number shown on the button pressed (i.e. if you click on 1, then num = 1).
def btn_clk(num):
    full = disp.get()
    disp.delete(0,END)
    disp.insert(0, str(full) + str(num))
    return

# This function clears the display.
def btn_clr():
    disp.delete(0,END)

# This function stores the current number, clears the display, and sets the status to +.
def btn_plus():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "+"
    disp.delete(0,END)

# This function stores the current number, clears the display, and sets the status to -.
def btn_sub():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "-"
    disp.delete(0,END)

# This function stores the current number, clears the display, and sets the status to *.
def btn_multi():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "*"
    disp.delete(0,END)

# This function stores the current number, clears the display, and sets the status to /.
def btn_div():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "/"
    disp.delete(0,END)
    
# This function takes the int first and based on the status adds to/subtracts from/multiplies by/divides by the second number, which is what is currently in the display box.
# It then clears the display box and shows the result in the status box.
def btn_eql():
    current = disp.get()
    disp.delete(0, END)
    if status == "+":
            disp.insert(0, first + int(current))
    if status == "-":
            disp.insert(0, first - int(current))
    if status == "*":
            disp.insert(0, first * int(current))
    if status == "/":
            disp.insert(0, int(first / int(current)))
    

# Creates the number buttons for the calculator. The command will be called to place the numbers in the display.
b_1 = Button(win, text="1", padx=30, pady=10, command=lambda: btn_clk(1))
b_2 = Button(win, text="2", padx=30, pady=10, command=lambda: btn_clk(2))
b_3 = Button(win, text="3", padx=30, pady=10, command=lambda: btn_clk(3))
b_4 = Button(win, text="4", padx=30, pady=10, command=lambda: btn_clk(4))
b_5 = Button(win, text="5", padx=30, pady=10, command=lambda: btn_clk(5))
b_6 = Button(win, text="6", padx=30, pady=10, command=lambda: btn_clk(6))
b_7 = Button(win, text="7", padx=30, pady=10, command=lambda: btn_clk(7))
b_8 = Button(win, text="8", padx=30, pady=10, command=lambda: btn_clk(8))
b_9 = Button(win, text="9", padx=30, pady=10, command=lambda: btn_clk(9))
b_0 = Button(win, text="0", padx=30, pady=10, command=lambda: btn_clk(0))

# Creates the function buttons for the calculator.
b_plus = Button(win, text="+", padx=29, pady=10, command=btn_plus)
b_clear = Button(win, text="clear", padx=64, pady=10, command=btn_clr)
b_equal = Button(win, text="=", padx=72, pady=10, command=btn_eql)
b_multi = Button(win, text="*", padx=30, pady=10, command=btn_multi)
b_sub = Button(win, text="-", padx=30, pady=10, command=btn_sub)
b_div = Button(win, text="/", padx=29, pady=10, command=btn_div)

# Places the buttons in win. These are grouped by row and sorted by ascending column order for clarity.
b_7.grid(row=1, column=0)
b_8.grid(row=1, column=1)
b_9.grid(row=1, column=2)

b_4.grid(row=2, column=0)
b_5.grid(row=2, column=1)
b_6.grid(row=2, column=2)

b_1.grid(row=3, column=0)
b_2.grid(row=3, column=1)
b_3.grid(row=3, column=2)

b_0.grid(row=4, column=0)
b_clear.grid(row=4, column=1, columnspan=2)

b_plus.grid(row=5, column=0)
b_equal.grid(row=5, column=1, columnspan=2)

b_sub.grid(row=6, column=0)
b_multi.grid(row=6, column=1)
b_div.grid(row=6, column=2)

# The .mainloop() part of this command starts the window's loop. This is what allows the program to run. Clicking the "X" on the window created by this script ends the loop.
win.mainloop()