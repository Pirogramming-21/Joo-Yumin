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
    review = get_object_or_404(Review, pk=pk)
    if request.method=="POST":
        review.title=request.POST["title"]
        review.release=request.POST["release"]
        review.director=request.POST["director"]
        review.actor=request.POST["actor"]
        review.genre=request.POST["genre"]
        review.score=request.POST["score"]
        review.running_time=request.POST["running_time"]
        review.content=request.POST["content"]

        review.save() # 기존에 있던 pk의 값을 바꾸고 재저장 하고싶다!

        return redirect(f"/{pk}")

    else:
        # GET 요청일 경우, 기존 데이터를 폼 없이 보여줌
        context = {
            'review': review
        }
    return render(request, 'review_update.html', context) # context를 통해 템플릿에 전달
