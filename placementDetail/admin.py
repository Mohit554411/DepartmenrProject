from django.contrib import admin
from placementDetail.models import PlacementDetail
# Register your models here.
class PlacementAdmin(admin.ModelAdmin):
    list_display = ('usn','student_name','company','year')
admin.site.register(PlacementDetail,PlacementAdmin)