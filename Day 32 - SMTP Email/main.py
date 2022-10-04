import smtplib
import datetime as dt
import random
import pandas

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

#   Constants
GMAIL_USERNAME = "ernestlow32@gmail.com"
GMAIL_PASSWORD = "sfotzjbrgawfirqv"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = GMAIL_USERNAME, password = GMAIL_PASSWORD)

now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict("records")
# print(data_dict)        #   Debug

# 2. Check if today matches a birthday in the birthdays.csv

for x in data_dict :
    if day == x["daily"] and month == x["month"] :
        randthree = random.randint(1,3)
        with open (f"./letter_templates/letter_{randthree}.txt") as file :
            letter = file.read()
        randthree = random.randint(1,3)
        with open (f"./letter_templates/letter_{randthree}.txt") as file :
            letter = file.read()
        finished_letter = letter.replace("[NAME]", x["name"])
        connection.sendmail(from_addr = GMAIL_USERNAME, to_addrs = x["email"], 
        msg = f"Subject: Happy Birthday {x['name']}!\n\n{finished_letter}")


#   Test code

# test_dict = {'name': 'Katherine', 'email': 'ernestlow32@yahoo.com.sg', 'year': 1959, 'month': 6, 'daily': 13}

# randthree = random.randint(1,3)
# with open (f"./letter_templates/letter_{randthree}.txt") as file :
#     letter = file.read()
# finished_letter = letter.replace("[NAME]", test_dict["name"])


# connection.sendmail(from_addr = GMAIL_USERNAME, to_addrs = test_dict["email"], 
# msg = f"Subject: Happy Birthday {test_dict['name']}!\n\n{finished_letter}")



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.


#   End connection
connection.close()
