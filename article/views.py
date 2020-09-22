from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.http import Http404, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render, reverse)
from django.views import View

from departments.models import Departments, Lessons, Years
from user.models import UserProfile

from .forms import ArticleDeleteRequestForm, ArticleForm, ImageForm
from .models import Article, ArticleDeleteRequest, Comment, Images

# Create your views here.

@login_required(login_url = "user:login")
def articles(request):
    if request.user.is_superuser:
        keyword = request.GET.get("keyword")

        if keyword:
            articles = Article.objects.filter(title__contains = keyword)
            return render(request,"articles.html",{"articles":articles})
        articles = Article.objects.all()

        return render(request,"articles.html",{"articles":articles})
    else:
        raise Http404

def index(request):
    #category = Category.objects.all()
   
    return render(request,"index.html")
#    return HttpResponse("Anasayfa")
#    return HttpResponse("<h3>Anasayfa</h3>")
def about(request):
    return render(request,"about.html")

#def communication(request):
 #   return render(request,"communication.html")

#def detail(request,id):
#    return HttpResponse("Detail:"+ str(id))


@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addArticle(request):
    articleForm = ArticleForm(request.POST or None,request.FILES or None)
    imageForm = ImageForm(request.POST or None,request.FILES or None) 
    if articleForm.is_valid() and imageForm.is_valid():
        article = articleForm.save(commit=False)
        article.author = request.user
        

       # image = imageForm.save()
        #imag
        #image.article = article
       # image.save()
        article.save()


        messages.success(request,"The article was created successfully")
        return redirect("article:dashboard")
    context = {
        "articleForm":articleForm,
        "imageForm":imageForm
    }    
    return render(request,"addarticle.html",context)



# def userUploadPhoto(request):
#     if request.method == "POST":
#         form = userUploadPhoto(request.POST,files=request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             #image.save()
#             data={'is_valid':True,'image-url':image.article_image.url,'name': image.article_image.name,'success':'Photos Uploaded'}
#             # URL atayabilriz..
#             return JsonResponse(data=data)
#         else:
#             return JsonResponse(data={'is_valid':False})
#     else:
#         return HttpResponseRedirect(reverse('article:addarticle'))








@login_required(login_url = "user:login")
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    images = Images.objects.filter(article=article)
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments,"images":images})

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id,author = request.user)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    ImageFormset = modelformset_factory(Images, form=ImageForm, extra=5)
    formset = ImageFormset(request.POST or None,request.FILES or None)
    if form.is_valid() and formset.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        data = Images.objects.filter(article=article)
        for index, f in enumerate(formset):
            if f.cleaned_data:
                if f.cleaned_data['id'] is None:
                    photo = Images(article=article, article_image=f.cleaned_data.get('article_image'))
                    photo.save()
                elif f.cleaned_data['article_image'] is False:
                    photo = Images.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                    photo.delete()
                else:
                    photo = Images(article=article, article_image=f.cleaned_data.get('article_image'))
                    d = Images.objects.get(id=data[index].id)
                    d.image = photo.image
                    d.save()

        messages.success(request,"Updated with Success")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form,"formset":formset})

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article =get_object_or_404(Article,id = id,author = request.user)

    article.delete()

    messages.success(request,"Deleted with Success")

    return redirect("article:dashboard")
#IMPORTANT
def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    profil = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
    
        comment_content = request.POST.get("comment_content")
    #    'User' object has no attribute 'profile'
        newComment = Comment(comment_author = profil, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))



@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.user.id == comment.comment_author.user_id:
        comment.delete()
    return redirect('article:detail', id=comment.article.id)

#def comment_edit(request,id):
    #comment= get_object_or_404(Comment,id=id)
    #if request.user.username == comment.comment_author: 


@login_required(login_url = "user:login")
def showArticle(request,id):
    #articlesnames = get_object_or_404(Article,lessons_id = lessons_id)
    keyword = request.GET.get("keyword")

    if keyword:
        articlesnames = Article.objects.filter(lessons_id = id,title__contains = keyword)
        return render(request,"articletable.html",{"articlesnames":articlesnames})
    articlesnames = Article.objects.filter(lessons_id = id)

    return render(request,"articletable.html",{"articlesnames":articlesnames})


# def showuserdep(request,id):
#     depnames = Departments.objects.filter(id=id,departments_id = id)
#     context = {
#         "depnames":depnames
#     }
#     return render(request,"layout.html",context)
#def showYears(request):
 #   years = Year.objects.all()
  #  return render(request,"layout.html",{"years":years})
@login_required(login_url = "user:login")
def deleteRequest(request,id):
    article = get_object_or_404(Article,id = id)
    if article.author == request.user:
        if request.method == 'POST':
            form = ArticleDeleteRequestForm(request.POST)
            if form .is_valid():
                deleterequest = ArticleDeleteRequest()
                deleterequest.article =article
                deleterequest.request_author = form.cleaned_data['request_author']
                deleterequest.email = form.cleaned_data['email']
                deleterequest.request_content = form.cleaned_data['request_content']
                #request = form.save(commit=False)
                
                deleterequest.save()
                messages.success(request,"The message has been delivered")
                return redirect("article:dashboard")        
        else:
            form = ArticleDeleteRequestForm()
        return render(request,"deleterequest.html",{"form":form})
    else:
        raise Http404






#def deletePost(request):
 #   articles = Article.objects.all()
  #  context = {
   #     "articles": articles
    #}

    #if request.user.is_superuser:
     #   keyword = request.GET.get("keyword")
      #  if keyword:
       #     articles = Article.objects.filter(title__contains = keyword)
        #    context = {
         #       "articles": articles
          #  }   
           # return render(request,"delete-post-admin.html",context)
        #articles = Article.objects.all()
        #context = {
        #    "articles": articles
        #}
        #return render(request,"delete-post-admin.html",context)
    #else:
     #   raise Http404




#def copyPost(request,id):
 #   ghostuser = User.objects.get(username="ghostuser")
  #  Article.objects.filter(id=id).update(author=ghostuser)

   # return redirect("article:deletepost")



# class BasicUploadView(View):
#     def get(self, request):
#         photos = Images.objects.all()
#         return render(self.request, 'addarticle.html', {'photos':photos})

#     def post(self, request):
#         if request.method == 'POST':
#             #articleForm = ArticleForm(request.POST)
#             form = ImageForm(self.request.POST, self.request.FILES)
#             if form.is_valid() and articleForm.is_valid():
#                 photo = form.save()
#                 #article = form.save(commit=False)
#                 #article.author = request.user
#                 #photo.article = article
#                 #article.save()
#                 data = {'is_valid': True, 'name': photo.article_image.name, 'url': photo.article_image.url}
#             else:
#                 data = {'is_valid': False}
#             return JsonResponse(data)
#         else:
#             return HttpResponseRedirect(reverse('article:addarticle'))
