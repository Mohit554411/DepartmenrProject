from django.contrib import admin
from activity.models import ActivityDetails
# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_title','activity_det','activity_img1','activity_img2','activity_img3','img1_title','img2_title','img3_title')

admin.site.register(ActivityDetails,ActivityAdmin)