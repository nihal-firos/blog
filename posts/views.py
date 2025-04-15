from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pid):
    posts = Post.objects.get(id=pid)
    return render(request, 'post.html', {'posts': posts})   