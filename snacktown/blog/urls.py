from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('update/<int:pk>/', views.blog_update, name='blog_update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'), 
    path('register/', views.register, name='register'),
    path('<int:post_id>/review/create/', views.review_create, name='review_create'),
    path('review/<int:pk>/edit/', views.review_update, name='review_update'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
]