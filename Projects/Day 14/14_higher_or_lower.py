import random
import os

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""




# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def random_celeb():
    i = random.randint(0, len(data) - 1)
    return i

def comparison(celeb_a,celeb_b,guess):
    if (celeb_a > celeb_b and guess == "A") or (celeb_a < celeb_b and guess == "B"):
        return True
    else:
        return False

def higher_or_lower():
    print(art.logo)
    game_over = False
    score = 0
    higher = 0
    while not game_over:
        index = random_celeb()
        index2 = random_celeb()
        b_celeb = data[index2]['follower_count']
        if score == 0:
            a_celeb = data[index]['follower_count']
            print(f"{data[index]['name']}, a {data[index]['description']}, from {data[index]['country']}")
            print("Followers: ",a_celeb, "Index: ", index,"\n")
        else:
            a_celeb = data[higher]['follower_count']
            print(f"{data[higher]['name']}, a {data[higher]['description']}, from {data[higher]['country']}")
            print("Followers: ", a_celeb, "Higher: ", higher,"\n")

        print("V/S\n")

        print(f"{data[index2]['name']}, a {data[index2]['description']}, from {data[index2]['country']}")
        print("Followers: ",b_celeb, "Index: ", index2,"\n")
        answer = input("Who has more followers?\nType 'A' or 'B': ").upper()
        compare = comparison(a_celeb,b_celeb,answer)
        if compare:
            if answer == "A" and score == 0:
                higher = index
            elif answer == "A":
                higher = higher
            else:
                higher = index2
            score += 1
            print(f"\nYou're right! Current Score: {score}")
            print("=====================================\n")
        else:
            print(f"\nSorry, that's wrong. Final Score: {score}")
            game_over = True

higher_or_lower()

while input("Do you want to play again?(y/n): ") == "y":
    clear_screen()
    higher_or_lower()