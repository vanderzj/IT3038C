# This Python program allows users to play the game Snake.
# In Snake, your goal is to collect fruit, represented by red dots. Each dot is worth 10 points.
# Each time you collect a fruit, your snake gets longer. You lose if you run into the walls or your own body.
# To control the Snake, you can turn it to the left or right by pressing the corresponding arrow key to rotate it (i.e. if the snake is going right and you want it to go down, press the down key)
# The Snake constantly moves forward, and you cannot move backwards.

# This program was created using the tutorials made by TokyoEdTech on Youtube. 
# You can find his channel at https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg and the playlist of Snake tutorials at https://www.youtube.com/playlist?list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ

import turtle
import time
import random

# Variables to keep track of the score with.
score = 0
topScore = 0

# Object: Game Window - This is the window in which the game will be played.
win = turtle.Screen()
win.title("Snake")
win.bgcolor("black")
win.setup(width=750, height=750) # Sets the size for the game window. The center point of the window is (0,0). Anything with an x value of -375 < x < 375 or a y value of -375 < y < 375 will be offscreen.
win.tracer(0) # The .tracer attribute controls the animation speed. By setting it to 0, the game has no animations to show so it moves as fast as possible.

# Object: Snake Head - This is what the player will be actively controlling.
SnkH = turtle.Turtle()
SnkH.speed(0)
SnkH.shape("square")
SnkH.color("yellow")
SnkH.penup() # This tells the window to erase the snake head's current position on the screen when it moves to a new position.
SnkH.goto(0,0) # This tells the snake to start in the center of the screen.
SnkH.direction = "stop"

# Object: Fruit - These are the objects that the player wants to collect by steering the snake head into them.
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("pink")
fruit.penup() # This tells the window to erase the fruit's current position on the screen when it moves to a new position.
fruit.goto(random.randint(-360,360),random.randint(-360,360)) # Sets the fruit's initial position.

# Object: Marker - This lets us create the user UI to display the score.
mkr = turtle.Turtle()
mkr.speed(0)
mkr.color("white") # Sets the text color.
mkr.penup() # Erases the old text when new text is written.
mkr.hideturtle() # Hides the object from view.
mkr.goto(0,330)
mkr.write ("Score: 0  Top Score: 0", align="center", font=("Courier", 30, "normal"))

# Object List: Snake Body - Each time a Fruit is eaten, the Snake's Body gets bigger. If the Snake Head collides with the Snake Body, the player loses.
SnkB = [] # This is just the container, new Body Parts are spwaned in the Controller Loop below.

# Function: Snake Movement - This function tells the snake head how to move, based on the direction we have given it.
def SnkMove():
    yCoor = SnkH.ycor()
    xCoor = SnkH.xcor()
    if SnkH.direction == "up":
        SnkH.sety(yCoor + 20)
    if SnkH.direction == "down":
        SnkH.sety(yCoor - 20)
    if SnkH.direction == "right":
        SnkH.setx(xCoor + 20)
    if SnkH.direction == "left":
        SnkH.setx(xCoor - 20)

# Function: CDup - Allows us to change the snake head's direction to up as long as the snake's current direction is not down.
def CDup():
    if SnkH.direction != "down":
        SnkH.direction = "up"

# Function: CDdown - Allows us to change the snake head's direction to down as long as the snake's current direction is not up.
def CDdown():
    if SnkH.direction != "up":
        SnkH.direction = "down"

# Function: CDright - Allows us to change the snake head's direction to right as long as the snake's current direction is not left.
def CDright():
    if SnkH.direction != "left":
        SnkH.direction = "right"

# Function: CDleft - Allows us to change the snake head's direction to left as long as the snake's current direction is not right.
def CDleft():
    if SnkH.direction != "right":
        SnkH.direction = "left"

# Connects the above functions to the corresponding arrow keys on the keyboard.
win.listen()
win.onkeypress(CDup, "Up")
win.onkeypress(CDdown, "Down")
win.onkeypress(CDright, "Right")
win.onkeypress(CDleft, "Left")

# Game Controller - This loop updates the game window to show which actions/interactions are occuring.
GameSpeed = 0.1 # This variable controls the speed of the game. Without it, we would not be able to play the game as it would move too quickly and we would lose as soon as the game begins.
while True:
    win.update()

    if SnkH.xcor() > 360 or SnkH.xcor() < -360 or SnkH.ycor() > 360 or SnkH.ycor() < -360: # Snake Head has collided with the border and has gone offscreen. Game Over!
        time.sleep(1)
        SnkH.goto(0,0) # Resets the Snake Head.
        SnkH.direction = "stop" # Stops the Snake Head so the player can choose whether or not to play again.
        
        for BP in SnkB: # Sends all Body Parts offscreen.
            BP.goto(-800, 800)

        SnkB.clear() # Clears the Body Parts list.

        score = 0 # Sets the score back to 0 so the new game starts with an accurate score.
        mkr.clear() # Erases the current score so the new score can be written.
        mkr.write ("Score: {}  Top Score: {}".format(score, topScore), align="center", font=("Courier", 30, "normal")) # Updates the score display.

    if SnkH.distance(fruit) < 20: # Snake Head has collided with a Fruit. That Fruit is eaten, the Snake Body grows, and a new Fruit appears.
        fruit.goto(random.randint(-360,360),random.randint(-360,360)) # Spawns a new Fruit.

        new_BP = turtle.Turtle() # Creates a new Body Part (BP) for the Snake's body.
        new_BP.speed(0) # Sets animation speed to 0 because there is no animation.
        new_BP.shape("square")
        new_BP.color("green")
        new_BP.penup() # This tells the window to erase the body part's current position on the screen when it moves to a new position.
        SnkB.append(new_BP) # Adds this new body part to the end of the list containing all of the body parts.

        GameSpeed = GameSpeed * 0.9 # Increases the game's speed by 10% of its current speed whenever a fruit is collected.

        score += 10 # Increases the score when you get a fruit.

        if score > topScore: # Updates the Top Score if it has been beaten.
            topScore = score

        mkr.clear() # Erases the current score so the new score can be written.
        mkr.write ("Score: {}  Top Score: {}".format(score, topScore), align="center", font=("Courier", 30, "normal")) # Updates the score display.


    for n in range(len(SnkB)-1, 0, -1): # Moves the end body part forward as the whole snake moves.
        SnkB[n].goto(SnkB[n-1].xcor(),SnkB[n-1].ycor())

    if len(SnkB) > 0: # Moves Body Part 0 to the head's position.
        SnkB[0].goto(SnkH.xcor(),SnkH.ycor())

    SnkMove()

    for BP in SnkB: # Snake Head has collided with Snake Body. Game Over!
        if BP.distance(SnkH) < 20: 
            time.sleep(1)
            SnkH.goto(0,0) # Resets the Snake Head.
            SnkH.direction = "stop" # Stops the Snake Head so the player can choose whether or not to play again.
        
            for BP in SnkB: # Sends all Body Parts offscreen.
                BP.goto(-800, 800)

            SnkB.clear() # Clears the Body Parts list.

            score = 0 # Sets the score back to 0 so the new game starts with an accurate score.
            mkr.clear() # Erases the current score so the new score can be written.
            mkr.write ("Score: {}  Top Score: {}".format(score, topScore), align="center", font=("Courier", 30, "normal")) # Updates the score display.

    time.sleep(GameSpeed) # This function applies the game speed variable to control how quickly everything moves. To speed it up, you can decrease the GameSpeed variable. To slow it down, increase the variable.


# This line keeps window (and by extension, the game) from closing before we are done with it.
win.mainloop()