import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday

with open ("quotes.txt") as file :
    quotes = file.readlines()

new_quotes = [x.strip("\n") for x in quotes]

GMAIL_USERNAME = "ernestlow32@gmail.com"
GMAIL_PASSWORD = "sfotzjbrgawfirqv"
DESTINATION = "ernestlow32@yahoo.com.sg"


quote_msg = random.choice(new_quotes)
print(quote_msg)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = GMAIL_USERNAME, password = GMAIL_PASSWORD)
connection.sendmail(from_addr = GMAIL_USERNAME, to_addrs = DESTINATION, 
msg = f"Subject: SMTP Test\n\n{quote_msg}")
connection.close()




#   4 = Friday
# if day == 4 :
