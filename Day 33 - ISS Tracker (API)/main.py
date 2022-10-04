import requests
from datetime import datetime
import smtplib

#   Constants
MY_LAT = 1.352083 # Your latitude
MY_LONG = 103.819839 # Your longitude
GMAIL_USERNAME = "ernestlow32@gmail.com"
GMAIL_PASSWORD = "sfotzjbrgawfirqv"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(sunset)

time_now = datetime.now()
time = int(str(time_now).split()[1].split(":")[0])


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.\


#   5 Degrees of latitude / longitude, between dusk and dawn
if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5 and (time > sunset == True or time < sunrise == True):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = GMAIL_USERNAME, password = GMAIL_PASSWORD)
    connection.sendmail(from_addr = GMAIL_USERNAME, to_addrs = "ernestlow32@yahoo.com.sg", msg = f"Subject: ISS in Position!!\n\nLook up! The ISS is above you now!")



