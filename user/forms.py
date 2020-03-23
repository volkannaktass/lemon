from django import forms
from django.contrib.auth.models import User #Group
from .models import UserProfile
from django.db import models
#from django.contrib.auth import authenticate
from departments.models import Category,Departments
from django.contrib.auth.forms import UserChangeForm

class LoginForm(forms.Form):
     username = forms.CharField(label = "Username")
     password = forms.CharField(label = "Password",widget = forms.PasswordInput)




class RegisterForm(forms.Form):
    #user1 = models.ForeignKey(UserProfile, related_name='alluser', on_delete=models.CASCADE)
    username = forms.CharField(max_length = 50,label = "Username")
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label = "Confirm Password",widget = forms.PasswordInput)
    email = forms.EmailField(widget=forms.TextInput(),label=("Email address:"))
   # category=models.ForeignKey(Category,on_delete=models.CASCADE)
    first_name = forms.CharField(max_length = 100,label = "Name")
    last_name = forms.CharField(max_length=100,label="Surname")
    #groups = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)
    #student_id = forms.CharField(max_length= 8,label="Student Id")
    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")
        #category = self.cleaned_data.get("category")
        #first_name = self.cleaned_data.get("first_name")
        #groups = self.cleaned_data.get("groups")
        #student_id = self.cleaned_data.get("student_id")
        
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("That user is already taken")
        long = len(User.objects.filter(email=email))
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords Do Not Match")
        elif long > 0:
            raise forms.ValidationError('This E-mail Has Already Been Used')
        
        values = {
            'first_name' : first_name,
            "last_name" : last_name,
            "username" : username,
            "password" : password,
            "email" : email,
            #"category" : category,
            #"first_name" : first_name,
            #"groups" : groups,
            #"student_id" : student_id
        }
        return values
# ---Same register from forms.ModelForm
#class RegisterForm(forms.ModelForm):

    #def __init__(self,*args,**kwargs):
     #   super(RegisterForm,self).__init__(*args,**kwargs)
      #  for field in self.fields:
       #     self.fields[field].widget.attrs= {'class':form-control}

#    class Meta:
#        model = User
#        fields = ['first_name','last_name','username','email','password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('faculty','departments','student_number')




class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            #'phone_number',
        )

class EditProfileForm2(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )
