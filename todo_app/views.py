from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    request_data = dict(request.GET.items())
    a = request_data['a']
    b = request_data['b']
    name = request_data['name']
    age = request_data['age']
    return render(request, 'index.html', {'name': name, 'result': int(a) * int(b), 'age': int(age)},)

def bye(request):
    return HttpResponse('<h1>Auf Wiedersehen</h1>')