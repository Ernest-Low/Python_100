#Coffee Machine V2 with OOP (Course version)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
new_menu = Menu()
new_coffee_maker = CoffeeMaker()
new_money_machine = MoneyMachine()

on = True
clearConsole()

while on == True :
    print("Coffee Machine v2.0\nLatte\nEspresso\nCappuccino")
    input_value = input().lower()
    if input_value == "report" :
        new_coffee_maker.report()
        new_money_machine.report()
        print("\n\n")
    elif input_value == "off" :
        print("Turning off..")
        exit()
    elif input_value != "" :
        try :
            item = new_menu.find_drink(input_value)
            sufficient = new_coffee_maker.is_resource_sufficient(item)
            if sufficient == True :
                paid = new_money_machine.make_payment(item.cost)
                if paid == True :
                    new_coffee_maker.make_coffee(item)
            print("\n\n")
        except :
            print("\n\n")
            continue
        
    
    
        



# new_menu.find_drink(input("Enter a drink name"))

# print(new_menu.find_drink("latte"))
# print(new_menu.__init__)