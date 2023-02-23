"""
resources 
    3000ml water
    2000ml milk
    200g coffee
3 drinks
    Espresso - $1.50 - 50ml water, 18g coffee
    Latte - $2.50 - 200ml water, 24g coffee, 150ml milk
    Cappuccino - $3.00 - 250ml water, 24g coffee, 100ml milk
Taking Coins
    penny - 1c
    Nickle - 5c
    Dime - 10c
    Quarter - 25c
"""


class Machine:
    def __init__(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price
        self.water = 3000
        self.milk = 2000
        self.coffee = 200

    def print(self):
        print(self.ingredients, self.price)


class Balance:
    def deposit(self):
        coins = [1, 5, 10, 25]


class Coffee:
    def espresso(self):
        ingredients = {"water": 50, "milk": 0, "coffee": 18}
        price = 1.5
        return Machine(ingredients, price)

    def latte(self):
        ingredients = {"water": 200, "milk": 150, "coffee": 24}
        price = 2.5
        return Machine(ingredients, price)

    def cappuccino(self):
        ingredients = {"water": 250, "milk": 100, "coffee": 24}
        price = 3
        return Machine(ingredients, price)


coffeeMachine = Coffee()
coffeeMachine.latte().print()
