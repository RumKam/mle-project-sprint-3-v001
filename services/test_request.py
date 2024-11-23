import requests
import time
import json 
import random

url_init = "http://localhost:4601/test_real_estate_app/"

for i in range(30):

    user_id = str(i)
    model_params = {
        "cat__building_type_int_4": 0.0,
        "cat__building_type_int_6": 1.0,
        "cat__building_type_int_1": 0.0,
        "cat__cluster_region_2": 0.0,
        "cat__cluster_region_1": 1.0,
        "exp(sqrt(distance_to_center) - sqrt(longitude))": random.uniform(0.1, 0.2),
        "num__rb__longitude": random.uniform(0.1, 0.2),
        "num__rb__ceiling_height": 0.0,
        "num__rb__floor": random.uniform(0.16, 0.17),
        "cat__cluster_region_3": 0.0,
        "cat__building_type_int_2": 0.0,
        "num__pol__1": 1.0,
        "num__pol__ceiling_height total_area": random.uniform(122.7, 124.9),
        "cat__building_type_int_3": 0.0,
        "num__kbd__total_area": 1.0,
        "exp(-distance_to_center + sqrt(longitude))": random.uniform(0.000074, 0.000076),
        "num__rb__build_year": random.uniform(-0.15, -0.19),
        "num__pol__ceiling_height": random.uniform(2.6, 3.2),
        "num__pol__ceiling_height total_area^2": random.uniform(5806.7, 5806.9),
        "num__kbd__ceiling_height": 1.0,
        "num__pol__total_area^3": random.uniform(103161.6, 103161.9),
        "num__rb__flats_count": random.uniform(0.33, 0.34)
    }

    url = f"{url_init}?user_id={user_id}"

    try:
        response = requests.post(url, json=model_params)
        # Сделаем паузы между запросами
        time.sleep(random.uniform(0.1, 5.0))

        # Проверка успешности запроса
        if response.status_code == 200:
            prediction = response.json()
            print(f"User ID: {i}, Prediction: {prediction}")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")