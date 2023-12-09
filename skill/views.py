# Create your views here.
from typing import Any, Dict
from django.shortcuts import render
from .models import skill
from django.views.generic.base import TemplateView


class indexView(TemplateView):
    template_name = 'skill/index.html'

    def get_context_data(self):
        skills = skill.objects.all()
        context = {
            'title': 'Skill',
            'skill': skills}

        return context

# def index(request):
#     skills = skill.objects.all()
#     context = {
#         'title': 'Skill',
#         'skill': skills
#     }
#     return render(request, 'skill/index.html', context)
