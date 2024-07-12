from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def list(request):
    reviews = Review.objects.all()
    context = {
        "reviews":reviews
    }
    return render(request, 'review_list.html')