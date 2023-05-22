from django.urls import path
from converter_app.controllers.views import index, convert

urlpatterns = [
    path('', index, name='index'),
    path('converter/', convert, name='converter'),
]
