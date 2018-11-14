from __future__ import unicode_literals

from django.db import models


class Article_python(models.Model):
    title = models.CharField(max_length=50)
    main_content = models.CharField(max_length=50,default="")
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(u'PHOTO',upload_to='uploadImage')

class Article_net(models.Model):
    title = models.CharField(max_length=50)
    main_content = models.CharField(max_length=50,default="")
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(u'PHOTO',upload_to='uploadImage')

class Article_deep_learning(models.Model):
    title = models.CharField(max_length=50)
    main_content = models.CharField(max_length=50,default="")
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(u'PHOTO',upload_to='uploadImage')

class Article_personal(models.Model):
    title = models.CharField(max_length=50)
    main_content = models.CharField(max_length=50, default="")
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(u'PHOTO',upload_to='uploadImage')
    #def get_absolute_url(self):
        #return reverse('mysecondblog:article', kwargs={'id': self.id})


   # def __unicode__(self):
         #return 'name:'+self.name+';age:'+str(self.age)+';birthday:'+str(self.birthday)
# Create your models here.
