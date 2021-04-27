# Password Generator by John Denny 16/04/2021
import random
from random import randint
import string

# Initialize variables Character Type, The counter for amount of runs and defines the password as empty
CharacterType = randint(1, 3)
Run = 0
password = ""

# Welcome Message
print("Welcome to PassGen a password generator")
PassLength = input("How many characters would you like your password to be?") # Requests how long your password should be

# For loop which generates the password
for Run in range(1, int(PassLength)): # Runs the requested amount of times
    CharacterType = randint(1, 3) # Generates a random number between 1 and 3 to determine what type of character  will be used
    
    # If the number is 1 generate a random letter 
    if CharacterType == 1:
        x = random.choice(string.ascii_letters)
        password = password + str(x)
        Run = Run + 1


    # If the number is 2 generate a random number between 1 and 9
    if CharacterType == 2:
        x = random.choice(string.digits)
        password = password + str(x)
        Run = Run + 1

    # If the number is 3 generate a random punctuation
    if CharacterType == 3:
        x = random.choice(string.punctuation)
        password = password + str(x)
        Run = Run + 1

    # If the amount of Runs is equalled to the amount requested stop the program and present the password otherwise run
    if Run == int(PassLength):
        print("Here is your password: " +"\n" + str(password))
    else:
        pass