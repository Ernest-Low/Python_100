# Day 11 - Capstone Blackjack

import random
import os
from art import logo

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#   Clubs: \u2663  Spades: \u2660  Diamond: \u2666  Heart: \u2665
cardtype = ["A\u2663", "2\u2663", "3\u2663", "4\u2663", "5\u2663", "6\u2663", "7\u2663", "8\u2663", "9\u2663", "10\u2663", "J\u2663", "Q\u2663", "K\u2663",
            "A\u2660", "2\u2660", "3\u2660", "4\u2660", "5\u2660", "6\u2660", "7\u2660", "8\u2660", "9\u2660", "10\u2660", "J\u2660", "Q\u2660", "K\u2660",
            "A\u2666", "2\u2666", "3\u2666", "4\u2666", "5\u2666", "6\u2666", "7\u2666", "8\u2666", "9\u2666", "10\u2666", "J\u2666", "Q\u2666", "K\u2666",
            "A\u2665", "2\u2665", "3\u2665", "4\u2665", "5\u2665", "6\u2665", "7\u2665", "8\u2665", "9\u2665", "10\u2665", "J\u2665", "Q\u2665", "K\u2665"]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
score = [0,0,0]

def init() :
    global cards_exhausted
    global player
    global dealer
    global gamestatus
    cards_exhausted = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    player = ["Player",[],[]]
    dealer = ["Dealer",[],[]]
    gamestatus = True

def draw_card() :
    card = []
    drawvalid = False
    while drawvalid == False :
        cardno = random.randint(0, 35)
        if cards_exhausted[cardno] == 1 :
            card.append(cards[cardno])
            card.append(cardtype[cardno])
            cards_exhausted[cardno] = 0
            drawvalid = True
    return card

def addtohand(hand, cards, mention) :
    hand[1].append(cards[0])
    hand[2].append(cards[1])
    if mention == True :
        print(f"{hand[0]} draws {cards[1]}")

def check_value(cardlist) :
    value = 0
    for x in cardlist[1] :
        value += x
    value = check_ace(cardlist)
    return value

def check_ace(cardlist) :
    value = 0
    for x in cardlist[1] :
        value += x
    if value > 21 and 11 in cardlist[1] :
        value -= 10
    return value
        
def draw_prompt() :
    global gamestatus
    drawcheck = input("Do you want to draw another card? Y/N\n").lower()
    while drawcheck != "y" and drawcheck != "n" :
        print("Invalid Input")
        drawcheck = input("Do you want to draw another card? Y/N\n").lower()
    if drawcheck == "y" :
        addtohand(player, draw_card(), True)
        gamestatus = check_win(False)
        if gamestatus == True :
            print(f"Your cards: {printcards(player)}")
            print(f"Your total card value: {check_value(player)}")
            return True
        else :
            return False
    else :
        return False
    
def check_win(final) :
    playervalue = check_value(player)
    dealervalue = check_value(dealer)
    if dealervalue == 21 :
        print("Blackjack! You lose!")
        print(f"Your final hand: {printcards(player)}, Dealer final hand: {printcards(dealer)}")
        print(f"Your score was {playervalue} and the dealer had {dealervalue}")
        score[1] += 1
        return False
    elif playervalue == 21 :
        print("Blackjack! You win!")
        print(f"Your final hand: {printcards(player)}, Dealer final hand: {printcards(dealer)}")
        print(f"Your score was {playervalue} and the dealer had {dealervalue}")
        score[0] += 1
        return False
    elif playervalue > 21 :
        print(f"Bust! You lost!")
        print(f"Your final hand: {printcards(player)}, Dealer final hand: {printcards(dealer)}")
        print(f"Your score was {playervalue} and the dealer had {dealervalue}")
        score[1] += 1
        return False
    elif dealervalue > 21 :
        print(f"Bust! You win!")
        print(f"Your final hand: {printcards(player)}, Dealer final hand: {printcards(dealer)}")
        print(f"Your score was {playervalue} and the dealer had {dealervalue}")
        score[0] += 1
        return False
    if final == True :
        print(f"Your final hand: {printcards(player)}, Dealer final hand: {printcards(dealer)}")
        if playervalue == dealervalue :
            print(f"Draw! Both have total score of {playervalue}")
            score[2] += 1
        elif playervalue > dealervalue :
            print(f"You win! Your score was {playervalue} and the dealer had {dealervalue}")
            score[0] += 1
        else :
            print(f"You lose! Your score was {playervalue} and the dealer had {dealervalue}")
            score[1] += 1
        return False
    return True
    

def printcards(cardlist) :
    list = " ".join(cardlist[2])
    return list


def maingame() :
    global gamestatus
    print(logo)
    addtohand(player, draw_card(), False)
    addtohand(player, draw_card(), False)
    addtohand(dealer, draw_card(), False)
    addtohand(dealer, draw_card(), False)

    print(f"Your cards: {printcards(player)}")
    print(f"Your total card value: {check_value(player)}")
    print(f"Dealer's upcard: {dealer[2][0]}")
    drawing = draw_prompt()
    while drawing == True :
        drawing = draw_prompt()
    if check_value(dealer) < 16 :
        print("The dealer's hand was below 16 in value, they draw a card")
        addtohand(dealer, draw_card(), True)
    if gamestatus == True :
        while check_value(dealer) < 16 :
            print("The dealer's hand was below 16 in value, they draw a card")
            addtohand(dealer, draw_card(), True)
        gamestatus = check_win(True)
    print(f"Your score this session: {score[0]} Wins, {score[1]} Loss, {score[2]} Ties")
    again = input("Go again? Y/N\n").lower()
    while again != "y" and again != "n" :
        print("Invalid Input")
        again = input("Go again? Y/N\n").lower()
    if again == "y" :
        init()
        clearConsole()
        maingame()
    else :
        print("Game Over!")
        print(f"Your score this session: {score[0]}Wins, {score[1]}Loss, {score[2]}Ties")


init()
maingame()
