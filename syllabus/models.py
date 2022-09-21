from django.db import models

# Create your models here.
class SyllabusDetails(models.Model):
    title = models.TextField()
    file = models.FileField(upload_to="syllabus/", max_length=250, default=True)