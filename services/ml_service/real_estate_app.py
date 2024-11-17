"""FastAPI-приложение для модели предсказания цены."""

from fastapi import FastAPI, Body
# Если запускать приложение из контейнера, только с . импортируется обработчик
try:
    from fast_api_handler import FastApiHandler
except:
    from .fast_api_handler import FastApiHandler

# создаём FastAPI-приложение 
app = FastAPI()

# создаём обработчик запросов для API
app.handler = FastApiHandler()

@app.post("/api/real_estate/") 
def get_prediction_for_item(user_id: str, model_params: dict):
    
    all_params = {
            "user_id": user_id,
            "model_params": model_params
        }
    
    return app.handler.handle(all_params)