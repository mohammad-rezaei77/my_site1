
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import datetime

from traitlets import default
# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) :
        return self.name


class post2(models.Model):

    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    content=models.TextField()
    counted_view=models.IntegerField(default=0)
    category=models.ManyToManyField(category)
    status=models.BooleanField(default=False)
    login_required=models.BooleanField(default=False)
    publish_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    tags = TaggableManager()
    def __str__(self):
        return self.title
    class Meta:
        ordering=('-created_date',)
        verbose_name='Post'
        verbose_name_plural='Posts'

class test(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(default=None)

class sql_test(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0) 


class Comment(models.Model):
    post = models.ForeignKey(post2,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


