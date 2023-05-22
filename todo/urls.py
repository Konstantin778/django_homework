from django.contrib import admin
from django.urls import path, include

from auth_app.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
    path('auth/', include('auth_app.urls')),
    path('converter/', include('converter_app.urls')),
    path('', login_view, name='main')
]
