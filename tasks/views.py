from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm

from .models import Task

def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {'tasks': tasks})


def show(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/show.html', {'task': task})


def create(request):
    form = TaskForm()
    return render(request, 'tasks/create.html', {'form': form})


def store(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.status = 'doing'
        task.save()
        return redirect('/')
