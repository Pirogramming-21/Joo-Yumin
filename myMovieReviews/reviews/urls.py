from django.urls import path
from .views import *

app_name = 'MovieReviews'

urlpatterns = [
    path('', list),
    path('create/', create ),
    path('<int:pk>/', review_detail),
    path('<int:pk>/update/', review_update),
]