from django.contrib import admin
from django.urls import path
from todo_app.views import index, bye

urlpatterns = [
    path('', index, name='todo_main'),
    path('goodbye/', bye),
]
