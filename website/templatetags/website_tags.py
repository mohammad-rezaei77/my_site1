
from django import template
from blog.models import post2
from blog.models import category

register = template.Library()

@register.inclusion_tag('website/last_post.html') # lastposts in website/index.html 
def last_post():
    posts=post2.objects.filter(status=1).order_by('-created_date')[:6]
    return{'posts': posts}