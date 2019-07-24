from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
#    return HttpResponse("Anasayfa")
#    return HttpResponse("<h3>Anasayfa</h3>")
