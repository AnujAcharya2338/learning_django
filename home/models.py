from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    

class product(models.Model):
    pass 
