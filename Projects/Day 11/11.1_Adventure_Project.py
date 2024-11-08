import random
import adventure_art

encounters = ["monster", "treasure", "potion", "empty"]
victory_item = "Ancient Artifact"

def fight_monster(player_health, inventory):
    """Function to work out the monster encounters."""
    print("\nA wild monster appears!")
    choice_fight = input("Do you want to 'fight' or 'flee'?: ").lower()
    if choice_fight == "fight":
        result = random.choice([True, False])
        if result:
            print("You defeated the monster!\n")
        else:
            print("The monster hit you! You lost 20 health.\n")
            player_health -= 20
    elif choice_fight == "flee":
        if inventory:
            print("You managed to escape, but lost some items.\n")
            lost_item = inventory.pop(random.randrange(len(inventory)))
            print(f"You dropped 1 {lost_item}\n")
        else:
            print("You fled but had no items to lose.\n")
    else:
        print("You hesitated! You lost 20 health.\n")
        player_health -= 20
    return player_health, inventory

def find_treasure(inventory):
    """Function to work out the treasure encounters."""
    print("\nYou found a treasure chest!")
    choice_take = input("Do you want to 'take' the treasure or 'leave' it?: ").lower()
    if choice_take == "take":
        if random.randint(1, 5) == 1:
            print(f"You found the {victory_item}!")
            print("You added the Ancient Artifact to your inventory.\n")
            inventory.append(victory_item)
        else:
            print("It's a Gold Coin!")
            print("You added Gold Coin to your inventory.\n")
            inventory.append("Gold Coin")
    else:
        print("You decided to leave the treasure.\n")
    return inventory

def find_potion(player_health, inventory):
    """Function to work out the potion encounters."""
    print("\nYou found a potion!")
    choice_drink = input("Do you want to 'drink' the potion or 'save' it for later?: ").lower()
    if choice_drink == "drink":
        if player_health < 100:
            print("You drank the potion and recovered 20 health.\n")
            player_health += 20
        else:
            print("Your health is already full. You wasted the potion.\n")
    else:
        print("You stored the potion in your inventory.\n")
        inventory.append("Potion")
    return player_health, inventory

def empty_room():
    """Function to work out the empty room encounters."""
    print("\nThe room is empty. Nothing to do here.\n")

def rooms(choose_room):
    """Function to work out the random encounters."""
    return random.choice(choose_room)

def adventure_time():
    """Main game function for processing game flow."""
    player_health = 100
    inventory = []
    game_over = False

    print(adventure_art.logo)
    print("""Welcome to Adventure Time!\n
Your goal is to find the Ancient Artifact and escape 'ALIVE'.
Good luck, Adventurer!\n""")

    while not game_over:
        if player_health > 0 and victory_item not in inventory:
            print(f"Player Health: {player_health}")
            print(f"Inventory: {inventory}")
            cont = input("Do you want to continue exploring? (y/n): ")
            if cont == "y":
                encounter = rooms(encounters)
                if encounter == "monster":
                    player_health, inventory = fight_monster(player_health, inventory)
                elif encounter == "treasure":
                    inventory = find_treasure(inventory)
                elif encounter == "potion":
                    player_health, inventory = find_potion(player_health, inventory)
                else:
                    empty_room()
            else:
                print("You gave up...\n")
                game_over = True
        elif player_health <= 0:
            if "Potion" in inventory:
                drink = input("You are low on health. Do you want to drink a potion?(y/n): ").lower()
                if drink == "y":
                    print("You used a potion.\n")
                    inventory.remove("Potion")
                    player_health += 20
                else:
                    print("You Died.")
                    game_over = True
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
