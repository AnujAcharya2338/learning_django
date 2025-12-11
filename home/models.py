from django.db import models # type: ignore

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    

class Car (models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name