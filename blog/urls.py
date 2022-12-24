from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path("category/<slug:category_slug>/", views.category, name='category'),
    path("search/", views.search, name='search'),
]