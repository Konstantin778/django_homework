from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponseServerError

from converter_app.models import Currency


def index(request: WSGIRequest):
    return JsonResponse({'message': 'заглушка'})

def convert(request: WSGIRequest):
    # api/convert?from=EUR & to = RUB

    request_data = {
        "from": request.GET.get('from', False),
        "from_count": request.GET.get('from_count', False),
        "to": request.GET.get('to', False),
    }

    __validate_converter(request_data)

    result: float
    currency_from = Currency.objects.get(pk=request_data['from'])
    currency_to = Currency.objects.get(pk=request_data['to'])
    result = currency_to.value / currency_from.value * float(request_data['from_count'])

    return JsonResponse({
        'from': currency_from.id,
        'to': currency_to.id,
        'result': result,
    })


def __validate_converter(request_data: dict):
    validate_fields = {
        'from',
        'to',
        'from_count',
    }

    if validate_fields != request_data.keys():
        raise ValidationError('Обязательные поля from и  to', 422)