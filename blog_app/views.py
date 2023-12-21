from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,"index.html",{"posts":posts})


def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    return render(request,"post_detail.html",{"post":post})


def signup_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        
        user=User(username=username,email=email) 
        user.set_password(password)
        user.save()
        return redirect("login")

    return render(request,"signup.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def add_post(request):
    
    if request.method=="POST":
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        img=request.FILES.get("img")
        post=Post(title=title,desc=desc,img=img,author=request.user)
        post.save()
        return redirect("index")


    return render(request,"add_post.html",{})

@login_required
def update_post(request,id):
    post=Post.objects.get(id=id)
    if request.user==post.author:
        if request.method=="POST":
            post.title=request.POST.get("title")
            post.desc=request.POST.get("desc")
            post.img=request.FILES.get("img")
            post.save()

            return redirect("index")

        return render(request,"update_post.html",{"post":post})
    return redirect("index")


@login_required
def delete_post(request,id):
    post=Post.objects.get(id=id)
    if request.user==post.author:

        post.delete()
    
    return redirect("index")


