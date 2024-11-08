import random
import adventure_art

player_health = 100
inventory = []

encounters = ["monster","treasure","potion","empty"]
victory_item = "Ancient Artifact"


def fight_monster():
    """Function to work out the monster encounters."""
    global player_health
    print("\nA wild monster appears!")
    choice_fight = input("Do you want to 'fight' or 'flee'?: ").lower()
    if choice_fight == "fight":
        result = random.choice([True,False])
        if result:
            print("You defeated the monster!\n")
        else:
            print("The monster hit you! You lost 20 health.\n")
            player_health -= 20
    elif choice_fight == "flee":
        print("You managed to escape, but lost some items.\n")
        lost_item = inventory.pop(random.randrange(len(inventory)))
        print(f"You dropped 1 {lost_item}\n")
    else:
        print("You hesitated! You lost 20 health.\n")
        player_health -= 20

def find_treasure():
    """Function to work out the treasure encounters."""
    print("\nYou found a treasure chest!")
    choice_take = input("Do you want to 'take' the treasure or 'leave' it?: ").lower()
    if choice_take == "take":
        if random.randint(1, 5) == 1:
            print(f"You found the {victory_item}!")
            print("You added Ancient Artifact to your inventory.\n")
            inventory.append(victory_item)
        else:
            print("It's a Gold Coin!")
            print("You added Gold Coin to your inventory.\n")
            inventory.append("Gold Coin")
    else:
        print("You decided to leave the treasure.\n")

def find_potion():
    """Function to work out the potion encounters."""
    global player_health
    print("\nYou found a potion!")
    choice_drink = input("Do you want to 'drink' the potion or 'save' it for later?: ").lower()
    if choice_drink == "drink":
        if player_health == 100:
            print("Your health is already full.\nYou wasted a potion")
        else:
            print("You drank the potion and recovered 20 health.\n")
            player_health += 20
    else:
        print("You saved the potion in your inventory.\n")
        inventory.append("Potion")

def empty_room():
    """Function to work out the empty room encounters."""
    print("\nThe room is empty. Nothing to do here.\n")

def rooms(choose_room):
    """Function to work out the random encounters."""
    room = random.choice(choose_room)
    return room

def adventure_time():
    """Main game function for processing game flow."""
    global player_health
    print(adventure_art.logo)
    print("""Welcome to Adventure Time!\n
Your goal is to find the Ancient Artifact and escape 'ALIVE'.
Good luck, Adventurer!\n""")
    game_over = False
    while not game_over:
        if player_health != 0 or victory_item not in inventory:
            print(f"Player Health: {player_health}")
            print(f"Inventory: {inventory}")
            cont = input("Do you want to continue exploring? (y/n): ")
            if cont == "y":
                if rooms(encounters) == "monster":
                    fight_monster()
                elif rooms(encounters) == "treasure":
                    find_treasure()
                elif rooms(encounters) == "potion":
                    find_potion()
                else:
                    empty_room()
            else:
                print("You gave up...")
                game_over = True
        elif player_health == 0:
            if "Potion" in inventory:
                drink = input("You are low on health. Do you want to drink a potion?(y/n): ").lower()
                if drink == "y":
                    print("You used a potion.")
                    inventory.remove("Potion")
                    player_health += 20
                else:
                    print("You Died.")
                    game_over = True
        elif victory_item in inventory:
            print("Congratulations! You found the Ancient Artifact!")
            game_over = True
        else:
            print("Game Over")
            game_over = True
    print("Your final stats:\n")
    print(f"Player Health: {player_health}")
    print(f"Inventory: {inventory}")

while input("Do you want to start a new adventure?(y/n): ") == "y":
    print("\n" * 50)
    adventure_time()