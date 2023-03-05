import requests
import datetime as dt


"""
Georgetown, CO
"""
MY_LAT = 39.7061
MY_LONG = -105.6975


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
print(sunrise.split(":")[0])

sunset = data["results"]["sunset"]
print(sunset.split(":")[0])

time_now = dt.datetime.now()
formatted_time = time_now.strftime("%I:%M:%S %p")
print(formatted_time.split(":")[0])