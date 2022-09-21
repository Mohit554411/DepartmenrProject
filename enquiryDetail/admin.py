from django.contrib import admin
from enquiryDetail.models import EnquiryDetail
# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','subject','msg')

admin.site.register(EnquiryDetail,EnquiryAdmin)