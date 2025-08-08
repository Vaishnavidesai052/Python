

# import requests
# from datetime import datetime

# GENDER = "female"
# WEIGHT_KG = 50
# HEIGHT_CM = 149
# AGE = 21

# APP_ID = "4e0af1c4"
# API_KEY = "64858045bf054aa9ce640ff42fbcaa2e"

# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint =  "https://api.sheety.co/0f2b567a17bef75011e5ac30d5326338/workoutTracking/workouts"

# exercise_text = input("Tell me which exercises you did: ")

# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }

# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()

# ################### Start of Step 4 Solution ######################

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#     print(sheet_response.text)

#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# #Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint, 
#   json=sheet_inputs, 
#   auth=(
#       "Vaishnavi052", 
#       "Kalavatiaai@1",
#   )
# )

import requests
from datetime import datetime

# Your personal info
GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 149
AGE = 21

# Nutritionix API credentials
APP_ID = "4e0af1c4"
API_KEY = "64858045bf054aa9ce640ff42fbcaa2e"

# Sheety API URL from your API tab
SHEET_ENDPOINT = "https://api.sheety.co/0f2b567a17bef75011e5ac30d5326338/workoutTracking/workouts"

# Ask user for exercises
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
result = response.json()

# Current date/time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Loop through exercises and send to Sheety
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

    # POST to Sheety with Basic Authentication
    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_inputs,
        auth=(
            "Vaishnavi052",  # <-- your Sheety username
            "Kalavatiaai@1"  # <-- your Sheety password
        )
    )

    print(sheet_response.text)
