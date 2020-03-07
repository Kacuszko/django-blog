from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Mateusz Kacaliński',
        'title': 'Thats post title',
        'content': 'Thats post content',
        'date_posted': 'August 28, 2020'
    },
    {
        'author': 'Maria Dudziak',
        'title': 'Another post title',
        'content': 'Another post content',
        'date_posted': 'August 30, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})