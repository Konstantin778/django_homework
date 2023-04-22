from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'todo_main.html')

def bye(request):
    return HttpResponse('<h1>Auf Wiedersehen</h1>')