from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=True).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=True)
    return posts



@register.filter
def snippet(value,arg=20):
    return value[:arg]+'...'


now= timezone.now()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(arg=4):
    posts = Post.objects.filter(published_date__lte=now,status=True).order_by("-published_date")[:arg]
    return {"posts":posts}