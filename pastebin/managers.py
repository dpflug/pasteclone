from django.db import models
from django.utils import timezone

class PasteManager(models.Manager):
    def remove_expired(self):
        """Removes expired posts...
        There are better ways to do this (Celery, for instance),
        but I'm not running a full site."""
        exp_time = timezone.now() - timezone.timedelta(30)
        self.filter(accessed__lt=exp_time).delete()
