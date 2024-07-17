from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def main(request, sort_by=None):
    sort_key = request.GET.get('sort', 'new')  # 기본 정렬 기준을 'new'로 설정합니다.
    
    if sort_key == 'star':
        posts = Post.objects.order_by('-interest')
    elif sort_key == 'name':
        posts = Post.objects.order_by('title')
    elif sort_key == 'register':
        posts = Post.objects.order_by('created_date')
    elif sort_key == 'new':
        posts = Post.objects.order_by('-created_date')
    else:
        posts = Post.objects.all()

    sort_choices = [
        ('star', '찜하기순'),
        ('name', '이름순'),
        ('register', '등록순'),
        ('new', '최신순'),
    ]

    ctx = {'posts': posts, 'sort_choices': sort_choices, 'current_sort': sort_key}

    return render(request, 'posts/list.html', ctx )

def create(request):
    if request.method == "GET":
        form = PostForm()
        ctx = {'form': form}
        return render(request, 'posts/create.html', ctx)
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect("posts:main")

def delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "GET":
        form = PostForm(instance=post)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'posts/update.html', ctx)
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect('posts:detail', pk)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    like_posts = request.session.get('liked_posts', [])
    ctx = {'post': post, 'like_posts': pk in like_posts }
    return render(request, 'posts/detail.html', ctx)


def toggle_like(request, pk):
    post = Post.objects.get(id=pk)
    like_posts = request.session.get('liked_posts', [])

    if pk in like_posts:
        like_posts.remove(pk)
        liked = False
    else:
        like_posts.append(pk)
        liked = True

    request.session['liked_posts'] = like_posts
    messages.success(request, '게시물을 찜했습니다.' if liked else '찜한 게시물을 취소했습니다.')

    return redirect('posts:detail', pk=pk)
