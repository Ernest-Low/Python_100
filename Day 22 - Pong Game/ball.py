from turtle import Turtle
import random
import time

class Ball (Turtle) :
    def __init__ (self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 6
        self.xdir = random.choice([1,-1])
        self.ymove = random.randint(2,6)
        self.ydir = random.choice([1,-1])

    def movement (self) :
        new_x = self.xcor() + self.xmove * self.xdir
        new_y = self.ycor() + self.ymove * self.ydir
        self.goto(new_x, new_y)
    
    def ybounce (self) :
        self.ydir = self.ydir * -1
        
    def xbounce (self) :
        self.xdir = self.xdir * -1

    def speedup (self) :
        self.xmove += 0.5
    
    def reset (self) :
        self.xmove = 5
        self.xdir = random.choice([1,-1])
        self.ymove = random.randint(2,6)
        self.ydir = random.choice([1,-1])
        self.goto(0,0)
