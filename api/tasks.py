from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time
from .models import File

@shared_task
def delete_file(**kwargs):
    """Deleting time when after sleed delay"""
    time.sleep(kwargs['time'])
    file = File.objects.get(pk=kwargs['file']['id'])
    file.delete()