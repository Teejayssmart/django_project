from django.shortcuts import render
from .models import Post

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 5343fe1 (Creating App Challenge)
# Create your views here.


def posts_list(request):
<<<<<<< HEAD
  posts = Post.objects.all().order_by('-date')
  return render(request, 'posts/posts_list.html', {'posts' : posts})
=======
# Create your views here.


def posts_list(request):
=======
>>>>>>> 5343fe1 (Creating App Challenge)
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
<<<<<<< HEAD
    return render(request, 'posts/post_page.html', {'post': post})
>>>>>>> dfe5f18 (creating admin panel)
=======
    return render(request, 'posts/post_page.html', {'post': post})
>>>>>>> 5343fe1 (Creating App Challenge)
