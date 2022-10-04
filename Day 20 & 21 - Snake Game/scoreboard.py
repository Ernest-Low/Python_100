from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
FONT2 = ("Courier", 24, "normal")


class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.ht()
        self.score = 0
        self.highest_score = 0
        self.penup()
        self.goto(0,280)
        self.pencolor("white")
        self.high_score()
        self.scoretracker()
        
    
    def scoretracker (self) :
        self.clear()
        self.goto(0,280)
        self.write(f"Score: {self.score}   High Score: {self.highest_score}", False, align = ALIGNMENT, font = FONT)
    
    def game_over (self) :
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align = ALIGNMENT, font = FONT2)
        self.high_score()

    def add_score (self) :
        self.score += 1
        self.scoretracker()
    
    def new_round(self) :
        self.score = 0

    def high_score (self) :
        with open ("high_score.txt", mode = "r+") as file :
            contents = int(file.read())
            if self.score > contents :
                file.write(str(self.score))
                self.highest_score = self.score
            else :
                self.highest_score = contents
