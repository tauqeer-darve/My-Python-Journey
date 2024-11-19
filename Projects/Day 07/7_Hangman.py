import random
import os
import time

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Display logo
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo, "\n")

# List of stages representing each hangman drawing for the game.
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# List of words from which a random word is chosen for the game.
word_list = [
    "adventure", "balloon", "candle", "diamond", "elephant", "feather", "guitar", "horizon",
    "island", "jungle", "kingdom", "lemonade", "mountain", "notebook", "ocean", "piano",
    "quilt", "rainbow", "sunflower", "treasure", "umbrella", "volcano", "whisper",
    "yesterday", "zebra", "butterfly", "carousel", "dolphin", "enchanted", "firefly",
    "galaxy", "honey", "igloo", "jigsaw", "kitchen", "lantern", "mystery", "noodle",
    "orchard", "puzzle", "quicksand", "raspberry", "sapphire", "tornado", "unicorn",
    "victory", "wonder", "yacht", "zipper"
]

# Function to play the game
def play_hangman():
    lives = 6
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    placeholder = "_" * word_length
    correct_list = []

    # Print the initial hangman stage and placeholder
    print(f"{stages[lives]}\n")
    print(f"Word to guess: {placeholder}")
    print("Lives: 6/6")
    

    game_over = False

    while not game_over:
        guess = input("\nGuess a letter: ").lower()
        clear_screen()
        print(logo, "\n")

       
        if guess in correct_list:
            print(f"You've already guessed '{guess}'.")       
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                if guess not in correct_list:
                    correct_list.append(guess)
            elif letter in correct_list:
                display += letter
            else:
                display += "_"

        # Check if guess is incorrect
        if guess not in chosen_word:
            lives -= 1
            print(f"Wrong guess! {lives}/6 lives remaining.")
            

        # Update and print the hangman stage
        print(f"{stages[lives]}\n")
        print(f"Word to guess: {display}")
        

        # End the game if out of lives
        if lives == 0:
            print("Out of lives! You lose.")
            print(f"The word was '{chosen_word}'")
            time.sleep(1)
            game_over = True

        # End the game if the word is guessed
        if "_" not in display:
            print("Guessed the word! You win!")
            time.sleep(1)
            game_over = True

# Main loop for replaying the game
while True:
    play_hangman()
    retry = input("\nDo you want to play again? (y/n): ").lower()
    if retry != "y":
        print("Thanks for playing! Goodbye!")
        time.sleep(2)
        break
    clear_screen()
    print(logo)