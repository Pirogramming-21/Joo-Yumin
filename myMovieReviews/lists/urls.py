from django.urls import path
from .views import *

app_name = 'list'

urlpatterns = [
    path('', movie_list, name='movie_list'),
]