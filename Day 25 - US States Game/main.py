# Day 25 - US States Game (Guess the states, 5 lives)

import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width = 720, height = 480)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.ht()
writer.speed("fastest")

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
print(states)           # Cheat sheet of states
answers = []
wrong_guesses = 0

game_over = False

answer_state = screen.textinput(title = "Guess the State", prompt = "What's a state's name?").title()

while game_over == False :
    if answer_state in states and answer_state not in answers:
        x_cor = int(data.x[data["state"] == answer_state])
        y_cor = int(data.y[data["state"] == answer_state])
        writer.goto(x_cor, y_cor)
        writer.write(answer_state, align = "center")
        screen.update()
        answers.append(answer_state)
        if len(answers) == 50 :
            game_over = True
            print(f"Game Over, you win! You guessed incorrectly {wrong_guesses} times")
            screen.bye()
            break
        answer_state = screen.textinput(title = "Guess the State", prompt = "You got it!\nWhat's another state's name?").title()
    elif answer_state not in states :
        answer_state = screen.textinput(title = "Guess the State", prompt = f"State not found, you have {5 - wrong_guesses} lives left.\nWhat's another state's name?").title()
        wrong_guesses += 1
    elif answer_state in answers :
        answer_state = screen.textinput(title = "Guess the State", prompt = "State already filled in\nWhat's another state's name?").title()
    if wrong_guesses >= 5 :
        game_over = True
        print(f"Game over, you lose! You guessed {len(answers)} states. Check out the Learning.csv to learn what you missed.")
        screen.bye()

learning = [x for x in states if x not in answers]
# for state in states :
#     if state not in answers :
#         learning.append(state)
df = pandas.DataFrame(learning, columns=["Countries :"])
df.to_csv('Learning.csv')



# turtle.mainloop()
# screen.exitonclick()