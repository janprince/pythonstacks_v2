from django.shortcuts import render, redirect


def index(request):
    return redirect("blog:index")


def contact(request):
    return render(request, "main/contact.html")