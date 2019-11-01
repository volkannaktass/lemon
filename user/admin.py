from django.contrib import admin
from .models import UserProfile
# Register your models here.



# Add username and provide to see username on the admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user","faculty","departments","student_number","phone_number","gender"]
    list_display_links = ["faculty","departments"]
    search_fields = ["faculty","departments","student_number","phone_number"]
    list_filter = ["departments"]

admin.site.register(UserProfile,UserProfileAdmin)