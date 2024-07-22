from django.urls import path
from .views import *

app_name = 'list'

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('lists/create/', review_create, name='review_create'),
]