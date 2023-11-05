import sys

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
            "coffee": 150,
            "milk": 100,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 50,
        },
        "cost": 3.0,
    }
}

coins = 0
resources = {
    "water": 500,
    "milk": 400,
    "coffee": 300
}

total_coins_earned = 0

def get_beverage_cost(beverage_name):
    cost = MENU[beverage_name]["cost"]
    return cost

def coins_handler(quarters, dimes, nickels, pennies, beverage_name):
    cost = get_beverage_cost(beverage_name)
    coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    
    if coins == cost:
        print(f"Here is your {beverage_name} ☕ Enjoy!")
        return True
    elif coins > cost:
        change = coins - cost
        print(f"Here is your {beverage_name} ☕ Enjoy! Your change is {change}$.")
        return True
    else:
        print("Not enough coins inserted.")
        return False

def check_resources(beverage_name):
    ingredients = MENU[beverage_name]["ingredients"]
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry, we ran out of {ingredient}.")
            return False
    return True

def deduct_resources(beverage_name):
    ingredients = MENU[beverage_name]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount

def report():
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    
    return f"Water: {water}ml\nCoffee: {coffee}g\nMilk: {milk}ml"

while True:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option == "off":
        sys.exit("The machine is off.")

    if option == "report":
        report_text = report()
        print(report_text)
        print(f"Total coins earned: {total_coins_earned}$")
        continue

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    if check_resources(option):
        if coins_handler(quarters, dimes, nickels, pennies, option):
            deduct_resources(option)
            coins = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            total_coins_earned += coins
    else:
        sys.exit("The machine is out of ingredients. Cannot continue operation.")
