from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='blog-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='blog-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='blog-logout'),
    path('profile/', views.profile, name='user-profile'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'), name='user-pw-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
