from django.urls import path, include
from django.contrib import admin
from .views import indexView

app_name = 'app_skill'

urlpatterns = [
    path('', indexView.as_view(), name='skill')
]
