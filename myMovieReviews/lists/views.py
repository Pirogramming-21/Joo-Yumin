from django.shortcuts import render
from .models import List

# Create your views here.
def movie_list(request):
    lists = List.objects.all()
    return render(request, 'movie_list.html', {'lists': lists})



