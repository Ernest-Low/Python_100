#Day 18 - Hirst painting mockup

from turtle import Turtle, Screen, colormode, screensize
import random
import colorgram

tim = Turtle()
# tim.shape("turtle")

tim.pensize(1)
# tracer(False)
tim.speed("fastest")
tim.penup()
colormode(255)
screensize(500,500)
tim.hideturtle()


colornumber = 10
colorlist = []
colors = colorgram.extract('image.jpg', colornumber)
for i in range(0,colornumber - 1) :
    color = colors[i].rgb
    # print(color)
    colorlist.append((color.r,color.g,color.b))
# print(colorlist)

for y in range (1, 11) :
    tim.setpos(-230,-280 + y*50)
    tim.dot(30, random.choice(colorlist))
    for x in range (9) :
        tim.forward(50)
        tim.dot(30, random.choice(colorlist))
    




# for i in range (200):
    # colormode(255)
    # tim.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # tim.setheading(90*random.randint(0,3))
    # # update()
    # tim.forward(20)
    # # update()

# x = 72
# y = 360 / x
# z = 0
# for i in range (x + 1) :
#     colormode(255)
#     tim.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     tim.circle(100)
#     # update()
#     tim.setheading(z)
#     z += y
#     # update()


screen = Screen()
screen.exitonclick()













