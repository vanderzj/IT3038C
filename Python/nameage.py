import time

start_time = time.time()

#gets user's name and age
print('What is your name?')
myName = input()
print('Hello ' + myName + '. That is a good name. How old are you?')
myAge = input()

#Gives different responses based on the user's age.
if myAge < 13:
    print("Learning young, that's good.")
elif myAge == 13:
    print("Teenager Detected")
elif myAge > 13 and myAge <= 26:
    print("Now you're a double teenager!")
elif myAge > 26 and myAge < 34:
    print("Getting older...")
else:
    print("You're probably older than Python!")

#prgmAge = time the program has been running
prgmAge = int(time.time() - start_time)
print(str(myAge) +"? That's funny, I'm only " + str(prgmAge) + " seconds old.")
print(" I wish I was " + str(int(myAge) * 2) + " years old.")

time.sleep(3)
print("I'm tired. Goodnight!")