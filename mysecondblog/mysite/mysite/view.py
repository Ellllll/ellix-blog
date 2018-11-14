from django.shortcuts import render
from mysecondblog import models


def index(request):
    context = {}
    return render(request, 'index.html', context)

def python(request):
    articles = models.Article_python.objects.all()
    return render(request,'blog_python.html',{'articles':articles})

def net(request):
    articles=models.Article_net.objects.all()
    return render(request,'blog_net.html',{'articles':articles})

def deep_learning(request):
    articles = models.Article_deep_learning.objects.all()
    return render(request,'blog_deep_learning.html',{'articles':articles})

def personal(request):
    articles=models.Article_personal.objects.all()
    return render(request, 'blog_personal.html', {'articles': articles})

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def article_python(request,id):
    article_ = models.Article_python.objects.get(id=id)
    return render(request, 'single-blog-post-sidebar.html', {'article': article_})

def article_net(request,id):
    article_ = models.Article_net.objects.get(id=id)
    return render(request, 'single-blog-post-sidebar.html', {'article': article_})

def article_deep_learning(request,id):
    article_ = models.Article_deep_learning.objects.get(id=id)
    return render(request, 'single-blog-post-sidebar.html', {'article': article_})

def article_personal(request,id):
    article_ = models.Article_personal.objects.get(id=id)
    return render(request, 'single-blog-post-sidebar.html', {'article': article_})
