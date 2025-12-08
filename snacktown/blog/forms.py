from django import forms
from .models import Review
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image',]
     

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['menu_item', 'rating', 'comment',]