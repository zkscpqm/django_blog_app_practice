from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
