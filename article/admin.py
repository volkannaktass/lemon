from django.contrib import admin
from django.contrib.auth.models import User
from .models import Article,Comment
# Register your models here.

admin.site.register(Comment)

#admin.site.register(Article)

def copy(modeladmin, request, queryset):
    pass

copy.short_description = "Mark selected stories as published"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    actions = [copy]
    class Meta:
        model = Article


