"""FastAPI-приложение для модели предсказания цены."""
import numpy as np
from fastapi import FastAPI, Body
# Если запускать приложение из контейнера, только с . импортируется обработчик
try:
    from fast_api_handler import FastApiHandler
except:
    from .fast_api_handler import FastApiHandler

from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
import time

# создаём FastAPI-приложение 
app = FastAPI()

# создаём обработчик запросов для API
app.handler = FastApiHandler()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# создаем гистограмму для предсказаний
app_predictions = Histogram(
    # имя метрики
    "app_predictions",
    #описание метрики
    "Histogram of predictions",
    #указаываем корзины для гистограммы
    buckets=(1e6, 3e6, 5e6, 7e6, 1e7, 3e7, 5e7, 7e8)
)

# создаем гистограмму для времени отклика
app_prediction_time = Histogram(
    "prediction_time_seconds",
    "Histogram of prediction time (seconds)",
    buckets=(0.1, 0.3, 0.5, 1, 3, 5)
)

app_predictions = Histogram(
    # имя метрики
    "app_predictions",
    #описание метрики
    "Histogram of predictions",
    #указазываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
)

@app.post("/test_real_estate_app/") 
def test_get_prediction_for_item(
    user_id: str,
    model_params: dict = Body(
        example={
          "cat__building_type_int_4": 1.0,
          "cat__building_type_int_6": 0.0,
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
          "num__pol__ceiling_height": 2.640000,
          "num__pol__ceiling_height total_area^2": 5806.971009,
          "num__kbd__ceiling_height": 1.0,
          "num__pol__total_area^3": 103161.719069,
          "num__rb__flats_count": 0.338624
        }
    )
):
    """Функция для получения вероятности оттока пользователя.

    Args:
        user_id (str): Идентификатор пользователя.
        model_params (dict): Параметры пользователя, которые мы должны подать в модель.

    Returns:
        dict: Предсказание цены недвижимости.
    """
    all_params = {
        "user_id": user_id,
        "model_params": model_params
    }

    start_time = time.time()  # Начало замера времени
    response = app.handler.handle(all_params)
    end_time = time.time()  # Конец замера времени

    # метрика
    app_predictions.observe(response['prediction'])

    # Время отклика
    response_time = end_time - start_time
    # метрика времени отклика
    app_prediction_time.observe(response_time)

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4601)