from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.URLField(max_length=200)
    uuid = models.CharField(max_length=5)