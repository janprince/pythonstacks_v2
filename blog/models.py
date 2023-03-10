from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


# Author model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.get_full_name()}"


# Category model
class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f'{self.category}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:category', args=[str(self.slug)])


# Post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True)
    meta_description = models.TextField(max_length=200, blank=True)
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, blank=False, related_name='posts', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    last_mod = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:detail', args=[str(self.slug)])


# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=99)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment on ''{self.post}'' by {self.name}"


# # Comment Reply
# class ReplyComment(models.Model):
#     name = models.ForeignKey(Author, on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies", blank=False)
#     reply_message = models.TextField(blank=False)
#     created_on = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['id']
#
#     def __str__(self):
#         return f"Reply: {self.reply_message}"


