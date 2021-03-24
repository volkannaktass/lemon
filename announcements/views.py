from django.shortcuts import render
from .models import Announcements
# Create your views here.


def showAnnouncements(request):
    announcements = Announcements.objects.all()
    context = {
        "announcements" : announcements,
    }

    return render(request,"announcements.html",context) 
