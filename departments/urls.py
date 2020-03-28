from django.contrib import admin
from django.urls import path
from . import views

app_name = "departments"
urlpatterns = [
   path('lessonsfirst/',views.lessonsFirst,name = "lessonsfirst"),
   path('lessonssecond/',views.lessonsSecond,name = "lessonssecond"),
   path('lessonsthird/',views.lessonsThird,name = "lessonsthird"),
   path('lessonsfourth/',views.lessonsFourth,name = "lessonsfourth"),
   path('facultycommoncourses/',views.facultyCommonCourses,name = "facultycommoncourses"),
   path('commoncourses/',views.commonCourses,name = "commoncourses"),
   path('commoncoursestable/<int:id>',views.showcommonCourses,name = "commoncoursestable"),
]
