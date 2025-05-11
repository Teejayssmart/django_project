from django.shortcuts import render
from .models import Post

<<<<<<< HEAD

# Create your views here.

def posts_list(request):
  posts = Post.objects.all().order_by('-date')
  return render(request, 'posts/posts_list.html', {'posts' : posts})
=======
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})
>>>>>>> dfe5f18 (creating admin panel)
