import random
from unicodedata import digit

def my_input(prompt: str):
    while True:
        guess = input(prompt)

        # check if guess is int
        try:
            int(guess)
        except ValueError:
            continue
        
        return guess

goal = random.randint(1, 100)

guess = my_input("Guess my whole number between 1 and 100: ")

#print(type(guess))

while guess != goal:
    if int(guess) < 1 or int(guess) > 100:
        print("Your guess is supposed to be between 1 and 100")
        guess = my_input("Please guess again: ")

    elif not guess.isnumeric():
        print("That is not a whole number")
        guess = my_input("please put a whole number this time: ")
    elif int(guess) < goal:
        print("Your guess was too low") 
        guess = my_input("Try again: ")
    elif int(guess) > goal:
        print("Your guess was too high") 
        guess = my_input("Try again: ")
    elif int(guess) == goal:
        break
print("Correct!")

