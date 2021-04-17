# Simple Image Viewer w/ GUI by Zack Vanderpool
# Based on the tutorials by John Elder for his Youtube Channel, Codemy.com
# His channel can be found at https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw
# I used videos 8 and 9 of the playlist "Python GUI's with TKinter," which can be found at https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

# This program builds a GUI that can be used to view up to 5 images at a time.
# It has next and previous buttons to scroll through the pictures, and an exit button to exit the program.
# For the program to work correctly, you must put it in a directory containing a folder named "pictures".
# Inside the "pictures" folder, you'll need 5 .jpg files named "image1.jpg" through "image5.jpg".
# If you want to change the max number of pictures the viewer can show, you can add more "pic#" variables to the code block at line along with the file path to the pictures.
# Once you've done that, make sure to add the new pics to the picList list variable.

from tkinter import * # Imports tkinter, a Python module used to make GUIs.
from PIL import ImageTk,Image # Imports Pillow, a Python module used to display images.

win = Tk() # Creates the window our program's content will be displayed in.
win.title('Tkinter Photo Viewer') # Gives our window a name to be displayed at the top of the window.

# Creates pictures that we will use to populate the pictures list.
pic1 = ImageTk.PhotoImage(Image.open("pictures/image.jpg"))
pic2 = ImageTk.PhotoImage(Image.open("pictures/image2.jpg"))
pic3 = ImageTk.PhotoImage(Image.open("pictures/image3.jpg"))
pic4 = ImageTk.PhotoImage(Image.open("pictures/image4.jpg"))
pic5 = ImageTk.PhotoImage(Image.open("pictures/image5.jpg"))

picList = [pic1, pic2, pic3, pic4, pic5] # Puts each picture into a list.

lbl = Label(image=pic1) # Creates the label where our pictures will be displayed.
lbl.grid(row=0, column=0, columnspan=3) # Places the label created above into the window. 

def next(pic_num): # A function to move to the next image.
    global lbl
    global btn_next
    global btn_prvs

    lbl.grid_forget() # Removes current picture to make room for next one.
    lbl = Label(image=picList[pic_num - 1]) # Recreates the label to show the next picture.
    # Recreates the buttons so that they have an updated pic_num variable to work with. Without this, the buttons will not work.
    btn_next = Button(win, text="->", command=lambda: next(pic_num + 1))
    btn_prvs = Button(win, text="<-", command=lambda: prvs(pic_num - 1))

    if pic_num == len(picList): # Disables the next button if there are no pictures to continue forward to.
        btn_next = Button(win, text="->", state = DISABLED)

    # Replaces the current navigation buttons with the updated ones.
    lbl.grid(row=0, column=0, columnspan=3)
    btn_prvs.grid(row=1, column=0)
    btn_next.grid(row=1, column=2)

def prvs(pic_num): # A function to move to the previous image.
    global lbl
    global btn_next
    global btn_prvs

    lbl.grid_forget() # Removes current picture to make room for next one.
    lbl = Label(image=picList[pic_num - 1]) # Recreates the label to show the next picture.
    # Recreates the buttons so that they have an updated pic_num variable to work with. Without this, the buttons will not work.
    btn_next = Button(win, text="->", command=lambda: next(pic_num + 1))
    btn_prvs = Button(win, text="<-", command=lambda: prvs(pic_num - 1))

    if pic_num == 1: # Disables the previous button if there are no pictures to go backwards to.
        btn_prvs = Button(win, text="<-", state = DISABLED)

    # Replaces the current navigation buttons with the updated ones.
    lbl.grid(row=0, column=0, columnspan=3)
    btn_prvs.grid(row=1, column=0)
    btn_next.grid(row=1, column=2)

btn_prvs = Button(win, text="<-", command=prvs, state = DISABLED) # Creates the previous button, used to scroll through the list of images.
btn_exit = Button(win, text="Exit Viewer", command=win.quit) # Creates an exit button for the program, used to exit the program.
btn_next = Button(win, text="->", command=lambda: next(2)) # Creates the next button, used to scroll through the list of images.

# Places navigation/exit buttons into the window.
btn_prvs.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_next.grid(row=1, column=2)

win.mainloop() # This line tells the program to continue looping through all above lines. Without it, our program would only show up for a split second and would not be usable.