from django.contrib import admin
from django.urls import path
from . import views

app_name = "departments"
urlpatterns = [
   path('lessonsfirst/',views.lessonsFOECEfirst,name = "lessonsfirst"),
   path('lessonssecond/',views.lessonsFOECEsecond,name = "lessonssecond"),
   path('lessonsthird/',views.lessonsFOECEthird,name = "lessonsthird"),
   path('lessonsfourth/',views.lessonsFOECEfourth,name = "lessonsfourth"),
]
