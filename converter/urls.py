from django.urls import path
from converter.views import converter

urlpatterns = [
    path('', converter),
]