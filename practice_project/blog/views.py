from django.shortcuts import render


posts = [
    {
        'author': 'Georgi',
        'title': 'first post',
        'content': 'lorem ipsum',
        'date_posted': '27-01-2020'
    },
    {
        'author': 'Vanya',
        'title': 'second post',
        'content': 'lorem ipsum 2',
        'date_posted': '21-03-2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context={'title': 'Page title'})