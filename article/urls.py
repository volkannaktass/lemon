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
   path('',views.articles,name = "articles"),
   path('comment/<int:id>',views.addComment,name = "comment"),
   path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
   #path('deletecomment/<int:id>',views.deleteComment,name = "deletecomment"),
   path('articletable/<int:id>',views.showArticle,name = "articletable"),
   #path('comment/<int:id>/approve/', views.comment_approve, name='comment_approve'),
   #path('comment/<int:id>/remove/', views.comment_remove, name='comment_remove'),
]


