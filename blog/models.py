from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField

User = get_user_model()


class BlogPost(models.Model):
    """
    Model representing a blog post.
    
    """ 

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    """
    Model representing a menu item.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model representing a review for a menu item.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.menu_item} ({self.rating})"