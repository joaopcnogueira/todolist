from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from .forms import TaskForm

from .models import Task

@require_GET
def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})


@require_GET
def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})


@require_GET
def show(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/show.html', {'task': task})


@require_GET
def create(request):
    form = TaskForm()
    return render(request, 'tasks/create.html', {'form': form})


@require_POST
def store(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.status = 'doing'
        task.save()
        return redirect('/')
