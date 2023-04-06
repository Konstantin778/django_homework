from django.shortcuts import render

def binary_sum(request):
    request_data = dict(request.GET.items())
    first = request_data['first']
    second = request_data['second']
    result = bin(int(first) + int(second))
    return render(request, 'homework.html', {'result': result})


def sentence_case(request):
    if request.method == 'GET':
        return render(request, 'homework.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).capitalize()
        return render(request, 'homework.html', {'output': output_data})


def lower_case(request):
    if request.method == 'GET':
        return render(request, 'homework.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).lower()
        return render(request, 'homework.html', {'output': output_data})


def upper_case(request):
    if request.method == 'GET':
        return render(request, 'homework.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).upper()
        return render(request, 'homework.html', {'output': output_data})


def capitalize_each_word(request):
    if request.method == 'GET':
        return render(request, 'homework.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).title()
        return render(request, 'homework.html', {'output': output_data})


def toggle_case(request):
    if request.method == 'GET':
        return render(request, 'homework.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).swapcase()
        return render(request, 'homework.html', {'output': output_data})
