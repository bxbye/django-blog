from django.shortcuts import render
from .models import Post

# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': posts})