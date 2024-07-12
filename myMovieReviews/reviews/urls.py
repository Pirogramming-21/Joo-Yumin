from django.urls import path
from .views import *

app_name = 'MovieReviews'

urlpatterns = [
    path('', list, name='list'),
]