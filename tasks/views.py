from django.http.response import HttpResponse
from django.shortcuts import render


def helloworld(request):
    return HttpResponse('Hello World!')


def tasklist(request):
    return render(request, 'tasks/list.html')


def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})