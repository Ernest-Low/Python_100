#Day 20 & 21 : Turtle-snake. Guided step-by-step in the course, but my ideas / previous iterations in the comments

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundary import Boundary

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(False)
# screen.delay(2000)  # Delay i think?


# snake1 = Turtle()
# snake2 = Turtle()
# snake3 = Turtle()

# snake_body = [snake1, snake2, snake3]
# start_position = [(-20,0), (0,0), (20,0)]
# segments = []
# positions = [(-20,0), (0,0), (20,0)]

# Only move the "tail" to the front (based on which direction the snake input is going)
# On new segment add, the latest segment is added to the 'tail', the turtle added to the list so that it's next to move
# if latest move is [3], add it at [4] so that it moves next, the rest in the list are pushed up a value!
# Also needs to save their positions so that food can be generated (multiple of 20 either direction) at locations while not being in the snake collision
# Also used to check lose conditions (next movement square is already occupied)



# for pos in start_position :
#         seg = Turtle("square")
#         seg.color("white")
#         seg.penup()
#         seg.goto(pos)
#         segments.append(seg)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
boundary = Boundary()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

def round_over () :
    scoreboard.game_over()
    screen.update()
    time.sleep(5)
    scoreboard.new_round()
    scoreboard.scoretracker()
    snake.delete()
    snake.create_snake()


while game_over == False :    
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15 :
        scoreboard.add_score()
        food.refresh()
        snake.extend()
        
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280 :
        round_over()
    
    for seg in snake.segments[1:] :
        # if seg == snake.head :
        #     pass
        if snake.head.distance(seg) < 10 :
            round_over()



    


        




screen.exitonclick()