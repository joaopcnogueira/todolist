from django.http.response import HttpResponse
from django.shortcuts import render


def helloworld(request):
    return HttpResponse('Hello World!')
