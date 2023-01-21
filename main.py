import requests
from datetime import datetime
import os

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = "male"
WEIGHT = "97"
HEIGHT = "186"
AGE = "27"

user_choice = input("What exercises you did? ")

EXERCISES_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercises_params = {
    "query": user_choice,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=EXERCISES_ENDPOINT, json=exercises_params, headers=headers)
response.raise_for_status()
data = response.json()
activity = (data["exercises"][0]["user_input"]).title()
duration = round(data["exercises"][0]["duration_min"], 1)
calories_burned = round(data["exercises"][0]["nf_calories"], 0)

time_now = datetime.now()
formated_data = time_now.strftime("%d/%m/%Y")
formated_hour = time_now.strftime("%H:%M:%S")
sheety_endpoint = "https://api.sheety.co/cd675e558ad384f88c547d84d166fe71/myWorkoutsDaniel/workouts"
sheety_params = {
    "workout": {
        "date": formated_data,
        "time": formated_hour,
        "exercise": activity,
        "duration": duration,
        "calories": calories_burned
    }
}
headers_sheety = {
    "Authorization": "Bearer Daniel"
}

response_sheety = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers_sheety)
response_sheety.raise_for_status()
