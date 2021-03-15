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

# This function stores a number in the global variable first so the function btn_eql can add them together.
def btn_plus():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "+"
    disp.delete(0,END)

def btn_sub():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "-"
    disp.delete(0,END)

def btn_multi():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "*"
    disp.delete(0,END)

def btn_div():
    current = disp.get()
    global first 
    first = int(current)
    global status
    status = "/"
    disp.delete(0,END)
    
# This function takes the int first and adds to/subtracts from/multiplies by/divides by the second number, which is what is currently in the display box.
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
            disp.insert(0, first / int(current))
    

# Creates the number buttons for the calculator. The command will be called to place the numbers in the display and add them together.
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

# Places the buttons in win
b_1.grid(row=3, column=0)
b_2.grid(row=3, column=1)
b_3.grid(row=3, column=2)

b_4.grid(row=2, column=0)
b_5.grid(row=2, column=1)
b_6.grid(row=2, column=2)

b_7.grid(row=1, column=0)
b_8.grid(row=1, column=1)
b_9.grid(row=1, column=2)

b_0.grid(row=4, column=0)
b_clear.grid(row=4, column=1, columnspan=2)

b_plus.grid(row=5, column=0)
b_equal.grid(row=5, column=1, columnspan=2)

b_sub.grid(row=6, column=0)
b_multi.grid(row=6, column=1)
b_div.grid(row=6, column=2)

# The .mainloop() part of this command starts the window's loop. This is what allows the program to run. Clicking the "X" on the window created by this script ends the loop.
win.mainloop()