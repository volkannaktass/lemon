from django.contrib import admin
from django.contrib.auth.models import User
from .models import Article,Comment,Images,ArticleDeleteRequest
# Register your models here.

#admin.site.register(Comment)

#admin.site.register(Article)

def copy(modeladmin, request, queryset):
    ghostuser = User.objects.get(username="ghostuser")
    queryset.update(author=ghostuser)

copy.short_description = "Copy article to ghostuser"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    actions = [copy]
    class Meta:
        model = Article



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article","comment_author","rate","comment_date"]
    readonly_fields = ["comment_author","rate","comment_content","article"]                
  

        

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["article","article_image"]


@admin.register(ArticleDeleteRequest)
class ArticleDeleteRequestAdmin(admin.ModelAdmin):
    list_display = ["article","request_author","email","using_status","created_date","update_date"]
