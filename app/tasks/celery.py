from celery import Celery

from app.config import settings

# celery -A app.tasks.celery:celery worker --loglevel=INFO
# celery -A app.tasks.celery:celery flower
celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=["app.tasks.tasks"]
)
