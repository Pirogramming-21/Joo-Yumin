from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            release = request.POST["release"],
            director = request.POST["director"],
            actor = request.POST["actor"],
            genre = request.POST["genre"],
            score = request.POST["score"],
            running_time = request.POST["running_time"],
            content = request.POST["content"]
        )
        return redirect("/")
    return render(request, 'review_create.html')