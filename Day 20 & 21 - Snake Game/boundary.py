from turtle import Turtle

class Boundary(Turtle) :
    def __init__(self) :
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.ht()
        self.goto(-280, 280)
        self.pendown()
        self.goto(280,280)
        self.goto(280,-280)
        self.goto(-280,-280)
        self.goto(-280,280)
