from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import HimArticles

def index(request):
    return HttpResponse('HIM')


def blog_title(request):
    blogs = HimArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request,article_id):
    article = HimArticles.objects.get(id=article_id)
    pub = article.publish
    return render(request,'blog/contents.html',{"article":article,"publish":pub})