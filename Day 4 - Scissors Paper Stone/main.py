#Day 4 Exercise - Scissors Paper Stone

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game = True
wins = 0
loss = 0
draw = 0

print("Welcome to a completely fair Scissors Paper Stone")

while game == True :
    pick = True
    while pick == True :
        print("Cast your move!\n1 for Scissors\n2 for Paper\n3 for Stone!")
        choice = input()
        if choice[0] == "1" or choice[0] == "2" or choice[0] == "3" :
            pick = False
            choice = int(choice[0])
        else :
            print("Invalid input, again!")
    
    if choice == 1 :
        player = scissors
    elif choice == 2 :
        player = paper
    else :
        player = rock
    
    ene_rand = random.randint(1,3)
    if ene_rand == 1 :
        enemy = scissors
    elif ene_rand == 2 :
        enemy = paper
    else :
        enemy = rock
    print("And the results are:\nYour Pick:\n" + player)
    print("And the opponent picked:\n" + enemy)
    if ene_rand == choice :
        print("It's a draw!")
        draw += 1
    elif ene_rand == 1 and choice == 2 :
        print("You lose!")
        loss += 1
    elif ene_rand == 2 and choice == 3 :
        print("You lose!")
        loss += 1
    elif ene_rand == 3 and choice == 1 :
        print("You lose!")
        loss += 1
    else :
        print("You win!")
        wins += 1
    gameover = input("Go again? Y / N ")
    if gameover.lower() == "y" :
        print(f"Next round! Current score: {wins} Wins {loss} Losses {draw} Draws")
    else :
        game = False
        print(f"Game Over! Ending score: {wins} Wins {loss} Losses {draw} Draws")





