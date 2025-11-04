from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('tag/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]