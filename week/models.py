from django.db import models

# Create your models here.
class Week(models.Model):
    day_of_week = models.CharField(max_length=20)
