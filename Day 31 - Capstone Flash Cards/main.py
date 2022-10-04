#   Day 31 - Capstone Flash Cards (TKinter)


from tkinter import *
import pandas
import random
from tkinter import messagebox


#   Constants
BACKGROUND_COLOR = "#B1DDC6"

#   Convert csv to dict
data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict("records")
try :
    prev_known = pandas.read_csv("./data/known_words.csv")
    known = prev_known.to_dict("records")
    # print(known)        #   Debug
except :
    known = []
try :
    prev_unknown = pandas.read_csv("./data/unknown_words.csv")
    unknown = prev_unknown.to_dict("records")
except :
    unknown = []
# print(data_dict['French'][0])
# print(data_dict['English'][0])

#   Globals
rewind = False
current_card = {"Placeholder" : "Empty"}
finished = False


#   Update Known List
def known_list () :
    global known
    known_df = pandas.DataFrame(known)
    known_df.to_csv("./data/known_words.csv", index = False)

#   Countdown
def count_down (count) :
    if count > 0 and rewind == False:
        window.after(100, count_down, count - 1)
    elif count == 0 and rewind == False :
        reveal_card()
    elif rewind == True :
        pass

#   Function to show a new card (random, non repeated)
def random_card () :
    global rewind, current_card, finished
    rewind = False
    card_canv.itemconfig(front_back, image = card_img_front)
    current_card = random.choice(data_dict)
    while current_card in known and finished != True:
        current_card = random.choice(data_dict)
    # print(current_card)       #   Debug
    card_canv.itemconfig(card_title, text = "French", fill = "black", font = ("Arial", 40, "italic"))
    card_canv.itemconfig(card_word, text = current_card["French"], fill = "black", font = ("Arial", 60, "bold"))
    count_down(29)      #   Seconds * 10 - 1, 29 is 3s

#   Reveal card
def reveal_card () :
    global current_card
    card_canv.itemconfig(front_back, image = card_img_back)
    card_canv.itemconfig(card_title, text = "English", fill = "white", font = ("Arial", 40, "italic"))
    card_canv.itemconfig(card_word, text = current_card["English"], fill = "white", font = ("Arial", 60, "bold"))
    
    # card_canv.itemconfig(language_text, text = "English", fill = "white", font = ("Arial", 40, "italic"))
    # card_canv.itemconfig(word_text, text = data_dict['English'][rand], fill = "white", font = ("Arial", 60, "bold"))
    
#   Function to add card to known
def right_press () :
    global known, current_card, finished
    if len(known) == len(data_dict) and finished == False:
        finished = True
        messagebox.showinfo(title = "Finished!", message = "All flash cards checked!")
    if current_card != {"Placeholder" : "Empty"} and finished == False:
        known.append(current_card)
        remove_unknown()
    known_list()
    # print(current_card)     #Debug
    button_delay()

#   Function to remove card from learning list
def remove_unknown () :
    global current_card, finished, unknown
    if finished == False :
        try :
            res = [i for i in unknown if i["French"] != current_card["French"]]
        except :
            res = unknown
        unknown = res
    update_unknown()
    
#   Function to add card to learning list
def add_unknown () :
    global current_card, finished, unknown
    if finished == False and current_card != {"Placeholder" : "Empty"}:
        unknown.append(current_card)
    update_unknown()
    button_delay()

#   Function to update learning list
def update_unknown () :
    global unknown
    unknown_df = pandas.DataFrame(unknown)
    unknown_df.to_csv("./data/unknown_words.csv", index = False)


#   A 0.1s delay on the button to drop the previous count
def button_delay () :
    global rewind
    if rewind == False :
        rewind = True
        window.after(100, random_card)


#   Window
window = Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

#   Frame for card canvas
frame = Frame(window)
frame.grid(column = 0, row = 0, columnspan= 2)

#   Card Canvas Image
card_canv = Canvas(frame, width = 800, height = 526, highlightthickness= 0, bg = BACKGROUND_COLOR)
card_img_front = PhotoImage(file = "./images/card_front.png")
card_img_back = PhotoImage(file = "./images/card_back.png")
# card_canv.create_image(400, 263, image = card_img_back)
front_back = card_canv.create_image(400, 263, image = card_img_front)
card_canv.grid(column = 0, row = 0)


#   Frame is 800, 526
#   Language
#   Define canvas text and starting text
card_title = card_canv.create_text(400, 150, text = "Welcome", fill = "black", font = ("Arial", 30, "italic"))
card_word = card_canv.create_text(400, 263, text = "Press a button to start", fill = "black", font = ("Arial", 30, "bold"))

# language = "French"
# language_label = Label(frame, text = language, font = ("Arial", 40, "italic"), bg = "white")
# language_label.place(x = 400, y = 150, anchor = CENTER)

# #   Text
# text_show = "trouve"
# text_label = Label(frame, text = text_show, font = ("Arial", 60, "bold"), bg = "white")
# text_label.place(x = 400, y = 263, anchor = CENTER)


#   Right Button
right_img = PhotoImage(file = "./images/right.png")
right_button = Button(image = right_img, bg = BACKGROUND_COLOR, borderwidth = 0, command = right_press)
right_button.grid(column = 1, row = 1)

#   Wrong Button
wrong_img = PhotoImage(file = "./images/wrong.png")
wrong_button = Button(image = wrong_img, bg = BACKGROUND_COLOR, borderwidth = 0, command = add_unknown)
wrong_button.grid(column = 0, row = 1)

# random_card()

window.mainloop()