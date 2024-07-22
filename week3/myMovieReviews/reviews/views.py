from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Review
from django.http import HttpResponse

# Create your views here.
def list(request):
    reviews = Review.objects.filter(is_deleted=False)
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
            content = request.POST["content"],
        )
        return redirect("/")
    return render(request, 'review_create.html')

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'review_detail.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)
    if request.method=="POST":
        title = request.POST.get("title")
        release=request.POST.get("release")
        director=request.POST.get("director")
        actor=request.POST.get("actor")
        genre=request.POST.get("genre")
        score=request.POST.get("score")
        running_time=request.POST.get("running_time")
        content=request.POST.get("content")


        review.title = title
        review.release = release
        review.director = director
        review.actor = actor
        review.genre = genre
        review.score = score
        review.running_time = running_time
        review.content = content 
        
        review.save() 

        return redirect(f"/{pk}")
    context={
        "review":review
    }
    return render(request, 'review_update.html', context) 

def review_delete(request, pk):
    if request.method=="POST":
        review = get_object_or_404(Review, id=pk)
        review.is_deleted = True
        review.save()
    return redirect("/")
