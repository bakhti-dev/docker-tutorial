import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

celery_app = Celery('a_core')

# Load settings from Django's settings
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks
celery_app.autodiscover_tasks()

# Set default concurrency
celery_app.conf.worker_concurrency = 4
