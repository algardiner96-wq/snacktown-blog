from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Blog
    path('', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # Menu & Reviews
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/reviews/', views.menu_item_reviews, name='menu_item_reviews'),
    path('menu/<int:pk>/review/add/', views.add_review, name='add_review'),
    path('review/<int:pk>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),
]
