from django.urls import path

from converter_app.controllers.api import index, convert

urlpatterns = [
    path('', index, name='index'),
    path('convert/', convert, name='convert'),
]

"""
http://127.0.0.1:8000/converter/api/convert?from=EUR&to=RUB
"""