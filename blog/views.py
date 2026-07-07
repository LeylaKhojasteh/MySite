from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

now= timezone.now()

def post_view(pid):
    post = Post.objects.get(id=pid)
    post.counted_views+=1
    post.save()

posts = Post.objects.filter(published_date__lte=now,status=True)   


        
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_date__lte=now,status=True)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post_view(pid)
    post = get_object_or_404(Post,id=pid, status=True, published_date__lte=now)
    posts = list(Post.objects.filter(published_date__lte=now,status=True))
    prv_post = None
    nxt_post = None
    index = posts.index(post)
    if (index>0):
        prv_post = posts[index-1]
    if(index < len(posts)-1):
         nxt_post = posts[index+1]

    context = {'post':post,'prv':prv_post,'nxt':nxt_post}

    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    post = get_object_or_404(Post,id=pid)
    context = {'post':post}
    return render(request,'test.html',context)