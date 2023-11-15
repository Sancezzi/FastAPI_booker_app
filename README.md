# Booker - Бронирование отелей
Приложение на FastAPI с использованием SQLAlchemy, Celery, Redis, Docker, а также многими другими библиотеками и технологиями.

## Для корректной работы приложения заполните .env_docker.
```
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=
SMTP_USE_SSL=
```

## Запуск приложения
Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:  
```
uvicorn app.main:app --reload
```  

### Celery & Flower
Для запуска Celery используется команда  
```
celery --app=app.tasks.celery:celery worker -l INFO 
``` 
Для запуска Flower используется команда  
```
celery --app=app.tasks.celery:celery flower
``` 

### Docker compose
Для запуска всех сервисов (БД, Redis, веб-сервер (FastAPI), Celery, Flower, Grafana, Prometheus) необходимо использовать файл docker-compose.yml и команды
```
docker compose build
docker compose up
```
