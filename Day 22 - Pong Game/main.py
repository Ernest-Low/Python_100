#Day 22 - Pong Game

from turtle import Screen
from paddle import Leftpaddle, Rightpaddle
from ball import Ball
import time
from scoreboard import Boundary, Scoreboard

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(False)

ball = Ball()
x_cool = 60

leftpaddle = Leftpaddle()
rightpaddle = Rightpaddle()
boundary = Boundary()
scoreboard = Scoreboard()

screen.onkey(leftpaddle.move_up, "w")
screen.onkey(leftpaddle.move_down, "s")
screen.onkey(rightpaddle.move_up, "Up")
screen.onkey(rightpaddle.move_down, "Down")

def reset() :
    ball.reset()
    leftpaddle.reset()
    rightpaddle.reset()
    screen.update()
    time.sleep(5)

game_over = False
while game_over == False :
    time.sleep(0.025)   # count 40 for 1s
    screen.update()
    ball.movement()
    if ball.ycor() >= 290 or ball.ycor() <= -290 :
        ball.ybounce()
    if x_cool < 60 :
        x_cool += 1
    if ball.xcor() >= 360 and abs(rightpaddle.ycor() - ball.ycor()) < 50 and x_cool == 60:
        ball.xbounce()
        ball.speedup()
        x_cool = 0
    if ball.xcor() <= -360 and abs(leftpaddle.ycor() - ball.ycor()) < 50 and x_cool == 60:
        ball.xbounce()
        ball.speedup()
        x_cool = 0
    if ball.xcor() >= 400 :
        scoreboard.left_scored()
        reset()
    if ball.xcor() <= -400 :
        scoreboard.right_scored()
        reset()


screen.exitonclick()
