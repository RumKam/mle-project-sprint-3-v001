# Инструкции по запуску микросервиса

## 1. FastAPI микросервис в виртуальном окружение
```python
# клонирование директории
git clone https://github.com/RumKam/mle-project-sprint-3-v001.git
# Переход в необходимую директорию
cd mle-project-sprint-3-v001/services
# обновление локального индекса пакетов
sudo apt-get update
# установка расширения для виртуального пространства
sudo apt-get install python3.10-venv
# создание виртуального пространства
python3.10 -m venv .venv_project_name 
# активация окружения
source .venv_project_name/bin/activate 
# установка пакетов
pip install -r requirements.txt

# команда перехода в директорию
cd mle-project-sprint-3-v001/services/ml_service

# команда запуска сервиса с помощью uvicorn
uvicorn real_estate_app:app --reload --port 4601 --host 0.0.0.0

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:4601/test_real_estate_app/?user_id=1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
```

Для просмотра документации API и совершения тестовых запросов зайти на http://0.0.0.0:4601/docs

## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию
cd mle-project-sprint-3-v001/services

# команда для запуска микросервиса в режиме без docker compose
docker image build . --tag test_real_estate_app -f Dockerfile_ml_service
docker container run --publish 4601:4601 --env-file .env --volume=./models:/models test_real_estate_app

# Проверить доступ
http://localhost:4601/docs

# проверка статуса контейнера
docker container ls -a | grep test_real_estate_app
# остановка контейнера
docker stop <ID контейнера>
# удаление контейнера
docker rm <ID контейнера>

# команда для запуска микросервиса в режиме docker compose
docker compose up  --build
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:4601/test_real_estate_app/?user_id=1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию
cd mle-project-sprint-3-v001/services
# команда для запуска микросервиса в режиме docker compose
docker compose up  --build
# команда остановки микросервиса
docker compose down
# перед повторным запуском микросервиса убедитесь в том, что микросервис остановлен
docker compose ls
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:4601/test_real_estate_app/?user_id=1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
```

## 4. Скрипт симуляции нагрузки

Скрипт генерирует 30 запросов с рандомным тайм-аутом от 0,01 до 1 секунды

```bash
# команды необходимые для запуска скрипта
python test_request.py
```

Адреса сервисов:
- микросервис: http://localhost:4601
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
