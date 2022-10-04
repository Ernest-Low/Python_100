#Day 10 Python Project - Python Calculator

import os
from art import logo

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def addition (n1, n2) :
    """Addition return n1 + n2"""
    return n1 + n2

def subtract (n1, n2) :
    """Subtrat return n1 - n2"""
    return n1 - n2

def multiply (n1, n2) :
    """Subtrat return n1 * n2"""
    return n1 * n2

def division (n1, n2) :
    """Subtrat return n1 / n2"""
    return n1 / n2

operations = {
    "+" : addition,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}


def calculator (answer) :
    print("Python Calculator initialized")
    if answer == 0 :
        num1 = input("What is the first number?\n")
        while num1.replace('.','',1).isdigit() == False :
            print("Invalid Input")
            num1 = input("What is the first number?\n")
        num1 = float(num1)
    else :
        num1 = answer
    for x in operations :
        print (x)
    operation = input("Select an operation from the above symbols.\n")
    while operation != "+" and operation != "-" and operation != "*" and operation != "/" :
        print("Invalid Input")
        operation = input("Select an operation from the above symbols.\n")
    num2 = input("What is the next number?\n")
    while num2.replace('.','',1).isdigit() == False :
        print("Invalid Input")
        num2 = input("What is the next number?\n")
    num2 = float(num2)
    answer = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    again(answer)

    
def again(answer) :
    cont = input("Continue with your current final number? Yes/No/Exit\n").lower()
    while cont[0] != "y" and cont[0] != "n" and cont[0] != "e":
        print("Invalid Input")
        cont = input("Go Again? Y/N\n").lower()
    if cont[0] == "y" :
        clearConsole()
        calculator(answer)
    elif cont[0] == "n" :
        clearConsole()
        answer = 0
        calculator(answer)
    else :
        print("Calculator End")

answer = 0
print (logo)
calculator(answer)

