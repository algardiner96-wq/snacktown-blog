from django.contrib import admin
from .models import BlogPost, MenuItem, Review


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'menu_item')
    search_fields = ('comment', 'user__username', 'menu_item__name')
