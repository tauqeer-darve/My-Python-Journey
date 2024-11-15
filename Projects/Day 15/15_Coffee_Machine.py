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

def making(cost1, water_av, wat, coffee_av, coff, milk_av, mil,earning):
    """Function to process the making of coffee"""
    if water_av >= wat and coffee_av >= coff and milk_av >= mil:
        print("Please insert coins.")
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        money = round(quarters + dimes + nickles + pennies, 2)
        if money >= cost1:
            earning += cost1
            money -= cost1
            water_av -= water
            milk_av -= milk
            coffee_av -= coffee
            for _ in range(3):
                time.sleep(1)
                print(".")
            time.sleep(1)
            print(f"Here is your ${money} in change.")
            print(f"And here is your {choice} ☕️, Enjoy!\n")
            return [water_av, milk_av, coffee_av, earning]
        else:
            print("Sorry that's not enough money. Money refunded.\n")
    elif water_av < wat:
        print("Sorry, there is not enough water.\n")
    elif coffee_av < coff:
        print("Sorry, there is not enough coffee.\n")
    elif milk_av < mil:
        print("Sorry, there is not enough milk.\n")

def resources_report(wat_av,mil_av,coff_av,earning):
     """report generation function"""
     print("Processing",end='')
     for _ in range(3):
         time.sleep(1)
         print(".", end="")
     time.sleep(1)
     print(f"\nWater: {wat_av}")
     print(f"Milk: {mil_av}")
     print(f"Coffee: {coff_av}g")
     print(f"Money: ${earning}\n")


def process():
    """Tiny ... animation"""
    for _ in range(3):
        time.sleep(1)
        print(".", end="")
    time.sleep(1)


stop = False
earnings = 0
water_available = resources["water"]
milk_available = resources["milk"]
coffee_available = resources["coffee"]
report = ""
run = 0
while not stop:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU:
        water = MENU[f'{choice}']["ingredients"]["water"]
        if choice == "espresso":
            milk = 0
        else:
            milk = MENU[f'{choice}']["ingredients"]["milk"]
        coffee = MENU[f'{choice}']["ingredients"]["coffee"]
        cost = MENU[f'{choice}']["cost"]

        if choice == "latte":
            report = making(cost,water_available,water,coffee_available,coffee,milk_available,milk,earnings)
            run += 1

        elif choice == "cappuccino":
            report = making(cost,water_available,water,coffee_available,coffee,milk_available,milk,earnings)
            run += 1

        elif choice == "espresso":
            report = making(cost,water_available,water,coffee_available,coffee,milk_available,milk,earnings)
            run += 1

        if report:
            water_available = report[0]
            milk_available = report[1]
            coffee_available = report[2]
            earnings = report[3]

    elif choice == "report":
        resources_report(water_available,milk_available,coffee_available,earnings)

    elif choice == "off":
        power = "Switching Off"
        print("Switching Off",end='')
        process()
        stop = True

    else:
        print("Invalid option.")