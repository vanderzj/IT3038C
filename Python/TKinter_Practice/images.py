from tkinter import * # Imports tkinter, a Python module used to make GUI's
from PIL import ImageTk,Image # Imports Pillow, a Python module used to display images.

# Creates the window our program's content will be displayed in.
win = Tk()
win.title('Tkinter Photo Viewer')

img_file = "C:/IT3038C/Python/TKinter_Practice/image.PNG"

img_dis = ImageTk.PhotoImage(Image.open(img_file))
lbl = Label(image=img_dis)
lbl.pack()


# Creates an exit button for the program and places it in the window.
btn_exit = Button(win, text="Exit Program", command=win.quit)
btn_exit.pack()

# This line tells the program to continue looping through all above lines. Without it, our program would only show up for a split second and would not be usable.
win.mainloop()

