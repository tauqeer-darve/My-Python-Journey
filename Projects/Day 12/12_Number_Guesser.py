import random
import os

logo = r"""
   ______                        __  __                                  __             
  / ____/_  _____  __________   / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     

"""

EASY_DIFF = 10
HARD_DIFF = 5

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


def num_to_guess():
    num = random.randint(1,100)
    return num

def diff(chances):
    if chances == "easy":
        chances = EASY_DIFF
        return chances
    else:
        chances = HARD_DIFF
        return chances

def num_checker(number,guess):
    if number == guess:
        print(f"\nYou got it! The answer was {number}.\n")
        return True
    elif number > guess:
        print("Too low")
    elif number < guess:
        print("Too high")


def guess_the_number():
    game_over = False
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chances = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number = num_to_guess()
    tries = diff(chances)
    while not game_over:
        if tries > 1:
            print(f"\nYou have {tries} attempts remaining to guess the number.")
        else:
            print(f"\nYou have {tries} attempt remaining to guess the number.")
        tries -= 1
        guess = int(input("Make a guess: "))
        if num_checker(number,guess):
            game_over = True
        elif tries == 0:
            print(f"\nYou've run out of guesses. The number was {number}.\n")
            game_over = True

guess_the_number()

while input("Do you want to play again?(y/n): ").lower() == "y":
    clear_screen()
    guess_the_number()