import random
import art
import words

# Game title logo from art.py
print(art.logo,"\n")

# Uses the ASCII art in art.py for defining stages
stages = art.stages

# Uses the list of words in words.py
word_list = words.word_list


# Set the number of lives at the start of the game.
lives = 6

# Select a random word from the word list for the player to guess.
chosen_word = random.choice(word_list)

#Debugging: Displays the chosen word for testing.
#print(chosen_word)


# Create a placeholder to display hidden letters as underscores.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")
print("Lives: 6/6")

# Flag to control the game's while loop.
game_over = False

# List to track correctly guessed letters to be displayed.
correct_list = []

# Main game loop continues until the player wins or runs out of lives.
while not game_over:

    # Prompt player to guess a letter.
    guess = input("Guess a letter: ").lower()
    display = ""

    # Check each letter in the chosen word for matches with the player's guess.
    for letter in chosen_word:
        if letter == guess:
            # Add correct guessed letter to the display string.
            display += letter
            # Add letter to correct_list if it hasn’t been added already.
            if guess not in correct_list:
                correct_list.append(guess)
            elif guess in correct_list:
                print("Letter already guessed.")  # Inform player of duplicate guesses.
        elif letter in correct_list:
            # If letter was guessed previously, display it as well.
            display += letter
        else:
            # For letters not yet guessed, display an underscore.
            display += "_"

    print(display)  # Show current state of the guessed word.

    # If the guessed letter is not in the chosen word, reduce lives.
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! {lives}/6 lives remaining.")

    # Print the current hangman stage based on remaining lives.
    print(stages[lives])

    # Check if the player has run out of lives to end the game.
    if lives == 0:
        print("Out of lives! You lose.")
        print(f"The word was '{chosen_word}'")
        game_over = True

    # Check if there are no underscores left, meaning the word was guessed correctly.
    if "_" not in display:
        print("Guessed the word! You win!")
        game_over = True
