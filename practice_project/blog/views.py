from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost


class PostListView(ListView):

    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):

    model = BlogPost


class PostCreateView(LoginRequiredMixin, CreateView):

    login_url = '/user/login/'
    model = BlogPost
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', context={'title': 'Page title'})