'''
USAGE - The code is a Python program for tracking and logging workout sessions. 
        It imports the "os" and "requests" libraries, as well as the "datetime" module.
        The program retrieves the user's nutrition API key, app ID, and bearer token 
        from environment variables, and sets other parameters such as gender, weight, 
        height, and age. The user is prompted to input the exercise they did, 
        and the program sends a request to the Nutritionix API with the exercise 
        information and parameters. The response is then processed to extract 
        details such as exercise name, duration, and calories burned.
        The program then formats the workout information into a JSON object 
        and sends a request to a Sheety API endpoint to log the data into a 
        Google Sheet. Finally, the program prints the response from the Sheety API.

AUTHOR - https://github.com/Ahendrix9624/
'''

import os 
import requests
from datetime import datetime

API_KEY = os.environ.get("NUTRITION_API_KEY")
APP_ID =  os.environ.get("NUTRITION_ID")
BEARER_TOKEN = os.environ.get("NUTRITION_BEARER")
GENDER = "male"
WEIGHT_LBS = 165
HEIGHT_IN = 68
AGE = 26

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint =  "https://api.sheety.co/c3a4f36d8bee5471a51e31683ce499cd/workoutTracker/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_LBS,
    "height_cm": HEIGHT_IN,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
"Authorization": BEARER_TOKEN
}

sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)

print(sheet_response.text)