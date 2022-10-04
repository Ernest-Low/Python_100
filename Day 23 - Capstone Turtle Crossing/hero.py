from turtle import Turtle

class Hero (Turtle) :
    def __init__(self) :
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset()

    def reset (self) :
        self.goto(0, -280)

    def move_up (self) :
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)
    
    def move_down (self) :
        if not self.ycor() <= -280 :
            new_y = self.ycor() - 15
            self.goto(self.xcor(), new_y)