from django.conf import settings
from celery.schedules import crontab
from celery import Celery
from datetime import timedelta
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShoesOnlineStore.settings')

celery_app = Celery('ShoesOnlineStore')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'redis://localhost:6379'
celery_app.conf.result_backend = 'redis://localhost:6379'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
celery_app.conf.result_expires = timedelta(days=1)
# block client until task completed or not
celery_app.conf.task_always_eager = False
# how many task each worker do
celery_app.conf.worker_prefetch_multiplier = 4
celery_app.conf.enable_utc = False

celery_app.conf.update(timezone='Asia/Tehran')
celery_app.config_from_object(settings, namespace='CELERY')
# Celery Beat Settings
celery_app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year=6),
        # 'args': (2,)
    }
}
# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
