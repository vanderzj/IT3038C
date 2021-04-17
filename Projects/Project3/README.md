Simple Image Viewer w/ GUI by Zack Vanderpool
=====

Based on the tutorials by John Elder for his Youtube Channel, Codemy.com
His channel can be found at https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw
I used videos 8 and 9 of the playlist "Python GUI's with TKinter," which can be found at https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

This program builds a GUI that can be used to view up to 5 images at a time.
It has next and previous buttons to scroll through the pictures, and an exit button to exit the program.
For the program to work correctly, you must put it in a directory containing a folder named "pictures".
Inside the "pictures" folder, you'll need 5 .jpg files named "image1.jpg" through "image5.jpg".
You'll also need to install the Python Module "Pillow", which can be installed by running "pip install Pilow"
If you want to change the max number of pictures the viewer can show, you can add more "pic#" variables to the code block at line along with the file path to the pictures.
Once you've done that, make sure to add the new pics to the picList list variable.