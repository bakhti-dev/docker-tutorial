#!/bin/bash

# Start Celery Beat
celery -A a_core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler &

# Start Flower
celery -A a_core flower --basic_auth=admin:1212 --port=5555
