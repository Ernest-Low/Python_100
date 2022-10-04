#Day 19 - Turtle Racing

from turtle import Turtle, Screen, textinput
import random

screen = Screen()
screen.setup(width = 500, height = 400)

# Red, Green, Blue, Yellow, Purple, Orange, Grey

red = Turtle()
# red.color("red")
# red.name = ("red")
green = Turtle()
# green.color("green")
# green.name = ("green")
blue = Turtle()
# blue.color("blue")
# blue.name = ("blue")
black = Turtle()
# black.color("black")
# black.name = ("black")
purple = Turtle()
# purple.color("purple")
# purple.name = ("purple")
orange = Turtle()
# orange.color("orange")
# orange.name = ("orange")
grey = Turtle()
# grey.color("grey")
# grey.name = ("grey")

all_turtles = [red,green,blue,black,purple,orange,grey]
turtle_strings = ["red","green","blue","black","purple","orange","grey"]

y = 0
for idx, turt in enumerate(all_turtles) :
    turt.color(turtle_strings[idx])
    turt.name = (turtle_strings[idx])
    turt.penup()
    turt.shape("turtle")
    turt.goto(-220, -150 + y)
    y += 50


# for x in all_turtles :
#     x.penup()
#     x.shape("turtle")
#     x.goto(-220, -150 + y)
#     y += 50

bet = textinput("Race Bets!", "Who do you think will win?!\nRed/Green/Blue/Black/Purple/Orange/Grey").lower()
while bet not in turtle_strings :
    bet = textinput("Race Bets!", "Invalid Input!\nWho do you think will win?!\nRed/Green/Blue/Black/Purple/Orange/Grey").lower()


race = True
result = [""]
while race == True :
    random.shuffle(all_turtles)
    for x in all_turtles :
        posx = x.pos()
        posy = posx[1]
        posx = posx[0] + random.randint(2,7)
        x.goto(posx,posy)
        if x.pos()[0] > 220 :
            race = False
            result = x
            break

    # for x in all_turtles :
    #     if x.pos()[0] > 220 :
    #         race = False
    #         result = x
            
if bet == result.name :
    print(f"{(result.name).title()} Wins! You win!")
else :
    print(f"{(result.name).title()} Wins! You lose!")

# Potentially add a list (descending) of their positions?
# How about having all of them keep running, then add their name as they pass the goal?
# results = []
# for turt in all_turtles :
#     pass
                


# def move_forward() :
#     tim.forward(10)

# def move_backward() :
#     tim.back(10)

# def turn_right() :
#     heading = tim.heading() - 10
#     tim.setheading(heading)

# def turn_left() :
#     heading = tim.heading() + 10
#     tim.setheading(heading)

# def reset_screen() :
#     tim.reset()

# screen.listen()
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backward)
# screen.onkey(key = "a", fun = turn_left)
# screen.onkey(key = "d", fun = turn_right)
# screen.onkey(key = "c", fun = reset_screen)



screen.exitonclick()