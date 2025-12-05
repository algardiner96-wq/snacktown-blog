from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
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
    - handles both GET and POST requests.   
    - Asigns the logged-in user as the author of the post.
    - redirects to the blog list view upon successful creation.
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})


def blog_update(request, pk):
    """
    Update an existing blog post.
    - retrieves the BlogPost object by its primary key (pk).
    - handles both GET and POST requests.
    - redirects to the blog list view upon successful update.
    """
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
    - retrieves the BlogPost object by its primary key (pk).
    - handles POST requests to confirm deletion.
    - redirects to the blog list view upon successful deletion.
    """
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