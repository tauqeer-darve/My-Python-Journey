import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process():
    """Tiny ... animation"""
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    time.sleep(1)

def check_resources(choice):
    """Check if resources are sufficient for the selected coffee"""
    ingredients = MENU[choice]["ingredients"]
    for item, amount in ingredients.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.\n")
            return False
    return True

def process_coins():
    """Process coin insertion and return the total money"""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def make_coffee(choice):
    """Deduct resources to make the selected coffee"""
    ingredients = MENU[choice]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"And here is your {choice} ☕️, Enjoy!\n")

def resources_report(earnings):
    """Generate a report of current resources"""
    print("Processing", end="", flush=True)
    process()
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${earnings}\n")

#Main program:
stop = False
earnings = 0

while not stop:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice in MENU:
        if check_resources(choice):
            money_inserted = process_coins()
            cost = MENU[choice]["cost"]

            if money_inserted >= cost:
                change = round(money_inserted - cost, 2)
                earnings += cost
                process()
                print(f"\nHere is your ${change} in change.")
                make_coffee(choice)
            else:
                print("Sorry that's not enough money. Money refunded.\n")

    elif choice == "report":
        resources_report(earnings)

    elif choice == "off":
        print("Switching Off", end="", flush=True)
        process()
        stop = True

    else:
        print("Invalid option.")