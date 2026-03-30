from django.http import HttpResponse
from django.shortcuts import render

from asdf.models import Post


def home(request):
    return render(request, "asdf/home.html")


def about(request):
    return render(request, "asdf/about.html")


def posts(request):
    posts = Post.objects.all()
    return render(request, "asdf/posts.html", {"posts": posts})
