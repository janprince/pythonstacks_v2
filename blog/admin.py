from django.contrib import admin
from .models import *


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'featured', 'likes']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('featured', )
    search_fields = ['title']
    actions = ['feature_posts']

    def feature_posts(self, request, queryset):
        queryset.update(featured=True)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    prepopulated_fields = {'slug': ('category',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'post', 'created_on', 'active']
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# class ReplyCommentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'reply_message', 'comment']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date', 'subject']


# Registering models
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

