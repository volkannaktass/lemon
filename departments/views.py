from django.shortcuts import render#,redirect,get_object_or_404
from .models import Lessons
from article.models import Article
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib.auth import login,authenticate,logout
# Create your views here.

@login_required(login_url = "user:login")
def lessonsFOECEfirst(request):
    #Lessons.objects.filter(departments_id = "1",years_id = "1",semesters_id = "1"):
    lessonsfall = Lessons.objects.filter(years_id = "1",departments_id = request.user.userprofile.departments_id,semesters_id = "1")
    lessonsspring= Lessons.objects.filter(years_id = "1",departments_id = request.user.userprofile.departments_id,semesters_id = "2")
    #x = Article.objects.filter(category_id = "1",departments_id = "1",years_id = "1",semesters_id = "1",lessons_id = lessons_id)
    #articlesnames = Article.objects.filter(lessons_id = id)
    context = {
        "lessonsfall" : lessonsfall,
        "lessonsspring" : lessonsspring,
        #"articlesnames" : articlesnames,
    }
    return render(request,"lessons_first.html",context)

@login_required(login_url = "user:login")
def lessonsFOECEsecond(request):
    lessonsfall = Lessons.objects.filter(years_id = "2",departments_id = "1",semesters_id = "1") 
    lessonsspring = Lessons.objects.filter(years_id = "2",departments_id = "1",semesters_id = "2")    
    context = {
        "lessonsfall" : lessonsfall,
        "lessonsspring" : lessonsspring,
    }
    return render(request,"lessons_second.html",context)

@login_required(login_url = "user:login")
def lessonsFOECEthird(request):
    lessonsfall = Lessons.objects.filter(years_id = "3",departments_id = "1",semesters_id = "1") 
    lessonsspring = Lessons.objects.filter(years_id = "3",departments_id = "1",semesters_id = "2")    
    context = {
        "lessonsfall" : lessonsfall,
        "lessonsspring" : lessonsspring,
    }
    return render(request,"lessons_third.html",context)


@login_required(login_url = "user:login")
def lessonsFOECEfourth(request):
    lessonsfall = Lessons.objects.filter(years_id = "4",departments_id = "1",semesters_id = "1") 
    lessonsspring = Lessons.objects.filter(years_id = "4",departments_id = "1",semesters_id = "2")    
    context = {
        "lessonsfall" : lessonsfall,
        "lessonsspring" : lessonsspring,
    }
    return render(request,"lessons_fourth.html",context)



