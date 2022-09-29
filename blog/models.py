
from django.db import models
from django.contrib.auth.models import User
import datetime
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
    publish_date=models.DateField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    


    #tag
    class Meta:
        ordering=('-created_date',)
        verbose_name='Post'
        verbose_name_plural='Posts'


