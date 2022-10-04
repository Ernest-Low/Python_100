""" 
3 Coffee flavors - 
$1.50   Espresso     50ml Water     18g Coffee
$2.50   Latte        200ml Water    24g Coffee      150ml Milk
$3.00   Cappuccino   250ml Water    24g Coffee      100ml Milk
"""
from resource import resources
from resource import menu
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def payment(cost) :
    # print(f"Debug: {cost}")
    print("Please insert coins.")
    quarters = input("How many quarters?: ")    #0.25
    while quarters.isdecimal() == False :
        print("Invalid Input")
        quarters = input("How many quarters?: ")    #0.25
    quarters = int(quarters)
    dimes = input("How many dimes?: ")          #0.10
    while dimes.isdecimal() == False :
        print("Invalid Input")
        dimes = input("How many dimes?: ")    #0.25
    dimes = int(dimes)
    nickles = input("How many nickles?: ")      #0.05
    while nickles.isdecimal() == False :
        print("Invalid Input")
        nickles = input("How many nickles?: ")    #0.25
    nickles = int(nickles)
    pennies = input("How many pennies?: ")      #0.01
    while pennies.isdecimal() == False :
        print("Invalid Input")
        pennies = input("How many pennies?: ")    #0.25
    pennies = int(pennies)
    all_coins = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    # print(f"Debug: Coins inserted value: {all_coins}")
    change = all_coins - cost
    change = round(change, 2)
    if change < 0 :
        print("Sorry that's not enough money. Money refunded.")
        return False
    else :
        print(f"Here is ${change} in change.")
        resources["money"] += all_coins
        return True

def report() :
    clearConsole()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def order(inputkey) :
    if inputkey == 1 :
        item = menu["espresso"]
        drink = "espresso"
    elif inputkey == 2 :
        item = menu["latte"]
        drink = "latte"
    elif inputkey == 3 :
        item = menu["cappuccino"]
        drink = "cappuccino"
    
    # print("Debug: Ingredient checking")
    water = item["ingredients"]["water"]             # Water cost of drink
    milk = item["ingredients"]["milk"]               # Milk cost of drink
    coffee = item["ingredients"]["coffee"]           # Coffee cost of drink
    water2 = resources["water"]                      # Current water in supply
    milk2 = resources["milk"]                        # Current milk in supply
    coffee2 = resources["coffee"]                    # Current coffee in supply
    if water > water2 :                              # Compare water cost to supply
        print("Sorry, there is not enough water")
        return
    elif milk > milk2 :                              # Compare milk cost to supply
        print("Sorry, there is not enough milk")
        return
    elif coffee > coffee2 :                          # Compare coffee cost to supply
        print("Sorry, there is not enough coffee")
        return
    paid = payment(item["cost"])                     # Call payment function with drink cost
    if paid == True :
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print(f"Here is your {drink}, enjoy! \U00002615 \n\n")


        


    
def inputcmd() :        # Main screen for machine
    on = True
    while on == True :
        print("Coffee Machine v1.0\n1: Espresso ($1.50)\n2: Latte ($2.50)\n3: Cappuccino ($3.00)")
        # print("Debug: report:  Print report | off : Shut down")
        inputkey = input("Enter a command: ")
        if inputkey == "off" :                  # Off / Exit
            on == False
            print("Shutting down...")
            exit()
        elif inputkey == "report" :             # Open report window
            report()
        elif inputkey == "1" or inputkey == "2" or inputkey == "3" :        # Order drink function
            inputkey = int(inputkey)
            order(inputkey)
        else:
            print("Invalid input")

clearConsole()
inputcmd()
# print("\U00002615")     #Coffee?
# print("\U0001F375")     #Tea?