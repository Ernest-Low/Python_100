from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface :
    def __init__ (self, quiz_brain : QuizBrain) :
        self.quiz = quiz_brain
        #   Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.answered = False

        #   Score (1, 0)
        # self.score_text = 0
        # self.score_label = Label(text = f"Score: {self.score_text}", bg = THEME_COLOR, fill = "white", font = ("Arial", 12, "normal"))
        self.score_label = Label(text = "Score: 0", bg = THEME_COLOR, fg = "white", font = ("Arial", 12, "normal"))
        self.score_label.grid(column = 1, row = 0)
        
        # #   Frame for textbox
        # self.frame = Frame(self.window, width = 300, height = 250)
        # self.frame.grid(column = 0, row = 1, columnspan = 2)

        #   Textbox (0, 1, columnspan 2)
        # self.display_text = "Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World"
        # self.display_label = Label(text = self.display_text, bg = "white", fill = THEME_COLOR, font = ("Arial", 20, "italic"))
        # self.display_label = Label(text = self.display_text, width = 30, height = 25)
        # self.display_label.config(padx = 20, pady = 20)
        # self.display_label.grid(column = 0, row = 1, columnspan = 2)
        self.display_canv = Canvas(width = 300, height = 250, highlightthickness = 0, bg = "white")
        self.canv_text = self.display_canv.create_text(150, 125, text = "Placeholder", fill = THEME_COLOR, font = ("Arial", 16, "italic"), width = 280)
        self.display_canv.grid(column = 0, row = 1, columnspan = 2, pady = 20)
        # self.message_text = Label(self.frame, text = self.display_text, bg = "white", fg = THEME_COLOR, font = ("Arial", 20, "italic"), wraplength = 260, height = 8, width = 30)
        # self.message_text.config(padx = 20, pady = 20)
        # self.message_text.grid(column = 0, row = 0)

        #   Tick Button (0, 2)
        tick_image = PhotoImage(file = "./images/true.png")
        self.tick_button = Button(image = tick_image, bg = THEME_COLOR, borderwidth = 0, command = self.return_true, state = "active")
        self.tick_button.grid(column = 0, row = 2)
        
        #   Cross Button (1, 2)
        cross_image = PhotoImage(file = "./images/false.png")
        self.cross_button = Button(image = cross_image, bg = THEME_COLOR, borderwidth = 0, command = self.return_false, state = "active")
        self.cross_button.grid(column = 1, row = 2)

        self.next_question()

        #   Window Mainloop
        self.window.mainloop()


    def next_question (self) :
        print("change text")
        q_text = self.quiz.next_question()
        self.display_canv.itemconfig(self.canv_text, text = q_text)

    def return_true (self) :
        self.tick_button.config(state = "disabled")
        self.cross_button.config(state = "disabled")
        self.answered = True
        self.answer_check(self.quiz.check_answer("true"))
        self.window.after(3000, self.to_next_question)

    def return_false (self) :
        self.tick_button.config(state = "disabled")
        self.cross_button.config(state = "disabled")
        self.answered = True
        self.answer_check(self.quiz.check_answer("false"))
        self.window.after(3000, self.to_next_question)

    def to_next_question (self) :
        # print("got here")
        self.display_canv.config(bg = "white")
        self.score_label.config(text = f"Score: {self.quiz.score}")
        if self.quiz.question_number < len(self.quiz.question_list) :
            # print("ran this")
            self.tick_button.config(state = "active")
            self.cross_button.config(state = "active")
            self.answered = False
            self.next_question()
        else :
            self.display_canv.itemconfig(self.canv_text, text = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.window.after(5000, self.window.destroy)
    
    def answer_check (self, check) :
        if check == True : 
            self.display_canv.config(bg = "green")
        else :
            self.display_canv.config(bg = "red")