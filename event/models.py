from turtle import title
from django.db import models

# Create your models here.


class EventDetails(models.Model):
    title = models.CharField(max_length=50,)
    imgs = models.FileField(
        upload_to="event/", max_length=250, default=True, null=True, blank=True)

