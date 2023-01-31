from django.contrib import admin
from django.urls import path,include
from . import views
#from django.conf.urls import url

app_name = "announcements"

urlpatterns = [
    path('announcements/',views.showAnnouncements,name = "announcements"),
    ]

