from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
from departments.models import Lessons,Departments,Years
from user.models import UserProfile
from django.http import Http404
#from departments.models import Category
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

def communication(request):
    return render(request,"communication.html")

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
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Created with Success")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

@login_required(login_url = "user:login")
def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id,author = request.user)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Updated with Success")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    article =get_object_or_404(Article,id = id,author = request.user)

    article.delete()

    messages.success(request,"Deleted with Success")

    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        #comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = request.user, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))


#def comment_approve(request, id):
 #   comment = get_object_or_404(Comment, id=id)
  #  comment.approve()
   # return redirect(reverse("article:detail",kwargs={"id":id}))

#def comment_remove(request, id):
 #   comment = get_object_or_404(Comment, id=id)
  #  comment.delete()
   # return redirect(reverse("article:detail",kwargs={"id":id}))

#def deleteComment(request,id):
 #   article = get_object_or_404(Article,id = id)
  #  if request.method == "POST":
        

   #     newComment = Comment(comment_author = request.user, comment_content = comment_content)
    #    newComment.article = article
     #   newComment.save()
    #Comment.delete()
    #return redirect(reverse("article:detail",kwargs={"id":id}))

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

