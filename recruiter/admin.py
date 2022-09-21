from django.contrib import admin
from recruiter.models import RecruiterDetails
# Register your models here.
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ("company_name","salary")
admin.site.register(RecruiterDetails,RecruiterAdmin)