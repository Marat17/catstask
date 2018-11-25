from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    breed = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=10)