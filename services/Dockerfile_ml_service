FROM python:3.11-slim
# возьмем образ, который мы скачали ранее и в котором уже установлен python

LABEL author=${AUTHOR}
# добавим label, используя переменную среды

COPY . ./services
# копируем файлы в Docker

WORKDIR services
# изменяем рабочую директорию Docker 

RUN pip3 install -r requirements.txt
# инструкция для установки библиотек

EXPOSE ${APP_DOCKER_PORT}
# инструкции для открытия порта, указанного в переменной среды


VOLUME /models
# примонтируйте том с моделями

CMD uvicorn ml_service.real_estate_app:app --reload --port ${APP_DOCKER_PORT} --host 0.0.0.0
# измените команду запуска, учитывая порт из .env