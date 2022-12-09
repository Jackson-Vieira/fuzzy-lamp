import os 
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fuzzy_lamp.settings")
app = Celery("fuzzy_lamp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()