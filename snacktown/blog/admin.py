from django.contrib import admin
from .models import MenuItem, Review, BlogPost
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Review)
admin.site.register(BlogPost)