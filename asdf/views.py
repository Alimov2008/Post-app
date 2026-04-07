from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from asdf.models import Post

from .forms import PostForm


def home(request):
    return render(request, "asdf/home.html")


@login_required
def about(request):
    return render(request, "asdf/about.html")


@login_required
def posts(request):
    posts = Post.objects.all()
    return render(request, "asdf/posts.html", {"posts": posts})


@login_required
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "asdf/post_details.html", {"post": post})


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "asdf/my_posts.html", {"posts": posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect("posts")
    else:
        form = PostForm()
    return render(request, "asdf/create_post.html", {"form": form})


@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        return HttpResponseForbidden("you are not the creator of this post")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    return render(request, "asdf/update_post.html", {"form": form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        return HttpResponseForbidden("you are not creator on this post")
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    return render(request, "asdf/delete_post.html", {"post": post})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
