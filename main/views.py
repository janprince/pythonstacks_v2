from django.shortcuts import render, redirect


def index(request):
    return redirect("blog:index")


def contact(request):
    return render(request, "main/contact.html")


def robots(request):
    return render(request, "main/others/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "main/others/ads.txt", content_type="text/plain")