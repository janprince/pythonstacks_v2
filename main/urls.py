from django.urls import path
from . import views

app_name = "main"   # change
urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact")
]