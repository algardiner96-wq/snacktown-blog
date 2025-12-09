from django.shortcuts import render, get_object_or_404
from .models import BlogPost, MenuItem, Review


def home(request):
    """Homepage with recent blog posts and menu items"""
    recent_posts = BlogPost.objects.order_by('-created_at')[:2]
    menu_items = MenuItem.objects.all()[:3]
    recent_reviews = Review.objects.order_by('-created_at')[:5]
    
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
    reviews = Review.objects.filter(menu_item=menu_item).order_by('-created_at')
    
    context = {
        'menu_item': menu_item,
        'reviews': reviews,
    }
    return render(request, 'blog/menu_item_reviews.html', context)
