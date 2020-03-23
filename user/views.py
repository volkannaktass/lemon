from django.shortcuts import render,redirect,get_object_or_404
from .forms import (
    RegisterForm,
    LoginForm,
    UserProfileForm,
    EditProfileForm,
    EditProfileForm2
)
#from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User #Group
from django.contrib.auth import login,authenticate,logout
from .models import UserProfile
from article.models import Article
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.

"""Default Register"""

def register(request):

    form = RegisterForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    if form.is_valid() and profile_form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        #category = form.cleaned_data.get("category")
        #departments = form.cleaned_data.get("departments")
        #first_name = form.cleaned_data.get("first_name")
        #groups = form.cleaned_data.get("groups")
        #student_id = form.cleaned_data.get("student_id")
        newUser = User(first_name=first_name,last_name=last_name,username = username,email = email)
        newUser.set_password(password)
        user = newUser.save()
        print(user)
        profile = profile_form.save(commit=False)
        faculty = profile_form.cleaned_data.get('faculty')
        departments = profile_form.cleaned_data.get('departments')
        student_number = profile_form.cleaned_data.get('student_number')
        userprofile = UserProfile.objects.get(user = user)
        userprofile.faculty = faculty
        userprofile.departments = departments
        userprofile.student_number = student_number
        userprofile.save()
        #profile.user = user
        #profile.save()
        login(request,newUser)
        messages.info(request,"Registration Successful...")

        return redirect("index")
    context = {
            "form" : form,
            "profile_form" : profile_form,
        }
    return render(request,"register.html",context)
"""END"""

"""    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)

            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"register.html",context)
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request,"register.html",context)"""

"""DEFAULT LOGIN AND LOGOUT"""

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Username or Password is Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Login Successful")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Logout Successful")
    return redirect("index")
"""END"""

@login_required(login_url = "user:login")
def profileUser(request):
    return render(request,"profile.html")





def deleteaccount(request):
    user = get_user_model()
    users = user.objects.all()
    context = {
        "users":users
    }
    if request.user.is_superuser:
        return render(request,"delete-account.html",context)
    else:
        raise Http404



def deleteac(request,id):
    user = get_object_or_404(User,id = id)

    user.delete()

    return redirect("user:deleteaccount")


def copyaccount(request,id):
    usercp = get_object_or_404(User,id = id)
    ghostuser = User.objects.get(username="ghostuser")
    Article.objects.filter(author=usercp).update(author=ghostuser)
    usercp.delete()
    #Article.objects.filter(author_id=author_id).update(author_id=ghost_user.id)

    return redirect("user:deleteaccount")


#def user_edit_profile(request):
 #   data = {'genders':request.user.userprofile.genders,'student_numbers':request.user.userprofile.student_numbers,'phone_numbers':request.user.userprofile.phone_numbers}
  #  user_profile_form = UserProfileForm(request.POST or None,instance=request.user,initial=data)

   # return render(request,'user_edit_profile.html',context={'form':user_profile_form})



@login_required(login_url = "user:login")
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance= request.user)

        if form.is_valid():
            form.save()            
            return redirect('user:edit_profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'edit_profile.html',args)


@login_required(login_url = "user:login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)       
            return redirect('user:edit_profile')
            #return render(request,'')
        else:
            messages.info(request,"Your Password Could Not Be Verified!")
            return redirect('user:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'change_password.html',args)
