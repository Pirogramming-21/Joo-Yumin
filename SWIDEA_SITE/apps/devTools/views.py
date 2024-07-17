from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevToolForm
from apps.posts.models import Post

# Create your views here.

def create(request):
    if request.method == "GET":
        form = DevToolForm()
        ctx = {'form': form}
        return render(request, 'devTools/create.html', ctx)
    form = DevToolForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect("posts:main")

def list(request):
    devTools = DevTool.objects.all()
    ctx = {'devTools': devTools}
    return render(request, 'devTools/list.html', ctx)

def delete(request, pk):
    DevTool.objects.get(id=pk).delete()
    return redirect('devTools:list')

def update(request,pk):
    tool = DevTool.objects.get(id=pk)
    if request.method == 'GET':
        form = DevToolForm(instance=tool)
        ctx = {'form' : form, 'pk':pk}
        return render(request, 'devTools/update.html', ctx)
    
    form = DevToolForm(request.POST, instance=tool)
    if form.is_valid():
        form.save()
        return redirect('devTools:list')
    ctx = {'form': form, 'pk': pk}
    return render(request, 'devTools/update.html', ctx)

def detail(request, pk):
    devTool = DevTool.objects.get(id=pk)  # 여기서 devTool 객체를 가져옵니다.
    posts = Post.objects.filter(devtool_id=devTool.id)  # DevTool 객체의 ID로 필터링합니다.
    ctx = {'devTool': devTool, 'posts': posts}
    return render(request, 'devTools/detail.html', ctx)

