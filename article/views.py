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

from .forms import ArticleDeleteRequestForm, ArticleForm, ImageForm,FileForm
from .models import Article, ArticleDeleteRequest, Comment, Images,Files
from django.views.decorators.http import require_http_methods
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
@require_http_methods(["GET","POST"])
def addArticle(request):
    articleForm = ArticleForm(request.POST or None,request.FILES or None)
    form = ImageForm(request.POST or None,request.FILES or None)
    fileForm = FileForm(request.POST or None,request.FILES or None)
    images = request.FILES.getlist('article_image')
    files = request.FILES.getlist('myFile')    
    if articleForm.is_valid() and form.is_valid() and fileForm.is_valid():
        article = articleForm.save(commit=False)
        article.author = request.user
        article.save()
        for i in images:
            image_instance = Images(article_image=i,article=article)
            image_instance.save()
        for f in files:
            file_instance = Files(myFile=f,article=article)
            file_instance.save()
    
        messages.success(request,"The article was created successfully!")
        return redirect("article:dashboard")
    context = {"form":form,
               "articleForm":articleForm,
               "fileForm":fileForm
               } 
    return render(request,"addarticle.html",context)



@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id,author = request.user)
    attachedImage = Images.objects.filter(article=article)#article.resimler.all()[:10]
    attachedFiles = Files.objects.filter(article=article)#article.files.all()[:10]
    #print(type(attachedImage))
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    imageForm = ImageForm(request.POST or None,request.FILES or None)
    fileForm = FileForm(request.POST or None,request.FILES or None)
    images = request.FILES.getlist('article_image')
    files = request.FILES.getlist('myFile') 
    if form.is_valid() and imageForm.is_valid() and fileForm.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        for i in images:
            image_instance = Images(article_image=i,article=article)
            image_instance.save()
        for f in files:
            file_instance = Files(myFile=f,article=article)
            file_instance.save()


        messages.success(request,"Updated with Success")
        return redirect("article:dashboard")
    context = {
        "form":form,
        "imageForm":imageForm,
        "fileForm":fileForm,
        "attachedImage":attachedImage,
        "attachedFiles":attachedFiles
               } 

    return render(request,"update.html",context)

@login_required(login_url = "user:login")
def deleteImage(request,id):
    image = get_object_or_404(Images,id = id)
    tmp = image.article_id
    image.delete()
    return HttpResponseRedirect(reverse('article:update', args=(tmp,)))
    """(Bu SO cevabında belirtildiği gibi, tek öğeli tuple'ların parantezlerle çevrili bir ifadeden bir demeti tanımlayan belirsizliği gidermek için takip eden virgül gereklidir args=(obj.pk,))

Alternatif olarak, dokümanlarda belirtildiği gibi, bir liste kullanmak iyi sonuç verir: args=[obj.pk] """

@login_required(login_url = "user:login")
def deleteFile(request,id):
    file = get_object_or_404(Files,id = id)
    tmp = file.article_id
    file.delete()
    return HttpResponseRedirect(reverse('article:update', args=(tmp,)))

def upload_pdf(request):
    if request.method == 'POST':
         form = ImageForm(request.POST, request.FILES)
         files = request.FILES.getlist('article_image')
         if form.is_valid():
             for f in files:
                 file_instance = Images(article_image=f)
                 file_instance.save()
    else:
         form = ImageForm()
    return render(request, 'upload_pdf.html', {'form': form})






@login_required(login_url = "user:login")
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    images = Images.objects.filter(article=article)
    a = len(images)
    files = Files.objects.filter(article=article)
    comments = article.comments.all() #.filter(article=article)
    return render(request,"detail.html",{"article":article,"comments":comments,"images":images,"files":files,"range":range(a)})


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
        rate = request.POST.get("rating")
        print(rate)
        #    'User' object has no attribute 'profile'
        newComment = Comment(comment_author = profil, comment_content = comment_content, rate = rate)
       # newComment.rate=rate
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
        # comments = Comment.objects.filter(article = articlesnames)

        # ratelst = []
        # for i in comments:
        #     ratelst.append(i.rate)

        # avg = sum(ratelst) / len(ratelst)
        
        return render(request,"articletable.html",{"articlesnames":articlesnames})
    articlesnames = Article.objects.filter(lessons_id = id)
    # comments = Comment.objects.filter(article = articlesnames)

    # ratelst = []
    # for i in comments:
    #     ratelst.append(i.rate)

    # avg = sum(ratelst) / len(ratelst)                        

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
