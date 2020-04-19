from django.contrib import admin
from .models import UserProfile
# Register your models here.



# Add username and provide to see username on the admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user","image","faculty","departments","student_number","phone_number","gender"]
    list_display_links = ["user","image","faculty","departments","student_number"]
    search_fields = ["user","faculty","departments","student_number","phone_number","student_number"]
    list_filter = ["departments"]

admin.site.register(UserProfile,UserProfileAdmin)
