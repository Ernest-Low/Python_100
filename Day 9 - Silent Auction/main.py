import os
from art import logo

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def highest_check (bid_dict) :
    clash = {}
    winner = ""
    max = 0
    for key in bid_dict :
        if bid_dict[key] > max :
            max = bid_dict[key]
            winner = key
        elif bid_dict[key] == max :
            clash[winner] = max
            clash[key] = bid_dict[key]
    if clash == {} :
        clash[winner] = max
    return clash


def auction_info() :
    bidders = {}
    other = "y"
    while other == "y" :
        name = input("What is your name?\n")
        bid = input("What is your bid?\n")
        while bid.isdecimal() == False or bid == "0":
            print("Invalid Input")
            bid = input("What is your bid?\n")
        bid = int(bid)
        other = input("Are there any other bidders? Y/N\n").lower()
        while other != "y" and other != "n" :
            print("Invalid Input")
            other = input("Are there any other bidders? Y/N\n").lower()

        bidders[name] = bid
        clearConsole()
    return bidders

def mainprogram() :
    print(logo)
    print("Welcome to the secret auction program")
    participants = auction_info()
    winner = highest_check(participants)
    if len(winner) > 1 :
        print("Similar highest bids found")
        for key in winner :
            print(f"{key} bid ${winner[key]}")
    else :
        for key in winner :
            print(f"The winner is {key} is with a bid of ${winner[key]}!")

    again = ""
    again = input("Go again? Y/N\n").lower()
    while again != "y" and again != "n" :
        print("Invalid Input")
        again = input("Go again? Y/N\n").lower()
    if again == "y" :
        clearConsole()
        mainprogram()
    else : 
        print("The End")

mainprogram()



