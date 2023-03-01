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
        "cost": 1.5,
    },
}


def resources_check(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        return True


def insert_coins():
    total = int(input("quaters $0.25: ")) * 0.25
    total += int(input("dimes $0.10: ")) * 0.10
    total += int(input("nickles $0.05: ")) * 0.05
    total += int(input("pennies $0.01: ")) * 0.01
    return total


profit = 0

resources = {
    "water": 1000,
    "milk": 600,
    "coffee": 200,
}

power = True

while power:
    user_choice = input("What would you like? espresso/latte/cappuccino: ")
    if user_choice == "off":
        power = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if resources_check(drink["ingredients"]):
            insert_coins()
