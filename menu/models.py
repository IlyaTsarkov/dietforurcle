from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    calories = models.IntegerField()
    img = models.ImageField(upload_to='menu/images', blank=True)

