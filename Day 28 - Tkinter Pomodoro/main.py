#   Day 28 - Tkinter Pomodoro

from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#   Timer control
global active
active = False
global pomo_stage
#   pomo_stage  0 = 0w, 1= 1w, 2 = 1w1b, 3 = 2w1b, 4 = 2w2b, 5 = 3w2b, 6 = 3w3b, 7 = 4w3b
pomo_stage = 0   
global ticks
ticks = []

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_pomo () :
    global active
    global pomo_stage
    global ticks
    active = False
    pomo_stage = 0
    ticks = []
    canvas.itemconfig(timer_text, text = "25:00")
    tick_label.config(text = "".join(ticks))
    title_label.config(text = "Work", font = (FONT_NAME, 50, "bold"))



# ---------------------------- TIMER MECHANISM ------------------------------- # 

#   pomo_stage   0 = 0w, 1= 1w, 2 = 1w1b, 3 = 2w1b, 4 = 2w2b, 5 = 3w2b, 6 = 3w3b, 7 = 4w3b
def start_timer () :
    global active
    global pomo_stage
    global ticks
    if active == False :
        if pomo_stage == 7 :
            active = True
            #   Debug
            print("Triggered 20min break")
            count_down(LONG_BREAK_MIN * 60)
            # count_down(5)          #placeholder
        elif pomo_stage == 0 or pomo_stage % 2 == 0 :
            active = True
            #   Debug
            print("Triggered 25min work")
            title_label.config(text = "Work!", font = (FONT_NAME, 50, "bold"))
            count_down(WORK_MIN * 60)
            # count_down(5)          #placeholder
        elif pomo_stage % 2 != 0 :
            active = True
            #   Debug
            print("Triggered 5min break")
            count_down(SHORT_BREAK_MIN * 60)
            # count_down(5)          #placeholder
    else :
        pass




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count) :
    global active
    global pomo_stage
    if count > 0 and active == True:
        minutes = math.floor(count / 60)
        seconds = count - (minutes * 60)
        if minutes < 10 :
            minutes = f"0{minutes}"
        if seconds < 10 :
            seconds = f"0{seconds}"
        # print(f"{minutes}:{seconds}")     #   Debug
        canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
        window.after(1000, count_down, count - 1)
    elif count == 0 :
        canvas.itemconfig(timer_text, text = "00:00")
        pomo_stage += 1
        if pomo_stage == 7 :
            ticks.append("✔")
            tick_label.config(text = "".join(ticks))
            canvas.itemconfig(timer_text, text = "20:00")
            title_label.config(text = "Break", font = (FONT_NAME, 50, "bold"))
        elif pomo_stage % 2 != 0 :
            ticks.append("✔")
            tick_label.config(text = "".join(ticks))
            canvas.itemconfig(timer_text, text = "05:00")
            title_label.config(text = "Break", font = (FONT_NAME, 50, "bold"))
        else :
            canvas.itemconfig(timer_text, text = "25:00")
            title_label.config(text = "Work!", font = (FONT_NAME, 50, "bold"))
        active = False
        if pomo_stage > 7 :
            reset_pomo()
            print("Full reset")
        print("Finished")
    else :
        print("Stopped")


# ---------------------------- UI SETUP ------------------------------- #

#   Window
window = Tk()
window.title("Pomodoro")
window.config(padx = 60, pady = 30, bg = YELLOW)

#   Canvas image (Tomato)
#   Tomato:       1,1
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(103, 135, text = "25:00", fill = "white", font = (FONT_NAME, 20, "bold"))
canvas.grid(column = 1, row = 1)


#   Timer label:  1,0
title_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 50, "bold"))
title_label.grid(column = 1, row = 0)

#   Start button: 0,2
start_button = Button(text = "Start", command = start_timer, font = (FONT_NAME, 12, "bold"))
start_button.config(padx = 2, pady = 2, bg = PINK)
start_button.grid(column = 0, row = 2)

# Reset:        2,2
reset_button = Button(text = "Reset", command = reset_pomo, font = (FONT_NAME, 12, "bold"))
reset_button.config(padx = 2, pady = 2, bg = PINK)
reset_button.grid(column = 2, row = 2)

# Ticks:        1,3
tick_label = Label(text = "".join(ticks), bg = YELLOW, fg = GREEN, font = (FONT_NAME, 12, "normal"))
tick_label.grid(column = 1, row = 3)


window.mainloop()