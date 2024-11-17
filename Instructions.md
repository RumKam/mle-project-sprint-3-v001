# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```python
# клонирование директории
git clone https://github.com/RumKam/mle-project-sprint-3-v001.git
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
```
uvicorn real_estate_app:app --reload --port 8081 --host 0.0.0.0
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:...' \
```
Для просмотра документации API и совершения тестовых запросов зайти на http://127.0.0.1:8081/docs

## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:...' \
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...