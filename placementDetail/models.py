from operator import mod
from django.db import models

# Create your models here.
class PlacementDetail(models.Model):
    usn = models.CharField( max_length=15)
    student_name = models.CharField(max_length=50)
    company = models.CharField( max_length=50)
    year = models.CharField(max_length=4)