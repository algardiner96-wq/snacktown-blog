from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import BlogPost, MenuItem, Review
from .forms import ReviewForm, RegisterForm, LoginForm


def register(request):
    """Register a new user"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}! You are now logged in.")
            return redirect('blog:home')
    else:
        form = RegisterForm()
    
    return render(request, 'blog/register.html', {'form': form})


def user_login(request):
    """Login user"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('blog:home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    """Logout user"""
    username = request.user.username if request.user.is_authenticated else ''
    logout(request)
    if username:
        messages.success(request, f"Goodbye {username}, you have been logged out.")
    else:
        messages.success(request, 'You have been logged out.')
    return redirect('blog:home')


def home(request):
    """Homepage with recent blog posts and menu items"""
    recent_posts = BlogPost.objects.order_by('-created_at')[:2]
    menu_items = MenuItem.objects.all()[:3]
    recent_reviews = Review.objects.filter(approved=True).order_by('-created_at')[:5]
    
    context = {
        'recent_posts': recent_posts,
        'menu_items': menu_items,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'blog/home.html', context)


def blog_list(request):
    """List all blog posts"""
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, pk):
    """Single blog post detail"""
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})


def menu_list(request):
    """List all menu items"""
    items = MenuItem.objects.all()
    return render(request, 'blog/menu_list.html', {'items': items})


def menu_item_reviews(request, pk):
    """Reviews for a specific menu item"""
    menu_item = get_object_or_404(MenuItem, pk=pk)
    reviews = Review.objects.filter(menu_item=menu_item, approved=True).order_by('-created_at')
    
    # Check if user already reviewed this item
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(menu_item=menu_item, user=request.user).first()
    
    context = {
        'menu_item': menu_item,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'blog/menu_item_reviews.html', context)


@login_required
def add_review(request, pk):
    """Add a review for a menu item"""
    menu_item = get_object_or_404(MenuItem, pk=pk)
    
    # Check if user already reviewed this item
    existing_review = Review.objects.filter(menu_item=menu_item, user=request.user).first()
    if existing_review:
        messages.warning(request, 'You have already reviewed this item. Edit your existing review instead.')
        return redirect('blog:menu_item_reviews', pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.menu_item = menu_item
            review.user = request.user
            review.save()
            messages.success(
                request,
                f"Thanks {request.user.username}, your review for {menu_item.name} was submitted and awaits approval."
            )
            return redirect('blog:menu_item_reviews', pk=pk)
    else:
        form = ReviewForm()
    
    return render(request, 'blog/review_form.html', {
        'form': form,
        'menu_item': menu_item,
        'action': 'Add'
    })


@login_required
def edit_review(request, pk):
    """Edit a review"""
    review = get_object_or_404(Review, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Updated your review for {review.menu_item.name}, {request.user.username}."
            )
            return redirect('blog:menu_item_reviews', pk=review.menu_item.pk)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'blog/review_form.html', {
        'form': form,
        'menu_item': review.menu_item,
        'action': 'Edit'
    })


@login_required
def delete_review(request, pk):
    """Delete a review"""
    review = get_object_or_404(Review, pk=pk, user=request.user)
    menu_item_pk = review.menu_item.pk
    
    if request.method == 'POST':
        review.delete()
        messages.success(
            request,
            f"Deleted your review for {review.menu_item.name}, {request.user.username}."
        )
        return redirect('blog:menu_item_reviews', pk=menu_item_pk)
    
    return render(request, 'blog/review_confirm_delete.html', {
        'review': review
    })
