import time

start_time = time.time()

print('What is your name?')
myName = input()
print('Hello ' + myName + '. That is a good name. How old are you?')
myAge = input()
prgmAge = int(time.time() - start_time)
print(str(myAge) +"? That's funny, I'm only " + str(prgmAge) + " seconds old.")
print(" I wish I was " + str(int(myAge) * 2) + " years old.")

time.sleep(3)
print("I'm tired. Goodnight!")