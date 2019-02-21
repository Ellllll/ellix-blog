from django.shortcuts import render
from mysecondblog import models


def index(request):
    context = {}
    return render(request, 'index.html', context)

def category(request,category):
    articles = models.Article.objects.filter(category = category)
    return render(request,'category.html',{'articles':articles,'category':category})

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def article(request,category,id):
    article = models.Article.objects.filter(category=category,id=id)
    return render(request, 'single-blog-post-sidebar.html', {'article': article})