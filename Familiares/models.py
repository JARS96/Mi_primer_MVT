from django.db import models

# Create your models here.

class Familiares(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    date=models.DateField()
    