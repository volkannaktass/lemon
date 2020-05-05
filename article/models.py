from django.db import models
from ckeditor.fields import RichTextField
from departments.models import Lessons,Semesters,Category,Departments,Years,CommonCourses
from django.contrib.auth.models import User
from user.models import UserProfile
# Create your models here.



class Article(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE,blank=True, null=True)
    departments = models.ForeignKey(Departments,on_delete = models.CASCADE,blank=True, null=True)
    years = models.ForeignKey(Years,on_delete = models.CASCADE,blank=True, null=True)
    semesters = models.ForeignKey(Semesters,on_delete = models.CASCADE,blank=True, null=True)
    commoncourses = models.ForeignKey(CommonCourses,on_delete= models.CASCADE,blank=True, null=True,verbose_name = "Common Courses")
    lessons = models.ForeignKey(Lessons,on_delete= models.CASCADE)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    about = models.CharField(max_length = 200,verbose_name = "What is the subject of the Article")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True, null=True, verbose_name="File Upload")
    
        
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']    

  #  def snipped_content(self):
   #     return snipped_content[:50]+"..."


    


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name= "comments",null=True)
    comment_author = models.CharField(max_length= 50,verbose_name="Name")
    comment_content = models.CharField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_author_image = models.ImageField(verbose_name="Profile Image")
    

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']    

