from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def detail(request, slug):
    return render(request, "blog/post.html")


def search():
    return None


def category():
    return None