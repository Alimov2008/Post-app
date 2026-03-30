from django.shortcuts import get_object_or_404, redirect, render

from asdf.models import Post

from .forms import PostForm


def home(request):
    return render(request, "asdf/home.html")


def about(request):
    return render(request, "asdf/about.html")


def posts(request):
    posts = Post.objects.all()
    return render(request, "asdf/posts.html", {"posts": posts})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()
    return render(request, "asdf/create_post.html", {"form": form})


def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    return render(request, "asdf/update_post.html", {"form": form})
