from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('<username>/posts/', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
