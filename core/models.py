from django.db import models

# Create your models here.
class ScannedQR(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    role = models.CharField(max_length=100)