from turtle import Turtle
import random

COLORS = ["red","green","blue","purple","orange","grey"]

class Obstacle (Turtle) :
    def __init__(self) :
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len = 3, stretch_wid = 1.5)
        self.direction = 1      #   1 goes left, -1 goes right, changes from main
        self.speed = 3
    
    def movement(self) :
        new_x = self.xcor() + ( self.speed * self.direction * -1)
        self.goto(new_x, self.ycor())\
    
