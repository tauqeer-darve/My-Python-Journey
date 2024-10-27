import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''

rps = [rock,paper,scissors]
player_choice=int(input("Rock, Paper or Scissors?(Type 0 for Rock, Type 1 for Paper or Type 2 for Scissors):\n"))
game_choice=random.randint(0,2)
print(f"You chose: {rps[player_choice]}")
print(f"Computer chose: {rps[game_choice]}")
if player_choice >= 3 or player_choice < 0:
    print("Invalid Option. YOU LOSE!")
elif player_choice == 0 and game_choice == 2:
    print("You win!")
elif game_choice == 0 and player_choice == 2:
    print("You lose!")
elif player_choice < game_choice:
    print("You lose!")
elif game_choice < player_choice:
    print("You Win!")
elif player_choice == game_choice:
    print("It's a darw!")
else:
    print("Invalid Input!")

