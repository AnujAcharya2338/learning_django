from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()

class product(models.Model):
    pass 
