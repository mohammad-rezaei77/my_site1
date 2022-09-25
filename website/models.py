import email
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.


class contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('create_date',)
        verbose_name = 'message'
        verbose_name_plural = 'messages'
