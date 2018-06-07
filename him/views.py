from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import HimArticles

def index(request):
    return HttpResponse('HIM')


def blog_title(request):
    blogs = HimArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

