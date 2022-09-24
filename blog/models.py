
from django.db import models

# Create your models here.
class post2(models.Model):
    title=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    content=models.TextField()
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    publish_date=models.DateField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now_add=True)
    #tag image author categorys
    class Meta:
        ordering=('-created_date',)

  