from django.shortcuts import render
from django.views import View


def index(request):
    context = {
        'title': 'Achmad Irfan Afandi',
        'tile': 'Home',
        'subtitle': 'Data Analyst - Python Developer',
    }

    return render(request, 'index.html', context)
