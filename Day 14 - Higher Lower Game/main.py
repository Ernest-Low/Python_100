
from game_data import data
from art import logo
from art import vs
import os
import random
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#Add a score? Average number of right choices per rounds

#Refresh the conditions for game
def refresh() :
    global used_values
    used_values = []

#Pick a random non-repeating until 50 are met per round
def pick_dict () :
    global used_values
    if len(used_values) == 50 :
        victory()
    else :
        return_obj = []
        rand = random.randint(0, len(data)-1)
        while rand in used_values :
            rand = random.randint(0, len(data)-1)
        used_values.append(rand)
        return_obj = [rand, data[rand]]
        return return_obj


#Per match display
def match(obj1, obj2) :
    print (f"1: Name: {obj1['name']} | Description: {obj1['description']} | Country: {obj1['country']}")
    print(vs)
    print (f"2: Name: {obj2['name']} | Description: {obj2['description']} | Country: {obj2['country']}")
    # print(f"Debug: Follower Counts: {obj1['name']} : {obj1['follower_count']} | {obj2['name']} : {obj2['follower_count']}")
    choice = input("\nWho has more followers! 1/2\n")
    while choice != "1" and choice != "2" :
        print("Invalid Input")
        choice = input("Who has more followers! 1/2\n")
    choice = int(choice)
    if choice == 1 and obj1['follower_count'] >= obj2['follower_count'] :
        print("You got it! On to the next round!")
        print(f"Follower Counts: {obj1['name']} : {obj1['follower_count']} | {obj2['name']} : {obj2['follower_count']}")
        score[0] += 1
        print(f"Your current score: {score[0]}")
        time.sleep(5)
        clearConsole()
        new_match(obj1)
    elif choice == 2 and obj2['follower_count'] >= obj1['follower_count'] :
        print("You got it! On to the next round!")
        print(f"Follower Counts: {obj1['name']} : {obj1['follower_count']} | {obj2['name']} : {obj2['follower_count']}")
        score[0] += 1
        print(f"Your current score: {score[0]}")
        time.sleep(5)
        clearConsole()
        new_match(obj2)
    else :
        print("Oh no, you got it wrong :( Round over!")
        print(f"Follower Counts: {obj1['name']} : {obj1['follower_count']} | {obj2['name']} : {obj2['follower_count']}")
        print(f"Round's ending score: {score[0]}")
        score[2] += 1
        new_round()

#Victory at 49 consecutive corrects
def victory() :
    clearConsole()
    score[1] += score[0]
    score[2] += 1
    ave = score[1] / score[2]
    print(logo)
    print("You beat the game; All possible variations in the data have been used.")
    print(f"Final Score: Average of {ave} over {score[2]} rounds")
    
#Generate a new round or game over
def new_round() :
    score[1] += score[0]
    score[0] = 0
    choice = input("Go again? Y/N\n").lower()
    while choice != "y" and choice != "n" :
        print("Invalid Input")
        choice = input("Go again? Y/N\n").lower()
    if choice == "y" :
        refresh()
        clearConsole()
        obj1 = pick_dict()
        data1 = obj1[1]
        new_match(data1)
    else :
        print(logo)
        print("Game Over!")
        ave = score[1] / score[2]
        print(f"Final Score: Average of {ave} over {score[2]} rounds")


#Generate a new match
def new_match(obj) :
    data1 = obj
    obj2 = pick_dict()
    data2 = obj2[1]
    match(data1, data2)


#Welcome sequence
def main() :
    global score #Declare this variable only once!
    score = [0,0,0] #score[0] is current score, score[1] is total score, score[2] is rounds played
    print(logo)
    print("Welcome to Higher Lower Game! - Instagram Version\n")
    obj1 = pick_dict()
    data1 = obj1[1]
    new_match(data1)

# #Delete based on name
# def del_name(name) :
#     for i in range(len(data)) :
#         if data[i]['name'] == name :
#             del data[i]
#             break

# def vsdata (data) :
#     print(data['name'])
#     # print(data['follower_count'])   #Hide this!
#     print(data['description'])
#     print(data['country'])


#Running code outside functions - keep this short!
clearConsole()
refresh()
main()
