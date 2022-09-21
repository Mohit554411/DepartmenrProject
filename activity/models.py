from difflib import HtmlDiff
from email.policy import default
from tokenize import blank_re
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class ActivityDetails(models.Model):
    activity_title = models.TextField()
    activity_det = HTMLField()
    activity_img1 = models.ImageField( upload_to="activity/", max_length=250, default=True, null=True, blank=True)
    activity_img2 = models.ImageField( upload_to="activity/", max_length=250, default=True, null=True, blank=True)
    activity_img3 = models.ImageField( upload_to="activity/", max_length=250, default=True, null=True, blank=True)
    img1_title = models.TextField(default=True)
    img2_title = models.TextField(default=True)
    img3_title = models.TextField(default=True)
