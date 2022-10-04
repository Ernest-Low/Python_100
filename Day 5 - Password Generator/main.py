#Day 5 Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

characters = nr_letters + nr_symbols + nr_numbers
password_output = []

for x in range(0, characters) :
    chartype = random.randint(1,3)
    valid = False
    while valid == False :
        if chartype == 1 and nr_numbers > 0 :
            # charrandom = random.randint(0,9)
            # password_output.append(numbers[charrandom])
            password_output.append(random.choice(numbers))
            valid = True
            nr_numbers -= 1
        elif chartype == 2 and nr_symbols > 0 :
            charrandom = random.randint(0,8)
            password_output.append(symbols[charrandom])
            valid = True
            nr_symbols -= 1
        elif chartype == 3 and nr_letters > 0 :
            charrandom = random.randint(0,51)
            password_output.append(letters[charrandom])
            valid = True
            nr_letters -= 1
        else :
            chartype = random.randint(1,3)

password_final = "".join(password_output)
print(f"Your new possible password could be: {password_final}")

