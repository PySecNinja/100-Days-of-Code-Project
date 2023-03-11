"""
USAGE - This code fetches weather data from OpenWeatherMap API for a location specified 
        by the latitude and longitude, and then checks if it will snow in the next 12 hours. 
        If it will snow, the code sends a text message via Twilio API to a specified phone number.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key_weather = "9afd1eb66741444d53f93555e9008535"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

parameters = {
    "lat": 46.38,
    "lon": -100.19,
    "appid": api_key_weather,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

data = response.json()
# Parses the next 12 hour forecast
weather_slice = data["hourly"][:12]

will_snow = False

for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    # print(weather_code)
    if weather_code >= 600 and weather_code <= 622:
        will_snow = True

if will_snow:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                    body="Call in sick. Its a powder day! ❄️🏂🗻",
                    from_='+18888233160',
                    to='+13155613980'
                )

    print(message.sid)
