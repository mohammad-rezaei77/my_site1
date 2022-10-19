from django import template
from blog.models import post2,Comment
from blog.models import category


register = template.Library()
@register.simple_tag
def count():
    return post2.objects.filter(status=1).count()


@register.filter
def snipet(str):
    char1=""
    string=str.split(" ")
    print(len(string))
    if len(string)>20:
        string=string[:20]
        for char in string:
            char1=char1+ char+" "
        return char1+" ..."


@register.inclusion_tag('blog/blog_category_post.html')
def category_post():
    cate_dict={}
    posts=post2.objects.filter(status=1)
    categorys=category.objects.all()
    for name in categorys:
        cate_dict[name]=posts.filter(category=name).count()
    return {'categorys':cate_dict}

@register.simple_tag(name='comments_count')
def functions(pid):
    post = post2.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id,approved=True).count()
    

