from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.ht()
        self.penup()
        self.score = 0
        self.pencolor("white")
        self.left_score = 0
        self.right_score = 0
        self.scoretracker()
    
    def scoretracker (self) :
        self.goto(-40, 270)
        self.write(f"{self.left_score}", False, align = ALIGNMENT, font = FONT)
        self.goto(40, 270)
        self.write(f"{self.right_score}", False, align = ALIGNMENT, font = FONT)

    def left_scored (self) :
        self.left_score += 1
        self.clear()
        self.scoretracker()

    def right_scored (self) :
        self.right_score += 1
        self.clear()
        self.scoretracker()
        

class Boundary (Turtle) :
    def __init__(self) :
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.goto(0,300)
        self.pendown()
        self.setheading(270)
        for x in range (20) :
            self.forward(15)
            self.penup()
            self.forward(15)
            self.pendown()
        self.penup()