from data import MENU, resources
from data import resources
#print(resources)

def report(rsrc, money):
    print(f"Water: {rsrc['water']}ml")
    print(f"Milk: {rsrc['milk']}ml")
    print(f"Coffee: {rsrc['coffee']}g")
    print(f"Money: ${money}")


def ask_coins():
    print("Please insert coins:")
    inserted_quarters = int(input("How many quarters?: "))
    inserted_dimes = int(input("How many dimes?: "))
    inserted_nickles = int(input("How many nickles?: "))
    inserted_pennies = int(input("How many pennies?: "))
    paid_money = inserted_quarters * 0.25 + inserted_dimes * 0.1 + inserted_nickles * 0.05 + inserted_pennies * 0.01
    return paid_money


def check_resourses(resrc, coffee_type, data):
    if resrc['water'] - data[coffee_type]["ingredients"]["water"] > 0 and resrc['milk'] - data[coffee_type]["ingredients"]["milk"] > 0 and resrc['coffee'] - data[coffee_type]["ingredients"]["coffee"] > 0:
        return 1
    else:
        return 0


def resourses(resrc, coffee_type, data):
    resrc['water'] -= data[coffee_type]["ingredients"]["water"]
    resrc['milk'] -= data[coffee_type]["ingredients"]["milk"]
    resrc['coffee'] -= data[coffee_type]["ingredients"]["coffee"]
    return resrc


def check_transact(cash, price):
    if cash - price >= 0:
        return 1
    else:
        return 0
def transact(cash, cashbox, price):
    print(f"Your change is ${cash - price:5.2f}.")
    return cashbox + price




def coffee_machine(resources_data, data):
    order = ""
    money = 0
    while order != "off":
        order = input("What would you like? (espresso/latte/cappuccino/report): ")
        if order == 'off':
            return
        elif order == 'report':
            report(resources_data, money)
        elif order in ('espresso', 'latte', 'cappuccino'):
            given_cash = ask_coins()
            if check_resourses(resources_data, order, data) == 0:
                print("Not enough recourses")
            else:
                if check_transact(given_cash, money) == 0:
                    print("Not enough money.")
                else:
                    resources_data = resourses(resources_data, order, data)
                    money = transact(given_cash, money, data[order]['cost'])
                    print(f"Here is your {order}!☕")
        else:
            print("Please give right order.")


coffee_machine(resources, MENU)
