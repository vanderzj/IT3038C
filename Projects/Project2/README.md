Easy Calculator w/ GUI by Zack Vanderpool
======

Based on the tutorials by John Elder for his Youtube Channel, Codemy.com
His channel can be found at https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw
I used videos 1 through 7 of the playlist "Python GUI's with TKinter," which can be found at https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

This program builds a Calculator that can add, subtract, multiply, and divide using a GUI.
The number buttons (0-9) provide the numbers for the operations.
Type in a number and select which operation you would like to perform (add/subtract/multiply/divide).
When you do so, the number you typed is stored and the display is cleared to make room for the second number. 
Clicking an operation button also sets a status to tell the equals button which operation to perform.
Once you click the equals button, the equals button looks to the status to tell which operation to perform and then uses the two numbers to get your result.
Your result is then placed back into the display. You can use your result as the next number, or click clear to start over.

To run the program, double click it from your File Explorer.
You can also navigate to the directory it is stored in in PowerShell and enter "node .\Project2.py" to run it.

I used TKinter to create and place all of the objects (window, display, buttons) that pops up. 
