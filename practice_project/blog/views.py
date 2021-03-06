from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost


class PostListView(ListView):

    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):

    model = BlogPost
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BlogPost.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):

    model = BlogPost


class PostCreateView(LoginRequiredMixin, CreateView):

    login_url = '/user/login/'
    model = BlogPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    login_url = '/user/login/'
    model = BlogPost
    fields = ['title', 'content']

    def test_func(self):
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = BlogPost
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author


def about(request):
    return render(request, 'blog/about.html', context={'title': 'Page title'})