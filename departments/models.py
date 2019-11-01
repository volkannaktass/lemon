from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
#from user.models import UserProfile
#from ../article.models.py import Article # articlleri baglamayi unutma..
# Create your models here.



class Category(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    parentid = models.IntegerField()
    title = models.CharField(max_length=150)
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE,blank=True, null=True)
    keywords= models.CharField(max_length=255, blank=True, null=True)
    description= models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(choices=STATUS)
    image = models.ImageField(upload_to='media/',blank=True, null=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Departments(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #parentid = models.IntegerField()
    title = models.CharField(max_length=150)
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE,blank=True, null=True)
    keywords= models.CharField(max_length=255, blank=True, null=True)
    description= models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(choices=STATUS)
    image = models.ImageField(upload_to='media/',blank=True, null=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Years(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=150)
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE,blank=True, null=True)
    keywords= models.CharField(max_length=255, blank=True, null=True)
    #description= models.CharField(max_length=255, blank=True, null=True)    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #file = models.FileField(upload_to='media/',blank=True, null=True)
    #content =RichTextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return self.title

class Semesters(models.Model):
    years = models.ForeignKey(Years,on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

class Lessons(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    #author = models.ForeignKey("UserProfile", on_delete=models.CASCADE,blank=True, null=True)
    #author = models.ForeignKey("auth.User",on_delete = models.CASCADE,blank=True, null=True)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE,blank=True, null=True)
    years = models.ForeignKey(Years, on_delete=models.CASCADE,blank=True, null=True)
    semesters = models.ForeignKey(Semesters,on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=150)
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE,blank=True, null=True)
    keywords= models.CharField(max_length=255, blank=True, null=True)
    #description= models.CharField(max_length=255, blank=True, null=True)    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #file = models.FileField(upload_to='media/',blank=True, null=True)
    #content =RichTextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS)
    
    def __str__(self):
        return self.title
