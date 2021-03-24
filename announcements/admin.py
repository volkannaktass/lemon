from django.contrib import admin
from django.contrib.auth.models import User
from .models import Announcements
# Register your models here.





@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    
    class Meta:
        model = Announcements
