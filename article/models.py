from django.db import models
from ckeditor.fields import RichTextField
from departments.models import Lessons
from django.contrib.auth.models import User
# Create your models here.



class Article(models.Model):
    lessons = models.ForeignKey(Lessons,on_delete= models.CASCADE)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True, null=True, verbose_name="File Upload")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name= "comments",null=True)
    comment_author = models.CharField(max_length= 50,verbose_name="Name")
    comment_content = models.CharField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']    

