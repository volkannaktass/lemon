from django.shortcuts import render#,redirect,get_object_or_404
from .models import Lessons
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import login,authenticate,logout
# Create your views here.

@login_required(login_url = "user:login")
def lessonsAll(request):
    if Lessons.objects.filter(years_id = "1",departments_id = "1"):
        lessons = Lessons.objects.filter(years_id = "1",departments_id = "1")
        context = {
        "lessons" : lessons
    }
        return render(request,"lessons_first.html",context)
    else:
        pass
