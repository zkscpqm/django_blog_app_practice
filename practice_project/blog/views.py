from django.shortcuts import render
from .models import BlogPost


def home(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context={'title': 'Page title'})