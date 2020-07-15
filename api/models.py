from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField()
    date_created = models.DateTimeField(auto_now=True)
    death_time = models.DateTimeField(null=True)