"""DepartmentProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from DepartmentProject import views
from slugify import slugify
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('faculty/',views.faculty),
    path('events/',views.events),
    path('eventDetails/<title>',views.eventDetails),
    path('upcomingevents/',views.upcomingevents),
    path('activity/',views.activity),
    path('placements/',views.placements),
    path('ourRecruiter/',views.ourRecruiter),
    path('placementTraining/',views.placementTraining),
    path('placementAchievement/',views.placementAchievement),
    path('facility/',views.facility),
    path('contact/',views.contact),
    path('thankyou/',views.thankYou,name="thankyou"),
    path('footerDetails/<footer>',views.footerDetails)
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)