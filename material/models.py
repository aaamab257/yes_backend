from pyexpat import model
from django.db import models

# Create your models here.


class Division(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField()
    file = models.FileField()
    dis = models.CharField(max_length=255)

    def __str__(self):
        return self.title 


""" class MaterialItem(models.Model):
    title = models.CharField(max_length=255 , unique=True) """
