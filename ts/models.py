from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=25, decimal_places=1)
