from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Admin',
        'title': 'Blog post 1',
        'content': 'Blah Blah',
        'date_posted': 'Today'
    },
    {
        'author': 'Some User',
        'title': 'Blog post 2',
        'content': 'Bleah Bleah Bleah',
        'date_posted': 'Tomorrow'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog_app/home.html', context)

def about(request):
    return render(request, 'blog_app/about.html')
