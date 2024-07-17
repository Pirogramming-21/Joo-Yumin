from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevToolForm

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
    tools = DevTool.objects.all()
    ctx = {'tools':tools}
    return render(request, 'devTools/list.html', ctx )

def delete(request, pk):
    DevTool.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(request, pk):
    tool = DevTool.objects.get(id=pk)
    if request.method == "GET":
        form = DevToolForm(instance=tool)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'devTools/update.html', ctx)
    form = DevToolForm(request.POST, request.FILES, instance=tool)
    if form.is_valid():
        form.save()
    return redirect('devTools:detail', pk)

def detail(request, pk):
    tool = DevTool.objects.get(id=pk)
    ctx = {'tool':tool}
    return render(request, 'devTools/detail.html', ctx)

