alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

from art import logo

session = True
print(logo)
print("Caesar Coder Operational")
while session == True :
    type = ""
    while type != "encode" and type != "decode" :
        type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if type != "encode" and type != "decode" :
            print("Invalid input, try again")

    text = input("Type your message:\n")
    shift = str(input("Type the shift number:\n"))
    while shift.isdecimal() == False :
        print("Invalid Input")
        shift = str(input("Type the shift number:\n"))
    shift = int(shift)

    def caesar (text, shift, type) :
        if type == "encode" :
            keyword = "en"
        else :
            keyword = "de"
            shift *= -1
        print(f"Beginning {keyword}crypting {text} with a shift of {shift}")
        code = []
        text.replace(" ","")
        for x in text :
            if x.isdecimal() == True :
                codeshift = numbers.index(x) + (shift)
                while codeshift >= 10 :
                    codeshift -= 10
                while codeshift <= -1 :
                    codeshift += 10
                letter = numbers[codeshift]
                code += letter
            elif x.isalpha() == True :
                upper = False
                if x.isupper() == True :
                    x = x.lower()
                    upper = True
                codeshift = alphabet.index(x) + (shift)
                while codeshift >= 26 :
                    codeshift -= 26
                while codeshift <= -1 :
                    codeshift += 26
                letter = alphabet[codeshift]
                if upper == True :
                    code += letter.upper()
                else :
                    code += letter
            else :
                code += x
                continue
        fullcode = "".join(code)
        print(f"Your {keyword}crypted code is: {fullcode}")


    caesar(text,shift,type)
    sessioncheck = ""
    while sessioncheck != "y" and sessioncheck != "n" :
        sessioncheck = input("Go again? Y/N\n").lower()
        if sessioncheck == "n" :
            session = False
            print("Caesar Coder end.")
        elif sessioncheck != "y" :
            print("Invalid Input")
    