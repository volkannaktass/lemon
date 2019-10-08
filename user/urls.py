from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('deleteaccount/',views.deleteaccount,name = "deleteaccount"),
    path('deleteac/<int:id>',views.deleteac,name = "deleteac"),
    path('copyac/<int:id>',views.copyaccount,name = "copyac"),
    path('profile/',views.profileUser,name = "profile"),
]