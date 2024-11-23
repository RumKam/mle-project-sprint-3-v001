
"""Класс FastApiHandler, который обрабатывает запросы API."""
import pickle

class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # типы параметров запроса для проверки
        self.param_types = {
            "user_id": str,
            "model_params": dict
        }

        self.model_path = "../models/model_best.pkl"
        self.load_real_estate_model(model_path=self.model_path)
        
        # необходимые параметры для предсказаний модели оттока
        self.required_model_params = [
                'cat__building_type_int_4',
                'cat__building_type_int_6',
                'cat__building_type_int_1',
                'cat__cluster_region_2',
                'cat__cluster_region_1',
                'exp(sqrt(distance_to_center) - sqrt(longitude))',
                'num__rb__longitude',
                'num__rb__ceiling_height',
                'num__rb__floor',
                'cat__cluster_region_3',
                'cat__building_type_int_2',
                'num__pol__1',
                'num__pol__ceiling_height total_area',
                'cat__building_type_int_3',
                'num__kbd__total_area',
                'exp(-distance_to_center + sqrt(longitude))',
                'num__rb__build_year',
                'num__pol__ceiling_height',
                'num__pol__ceiling_height total_area^2',
                'num__kbd__ceiling_height',
                'num__pol__total_area^3',
                'num__rb__flats_count'
            ]

    def load_real_estate_model(self, model_path: str):

        try:
            with open(model_path, "rb") as f:
                 model = pickle.load(f)
                 
            self.model = model
            print(f"Model loaded. Success.: {e}")
        except Exception as e:
            print(f"Failed to load model: {e}")

    def real_estate_predict(self, model_params: dict) -> float:
        """Предсказываем цену недвижимости.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            int — цена на недвижимость
        """
        param_values_list = list(model_params.values())
        return self.model.predict(param_values_list)
        
    def check_required_query_params(self, query_params: dict) -> bool:
                """Проверяем параметры запроса на наличие обязательного набора.
                
                Args:
                    query_params (dict): Параметры запроса.
                
                Returns:
                        bool: True — если есть нужные параметры, False — иначе
                """
                if "user_id" not in query_params or "model_params" not in query_params:
                        return False
                
                if not isinstance(query_params["user_id"], self.param_types["user_id"]):
                        return False
                        
                if not isinstance(query_params["model_params"], self.param_types["model_params"]):
                        return False
                return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
            """Проверяем параметры пользователя на наличие обязательного набора.
        
            Args:
                model_params (dict): Параметры пользователя для предсказания.
        
            Returns:
                bool: True — если есть нужные параметры, False — иначе
            """
            if set(model_params.keys()) == set(self.required_model_params):
                return True
            return False
    
    def validate_params(self, params: dict) -> bool:
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
                
        if self.check_required_model_params(params["model_params"]):
            print("All model params exist")
        else:
            print("Not all model params exist")
            return False
        return True
        
    def handle(self, params):
            """Функция для обработки входящих запросов по API. Запрос состоит из параметров.
        
            Args:
                params (dict): Словарь параметров запроса.
        
            Returns:
                - **dict**: Словарь, содержащий результат выполнения запроса.
            """
            try:
                # валидируем запрос к API
                if not self.validate_params(params):
                    print("Error while handling request")
                    response = {"Error": "Problem with parameters"}
                else:
                    model_params = params["model_params"]
                    user_id = params["user_id"]
                    print(f"Predicting for user_id: {user_id} and model_params:\n{model_params}")
                    # получаем предсказания модели
                    y_pred = self.real_estate_predict(model_params)
                    response = {
                            "user_id": user_id, 
                            "prediction": y_pred
                        }
            except Exception as e:
                print(f"Error while handling request: {e}")
                return {"Error": "Problem with request"}
            else:
                return response
            
if __name__ == "__main__":

    # создаём тестовый запрос
    test_params = {
        "user_id": "1",
        "model_params": {
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
    }

    # создаём обработчик запросов для API
    handler = FastApiHandler()

    # делаем тестовый запрос
    response = handler.handle(test_params)
    print(f"Response: {response}")