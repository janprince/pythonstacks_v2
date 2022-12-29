from django.urls import path
from . import views

app_name = "main"   # change
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact")
]