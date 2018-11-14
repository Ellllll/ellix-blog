"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index,name='index' ),
    url(r'^python$',view.python,name='python'),
    url(r'^.net$',view.net,name='net'),
    url(r'^deep_learning$',view.deep_learning,name='deep_learning'),
    url(r'^personal$',view.personal,name='personal'),
    url(r'^contact$',view.contact,name='contact'),
    url(r'^python_(?P<id>\d+)/$', view.article_python, name='article_python'),
    url(r'^.net_(?P<id>\d+)/$', view.article_net, name='article_net'),
    url(r'^personal_(?P<id>\d+)/$', view.article_personal, name='article_personal'),
    url(r'^deep_learning_(?P<id>\d+)/$', view.article_deep_learning, name='article_deep_learning'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
