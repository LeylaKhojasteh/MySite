from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

now= timezone.now()

def post_view(pid):
    post = Post.objects.get(id=pid)
    post.counted_views+=1
    post.save()

posts = Post.objects.filter(status=True)   


        
# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    post_view(pid)
    post = get_object_or_404(Post,id=pid, status=True, published_date__lte=now)
    posts = list(Post.objects.filter(status=True))
    prv_post = None
    nxt_post = None
    index = posts.index(post)
    if (index>0):
        prv_post = posts[index-1]
    if(index < len(posts)-1):
         nxt_post = posts[index+1]

    context = {'post':post,'prv':prv_post,'nxt':nxt_post}

    return render(request,'blog/blog-single.html',context)


def blog_category(request,cat_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)



def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)  

    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)


def test(request):
    return render(request,'test.html')