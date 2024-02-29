import random
from unicodedata import digit

goal = random.randint(1, 100)

guess = input("Guess my whole number between 1 and 100: ")

while guess != goal:
    if int(guess) < 1 or int(guess) > 100:
        print("Your guess is supposed to be between 1 and 100")
        guess = input("Please guess again: ")

    elif not guess.isnumeric():
        print("That is not a whole number")
        guess = input("please put a whole number this time: ")
    elif int(guess) < goal:
        print("Your guess was too low") 
        guess = input("Try again: ")
    elif int(guess) > goal:
        print("Your guess was too high") 
        guess = input("Try again: ")
    elif int(guess) == goal:
        break
print("Correct!")

