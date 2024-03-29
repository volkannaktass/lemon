from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"
urlpatterns = [
   # path('create/',views.index,name = "index"),
   path('dashboard/',views.dashboard,name = "dashboard"),
   path('addarticle/',views.addArticle,name = "addarticle"),
   path('article/<int:id>',views.detail,name = "detail"),
   path('update/<int:id>',views.updateArticle,name = "update"),
   path('delete/<int:id>',views.deleteArticle,name = "delete"),
   path('delete-image/<int:id>',views.deleteImage,name = "deleteimage"),
   path('delete-file/<int:id>',views.deleteFile,name = "deletefile"),
   path('',views.articles,name = "articles"),
   path('comment/<int:id>',views.addComment,name = "comment"),
   path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
   #path('deletecomment/<int:id>',views.deleteComment,name = "deletecomment"),
   path('articletable/<int:id>',views.showArticle,name = "articletable"),
   path('test/',views.upload_pdf,name = "test"),

   #path('comment/<int:id>/approve/', views.comment_approve, name='comment_approve'),
   #path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
   path('deleterequest/<int:id>',views.deleteRequest,name = "deleterequest"),
   #path('user-upload-photo/',views.userUploadPhoto,name = "user-upload-photo"),
   #path('basic-upload/', views.BasicUploadView.as_view(), name='basic-upload'),
   #path('deletepost/',views.deletePost,name = "deletepost"),
   #path('copypost/<int:id>',views.copyPost,name = "copypost"),
   #path('basic-upload',views.BasicUploadView.as_view(),name = "basic_upload"),
]
