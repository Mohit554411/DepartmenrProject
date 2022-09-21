from django.db import models

# Create your models here.
class RecruiterDetails(models.Model):
    company_name = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)