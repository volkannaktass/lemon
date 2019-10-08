from django.db import models
from django.contrib.auth.models import User
#import uuid
#from django.db.models.signals import post_save
from departments.models import Category,Departments
#from django.dispatch import receiver
# Create your models here.



class UserProfile(models.Model):
    Male = 'Male'
    Female = 'Female'
    Other = "Other"
    Gender = ((Male,'Male'),(Female,"Female"),(Other,"Other"))
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    faculty = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE,blank=True, null=True)
    phone_number = models.CharField(max_length=11,verbose_name='Phone Number',blank=True)
    gender = models.CharField(max_length=1,default=3,verbose_name='Gender',choices=Gender,blank=True)
    student_number = models.CharField(max_length=8,verbose_name='Student Number',blank=True)    
    #student_id=models.CharField(max_length=8,  unique=True)

    #def __init__(self):
        #super(UserProfile,self).__init__()
        #self.student_id = str(uuid.uuid4())

    #def __unicode__(self):
        #return self.user
    #cat = models.ForeignKey("Category", on_delete=models.CASCADE,blank=True, null=True)
    #dep = models.ForeignKey("Departments", on_delete=models.CASCADE,blank=True, null=True)
    def get_full_name_or_username(self):
        if self.user.get_full_name():
            return self.user.get_full_name
        return self.user.username
    
    def __str__(self):
        #return self.user.username
        return self.get_full_name_or_username()

#def create_user_profile(instance,created,**kwargs):
 #  if created:
  #      UserProfile.objects.create(user=instance)
   # else:
	#    instance.user.save()
#post_save.connect(receiver=create_user_profile,sender=User)
