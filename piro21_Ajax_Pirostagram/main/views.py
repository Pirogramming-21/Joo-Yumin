from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def main(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main.html', ctx)




def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'post_new.html', ctx)


def delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('main')

def detail(request, pk):
  post = Post.objects.get(id=pk)
  comment_form = CommentForm()
  ctx = {'post':post, 'comment_form': comment_form}
  return render(request, 'post_detail.html', ctx)

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data['post_id']
        content = data['content']
        post =Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, content=content)
        return JsonResponse({'id': comment.id, 'content': comment.content, 'create_date': comment.create_date.strftime('%Y-%m-%d %H:%M:%S')})

@csrf_exempt
def delete_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_id = data['comment_id']
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({'result': 'success'})

@csrf_exempt
def like(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        post.like += 1
        post.save()
        return JsonResponse({'id': post_id, 'likes': post.like})
    return JsonResponse({'error': 'Invalid request'}, status=400)