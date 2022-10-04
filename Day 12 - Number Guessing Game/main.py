#Day 12 - Number Guessing Game


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import os
from art import logo

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def get_guess() :
    user_guess = input("Guess a number from 1 - 100\n")
    while user_guess.isdecimal() == False :
        print("Invalid Input")
        user_guess = input("Guess a number from 1 - 100\n")
    user_guess = int(user_guess)
    return user_guess

def get_turns() :
    user_turns = input("Choose between Easy Mode: 10 Turns | Hard Mode: 5 Turns\nEasy/Hard\n").lower()
    while user_turns != "easy" and user_turns != "hard" :
        print("Invalid Input")
        user_turns = input("Choose between Easy Mode: 10 Turns | Hard Mode: 5 Turns\nEasy/Hard\n").lower()
    if user_turns == "easy" :
        return 10
    else: 
        return 5


def check(check_value) :
    global total_turns
    global clears
    return_value = check_value
    if check_value[0] == check_value[1] :
        print(f"Winner! | Remaining Turns: {return_value[2]}")
        return_value[2] = -1
        total_turns += 1
        clears += 1
    elif check_value[0] > check_value[1] :
        return_value[2] -= 1
        total_turns += 1
        print(f"Too High | Remaining Turns: {return_value[2]}")
    elif check_value[0] < check_value[1] :
        return_value[2] -= 1
        total_turns += 1
        print(f"Too Low | Remaining Turns: {return_value[2]}")
    return return_value
    
def game_loss (check_value) :
    global clears
    print("Round over! You did not guess the number. Round over")
    clears += 1
    print(f"The number was: {check_value[1]}")


def main() :
    print(logo)
    turns = get_turns()
    goal = random.randint(1,100)
    guess = get_guess()
    check_value = [guess, goal, turns]
    check_value = check(check_value)
    while check_value[2] > 0 :
        check_value[0] = get_guess()
        check_value = check(check_value)
    if check_value[2] == 0 :
        game_loss(check_value)
    print(f"Current Session: Average turns used over {clears} rounds: {total_turns / clears}")
    again = input("Play again? Y/N\n").lower()
    while again != "y" and again != "n" :
        print("Invalid Input")
        again = input("Play again? Y/N\n").lower()
    if again == "y" :
        clearConsole()
        main()
    else:
        print(f"Game End | Average turns used over {clears} rounds: {total_turns / clears}")

clearConsole()
global total_turns
global clears
total_turns = 0
clears = 0
main()