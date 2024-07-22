from django.urls import path
from . import views
from .views import like

app_main = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('post_new/', views.post_new, name='post_new'),
    path('like/', like, name='like'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]