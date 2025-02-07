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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,


}
is_on= True
def is_enough(order):
    # is_enough = True
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    print("insert coins!")
    total = int(input("how many quaters: "))*0.25
    total += int(input("how many dimes: "))*0.1
    total += int(input("how many nickles: "))*0.05
    total += int(input("how many pennies: "))*0.01
    return total


def transaction_succ(money_received, costof_drink):
    if money_received >= costof_drink:
        change = round(money_received-costof_drink, 2)
        print(f"here is ur change {change}")
        global profit
        profit += costof_drink
        return True
    else:
        print("not enough money, money refunded")
        return False


def make_cofee(drink,order):
    for i in order:
        resources[i] -= order[i]
    print("here is ur drink ☕")


while is_on:
    user_input = (input("What would you like? (espresso/latte/cappuccino): "))
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        for key, value in resources.items():
            print(key, ":", value)
        print("profit: ",profit)
    else:
        drink= MENU[user_input]
        if is_enough(drink["ingredients"]):
            payment = process_coins()
            if transaction_succ(payment, drink['cost']):
                make_cofee(user_input, drink['ingredients'])



