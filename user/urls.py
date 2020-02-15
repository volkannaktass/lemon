from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('edit_profile/',views.edit_profile,name = "edit_profile"),
    path('change-password/',views.change_password,name = "change_password"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('deleteaccount/',views.deleteaccount,name = "deleteaccount"),
    path('deleteac/<int:id>',views.deleteac,name = "deleteac"),
    path('copyac/<int:id>',views.copyaccount,name = "copyac"),
    path('profile/',views.profileUser,name = "profile"),
    path('password-change/',PasswordChangeView.as_view(),name= 'password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(),name='password_change_done')
]