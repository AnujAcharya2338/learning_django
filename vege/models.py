from django.db import models

# Create your models here.

class Recepie(models.Model):
    recepe_name=models.CharField(max_length=100)
    recepe_description=models.TextField()
    recepe_image = models.ImageField(upload_to="recepies/")


