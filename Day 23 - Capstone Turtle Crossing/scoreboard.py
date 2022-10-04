from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"

class Scoreboard (Turtle) :
    def __init__ (self) :
        super().__init__()
        self.ht()
        self.penup()
        self.pencolor("black")
        self.score = 1
        self.level()
    
    def add_score (self) :
        self.score += 1
        self.level()

    def level (self) :
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.score}", False, align = ALIGNMENT , font = FONT)
    
    def game_over (self) :
        self.goto(0,0)
        self.write(f"GAME OVER", False, align = ALIGNMENT , font = ("Arial Black", 24, 'bold', "normal"))

    