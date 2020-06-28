from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse,HttpResponseRedirect
from .forms import ArticleForm,ImageForm,ArticleDeleteRequestForm
from django.contrib import messages
from .models import Article,Comment,Images,ArticleDeleteRequest
from django.contrib.auth.decorators import login_required
from departments.models import Lessons,Departments,Years
from user.models import UserProfile
from django.http import Http404
from django.forms import modelformset_factory
from django.contrib.auth.models import User
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
    ImageFormset = modelformset_factory(Images, form=ImageForm, extra=5)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        formset = ImageFormset(request.POST or None,request.FILES or None)
        if form.is_valid() and formset.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            images = formset.save(commit=False)
            for image in images:
                image.article = article
                image.save()
                
            #for f in formset:
             #   try:
              #      photo = Images(article=article)
               #     photo.save()
                #except Exception as e:
                 #   break
            messages.success(request,"Created with Success")
            return redirect("article:dashboard")
    else:
        form = ArticleForm()
        formset = ImageFormset(queryset=Images.objects.none())
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request,"addarticle.html",context)

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