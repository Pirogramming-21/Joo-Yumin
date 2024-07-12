from django.shortcuts import render, redirect, get_object_or_404
from django import forms
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

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'review_detail.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, id=pk)
    context = {
        'review': review
    }
    if request.method=="POST":
        review.title=request.POST["title"]
        review.release=request.POST["release"]
        review.director=request.POST["director"]
        review.actor=request.POST["actor"]
        review.genre=request.POST["genre"]
        review.score=request.POST["score"]
        review.running_time=request.POST["running_time"]
        review.content=request.POST["content"]

        review.save() 

        return redirect(f"/{pk}", id=pk)
    
    
    return render(request, 'review_update.html', context) 

def review_delete(request, pk):
    if request.method=="POST":
        review = get_object_or_404(Review, id=pk)
        review.delete()

        return redirect("/")
    return redirect("/")
