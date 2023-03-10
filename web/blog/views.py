from django.http import HttpResponse
from django.shortcuts import render

posts = [{
    'author': 'Magda',
    'title': 'Post 1',
    'content': 'Content 1',
    'date_posted': 'February 02,2023'
},
    {
        'author': 'Bożenka',
        'title': 'Post 2',
        'content': 'Content 2',
        'date_posted': 'February 03,2023'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
