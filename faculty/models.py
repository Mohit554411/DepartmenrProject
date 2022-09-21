from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class FacultyDetails (models.Model):
    name = models.CharField(max_length=30)
    qualification = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    faculty_img = models.FileField(upload_to="faculty/", max_length=250,null=True,default=True)
    faculty_details = HTMLField()