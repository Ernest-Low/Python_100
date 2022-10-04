from turtle import Turtle
START_POSITION = [(20,0), (0,0), (-20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :
    def __init__(self) :
        self.segments = []
        self.direction_change = True
        self.create_snake()
        

    def create_snake (self) :
        for pos in START_POSITION :
            self.add_segment(pos)
        self.head = self.segments[0]

    def add_segment (self, position) :
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)
    
    def delete (self) :
        for seg in self.segments :
            seg.goto(1000,1000)
            del(seg)
        self.segments.clear()

    def move(self) :
        for seg in range(len(self.segments) -1, 0, -1) :
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.direction_change = True
    
    def extend (self) :
        self.add_segment(self.segments[-1].pos())

    def up(self) :
        if self.head.heading() != DOWN and self.direction_change == True :
            self.head.setheading(UP)
            self.direction_change = False

    def right(self) :
        if self.head.heading() != LEFT and self.direction_change == True :
            self.head.setheading(RIGHT)
            self.direction_change = False
    
    def left(self) :
        if self.head.heading() != RIGHT and self.direction_change == True :
            self.head.setheading(LEFT)
            self.direction_change = False

    def down(self) :
        if self.head.heading() != UP and self.direction_change == True :
            self.head.setheading(DOWN)
            self.direction_change = False