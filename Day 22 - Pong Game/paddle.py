from turtle import Turtle
import time

STARTING_POS1 = (-380, 0)
STARTING_POS2 = (380, 0)

class Paddle (Turtle) :
    def __init__(self) :
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.startpos = ()
    
    def reset (self) :
        self.goto(self.startpos)

    def move_up(self) :
        if self.ycor() < 240 :
            ypos = self.ycor() + 20
            self.setpos(self.xcor(), ypos)
    
    def move_down(self) :
        if self.ycor() > -240 :
            ypos = self.ycor() - 20
            self.setpos(self.xcor(), ypos)
    

    
class Rightpaddle (Paddle) :
    def __init__(self):
        super().__init__()
        self.startpos = STARTING_POS2
        self.goto(self.startpos)
        self.game_active = True
        # self.shapesize(stretch_wid = 1, stretch_len = 5)
        # self.movement()

    # def movement (self) :
    #     while self.game_active == True :
    #         while self.ycor() < 250 :
    #             self.setheading(90)
    #             self.forward(10)
    #             # self.setpos(self.xcor, self.ycor() + 5)
    #         while self.ycor() > -250 :
    #             self.setheading(270)
    #             self.forward(10)
    #             # self.setpos(self.xcor, self.ycor() - 5)

    


class Leftpaddle (Paddle) :
    def __init__(self):
        super().__init__()
        self.startpos = STARTING_POS1
        self.goto(self.startpos)
    
    # def move_up(self) :
    #     if self.ycor() < 240 and self.active == True:
    #         ypos = self.ycor() + 20
    #         self.setpos(self.xcor(), ypos)
    
    # def move_down(self) :
    #     if self.ycor() > -240 and self.active == True:
    #         ypos = self.ycor() - 20
    #         self.setpos(self.xcor(), ypos)