from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,"index.html",{"posts":posts})

def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    return render(request,"post_detail.html",{"post":post})