from django.contrib import admin
from .models import Category,Lessons,Departments,Years,Semesters
# Register your models here.


class SemestersAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]
class YearsAdmin(admin.ModelAdmin):
    list_display = ["title","create_at","status"]
    list_display_links = ["title","create_at"]
    search_fields = ["title"]
    list_filter = ["status","create_at"]


class LessonsAdmin(admin.ModelAdmin):

    list_display = ["title","keywords","departments","years","semesters","create_at","status"]
    list_display_links = ["title","create_at"]
    search_fields = ["title","departments","years"]
    list_filter = ["departments","years","status","create_at"]
    
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["title", "status"]



class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ["title","category","status"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Lessons,LessonsAdmin)
admin.site.register(Years,YearsAdmin)
admin.site.register(Semesters,SemestersAdmin)
