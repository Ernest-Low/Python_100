import random

class quiz_brain :
    def __init__(self, questions) :
        self.question_number = 0
        self.score = 0
        self.question_list = questions
        random.shuffle(self.question_list)
        print(f"Welcome to Quizbrain! We have a total of {len(self.question_list)} questions, so be prepared!\n")
        self.next_question()
        
    def question_check(self, user_answer) :
        answer = (self.question_list[self.question_number].answer).lower()
        # print(f"You answered: {user_answer.capitalize()}")
        if answer[0] == user_answer[0] :
            self.score += 1
            print("You got it right!")
        else :
            print("Wrong!")
        print(f"The correct answer was: {answer.capitalize()}")
        print(f"Your current score: {self.score} / {self.question_number}")
        return
        

    def still_has_questions(self) :
        if self.question_number < len(self.question_list) :
            print("\nNext Question!\n")
            self.next_question()
        else :
            print(f"All questions complete! Your final score: {self.score} / {self.question_number}")
    

    def next_question(self) :
        question = self.question_list[self.question_number].text
        user_answer = input(f"Q.{self.question_number + 1}: {question} True / False? : ").lower()
        while user_answer != "true" and user_answer != "false" and user_answer != "t" and user_answer != "f":
            print("Invalid Input")
            user_answer = input(f"Q.{self.question_number + 1}: {question} True / False? : ").lower()
        self.question_check(user_answer)
        self.question_number += 1
        self.still_has_questions()
        