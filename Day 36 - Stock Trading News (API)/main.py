import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "9Q0CQSSMUBHGT97I"
NEWS_API_KEY = "7e69ca97eb2142099c7316e4af4aa65f"


#   Making it 1 week ago due to json returning really old data
today = dt.datetime.utcnow().date()
one_day = today - dt.timedelta(days=7)
two_day = one_day - dt.timedelta(days=1)

#   Fix the value if it's lower than 10
def val_fix (val) :
    if val < 10 :
        return (f"0{val}")
    else :
        return val


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

data2 = data["Time Series (60min)"]

yesterday_date = f"{one_day.year}-{val_fix(one_day.month)}-{val_fix(one_day.day)} 05:00:00"
day_before_date = f"{two_day.year}-{val_fix(two_day.month)}-{val_fix(two_day.day)} 05:00:00"

yesterday = float(data2[yesterday_date]["4. close"])
day_before = float(data2[day_before_date]["4. close"])
print(yesterday)
print(day_before)

difference = round(((abs(yesterday - day_before) / day_before ) * 100 ), 2)
print(difference)
if difference > 5 :
    print("Get News")

#   Difference between 2 days: Data 0 / 16 / 32

with open ("./response.txt", "a") as file :
    file.write(str(data2))




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

