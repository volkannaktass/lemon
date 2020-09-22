from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from departments.models import (Category, CommonCourses, Departments, Lessons,
                                Semesters, Years)
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
    UP_TO_DATE = "Up-to-date"
    OUT_OF_DATE = "Out-of-date"
    CHOICES = (
        (UP_TO_DATE,"Up to date"),
        (OUT_OF_DATE,"Out of date")
    )
    using_status = models.CharField(max_length = 20,choices=CHOICES)
    #article_image = models.ImageField(blank=True, null=True, verbose_name="Article's Image Upload")
    #articleFile = models.FileField(blank=True, null=True,verbose_name="File Upload")
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']    

  #  def snipped_content(self):
   #     return snipped_content[:50]+"..."


    


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name= "comments",null=True)
    comment_author = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE,related_name='yorumlar')
    comment_content = models.CharField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['comment_date']    



#def get_image_filename(instance, filename):
 #   title = instance.id
  #  slug = slugify(title)
   # return "article_images/%s-%s" % (slug, filename)

        
class Images(models.Model):
    article  = models.ForeignKey(to=Article,on_delete = models.CASCADE,blank=True, null=True,related_name='resimler')
    article_image = models.FileField(blank=True, null=True, verbose_name="Article's Image Upload")


    def __str__(self):
        return self.article.title + "Image"



class ArticleDeleteRequest(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,blank=True, null=True)
    request_author = models.CharField(max_length = 50,verbose_name="Username")
    email = models.CharField(max_length = 50)
    request_content = RichTextField(verbose_name="Why Do You Want to Delete?")

    CHOICES = (
        (1,"New"),
        (2,"Read")
    )
    using_status = models.IntegerField(choices=CHOICES,default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = "Article Delete Request Message"
        verbose_name_plural = "Article Delete Request Messages"
