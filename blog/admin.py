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
    list_display = ('menu_item', 'user', 'rating', 'created_at', 'approved')
    list_filter = ('rating', 'created_at', 'menu_item', 'approved')
    search_fields = ('comment', 'user__username', 'menu_item__name')
    actions = ['approve_reviews', 'disapprove_reviews']
    
    def approve_reviews(self, request, queryset):
        """Admin action to approve reviews"""
        queryset.update(approved=True)
        self.message_user(request, f'{queryset.count()} reviews approved.')
    
    def disapprove_reviews(self, request, queryset):
        """Admin action to disapprove reviews"""
        queryset.update(approved=False)
        self.message_user(request, f'{queryset.count()} reviews disapproved.')
