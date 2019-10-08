from django.contrib import admin
from .models import Category,Lessons,Departments,Years
# Register your models here.
class YearsAdmin(admin.ModelAdmin):
    list_display = ["title","departments","create_at","status"]
    list_display_links = ["title","create_at"]
    search_fields = ["title","departments"]
    list_filter = ["departments","status","create_at"]


class LessonsAdmin(admin.ModelAdmin):

    list_display = ["title","departments","years","create_at","status"]
    list_display_links = ["title","create_at"]
    search_fields = ["title","departments","years"]
    list_filter = ["departments","years","status","create_at"]
    
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["title", "status"]



class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Lessons,LessonsAdmin)
admin.site.register(Years,YearsAdmin)
