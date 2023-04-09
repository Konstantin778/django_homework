from django.shortcuts import render

def binary_sum(request):
    request_data = dict(request.GET.items())
    first = request_data['first']
    second = request_data['second']
    try:
        diapason = [x for x in range(int(first), int(second) + 1)]
        result = sum(diapason)
        if result < 1:
            return render(request,
                          'homework.html',
                          {'result': 'Второе число должно быть больше первого'}
            )
    except Exception as e:
        return render(request,
                      'homework.html',
                      {'result': 'Ошибка. Для совершения операции введите ДВА целых числа'}

        )
    return render(request, 'homework.html', {'result': result})


def sentence_case(request):
    if request.method == 'GET':
        return render(request, 'register_change.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).capitalize()
        return render(request, 'register_change.html', {'output': output_data})


def lower_case(request):
    if request.method == 'GET':
        return render(request, 'register_change.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).lower()
        return render(request, 'register_change.html', {'output': output_data})


def upper_case(request):
    if request.method == 'GET':
        return render(request, 'register_change.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).upper()
        return render(request, 'register_change.html', {'output': output_data})


def capitalize_each_word(request):
    if request.method == 'GET':
        return render(request, 'register_change.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).title()
        return render(request, 'register_change.html', {'output': output_data})


def toggle_case(request):
    if request.method == 'GET':
        return render(request, 'register_change.html', {'output': '-'})
    else:
        output_data = (dict(request.POST.items())['string']).swapcase()
        return render(request, 'register_change.html', {'output': output_data})


def text_replace(request):
    if request.method == 'GET':
        return render(request, 'text_replace.html', {'output': '-'})
    request_dict = dict(request.POST.items())
    input_data = request_dict['string']
    old_elem = request_dict['old_elem']
    new_elem = request_dict['new_elem']
    output_data = input_data.replace(old_elem, new_elem)
    return render(request, 'text_replace.html', {'output': output_data})

