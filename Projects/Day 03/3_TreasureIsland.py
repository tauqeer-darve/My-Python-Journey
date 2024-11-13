print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat, '
                    'Type "swim" to swim across, '
                    'or Type "build" to build a raft.\n').lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors. One red, "
                        "one yellow, and one blue. "
                        "Which colour do you choose?\n").lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            choice4 = input("You enter a room of beasts. "
                            "Do you want to 'fight' or 'flee'?\n").lower()
            if choice4 == "fight":
                print("The beasts are too strong. Game Over.")
            elif choice4 == "flee":
                print("You managed to escape, but you're lost in the woods. Game Over.")
            else:
                print("You hesitated and got caught. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    elif choice2 == "swim":
        print("You got attacked by an angry trout. Game Over.")

    elif choice2 == "build":
        print("You built a sturdy raft and crossed the lake safely!")
        choice5 = input("You see two paths on the island: one leading to a cave and another to a forest. "
                        "Do you want to go to the 'cave' or 'forest'?\n").lower()

        if choice5 == "cave":
            print("Inside the cave, you found ancient treasure! You Win!")
        elif choice5 == "forest":
            print("You got lost in the forest. Game Over.")
        else:
            print("That’s not a valid path. Game Over.")

    else:
        print("You chose an action that doesn't exist. Game Over.")

else:
    print("You fell into a hole. Game Over.")

