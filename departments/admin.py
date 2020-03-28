from django.contrib import admin
from .models import Category,Lessons,Departments,Years,Semesters,CommonCourses #,FacultyCommonCourses
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
    search_fields = ["title","departments","years","keywords"]
    list_filter = ["departments","years","status","create_at"]


# class FacultyCommonCoursesAdmin(admin.ModelAdmin):
#     list_display = ["title","keywords","faculty","create_at"]
#     list_display_links = ["title","create_at","faculty"]
#     search_fields = ["title","faculty","keywords"]
#     list_filter = ["faculty","create_at"]
    
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["title", "status"]



class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ["title","category","status"]


class CommonCoursesAdmin(admin.ModelAdmin):
    list_display = ["title","create_at"]
    list_display_links = ["title","create_at"]

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Lessons,LessonsAdmin)
admin.site.register(CommonCourses,CommonCoursesAdmin)
#admin.site.register(FacultyCommonCourses,FacultyCommonCoursesAdmin)
admin.site.register(Years,YearsAdmin)
admin.site.register(Semesters,SemestersAdmin)
