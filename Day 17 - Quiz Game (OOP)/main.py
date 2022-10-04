#Day 17 - Quiz Game (OOP) > Single Object for the entire quiz game (Functions stringed together in an object?)

from data import question_data
from questions_module import Question
from quiz_brain import quiz_brain
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

question_bank = []
for question in question_data :
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

cont = "y"
while cont == "y" :
    clearConsole()
    quiztime = quiz_brain(question_bank)
    cont = input("\nGo again? Y/N\n").lower()
    while cont != "y" and cont != "n" :
        print("Invalid Input")
        cont = input("Go again? Y/N\n").lower()
print("End")


# question = quiztime.question_list[quiztime.question_number].text
# response = quiztime.next_question()
# real_answer = (quiztime.question_list[quiztime.question_number].answer).lower()
# answer = input(f"{question} True / False? : ").lower()
# print(f"You answered {answer}, and the correct answer is {real_answer}")