from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class PostFeed(Feed):
    title = "Articles from PythonStacks"
    link = "/blog/"
    description = "Top Articles and Tutorials from PythonStacks"

    def items(self):
        return Post.objects.filter(featured=True).order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.last_mod

    def item_description(self, item):
        return item.meta_description
