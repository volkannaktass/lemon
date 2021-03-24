## view.py

def register(request):

    form = RegisterForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    if form.is_valid() and profile_form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        print(first_name)
        last_name = form.cleaned_data.get("last_name")
        print(last_name)
        username = form.cleaned_data.get("username")
        print(username)
        password = form.cleaned_data.get("password")
        print(password)
        email = form.cleaned_data.get("email")
        print(email)
        #category = form.cleaned_data.get("category")
        #departments = form.cleaned_data.get("departments")
        #first_name = form.cleaned_data.get("first_name")
        #groups = form.cleaned_data.get("groups")
        #student_id = form.cleaned_data.get("student_id")
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
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
        login(request,user)
        messages.info(request,"Registration Successful...")

        return redirect("index")
    context = {
            "form" : form,
            "profile_form" : profile_form,
        }
    return render(request,"register.html",context)






#models.py
class UserProfile(models.Model):
    Male = 'Male'
    Female = 'Female'
    Other = "Other"
    Gender = ((Male,'Male'),(Female,"Female"),(Other,"Other"))
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True) #related_name='profil'
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',verbose_name="Profile Image:",editable=True)
    faculty = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    departments = models.ForeignKey(Departments,on_delete=models.CASCADE,blank=True,null=True)
    phone_number = models.CharField(max_length=11,verbose_name='Phone Number',blank=True)
    gender = models.CharField(max_length=6,default=3,verbose_name='Gender',choices=Gender,blank=True)
    student_number = models.CharField(max_length=8,verbose_name='Student Number:*',blank=True, null=True)    


##forms.py


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('faculty','departments','student_number')
