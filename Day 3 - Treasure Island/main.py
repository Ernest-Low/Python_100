# Day 3 Project : Treasure Island


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("The island awaits, however you need to priotise an item to obtain for the journey. Choose between: Map / Weapon / Torchlight")
choiceone = input()
print("The journey begins. You reach the island admist much difficulty but now there is a path of three crossroads. Choose between: Left / Center / Right")
if choiceone.lower() == "map" :
    print("Reading the map, the right leads to the treasure, you should pick it!")
choicetwo = input()
if choicetwo.lower() == "left" :
    print("The path never seems to end, you cant help but feel like you've gotten stuck in an infinite loop, even retracing your steps doesn't work as you seem to be trapped.\nGame Over")
elif choicetwo.lower() == "center" :
    print("As you continue along the path, suddenly the ground gives way. Rows of spikes impale you at the bottom of the pit and you died.\nGame Over")
else :
    print("You come across a thick woods, it is too dark to make out anything. You barely make out the sound of footsteps behind you, slowly approaching. Choose between: Run / Turn / Climb")
    if choiceone.lower() == "torchlight" :
        print("With the torchlight, you can make out a small wooden shed ahead")
    choicethree = input()
    if choicethree.lower() == "turn" :
        print("You turn around and you're greeted by a tall thin dark figure. You look up to meet it's face and you black out as your ears buzz with unnatural static.\nGame Over")
    elif choicethree.lower() == "climb" :
        print("You attempt to climb a tree, but a branch breaks and you freefall to the ground, and to whatever awaits you there...\nGame Over")
    else :
        print("Running ahead, you come across a small wooden shed. You bolt inside and lock the door behind you. However, a skeleton that was sitting on a chair slowly gets up. Chosee between: Fight / Escape / Hide")
        choicefour = input()
        if choicefour.lower() == "escape" :
            print("You open the door to escape, but you're greeted by a featureless face with a tophat. Your vision blacks out and your ears buzz with unnatural static.\nGame Over")
        elif choicefour.lower() == "fight" and choiceone.lower() == "weapon" :
            print("You try to fight off the skeleton, but as you're about to land what could be a fatal blow, a hand rests on your shoulder. You turn around and meet a featureless face that seems to suck away your soul. You attempt to stab it but you black out.\nGame Over")
        elif choicefour.lower() == "fight" :
            print("You attempt to fight off the skeleton, but it stabs you with a rusty cutlass in the heart.\nGame Over")
        else :
            print("You hide in a corner behind a shelf, hoping it didn't notice you. You hear the door open, then close a short while later. You peek and see the skeleton just standing there motionlessly. There appears to be a chest behind the skeleton.")
            print("Choose between: Fight / Sneak / Escape")
            choicefive = input()
            if choicefive.lower() == "sneak" :
                print("You try to sneak behind the skeleton, but it suddenly stabs backwards and its blade buries itself in your face.\nGame Over")
            elif choicefive.lower() == "escape" :
                print("You bolt out through the door and keep running till you're back at the docks. You go home and never return.\nGame Over")
            elif choicefive.lower() == "fight" and choiceone.lower() != "weapon" :
                print("You attempt to fight off the skeleton, but it stabs you with a rusty cutlass in the heart.\nGame Over")
            else :
                print("You fight the skeleton and barely manage to defeat it. Heading to the chest, you open it and it's full of gold and treasure!\nGame Over you win!")
