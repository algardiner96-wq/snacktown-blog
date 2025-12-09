from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/reviews/', views.menu_item_reviews, name='menu_item_reviews'),
]
