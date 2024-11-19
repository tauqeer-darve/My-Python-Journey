import random
import os

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Easy Level
    password = ""
    for char in range(nr_letters):
        password += random.choice(letters)
    for char in range(nr_symbols):
        password += random.choice(symbols)
    for char in range(nr_numbers):
        password += random.choice(numbers)
    print(f"\nEasy password is: {password}")

    # Hard Level
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Hard password is: {password}")

# Main loop to allow generating multiple passwords
while True:
    pass_gen()
    retry = input("\nDo you want to generate another password? (y/n): ").lower()
    if retry != "y":
        break
    clear_screen()