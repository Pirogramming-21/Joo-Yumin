from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def movie_list(request):
    lists = Review.objects.all()
    return render(request, 'movie_list.html', {'lists': lists})


def review_create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            release = request.POST["release"],
            director = request.POST["director"],
            actor = request.POST["actor"],
            genre = request.POST["genre"],
            score = request.POST["score"],
            runningTime = request.POST["runningTime"],
            content = request.POST["content"]
        )



        return redirect("/")
    return render(request, 'review_create.html')
