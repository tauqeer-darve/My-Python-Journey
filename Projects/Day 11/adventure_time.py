import random
import os
import time

logo = r"""
⠀⠀⠀⠀⠀⠀⠀⠰⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⡟⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣼⣿⣀⣹⣿⡆⠀⢤⡄⢤⣄⢤⡤⠀⢤⣤⣤⣤⣤⢤⣄⠀⢤⣤⡤⣤⣤⣤⢠⡄⠀⣤⢤⡤⢤⡠⣤⠤⣴⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢹⣿⡇⠉⠉⢿⣿⡄⢸⡇⠀⢹⡏⢿⣠⡟⢹⣿⠤⠄⢸⡿⣷⣼⡇⠀⣿⡇⠀⢸⡇⠀⡇⢸⡇⣎⠀⣿⠶⠌⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠾⠿⠀⠀⠀⠘⠿⠿⠾⠿⠴⠛⠁⠘⠏⠀⠼⠿⠦⠖⠸⠃⠀⠙⠇⠀⠿⠇⠀⠘⠷⠚⠇⠾⠇⠘⠿⠿⠶⠶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⢠⣤⡤⠀⢲⣶⣶⡄⠀⠀⠀⣰⣶⣶⠖⠀⢲⣶⣶⠶⠶⢶⣶⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⢀⣸⣿⣉⣀⠀⢟⡉⠉⡉⣿⣿⢉⣉⣙⣛⣘⣿⣇⣀⡀⣿⢿⣿⡄⠀⣼⡿⣿⣿⢠⣤⣬⣭⣭⣤⣤⣤⣬⣤⣤⣀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⢇⣿⠰⠻⣿⣾⡿⠵⣿⣿⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⣍⠁⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢰⣶⡆⠀⣼⣿⡆⠀⠹⡿⠁⠀⣿⣿⡀⠀⣸⣿⣿⣤⣤⣤⣤⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⠀⠀⠀⠀⠀⠴⠟⠛⠂⠀⠀⠀⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠻⠋⠀⠀⠀⠀
"""



encounters = ["monster", "treasure", "potion", "empty", "weapon", "armor", "helmet", "random_event"]
victory_item = "Ancient Artifact"
player_max_health = 100

def shop_menu():
    print("\n=== WELCOME TO THE SHOP ===")
    print("Items available for purchase:")
    print("1. Potion - 5 Gold Coins")
    print("2. Sword - 10 Gold Coins")
    print("3. Axe - 10 Gold Coins")
    print("4. Bow - 10 Gold Coins")

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cap_health(health):
    """Ensure health doesn't exceed maximum."""
    return min(health, player_max_health)

def monster_battle(player_health, inventory, recap_log, damage_multiplier=1.0):
    monster_types = [
        {"name": "Goblin", "health": 30, "min_damage": 5, "max_damage": 10},
        {"name": "Orc", "health": 50, "min_damage": 8, "max_damage": 15},
        {"name": "Troll", "health": 70, "min_damage": 10, "max_damage": 20}
    ]
    
    monster = random.choice(monster_types)
    monster_health = monster["health"]
    last_player_damage = 0
    last_monster_damage = 0
    
    clear_screen()
    print(logo)
    print(f"\nA wild {monster['name']} appears!")
    recap_log.append(f"Encountered a {monster['name']}.")
    
    has_weapon = any(item in ["Sword", "Axe", "Bow"] for item in inventory)
    player_min_damage = 8 if has_weapon else 5
    player_max_damage = 15 if has_weapon else 10
    
    while monster_health > 0 and player_health > 0:
        clear_screen()
        print(logo)
        print(f"\nA wild {monster['name']} appears!")
        print(f"\nYour Health: {player_health}")
        print(f"{monster['name']}'s Health: {monster_health}")
        if last_player_damage:
            print(f"\nLast turn: You dealt {last_player_damage} damage to the {monster['name']}.")
        if last_monster_damage:
            print(f"Last turn: The {monster['name']} dealt {last_monster_damage} damage to you.")

        print("\nYour turn!")
        action = input("Choose your action (attack/heal/flee): ").lower()
        
        if action == "attack":
            last_player_damage = random.randint(player_min_damage, player_max_damage)
            monster_health -= last_player_damage
            print(f"You dealt {last_player_damage} damage to the {monster['name']}!")
            
        elif action == "heal" and "Potion" in inventory:
            inventory.remove("Potion")
            heal_amount = 20
            old_health = player_health
            player_health = cap_health(player_health + heal_amount)
            actual_heal = player_health - old_health
            print(f"You used a potion and recovered {actual_heal} health!")
            recap_log.append(f"Used a potion to heal {actual_heal} health.")
            last_player_damage = 0
            
        elif action == "heal":
            print("You don't have any potions!")
            last_player_damage = 0
            
        elif action == "flee":
            if random.random() < 0.5:  
                print("You successfully fled from the battle!\n")
                recap_log.append(f"Fled from the {monster['name']}.")
                if inventory:
                    lost_item = inventory.pop(random.randrange(len(inventory)))
                    print(f"But you dropped your {lost_item} while running!\n")
                    recap_log.append(f"Dropped {lost_item} while fleeing.")
                return player_health, inventory
            else:
                print("Couldn't escape!")
                recap_log.append("Failed to flee from battle.")
            last_player_damage = 0

        if monster_health > 0:
            time.sleep(1)
            print(f"\n{monster['name']}'s turn!")
            defense = 0
            if "Armor" in inventory:
                defense += 3
            if "Helmet" in inventory:
                defense += 2
                
            last_monster_damage = max(1, int(random.randint(monster["min_damage"], monster["max_damage"]) * damage_multiplier) - defense)
            player_health -= last_monster_damage
            print(f"The {monster['name']} attacks! You took {last_monster_damage} damage!")
            recap_log.append(f"Took {last_monster_damage} damage from {monster['name']}.")

        time.sleep(2)

    if player_health <= 0:
        print(f"\nThe {monster['name']} defeated you!")
        recap_log.append(f"Defeated by the {monster['name']}.")
    else:
        print(f"\nYou defeated the {monster['name']}!")
        recap_log.append(f"Victory against the {monster['name']}!")
        
        if random.random() < 0.3:
            loot = random.choice(["Potion", "Gold Coin"])
            inventory.append(loot)
            print(f"The {monster['name']} dropped a {loot}!")
            recap_log.append(f"Found {loot} after defeating {monster['name']}.")

    return player_health, inventory

def find_treasure(inventory, recap_log):
    """Treasure encounter with a chance to find the victory item and random gold coins."""
    print("\nYou found a treasure chest!")
    choice_take = input("Do you want to 'take' the treasure or 'leave' it?: ").lower()
    if choice_take == "take":
        if random.randint(1, 5) == 1:
            print(f"You found the {victory_item}!")
            inventory.append(victory_item)
            recap_log.append(f"Found the {victory_item}.")
        else:
            gold_coins = random.randint(1, 10)
            print(f"You found {gold_coins} Gold Coins!")
            inventory.append(f"{gold_coins} Gold Coins")
            recap_log.append(f"Found {gold_coins} Gold Coins.")
    else:
        print("You decided to leave the treasure.\n")
        recap_log.append("Left the treasure chest.")
    return inventory

def visit_shop(inventory):
    """Shop system where players can spend gold coins on potions or weapons."""
    clear_screen()
    print(logo)
    shop_menu()

    total_gold = sum(int(item.split()[0]) for item in inventory if "Gold Coins" in item)

    while True:
        clear_screen()
        print(logo)
        shop_menu()
        print(f"\nYour Gold Coins: {total_gold}")
        choice = input("Enter the number of the item you want to buy, or type 'exit' to leave the shop: ").lower()

        if choice == "1" and total_gold >= 5:
            inventory.append("Potion")
            total_gold -= 5
            print("You bought a Potion!")
        elif choice in ["2", "3", "4"] and total_gold >= 10:
            weapon = {"2": "Sword", "3": "Axe", "4": "Bow"}[choice]
            inventory.append(weapon)
            total_gold -= 10
            print(f"You bought a {weapon}!")
        elif choice == "exit":
            break
        else:
            print("Not enough Gold Coins or invalid choice.\n")
            time.sleep(2)

    inventory = [item for item in inventory if "Gold Coins" not in item]
    if total_gold > 0:
        inventory.append(f"{total_gold} Gold Coins")

    return inventory

def find_potion(player_health, inventory, recap_log):
    """Potion encounter to recover health or add to inventory."""
    print("\nYou found a potion!")
    choice_drink = input("Do you want to 'drink' the potion or 'save' it for later?: ").lower()
    if choice_drink == "drink":
        if player_health < player_max_health:
            old_health = player_health
            player_health = cap_health(player_health + 20)
            actual_heal = player_health - old_health
            print(f"You drank the potion and recovered {actual_heal} health.\n")
            recap_log.append(f"Drank a potion and recovered {actual_heal} health.")
        else:
            print("Your health is already full. You wasted the potion.\n")
            recap_log.append("Wasted a potion on full health.")
    else:
        inventory.append("Potion")
        print("You stored the potion in your inventory.\n")
        recap_log.append("Stored a potion in inventory.")
    return player_health, inventory

def find_weapon(inventory, recap_log):
    """Weapon encounter with a choice to take or leave it, limited to one weapon."""
    weapon = random.choice(["Sword", "Axe", "Bow"])
    print(f"\nYou found a {weapon}!")
    current_weapon = next((item for item in inventory if item in ["Sword", "Axe", "Bow"]), None)
    
    if current_weapon == weapon:
        print(f"You already have it. You keep your current weapon.\n")
        recap_log.append(f"Encountered {weapon} but kept the current one.")
        return inventory
    elif current_weapon:
        print(f"You already have a {current_weapon}. You can only carry one weapon.")
        choice_replace = input(f"Do you want to replace your {current_weapon} with the {weapon}? (yes/no): ").lower()
        if choice_replace == "yes":
            inventory.remove(current_weapon)
            inventory.append(weapon)
            print(f"You replaced your {current_weapon} with the {weapon}.\n")
            recap_log.append(f"Replaced {current_weapon} with {weapon}.")
        else:
            print(f"You decided to keep your {current_weapon}.\n")
            recap_log.append(f"Decided to keep {current_weapon}.")
    else:
        choice_take = input(f"Do you want to take the {weapon} or leave it? (take/leave): ").lower()
        if choice_take == "take":
            inventory.append(weapon)
            print(f"You added {weapon} to your inventory.\n")
            recap_log.append(f"Added {weapon} to inventory.")
        else:
            print(f"You decided to leave the {weapon}.\n")
            recap_log.append(f"Left the {weapon}.")
    return inventory
    
def find_armor(inventory, recap_log):
    """Armor encounter with a choice to take or leave it."""
    if "Armor" in inventory:
        print("\nYou found an armor.")
        print("You already have an armor on. You can't carry more than one.\n")
        recap_log.append("Encountered armor but already had one.")
    else:
        print("\nYou found a piece of Armor!")
        choice_take = input("Do you want to take the Armor or leave it? (take/leave): ").lower()
        if choice_take == "take":
            inventory.append("Armor")
            print("You added Armor to your inventory.\n")
            recap_log.append("Found and took Armor.")
        else:
            print("You decided to leave the Armor.\n")
            recap_log.append("Found but left Armor.")
    return inventory

def find_helmet(inventory, recap_log):
    """Helmet encounter with a choice to take or leave it."""
    if "Helmet" in inventory:
        print("\nYou found a Helmet.")
        print("You already have a helmet on. You can't carry more than one.\n")
        recap_log.append("Encountered helmet but already had one.")
    else:
        print("\nYou found a Helmet!")
        choice_take = input("Do you want to take the Helmet or leave it? (take/leave): ").lower()
        if choice_take == "take":
            inventory.append("Helmet")
            print("You added Helmet to your inventory.\n")
            recap_log.append("Found and took Helmet.")
        else:
            print("You decided to leave the Helmet.\n")
            recap_log.append("Found but left Helmet.")
    return inventory

def choose_difficulty():
    """Let player choose game difficulty."""
    clear_screen()
    print(logo)
    print("\n=== CHOOSE DIFFICULTY ===")
    print("1. Easy")
    print("   - Start with: Potion, Armor")
    print("   - More health (120)")
    print("   - Monsters deal less damage")
    print("\n2. Normal")
    print("   - Start with: Potion")
    print("   - Standard health (100)")
    print("   - Standard monster damage")
    print("\n3. Hard")
    print("   - No starting items")
    print("   - Less health (80)")
    print("   - Monsters deal more damage")
    
    while True:
        choice = input("\nEnter difficulty (1-3): ")
        if choice in ["1", "2", "3"]:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_starting_items(difficulty):
    """Get starting items and health based on difficulty."""
    if difficulty == "1":  # Easy
        return ["Potion", "Armor"], 120
    elif difficulty == "2":  # Normal
        return ["Potion"], 100
    else:  # Hard
        return [], 80


def show_tutorial():
    """Display game tutorial."""
    clear_screen()
    print(logo)
    print("\n=== TUTORIAL ===")
    print("\nBASIC CONCEPTS:")
    print("- Explore rooms to find items and face monsters")
    print("- Find the Ancient Artifact to win")
    print("- Stay alive while exploring")
    
    input("\nPress Enter to continue...")
    clear_screen()
    print(logo)
    print("\nCOMBAT TIPS:")
    print("- Weapons increase your damage (8-15 instead of 5-10)")
    print("- Armor reduces incoming damage by 3")
    print("- Helmet reduces incoming damage by 2")
    print("- Potions heal 20 health")
    
    input("\nPress Enter to continue...")
    clear_screen()
    print(logo)
    print("\nSTRATEGIES:")
    print("- Save potions for tough battles")
    print("- Fleeing might cost you an item but can save your life")
    print("- The Ancient Artifact appears in treasure chests")
    print("- Collect equipment to become stronger")
    input("\nPress Enter to continue...")

    clear_screen()
    print(logo)
    print("IN BATTLES, YOU CAN:\n- Attack the monster\n- Use a potion to heal\n- Try to flee (but you might lose an item!\n)")
    print("Good luck, Adventurer!\n")
    
    input("\nPress Enter to start your adventure...")
    
def random_event(player_health, recap_log):
    """Random event that affects player's health."""
    events = [
        ("You found a hidden spring! It healed you by 10 health.\n", 10, "Found a hidden spring and gained 10 health."),
        ("A sudden storm hit! You lost 10 health.\n", -10, "Got caught in a storm and lost 10 health.")
    ]
    event, health_change, log_message = random.choice(events)
    print(f"\n{event}")
    old_health = player_health
    player_health = cap_health(player_health + health_change)
    actual_change = player_health - old_health if health_change > 0 else health_change
    recap_log.append(log_message.replace("10", str(abs(actual_change))))
    return player_health

def empty_room():
    """Empty room encounter."""
    print("\nThe room is empty. Nothing to do here.\n")

def rooms(choose_room):
    """Random encounter function."""
    return random.choice(choose_room)

def adventure_time():
    clear_screen()
    print(logo)
    print("Welcome to Adventure Time!\nYour goal is to find the Ancient Artifact and escape 'ALIVE'.\n")
    
    if input("Would you like to see the tutorial? (y/n): ").lower() == 'y':
        show_tutorial()

    difficulty = choose_difficulty()
    inventory, player_health = get_starting_items(difficulty)
    
    attack_power = 5
    game_over = False
    recap_log = []
    first_turn = True  

    damage_multiplier = {
        "1": 0.8,
        "2": 1.0,
        "3": 1.2
    }[difficulty]

    clear_screen()
    print(logo)

    while not game_over:
        if player_health > 0 and victory_item not in inventory:
            if not first_turn:
                cont = input("Do you want to continue exploring? (y/n): ").lower()
                if cont == "n":
                    print("You chose to end the adventure.")
                    break
                elif cont != "y":
                    clear_screen()
                    print(logo)
                    print("\nYou gave up...\n")
                    recap_log.append("Gave up and ended the adventure.")
                    game_over = True
                    continue
            else:
                first_turn = False  

            if random.randint(1, 5) == 1:
                clear_screen()
                print(logo)
                cont = input("\nA shop appeared out of nowhere.\nDo you want to check it out? (yes/no): ").lower()
                if cont == "yes":
                    inventory = visit_shop(inventory)
                    continue

            clear_screen()
            print(logo)
            print(f"Player Health: {player_health}")
            print(f"Inventory: {inventory}")
            encounter = rooms(encounters)
            if encounter == "monster":
                player_health, inventory = monster_battle(player_health, inventory, recap_log, damage_multiplier)
                time.sleep(2)
            elif encounter == "treasure":
                inventory = find_treasure(inventory, recap_log)
                time.sleep(2)
            elif encounter == "potion":
                player_health, inventory = find_potion(player_health, inventory, recap_log)
                time.sleep(2)
            elif encounter == "weapon":
                inventory = find_weapon(inventory, recap_log)
                time.sleep(2)
            elif encounter == "armor":
                inventory = find_armor(inventory, recap_log)
                time.sleep(2)
            elif encounter == "helmet":
                inventory = find_helmet(inventory, recap_log)
                time.sleep(2)
            elif encounter == "random_event":
                player_health = random_event(player_health, recap_log)
                time.sleep(2)
            else:
                empty_room()
                recap_log.append("Entered an empty room.")
                time.sleep(2)
        elif player_health <= 0:
            print("You Died.")
            recap_log.append("Died in the adventure.")
            game_over = True
        elif victory_item in inventory:
            clear_screen()
            print(logo)
            print("Congratulations! You found the Ancient Artifact and won the game!\n")
            recap_log.append("Found the Ancient Artifact and won the game.")
            game_over = True
        else:
            print("Game Over")
            game_over = True
    
    print("Your final stats:")
    print(f"Player Health: {player_health}")
    print(f"Inventory: {inventory}")
    print("\nRecap of your adventure:")
    for log in recap_log:
        print(f"- {log}")

adventure_time()

while input("\nDo you want to start a new adventure?(y/n): ").lower() == "y":
    adventure_time()

print("Bye!")