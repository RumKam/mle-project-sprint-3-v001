import requests
import time
import json 

url = "http://localhost:4601/test_real_estate_app/"

for i in range(15):

    user_id = str(i)
    model_params = {
        "cat__building_type_int_4": 0.0,
        "cat__building_type_int_6": 1.0,
        "cat__building_type_int_1": 0.0,
        "cat__cluster_region_2": 0.0,
        "cat__cluster_region_1": 1.0,
        "exp(sqrt(distance_to_center) - sqrt(longitude))": 0.111202,
        "num__rb__longitude": 1.158362,
        "num__rb__ceiling_height": 0.0,
        "num__rb__floor": 0.166667,
        "cat__cluster_region_3": 0.0,
        "cat__building_type_int_2": 0.0,
        "num__pol__1": 1.0,
        "num__pol__ceiling_height total_area": 123.816009,
        "cat__building_type_int_3": 0.0,
        "num__kbd__total_area": 1.0,
        "exp(-distance_to_center + sqrt(longitude))": 0.000075,
        "num__rb__build_year": -0.181818,
        "num__pol__ceiling_height": 2.64,
        "num__pol__ceiling_height total_area^2": 5806.971009,
        "num__kbd__ceiling_height": 1.0,
        "num__pol__total_area^3": 103161.719069,
        "num__rb__flats_count": 0.338624
    }

    url = f"{url}?user_id={user_id}"

    try:
        response = requests.post(url, json=model_params)

        # Проверка успешности запроса
        if response.status_code == 200:
            prediction = response.json()
            print(f"User ID: {i}, Prediction: {prediction}")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")