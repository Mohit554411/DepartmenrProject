from django.db import models

# Create your models here.
class EnquiryDetail(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    mobile = models.CharField( max_length=12)
    subject = models.CharField( max_length=50)
    msg = models.TextField()