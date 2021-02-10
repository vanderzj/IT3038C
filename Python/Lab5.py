#Random is a Python module for generating random numbers. 
from random import randint

try:

    #gets a random int between 0 and 100. This is the number that the user will try to guess.
    n = randint(0,100)

    #Explains the game and gets the user's first guess.
    print("Guess a number between 0 and 100! What is your first guess?")
    UserNum = int(input())
    
    #x keeps track of the total number of guesses. 
    #h keeps track of the total number of guesses that are higher than n, and l keeps track of the guesses that are lower than n.
    x = 0
    h = 0
    l = 0

    #Loops until the user's guess = n.
    while True:

        #Keeps track of the number of guesses.
        x += 1

        #Breaks the loop if the user guesses correctly, or tells them that their guess was too high/low if user guesses incorrectly.
        if UserNum == n:
            break
        elif UserNum > 100 or UserNum < 0:
            print("Whoops, Invalid Guess! Keep your guesses between 0 and 100.")
        elif UserNum > n:
            print("Too high!")
            h += 1
        elif UserNum < n:
            print("Too low!")
            l += 1

        #Gets the next guess from the user.    
        print("What is your next guess?")
        UserNum = int(input())

    #End of game message.
    print("Yup, you guessed it! The number was " + str(n))

    #Tells the user how many guesses it took for them to guess correctly.
    if x == 1:
        print("You got it on your first try? What are you, a mind reader?")
    else:
        #Gives a different message based on if the user guessed higher than n more than they guessed lower, or vice versa.
        if h > l:
            print("It took you " + str(x) + " tries to guess. Guess lower next time!")
        elif l > h:
            print("It took you " + str(x) + " tries to guess. Guess higher next time!")

#Breaks if the user enters anything but a whole number.
except:
    print("Whoops, looks like something went wrong!")
    

