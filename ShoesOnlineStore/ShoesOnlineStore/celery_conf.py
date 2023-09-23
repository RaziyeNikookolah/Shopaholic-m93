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

celery_app.conf.beat_schedule = {
    'export_orders_daily': {
        'task': 'orders.tasks.email_export',
        # This will run the task every day at midnight
        'schedule': crontab(minute=50, hour=11),
    },
}


celery_app.autodiscover_tasks()
