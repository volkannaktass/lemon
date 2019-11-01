from django.contrib import admin
from django.urls import path
from . import views

app_name = "departments"
urlpatterns = [
   path('lessons/',views.lessonsAll,name = "lessons"),
]
