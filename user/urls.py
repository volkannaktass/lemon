from django.contrib import admin
from django.urls import path,include
from . import views
#from django.conf.urls import url
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetView,PasswordResetCompleteView

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
    #path('profile/',views.profileUser,name = "profile"),
    path('profile/',views.profileUser,name = "profile"),
    path('password-change/',PasswordChangeView.as_view(),name= 'password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(),name='password_change_done'),

#    path('password_reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
 #    name='password_reset_done'),

 #   path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url='password_reset_confirm'), name='password_reset_confirm'),
  #  path('password_reset/', PasswordResetView.as_view(email_template_name='registration/password_reset_email.html'), name='password_reset'),
    
   # path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),     name='password_reset_complete'),
]



