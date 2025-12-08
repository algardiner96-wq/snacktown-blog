from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseForbidden
# Create your views here.


def blog_list(request):
    """
    Display a list of all blog posts.
    - retrieves all BlogPost objects from the database.
    - passes them to the 'blog/blog_list.html' template for rendering.
    """
    posts = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_create(request):
    """
    Create a new blog post.
    - only superusers are allowed to create posts.
    - on POST request, saves the new post and redirects to the blog list view.
    """
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only superusers can create posts.")
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})


def blog_update(request, pk):
    """
    Update an existing blog post.
    - only superusers are allowed to edit posts.
    - retrieves the BlogPost object by primary key (pk).
    - on POST request, updates the post with the submitted data.
    """
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only superusers can edit posts.")
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form})


def blog_delete(request, pk):
    """
     Delete a blog post.
    - only superusers are allowed to delete posts.
    - retrieves the BlogPost object by primary key (pk).
    - on POST request, deletes the post and redirects to the blog list view.
     """
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only superusers can delete posts.")
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})


def register(request):
    """
    User registration view.
    - handles both GET and POST requests.
    - creates a new user and logs them in upon successful registration.
    - redirects to the blog list view after registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def review_create(request, post_id):
    """
    Create a new review for a menu item.
    - retrieves the BlogPost object by primary key (post_id).
    - on POST request, saves the new review and redirects to the blog list view.
    """
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.user = request.user
            review.save()
            return redirect('blog_list') 
    else:
        form = ReviewForm()
    return render(request, 'blog/review_form.html', {'form': form, 'post': post})


def review_update(request, pk):
    """
    Update an existing review.
    - retrieves the Review object by primary key (pk).
    - on POST request, updates the review with the submitted data.
    """
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden("You can only edit your own reviews.")
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'blog/review_form.html', {'form': form, 'post': review.post})


def review_delete(request, pk):
    """
    Delete a review.
    - retrieves the Review object by primary key (pk).
    - on POST request, deletes the review and redirects to the blog list view.
    """
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return HttpResponseForbidden("You can only delete your own reviews.")
    if request.method == 'POST':
        review.delete()
        return redirect('blog_list')
    return render(request, 'blog/review_confirm_delete.html', {'review': review})
