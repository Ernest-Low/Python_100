#    Day 35 - Rain Alert / SMS
#   Major problem - Subscirption required for the API :(
#   Won't work, will just write the code but it won't work.

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

account_sid = "AC9661780165769144e08284290ef28f7c"
auth_token = "2eac4c8367ab654f9af480e9cc597ae1"
proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
client = Client(account_sid, auth_token, http_client=proxy_client)

#   env - Environment Variables
#   Call in a running envrionment
#   export (variable name) = (variable value) - Create an environment variable
#   Then access env variable by os.environ.get("(variable name)")   -   Requires OS module

#   When triggering the call, go something like
#   export (env name) = (env val); export (env name) = (env val); python3 main.py

parameters = {
    "lat" : 1.352083,
    "lon" : 103.819839,
    "appid" : "6eac554f0fb2d8a386446c907ea1870f",
}

#   https://api.openweathermap.org/data/3.0/onecall?lat=1.352083&lon=103.819839&appid=6eac554f0fb2d8a386446c907ea1870f
#   https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params = parameters)
response.raise_for_status()
data = response.json()
print(data)

weather_data = data["hourly"][:12]
for hour_data in weather_data : 
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain = True

if will_rain == True :
    print("Bring an umbrella")

# for x in range(len(data["hourly"])) :
#     if data["hourly"][x]["weather"][0]["id"] < 700 :
#         print("Bring an umbrella")

#   Sends a sms!
# message = client.messages \
#                 .create(
#                      body="The rain is coming, bring an umbrella",
#                      from_='+19785707483',
#                      to='+6597344396'
#                  )
# print(message.status)


with open ("./response.txt", "a") as file :
    file.write(str(data))