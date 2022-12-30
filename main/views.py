from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    return redirect("blog:index")


def contact(request):
    new_contact = None

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            new_contact = True

    contact_form = ContactForm()
    context = {
        'new_contact': new_contact,
    }

    return render(request, "main/contact.html", context)


def robots(request):
    return render(request, "main/others/robots.txt", content_type="text/plain")


def ads(request):
    return render(request, "main/others/ads.txt", content_type="text/plain")