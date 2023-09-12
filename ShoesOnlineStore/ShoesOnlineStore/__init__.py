# it will run celery when django runs
from .celery_conf import celery_app
__all__ = ("celery_app",)
