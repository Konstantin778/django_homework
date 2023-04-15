from django.contrib import admin
from django.urls import path
from auth_app.views import login_view, registration, user_list

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration, name='registration'),
    path('user_list/', user_list, name='user_list'),
]