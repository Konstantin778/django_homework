from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from converter_app.models import Currency


def index(request):
    return HttpResponse('Hello converter')


def convert(request: WSGIRequest):

    if request.method == 'POST':
        from_type = request.POST.get('from')
        to_type = request.POST.get('to')
        from_count = request.POST.get('from_count', 0)

        request_data = {
            "from": from_type,
            "from_count": from_count,
            "to": to_type,
        }

        __validate_converter(request_data)

        currency_from = Currency.objects.get(pk=from_type)
        currency_to = Currency.objects.get(pk=to_type)
        result = currency_to.value / currency_from.value * float(from_count)

        return render(request, 'converter.html', {
            'result': result,
        })

    return render(request, 'converter.html')


def __validate_converter(request_data: dict):
    validate_fields = {
        'from',
        'to',
        'from_count',
    }

    if validate_fields != request_data.keys():
        raise ValidationError('Обязательные поля from, from_count и to', 422)
