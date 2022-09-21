from django.contrib import admin
from faculty.models import FacultyDetails
# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display=('name','qualification','designation','faculty_img','faculty_details')
admin.site.register(FacultyDetails,FacultyAdmin)