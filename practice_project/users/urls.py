from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='blog-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='blog-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='blog-logout'),
    path('profile/', views.profile, name='user-profile'),
    path('<username>/', LoginView.as_view(template_name='users/login.html'), name='blog-login'),
]
