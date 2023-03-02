from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

power = True

while power:
    user_choice = input(f"What would you like? {menu.get_items()} ")
    if user_choice == "off":
        power = False
    elif user_choice == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(user_choice)
        if machine.is_resource_sufficient(drink):
            print(drink)
