#Day 23 - Capstone Turtle Crossing - Done completely from scratch!!!

from turtle import Screen
import time
import random
from obstacle import Obstacle
from hero import Hero
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(False)
screen.listen()
hero = Hero()
scoreboard = Scoreboard()

screen.onkey(hero.move_up, "w")
screen.onkey(hero.move_down, "s")

game_over = False
spawn = random.randint(0, 5)
active_obstacles = []
global last_spawn
global last_spawns
last_spawn = 0          #   Lets ensure they dont spawn on the same last 6 y coordinates
last_spawns = [0,0,0,0,0,0]
global speed
speed = 3

def spawn_obstacle () :
    global last_spawn
    global last_spawns
    global speed
    ycor = random.randint(-12, 12) * 20
    while ycor in last_spawns :
        ycor = random.randint(-12, 12) * 20
    last_spawns[last_spawn] = ycor
    last_spawn += 1
    if last_spawn == 6 :
        last_spawn = 0
    xdir = random.choice([1,-1])
    xcor = 330 * xdir
    obstacle = Obstacle()
    obstacle.goto(xcor, ycor)
    obstacle.direction = xdir
    active_obstacles.append(obstacle)
    obstacle.speed = speed
     

#   Lets spawn obstacles from -260 - 260 (10 buffer space for turtle)
#   Spawn em every 0.8 - 1.3s at a difference of.. 20?
#   Half chance to spawn on other side  random.choice([1,-1])

#Random initial spawn (20 obstacles)
for x in range (20) :
    spawn_obstacle()
for obs in active_obstacles :
    xcor = random.randint(-14, 14) * 20
    obs.goto(xcor, obs.ycor())

while game_over == False :
    screen.update()
    time.sleep(0.1)
    spawn += 1
    if spawn >= 13 :
        spawn_obstacle()
        spawn = random.randint(0, 5)
        
    for obs in active_obstacles :
        obs.movement()
        if hero.distance(obs) < 30 :
            scoreboard.game_over()
            for obstructions in active_obstacles :
                if obstructions.ycor() < 60 and obstructions.ycor() > -60 :
                    # print("moved")
                    obstructions.goto(500, obstructions.ycor())
            screen.update()
            game_over = True
        elif abs(obs.ycor() - hero.ycor()) < 15 and hero.distance(obs) <= 38 :
            scoreboard.game_over()
            for obstructions in active_obstacles :
                if obstructions.ycor() < 60 and obstructions.ycor() > -60 :
                    # print("moved")
                    obstructions.goto(500, obstructions.ycor())
            screen.update()
            game_over = True
        if obs.xcor() > 330 or obs.xcor() < -330 :
            del(obs)

    if hero.ycor() >= 275 :
        hero.reset()
        scoreboard.add_score()
        speed += 0.8
        for obs in active_obstacles :
            obs.speed = speed





screen.exitonclick()