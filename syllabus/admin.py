from django.contrib import admin
from syllabus.models import SyllabusDetails
# Register your models here.
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('title','file')
admin.site.register(SyllabusDetails,SyllabusAdmin)