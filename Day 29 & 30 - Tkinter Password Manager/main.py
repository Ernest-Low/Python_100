#   Day 29/30, TKinter Password Manager

from tkinter import *
import random
import string
from tkinter import messagebox
import pyperclip
import json

#   CONSTANT
OWN_EMAIL = "dummy@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password () :
    S = 24  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = S))    
    # print("The randomly generated string is : " + str(ran))
    password_entry.delete(0, 'end')
    password_entry.insert(0, str(ran))
    pyperclip.copy(str(ran))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password (event) :
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #   Json Formatting
    new_data = {
    website : {
        "email": email,
        "password": password 
            }
    }

    #   Debug
    print(f"{website} | {email} | {password}")

    if website == "" or email == "" or password == "" :
        messagebox.showinfo(title = "Missing Information", message = "You have missing fields!")
    else :
        is_ok = messagebox.askokcancel(title = website, message = f"You have entered:\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
        if is_ok :
            try :
                with open ("savedpasswords.json", 'r') as file :
                    # file.write(f"{website} | {email} | {password}\n")
                    file_data = json.load(file)
                    file_data.update(new_data)
                    # file.seek(0)
            except :
                file_data = new_data

            with open ("savedpasswords.json", 'w') as file :
                json.dump(file_data, file, indent = 4)

            pyperclip.copy(password)
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')



        else :
            pass
        
#   Search Function

def search_website () :
    try: 
        with open ("savedpasswords.json", 'r') as file :
            file_data = json.load(file)
    except :
        messagebox.showinfo(title = "Error", message = "No saved passwords!")
    else :
        website = website_entry.get()
        try :
            messagebox.showinfo(title = website, message = f"Email: {file_data[website]['email']}\nPassword: {file_data[website]['password']}\nYour password has been copied to clipboard!")
            pyperclip.copy(file_data[website]['password'])
        except :
            messagebox.showinfo(title = "Error", message = "Website not registered!")



# ---------------------------- UI SETUP ------------------------------- #

#   Window
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

#   Canvas Image (Lock) (1, 0)
canvas = Canvas(width = 200, height = 200, highlightthickness = 0 )
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column = 1, row = 0)

#   Website Label (0, 1)
website_label = Label(text = "Website: ", font = ("arial", 12, "normal"))
website_label.grid(column = 0, row = 1)
website_label.focus()

#   Website Entry (1, 1, column span 2) 35 width
website_entry = Entry(width = 26)
website_entry.grid(column = 1, row = 1)

#   Search Button (2, 1)
password_button = Button(text = "Search", font = ("Arial", 10, "normal"), command = search_website)
password_button.config(padx = 30)
password_button.grid(column = 2, row = 1)


#   Email/Usename Label (0, 2)
email_label = Label(text = "Email/Username: ", font = ("arial", 12, "normal"))
email_label.grid(column = 0, row = 2)

#   Email/Username Entry (1, 2, column span 2) 35 width
email_entry = Entry(width = 47)
email_entry.grid(column = 1, row = 2, columnspan = 2)
email_entry.insert(0, OWN_EMAIL)

#   Password Label (0, 3)
password_label = Label(text = "Password: ", font = ("arial", 12, "normal"))
password_label.grid(column = 0, row = 3)

#   Password Entry (1, 3) 21 width
password_entry = Entry(width = 26)
password_entry.grid(column = 1, row = 3)

#   Password Button (2, 3)
password_button = Button(text = "Generate Password", font = ("Arial", 10, "normal"), command = random_password)
# add_button.config(padx = 2, pady = 2)
password_button.grid(column = 2, row = 3)

#   Enter to save?
window.bind('<Return>', save_password)


#   Add Button (1, 4, column span 2) 36 width
add_button = Button(text = "Add", font = ("Arial", 10, "normal"), width = 36, command = lambda : save_password(0))
# add_button.config(padx = 2, pady = 1)
add_button.grid(column = 1, row = 4, columnspan = 2)



window.mainloop()