from django.contrib import admin
from event.models import EventDetails
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','imgs')
admin.site.register(EventDetails,EventAdmin)