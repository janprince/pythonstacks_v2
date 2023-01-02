from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q


def index(request):
    posts = Post.objects.filter(featured=True)

    context = {
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.filter(featured=True)
    comments = post.comments.filter(active=True)
    categories = Category.objects.all()
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)  # pass in the data received to the CommentForm
        if comment_form.is_valid():
            # Create a comment but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "posts": posts[:3],
        "categories": categories,
        "comments": comments,
        'new_comment': new_comment,
    }

    return render(request, "blog/post.html", context)


def search(request, term):
    # term = term.lower()
    query_list = Post.objects.filter(Q(title__icontains=term), featured=True)

    context = {
        "posts": query_list,
    }

    return render(request, "blog/index.html", context)


def category():
    return None