from __future__ import absolute_import, unicode_literals

import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youbute.settings')
django.setup()

app = Celery('youbute')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))
